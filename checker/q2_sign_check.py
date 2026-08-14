"""
checker/q2_sign_check.py

Verifies the claim in Paper A (remark after Lemma 2.9):
  q_2(1/10) < 0  at  sigma_0 = 3/4.

Uses only Python's fractions.Fraction for exact rational arithmetic.
No floating-point, no external libraries.

Exit code: 0 if the claim is confirmed, 1 otherwise.
"""

from fractions import Fraction


def phi_j(rho_re: Fraction, rho_im: Fraction, j: int) -> tuple[Fraction, Fraction]:
    """
    Compute phi_j(rho) = 1 - (1 - rho^{-1})^j
    for rho = rho_re + i*rho_im, j >= 1.

    Returns (real_part, imag_part) as exact Fractions.
    """
    norm_sq = rho_re * rho_re + rho_im * rho_im
    # rho^{-1} = (rho_re - i*rho_im) / norm_sq
    inv_re = rho_re / norm_sq
    inv_im = -rho_im / norm_sq

    # w = 1 - rho^{-1}
    w_re = Fraction(1) - inv_re
    w_im = -inv_im  # = +rho_im / norm_sq

    # w^j by repeated multiplication
    pow_re, pow_im = Fraction(1), Fraction(0)
    for _ in range(j):
        pow_re, pow_im = (pow_re * w_re - pow_im * w_im,
                          pow_re * w_im + pow_im * w_re)

    # phi_j = 1 - w^j
    return Fraction(1) - pow_re, -pow_im


def q_j(sigma0: Fraction, T: Fraction, j: int) -> Fraction:
    """
    q_j(T) = 4 * Re[ phi_j(sigma0 + iT) + phi_j(1 - sigma0 + iT) ]
    """
    r1_re, _ = phi_j(sigma0, T, j)
    r2_re, _ = phi_j(Fraction(1) - sigma0, T, j)
    return Fraction(4) * (r1_re + r2_re)


sigma0 = Fraction(3, 4)
T = Fraction(1, 10)
j = 2

val = q_j(sigma0, T, j)

print(f"sigma_0 = {sigma0},  T = {T},  j = {j}")
print(f"q_2(1/10) = {val}  =  {float(val):.10f}")

if val < 0:
    print("PASS: q_2(1/10) < 0 confirmed.")
    raise SystemExit(0)
else:
    print(f"FAIL: expected q_2(1/10) < 0, got {val}")
    raise SystemExit(1)
