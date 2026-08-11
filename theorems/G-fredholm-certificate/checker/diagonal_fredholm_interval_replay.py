#!/usr/bin/env python3
"""Exact-rational interval replay for Problem OB-17.

No floating-point operation participates in a certificate.  Transcendental
values are enclosed by convergent rational series with explicit remainder
bounds.  The log-Gamma value is evaluated through a shifted Stirling/Binet
formula with a proved complex remainder bound.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial, isqrt


@dataclass(frozen=True)
class I:
    lo: Q
    hi: Q

    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def point(x):
        x = x if isinstance(x, Q) else Q(x)
        return I(x, x)

    def __add__(self, other):
        other = other if isinstance(other, I) else I.point(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, I) else -I.point(other))

    def __rsub__(self, other):
        return I.point(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, I) else I.point(other)
        vals = (self.lo * other.lo, self.lo * other.hi,
                self.hi * other.lo, self.hi * other.hi)
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        return I(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I.point(other)
        return self * other.reciprocal()


@dataclass(frozen=True)
class C:
    re: Q
    im: Q

    def __mul__(self, other):
        return C(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    def reciprocal(self):
        d = self.re * self.re + self.im * self.im
        return C(self.re / d, -self.im / d)

    def __pow__(self, n):
        if n < 0:
            return (self.reciprocal()) ** (-n)
        out = C(Q(1), Q(0))
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out


TOL = Q(1, 10**45)


def positive_series_log_from_y(y: Q, tol=TOL) -> I:
    """Enclose log((1+y)/(1-y)), 0 <= y < 1, by rational sums."""
    if not (0 <= y < 1):
        raise ValueError(y)
    y2 = y * y
    power = y
    s = Q(0)
    j = 0
    while True:
        s += power / (2 * j + 1)
        next_power = power * y2
        tail = 2 * next_power / ((2 * j + 3) * (1 - y2))
        if tail < tol:
            return I(2 * s, 2 * s + tail)
        power = next_power
        j += 1


LOG2 = positive_series_log_from_y(Q(1, 3))


def log_q(q: Q) -> I:
    """Rigorous natural-log enclosure for a positive rational."""
    if q <= 0:
        raise ValueError(q)
    k = q.numerator.bit_length() - q.denominator.bit_length()
    two_k = Q(2**k) if k >= 0 else Q(1, 2**(-k))
    r = q / two_k
    while r < 1:
        k -= 1
        r *= 2
    while r >= 2:
        k += 1
        r /= 2
    y = (r - 1) / (r + 1)
    return positive_series_log_from_y(y) + k * LOG2


def atan_small(x: Q, tol=TOL) -> I:
    """Alternating-series enclosure for atan(x), |x| <= 1/2."""
    if x < 0:
        return -atan_small(-x, tol)
    if x > Q(1, 2):
        raise ValueError(x)
    x2 = x * x
    power = x
    s = Q(0)
    k = 0
    sign = 1
    while True:
        s += sign * power / (2 * k + 1)
        next_term = power * x2 / (2 * k + 3)
        if next_term < tol:
            s_next = s - sign * next_term
            return I(min(s, s_next), max(s, s_next))
        power *= x2
        sign = -sign
        k += 1


PI = 16 * atan_small(Q(1, 5)) - 4 * atan_small(Q(1, 239))
LOGPI = I(log_q(PI.lo).lo, log_q(PI.hi).hi)


def atan_q(x: Q) -> I:
    """Rigorous atan enclosure, reduced to |argument| <= 1/2."""
    if x < 0:
        return -atan_q(-x)
    if x > 1:
        return PI / 2 - atan_q(1 / x)
    if x > Q(1, 2):
        r = (x - 1) / (x + 1)  # in (-1/3, 0]
        return PI / 4 + atan_small(r)
    return atan_small(x)


BERNOULLI = [
    Q(1, 6), Q(-1, 30), Q(1, 42), Q(-1, 30),
    Q(5, 66), Q(-691, 2730), Q(7, 6), Q(-3617, 510),
]

SHIFT = 16
STIRLING_TERMS = len(BERNOULLI)
A0 = Q(1, 4)
A = Q(SHIFT) + A0


def zeta_upper(s: int) -> Q:
    # zeta(s) = 1 + sum_{k>=2} k^-s
    # <= 1 + 2^-s + integral_2^infty x^-s dx.
    return Q(1) + Q(1, 2**s) + Q(1, 2**(s - 1) * (s - 1))


def stirling_remainder_bound() -> Q:
    m = STIRLING_TERMS
    s = 2 * m + 2
    return (2 * zeta_upper(s) * factorial(2 * m)
            / ((2 * PI.lo) ** s * A ** (2 * m + 1)))


def stirling_derivative_remainder_bound() -> Q:
    m = STIRLING_TERMS
    s = 2 * m + 2
    return (2 * zeta_upper(s) * factorial(2 * m + 1)
            / ((2 * PI.lo) ** s * A ** (2 * m + 2)))


R_LOGGAMMA = stirling_remainder_bound()
R_PSI = stirling_derivative_remainder_bound()


def theta_at(t: Q) -> I:
    """Certified enclosure of theta(t) at an exact rational t > 0."""
    b = t / 2
    w = C(A, b)
    result = (b / 2) * log_q(A * A + b * b)
    result += (A - Q(1, 2)) * atan_q(b / A)
    result -= b

    inv = w.reciprocal()
    for n, bern in enumerate(BERNOULLI, start=1):
        coeff = bern / (2 * n * (2 * n - 1))
        result += coeff * (inv ** (2 * n - 1)).im

    result += I(-R_LOGGAMMA, R_LOGGAMMA)
    for k in range(SHIFT):
        result -= atan_q(b / (A0 + k))
    result -= b * LOGPI
    return result


def theta_prime_at(t: Q) -> I:
    """Certified enclosure of theta'(t) at an exact rational t > 0."""
    b = t / 2
    w = C(A, b)
    inv = w.reciprocal()
    re_psi = Q(1, 2) * log_q(A * A + b * b)
    re_psi -= Q(1, 2) * inv.re
    for n, bern in enumerate(BERNOULLI, start=1):
        re_psi -= (bern / (2 * n)) * (inv ** (2 * n)).re
    re_psi += I(-R_PSI, R_PSI)
    for k in range(SHIFT):
        x = A0 + k
        re_psi -= x / (x * x + b * b)
    return (re_psi - LOGPI) / 2


def sign_of_theta_minus_level(t: Q, level: int) -> int:
    v = theta_at(t) - level * PI
    if v.hi < 0:
        return -1
    if v.lo > 0:
        return 1
    raise ArithmeticError("interval does not decide sign")


def bisect_level(level: int, lo=Q(10), hi=Q(40), width=Q(1, 10**11)) -> I:
    if sign_of_theta_minus_level(lo, level) >= 0:
        raise AssertionError("bad lower bracket")
    if sign_of_theta_minus_level(hi, level) <= 0:
        raise AssertionError("bad upper bracket")
    while hi - lo >= width:
        mid = (lo + hi) / 2
        if sign_of_theta_minus_level(mid, level) < 0:
            lo = mid
        else:
            hi = mid
    return I(lo, hi)


def floor_scaled(q: Q, digits: int) -> int:
    scale = 10**digits
    return (q.numerator * scale) // q.denominator


def ceil_scaled(q: Q, digits: int) -> int:
    scale = 10**digits
    return -((-q.numerator * scale) // q.denominator)


def sqrt_floor_scaled(q: Q, digits: int) -> int:
    scale = 10**digits
    a = q.numerator * scale * scale
    return isqrt(a // q.denominator)


def sqrt_ceil_scaled(q: Q, digits: int) -> int:
    k = sqrt_floor_scaled(q, digits)
    scale = 10**digits
    while Q(k * k, scale * scale) < q:
        k += 1
    return k


def fmt_scaled(k: int, digits: int) -> str:
    sign = "-" if k < 0 else ""
    k = abs(k)
    s = str(k).rjust(digits + 1, "0")
    return f"{sign}{s[:-digits]}.{s[-digits:]}" if digits else sign + s


def decimal_interval(x: I, digits: int) -> tuple[str, str]:
    return (fmt_scaled(floor_scaled(x.lo, digits), digits),
            fmt_scaled(ceil_scaled(x.hi, digits), digits))


def sqrt_interval(x: I, digits: int) -> tuple[str, str]:
    return (fmt_scaled(sqrt_floor_scaled(x.lo, digits), digits),
            fmt_scaled(sqrt_ceil_scaled(x.hi, digits), digits))


def strict_left(x: I, y: I) -> bool:
    """Return the certified strict-separation predicate x < y."""
    return x.hi < y.lo


def main():
    print("backend=Python fractions.Fraction (exact rational arithmetic)")
    print("pi", decimal_interval(PI, 45))
    print("log_pi", decimal_interval(LOGPI, 40))
    print("stirling_remainder", decimal_interval(I.point(R_LOGGAMMA), 35))
    print("psi_remainder", decimal_interval(I.point(R_PSI), 35))
    dp = theta_prime_at(Q(10))
    th10 = theta_at(Q(10))
    th40_minus_4pi = theta_at(Q(40)) - 4 * PI
    assert dp.lo > 0
    assert th10.hi < 0
    assert th40_minus_4pi.lo > 0
    print("theta_prime_10", decimal_interval(dp, 30))
    print("theta_10", decimal_interval(th10, 30))
    print("theta_40_minus_4pi",
          decimal_interval(th40_minus_4pi, 30))

    roots = []
    for level in range(5):
        root = bisect_level(level)
        roots.append(root)
        assert root.hi - root.lo < Q(1, 10**8)
        print(f"d_{level+1}", decimal_interval(root, 15),
              "width<", decimal_interval(I.point(root.hi - root.lo), 18)[1])

    stated_centers = [
        Q(1784559954, 10**8), Q(2317028270, 10**8),
        Q(2767018222, 10**8), Q(3171797995, 10**8),
        Q(3546718430, 10**8),
    ]
    for root, center in zip(roots, stated_centers):
        target = I(center - Q(1, 10**6), center + Q(1, 10**6))
        assert target.lo <= root.lo and root.hi <= target.hi

    print("derived")
    kappas = []
    zeros = []
    for n, d in enumerate(roots, 1):
        q = I(Q(1, 4) + d.lo * d.lo, Q(1, 4) + d.hi * d.hi)
        kappa = q.reciprocal()
        scale = 10**15
        zero_i = I(Q(sqrt_floor_scaled(q.lo, 15), scale),
                   Q(sqrt_ceil_scaled(q.hi, 15), scale))
        kappas.append(kappa)
        zeros.append(zero_i)
        zero = sqrt_interval(q, 11)
        print(f"kappa_{n}", decimal_interval(kappa, 14), "zero", zero)

    kappa_target = I(Q(31375953, 10**10) - Q(1, 10**8),
                     Q(31375953, 10**10) + Q(1, 10**8))
    zero_target = I(Q(178526027, 10**7) - Q(1, 10**5),
                    Q(178526027, 10**7) + Q(1, 10**5))
    assert kappa_target.lo <= kappas[0].lo
    assert kappas[0].hi <= kappa_target.hi
    assert zero_target.lo <= zeros[0].lo
    assert zeros[0].hi <= zero_target.hi

    # External comparison inputs only: Odlyzko's printed centers together with
    # his stated 3e-9 absolute accuracy for the first 100,000 zeros.
    gamma_centers = [Q(14134725142, 10**9), Q(21022039639, 10**9),
                     Q(25010857580, 10**9)]
    gamma = [I(c - Q(3, 10**9), c + Q(3, 10**9)) for c in gamma_centers]
    print("separation")
    for n in range(3):
        d = roots[n]
        zlo = zeros[n].lo
        assert strict_left(gamma[n], d)
        assert strict_left(d, zeros[n])
        gap_gd = I.point(d.lo - gamma[n].hi)
        gap_dz = I.point(zlo - d.hi)
        print(f"n={n+1}", "gamma", decimal_interval(gamma[n], 12),
              "gamma_to_d_gap>", decimal_interval(gap_gd, 12)[0],
              "d_to_zero_gap>", decimal_interval(gap_dz, 12)[0])

    print("mutations")
    mutated_zero_a = roots[0]  # exact identity 1/sqrt(1/d_1^2) = d_1
    mutation_a_passes = strict_left(roots[0], mutated_zero_a)
    mutated_d_b = gamma[0]
    mutation_b_passes = strict_left(gamma[0], mutated_d_b)
    assert not mutation_a_passes
    assert not mutation_b_passes
    assert strict_left(gamma[0], roots[0])
    print("a_mutated_zero", decimal_interval(roots[0], 12),
          "overlaps_d1=True strict_test=", mutation_a_passes)
    print("b_mutated_d", decimal_interval(gamma[0], 12),
          "overlaps_gamma1=True strict_test=", mutation_b_passes,
          "below_true_d1_gap>",
          decimal_interval(I.point(roots[0].lo - gamma[0].hi), 12)[0])

    N = 2048
    lnN = log_q(Q(N))
    numerator = ((lnN * lnN + 2 * lnN + 2) / N
                 + (lnN * lnN) / (N * N))
    tail = numerator / (4 * PI * PI)
    assert tail.hi < Q(1, 1000)
    print("tail_N_2048", decimal_interval(tail, 15))
    print("ALL_CERTIFIED_CHECKS_PASSED")


if __name__ == "__main__":
    main()
