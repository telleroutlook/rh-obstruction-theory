#!/usr/bin/env python3
"""Independent exact-rational witness for OB-24 B1.

The arithmetic and all certificate comparisons use Fraction and integers.

K5 in the supplied request does not define P, Z_+, Z_-, or X_sym.  This
checker therefore makes the review's minimal repair explicit:

* X_sym consists of finite multisets invariant, with multiplicity, under
  conjugation and rho -> 1-rho;
* P(Z) is 1 exactly when every atom of the nonempty multiset Z has real
  part 1/2;
* Z_+ = Q(1/2, 1) and Z_- = Q(3/4, 1).

Consequently, a successful run is a witness for the corrected specification;
it is not evidence that the missing definitions were present in the request.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import comb


F = Fraction


class QComplex:
    """Complex number with exact rational coordinates."""

    __slots__ = ("real", "imag")

    def __init__(self, real=0, imag=0):
        self.real = F(real)
        self.imag = F(imag)

    def __eq__(self, other):
        if not isinstance(other, QComplex):
            return NotImplemented
        return self.real == other.real and self.imag == other.imag

    def __add__(self, other):
        if not isinstance(other, QComplex):
            other = QComplex(other)
        return QComplex(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self):
        return QComplex(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        if not isinstance(other, QComplex):
            other = QComplex(other)
        return other - self

    def __mul__(self, other):
        if not isinstance(other, QComplex):
            other = QComplex(other)
        return QComplex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    __rmul__ = __mul__

    def inverse(self):
        denominator = self.real * self.real + self.imag * self.imag
        assert denominator != 0
        return QComplex(self.real / denominator, -self.imag / denominator)

    def __pow__(self, exponent):
        assert isinstance(exponent, int)
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        result = QComplex(1)
        base = self
        remaining = exponent
        while remaining:
            if remaining & 1:
                result = result * base
            base = base * base
            remaining >>= 1
        return result

    def conjugate(self):
        return QComplex(self.real, -self.imag)

    def key(self):
        return (self.real, self.imag)


ZERO = QComplex(0)
ONE = QComplex(1)


def one_minus(z):
    return ONE - z


def phi(j, rho):
    assert isinstance(j, int) and j >= 1
    assert rho != ZERO and rho != ONE
    return ONE - (ONE - rho.inverse()) ** j


def quartet(sigma, height):
    sigma = F(sigma)
    height = F(height)
    assert height > 0
    atoms = (
        QComplex(sigma, height),
        QComplex(1 - sigma, height),
        QComplex(sigma, -height),
        QComplex(1 - sigma, -height),
    )
    assert all(rho != ZERO and rho != ONE for rho in atoms)
    return atoms


def observation_r_atom(atoms, j, test_function=phi):
    total = QComplex(0)
    for rho in atoms:
        total = total + test_function(j, rho)
    return total


def li_closed_form(sigma, height, j):
    upper_pair = phi(j, QComplex(sigma, height)) + phi(
        j, QComplex(1 - sigma, height)
    )
    return 2 * upper_pair.real


def delta(j, height, sigma=F(3, 4)):
    value = observation_r_atom(quartet(sigma, height), j)
    assert value.imag == 0
    assert value.real == li_closed_form(F(sigma), F(height), j)
    return value.real


def delta_1_formula(height):
    y = 16 * F(height) * F(height)
    return 32 * (y + 3) / ((y + 9) * (y + 1))


def delta_2_formula(height):
    y = 16 * F(height) * F(height)
    numerator = 128 * (y**3 + 9 * y**2 + 31 * y - 9)
    denominator = (y + 9) ** 2 * (y + 1) ** 2
    return numerator / denominator


def poly_trim(polynomial):
    result = tuple(F(coefficient) for coefficient in polynomial)
    while len(result) > 1 and result[-1] == 0:
        result = result[:-1]
    return result


def poly_add(left, right):
    length = max(len(left), len(right))
    return poly_trim(tuple(
        (F(left[index]) if index < len(left) else 0)
        + (F(right[index]) if index < len(right) else 0)
        for index in range(length)
    ))


def poly_scale(scalar, polynomial):
    return poly_trim(tuple(F(scalar) * F(coefficient)
                           for coefficient in polynomial))


def poly_mul(left, right):
    result = [F(0)] * (len(left) + len(right) - 1)
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] += (
                F(left_coefficient) * F(right_coefficient)
            )
    return poly_trim(tuple(result))


def poly_square(polynomial):
    return poly_mul(polynomial, polynomial)


def leading_t_squared_limit(numerator, denominator):
    """Leading-coefficient limit after y=16*T^2."""
    numerator = poly_trim(numerator)
    denominator = poly_trim(denominator)
    assert len(denominator) == len(numerator) + 1
    return numerator[-1] / (16 * denominator[-1])


def symbolic_delta_formulas():
    """Cross-multiply the pair formulas as exact polynomial identities in y."""
    y_plus_1 = (1, 1)
    y_plus_9 = (9, 1)

    delta_1_numerator = poly_add(
        poly_scale(24, y_plus_1),
        poly_scale(8, y_plus_9),
    )
    delta_1_denominator = poly_mul(y_plus_9, y_plus_1)
    assert delta_1_numerator == (96, 32)

    first_delta_2_numerator = (9, 5)
    second_delta_2_numerator = (-1, 3)
    delta_2_numerator = poly_scale(16, poly_add(
        poly_mul(first_delta_2_numerator, poly_square(y_plus_1)),
        poly_mul(second_delta_2_numerator, poly_square(y_plus_9)),
    ))
    delta_2_denominator = poly_mul(
        poly_square(y_plus_9), poly_square(y_plus_1)
    )
    assert delta_2_numerator == (-1152, 3968, 1152, 128)

    return (
        (delta_1_numerator, delta_1_denominator),
        (delta_2_numerator, delta_2_denominator),
    )


def li_leading_constant(j):
    """Coefficient from the z^-1 and z^-2 terms of the binomial expansion."""
    sigma = F(3, 4)
    complementary_sigma = 1 - sigma
    return 2 * (
        j * (sigma + complementary_sigma) + 2 * comb(j, 2)
    )


def is_x_sym(atoms):
    counts = Counter(rho.key() for rho in atoms)
    conjugated = Counter(rho.conjugate().key() for rho in atoms)
    reflected = Counter(one_minus(rho).key() for rho in atoms)
    return counts == conjugated == reflected


def online_predicate(atoms):
    return int(bool(atoms) and all(rho.real == F(1, 2) for rho in atoms))


def constant_one(_j, _rho):
    return ONE


def r_symm_observation(atoms, j):
    total = QComplex(0)
    for rho in atoms:
        total = total + phi(j, rho) + phi(j, one_minus(rho))
    return total


def exact_joint_threshold(bound):
    epsilon = F(1, 1000)
    for height in range(1, bound + 1):
        if abs(delta(1, height)) < epsilon and abs(delta(2, height)) < epsilon:
            return height
    raise AssertionError("threshold not found within exact search bound")


def certify():
    if not __debug__:
        raise RuntimeError("certificate assertions require normal Python mode")

    sigma = F(3, 4)

    # K1: every delta evaluation traverses all four R-atoms, then checks the
    # independently coded conjugate-pair form.  Exercise all certificate inputs.
    exercised_heights = (1, 2, 89, 90, 100, 1000, 10000)
    for j in (1, 2):
        for height in exercised_heights:
            value = delta(j, height, sigma)
            formula = delta_1_formula(height) if j == 1 else delta_2_formula(height)
            assert value == formula

    # K2.
    assert delta(1, 1, sigma) == F(608, 425)

    # K3: exact polynomial identities and leading-coefficient certificates,
    # followed by exact sample rationals used only as regression anchors.
    delta_1_rational, delta_2_rational = symbolic_delta_formulas()
    assert leading_t_squared_limit(*delta_1_rational) == 2
    assert leading_t_squared_limit(*delta_2_rational) == 8
    assert li_leading_constant(1) == 2 == 2 * 1**2
    assert li_leading_constant(2) == 8 == 2 * 2**2
    expected_scaled = {
        (1, 100): F(51200960000, 25601600009),
        (1, 1000): F(512000096000000, 256000160000009),
        (1, 10000): F(5120000009600000000, 2560000016000000009),
        (2, 100): F(5243174918348788480000, 655441923020828800081),
        (2, 1000): F(524288294912063487998848000000,
                     65536081920030208002880000081),
        (2, 10000): F(52428800294912000634879999884800000000,
                      6553600081920000302080000288000000081),
    }
    for (j, height), expected in expected_scaled.items():
        assert delta(j, height) * height * height == expected
    for j, limit in ((1, F(2)), (2, F(8))):
        samples = [delta(j, height) * height * height
                   for height in (100, 1000, 10000)]
        assert samples[0] < samples[1] < samples[2] < limit

    # K4: exact exhaustive integer search; monotonicity is asserted only on the
    # load-bearing positive-integer range, which corrects the prompt's wording.
    assert all(delta(j, height + 1) < delta(j, height)
               for j in (1, 2) for height in range(1, 90))
    assert exact_joint_threshold(90) == 90
    assert delta(1, 90) == F(1382432, 5599152003)
    assert delta(2, 90) == F(30960832077619072, 31350503152698912009)
    assert delta(2, 89) == F(260579831018025856, 258028998573187534225)
    assert delta(1, 90) < F(1, 1000)
    assert delta(2, 90) < F(1, 1000)
    assert delta(2, 89) > F(1, 1000)

    # K5 under the explicit minimal definitions at the top of this file.
    z_plus = quartet(F(1, 2), 1)
    z_minus = quartet(F(3, 4), 1)
    assert is_x_sym(z_plus) and is_x_sym(z_minus)
    assert online_predicate(z_plus) == 1
    assert online_predicate(z_minus) == 0
    assert online_predicate(quartet(F(1, 2), 1)) == 1
    for height in (1, 10, 100):
        constant_value = observation_r_atom(
            quartet(F(3, 4), height), 1, constant_one
        )
        assert constant_value == QComplex(4)

    # K6: the reflected sum duplicates the R-atom sum because Q is invariant.
    r_atom = observation_r_atom(quartet(sigma, 1), 1)
    r_symm = r_symm_observation(quartet(sigma, 1), 1)
    assert r_atom == QComplex(F(608, 425))
    assert r_symm == 2 * r_atom == QComplex(F(1216, 425))

    with open(__file__, "rb") as source_file:
        source = source_file.read()
    source_text = source.decode("utf-8")
    forbidden = (
        "import " + "numpy",
        "import " + "scipy",
        "import " + "mpmath",
        "float" + "(",
    )
    assert all(token not in source_text for token in forbidden)

    print("K5_SPEC_REPAIR=explicit definitions in module docstring")
    for (j, height), value in expected_scaled.items():
        print("SCALED", j, height, value)
    print("DELTA_1_90", delta(1, 90))
    print("DELTA_2_90", delta(2, 90))
    print("DELTA_2_89", delta(2, 89))
    print("ALL_CERTIFIED_CHECKS_PASSED")
    print("SHA256", sha256(source).hexdigest())


if __name__ == "__main__":
    certify()
