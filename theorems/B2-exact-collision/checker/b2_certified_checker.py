#!/usr/bin/env python3
"""
Independent exact-rational certified checker for problem OB-21, block B2
("finite-collision pipeline").

Written from scratch, directly from the definitions in
OB-21-B2-certified-checker-request.md, WITHOUT consulting or adapting any
producer script. Standard library only (fractions.Fraction + integers).
No floating point appears anywhere in the certificate path: the file
contains no call to the float builtin and no numpy, scipy, or mpmath
import; all arithmetic is done with fractions.Fraction and Python
integers only.

Non-circularity note: nothing here assumes RH, uses any RH-equivalent
statement, or treats a zeta zero's location/reality as a premise. All
objects (L(t), Q, the multisets Z_+, Z_-) are FINITE, EXPLICITLY
CONSTRUCTED multisets of complex rationals fixed by the definitions
below; the only thing being certified is a finite algebraic identity
among their rational "observations" O_j.
"""

import hashlib
import math
from fractions import Fraction as Fr


# ---------------------------------------------------------------------------
# Complex-rational arithmetic: z = a + bi, a,b in Fraction.
# ---------------------------------------------------------------------------

class CFrac:
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        o = o if isinstance(o, CFrac) else CFrac(o)
        return CFrac(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, CFrac) else CFrac(o)
        return CFrac(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        o = o if isinstance(o, CFrac) else CFrac(o)
        return o - self

    def __mul__(self, o):
        if isinstance(o, CFrac):
            return CFrac(self.re * o.re - self.im * o.im,
                         self.re * o.im + self.im * o.re)
        # scalar (Fraction / int) multiplication
        return CFrac(self.re * o, self.im * o)

    __rmul__ = __mul__

    def __neg__(self):
        return CFrac(-self.re, -self.im)

    def recip(self):
        denom = self.re * self.re + self.im * self.im
        assert denom != 0, "division by zero complex-rational"
        return CFrac(self.re / denom, -self.im / denom)

    def conj(self):
        return CFrac(self.re, -self.im)

    def __eq__(self, o):
        o = o if isinstance(o, CFrac) else CFrac(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else ''}{self.im}i)"


ONE = CFrac(1, 0)
ZERO = CFrac(0, 0)


def cpow(z, j):
    """Integer power, j >= 0, by repeated multiplication (no shortcuts that
    could hide an error; j is always small here: j <= m <= a few)."""
    assert isinstance(j, int) and j >= 0
    p = CFrac(1, 0)
    for _ in range(j):
        p = p * z
    return p


# ---------------------------------------------------------------------------
# Test functions and observation, PER DEFINITION (traversal of the
# multiset, not the Chebyshev closed form).
# ---------------------------------------------------------------------------

def phi(j, rho):
    """phi_j(rho) = 1 - (1 - 1/rho)^j"""
    inv = rho.recip()
    base = ONE - inv
    return ONE - cpow(base, j)


def O(j, multiset):
    """multiset: list of (CFrac atom, positive-int multiplicity).
    O_j(Z) = sum_{rho in Z} [phi_j(rho) + phi_j(1-rho)], with multiplicity.
    Asserts the imaginary part is exactly 0 and returns the (Fraction)
    real part.
    """
    total = CFrac(0, 0)
    for atom, mult in multiset:
        assert isinstance(mult, int) and mult >= 0
        term = phi(j, atom) + phi(j, ONE - atom)
        total = total + mult * term
    assert total.im == 0, f"O_{j} not real: {total}"
    return total.re


# ---------------------------------------------------------------------------
# The finite objects L(t), Q.
# ---------------------------------------------------------------------------

def L(t):
    """L(t) = {1/2+it, 1/2-it}, as a list of (atom, mult=1) pairs."""
    t = Fr(t)
    return [(CFrac(Fr(1, 2), t), 1), (CFrac(Fr(1, 2), -t), 1)]


def Qset(T):
    """Q = {3/4+iT, 3/4-iT, 1/4+iT, 1/4-iT}."""
    T = Fr(T)
    return [
        (CFrac(Fr(3, 4), T), 1),
        (CFrac(Fr(3, 4), -T), 1),
        (CFrac(Fr(1, 4), T), 1),
        (CFrac(Fr(1, 4), -T), 1),
    ]


# ---------------------------------------------------------------------------
# Chebyshev closed-form cross-check route (independent second route).
# ---------------------------------------------------------------------------

def chebyshev_T(j, x):
    """T_0=1, T_1=x, T_{k+1}=2x T_k - T_{k-1}, exact Fraction x."""
    if j == 0:
        return Fr(1)
    Tprev, Tcur = Fr(1), x
    for _ in range(1, j):
        Tprev, Tcur = Tcur, 2 * x * Tcur - Tprev
    return Tcur


def chebyshev_C_entry(j, t):
    t = Fr(t)
    x = (4 * t * t - 1) / (4 * t * t + 1)
    return 4 * (1 - chebyshev_T(j, x))


# ---------------------------------------------------------------------------
# Exact-rational linear algebra: Gaussian elimination, determinant, solve.
# ---------------------------------------------------------------------------

def det_and_solve(Cmat, dvec):
    """Cmat: m x m list of Fraction rows. dvec: length-m list of Fraction.
    Returns (det, x) where x solves Cmat @ x = dvec (x is None if det==0).
    Exact Fraction Gaussian elimination with partial pivoting (any nonzero
    pivot; exactness makes the ordering irrelevant for correctness).
    """
    m = len(Cmat)
    A = [list(row) + [dvec[i]] for i, row in enumerate(Cmat)]
    sign = 1
    det = Fr(1)
    for col in range(m):
        piv = None
        for r in range(col, m):
            if A[r][col] != 0:
                piv = r
                break
        if piv is None:
            return Fr(0), None
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            sign = -sign
        pivot_val = A[col][col]
        det *= pivot_val
        for r in range(col + 1, m):
            factor = A[r][col] / pivot_val
            if factor != 0:
                for c2 in range(col, m + 1):
                    A[r][c2] -= factor * A[col][c2]
    det *= sign
    if det == 0:
        return det, None
    x = [Fr(0)] * m
    for i in range(m - 1, -1, -1):
        s = A[i][m]
        for j in range(i + 1, m):
            s -= A[i][j] * x[j]
        x[i] = s / A[i][i]
    return det, x


def mat_vec(Cmat, v):
    m = len(Cmat)
    return [sum(Cmat[i][k] * v[k] for k in range(m)) for i in range(m)]


# ---------------------------------------------------------------------------
# Multiset helpers (for K8 symmetry and predicate P).
# ---------------------------------------------------------------------------

def to_dict(pairs):
    """list[(CFrac, int)] -> dict[(re,im) -> mult], merging duplicates."""
    d = {}
    for atom, mult in pairs:
        key = (atom.re, atom.im)
        d[key] = d.get(key, 0) + mult
    return {k: v for k, v in d.items() if v != 0}


def predicate_P(mset_dict):
    """P(Z) = 1 iff every atom (with positive multiplicity) has real part 1/2."""
    for (re, im), mult in mset_dict.items():
        if mult > 0 and re != Fr(1, 2):
            return 0
    return 1


def symmetry_check(mset_dict):
    """Z is closed (with multiplicity) under rho -> conj(rho) and
    rho -> 1-rho."""
    ok_conj = True
    ok_refl = True
    for (re, im), mult in mset_dict.items():
        if mult == 0:
            continue
        conj_key = (re, -im)
        refl_key = (1 - re, im)
        if mset_dict.get(conj_key, 0) != mult:
            ok_conj = False
        if mset_dict.get(refl_key, 0) != mult:
            ok_refl = False
    return ok_conj, ok_refl


# ---------------------------------------------------------------------------
# The pipeline (per Sec. "The pipeline to reconstruct").
# ---------------------------------------------------------------------------

def run_instance(m, ts, T, label, report):
    assert len(ts) == m
    ts = [Fr(t) for t in ts]
    T = Fr(T)
    report.append(f"\n=== Instance {label}: m={m}, t={ts}, T={T} ===")

    # Step 2: C_{jk}, d_j  (per-definition route)
    Lsets = [L(t) for t in ts]
    Qs = Qset(T)
    Cmat = [[O(j, Lsets[k]) for k in range(m)] for j in range(1, m + 1)]
    dvec = [O(j, Qs) for j in range(1, m + 1)]

    # K1: realness already asserted inside O(); now cross-check Chebyshev route
    Cmat_cheb = [[chebyshev_C_entry(j, ts[k]) for k in range(m)] for j in range(1, m + 1)]
    for j in range(m):
        for k in range(m):
            assert Cmat[j][k] == Cmat_cheb[j][k], (
                f"K1 FAILED at j={j+1},k={k+1}: "
                f"per-def={Cmat[j][k]} vs chebyshev={Cmat_cheb[j][k]}"
            )
    report.append("K1: PASS (O_j real for all tested j; per-definition C matches Chebyshev route entry-by-entry)")
    report.append(f"C = {Cmat}")
    report.append(f"d = {dvec}")

    # K2: nonsingularity + rational solve
    det, x = det_and_solve(Cmat, dvec)
    assert det != 0, "K2 FAILED: det C == 0 (degenerate)"
    beta = [-xi for xi in x]
    # verify C beta = -d exactly
    Cb = mat_vec(Cmat, beta)
    neg_d = [-di for di in dvec]
    assert Cb == neg_d, f"K2 FAILED: C beta != -d ; C beta={Cb}, -d={neg_d}"
    report.append(f"K2: PASS. det C = {det}, beta = {beta}")

    # K3: integer scaling
    R = 1
    for b in beta:
        R = R * b.denominator // math.gcd(R, b.denominator)
    n_frac = [R * b for b in beta]
    for v in n_frac:
        assert v.denominator == 1, f"K3 FAILED: R*beta not integral: {v}"
    n = [int(v) for v in n_frac]
    M = max(abs(v) for v in n)
    for k in range(m):
        assert M + n[k] >= 0, f"K3 FAILED: M+n_{k+1} < 0"
    report.append(f"K3: PASS. R = {R}, n = {n}, M = {M}, M+n = {[M+nk for nk in n]}")

    # K4: exact collision  C n + R d = 0
    Cn = mat_vec(Cmat, [Fr(nk) for nk in n])
    residual = [Cn[j] + R * dvec[j] for j in range(m)]
    assert all(r == 0 for r in residual), f"K4 FAILED: residual={residual}"
    report.append(f"K4: PASS. C n + R d = {residual} (exact zero)")

    # Step 7: build Z_+ , Z_-
    Zplus_pairs = []
    for k in range(m):
        for atom, _ in Lsets[k]:
            Zplus_pairs.append((atom, M))
    Zplus = to_dict(Zplus_pairs)

    Zminus_pairs = []
    for k in range(m):
        for atom, _ in Lsets[k]:
            Zminus_pairs.append((atom, M + n[k]))
    for atom, _ in Qs:
        Zminus_pairs.append((atom, R))
    Zminus = to_dict(Zminus_pairs)

    # K5: predicate separation
    p_plus = predicate_P(Zplus)
    p_minus = predicate_P(Zminus)
    assert p_plus == 1, "K5 FAILED: P(Z_+) != 1"
    assert p_minus == 0, "K5 FAILED: P(Z_-) != 0"
    report.append(f"K5: PASS. P(Z_+) = {p_plus}, P(Z_-) = {p_minus}")

    # K8: symmetry
    conj_p, refl_p = symmetry_check(Zplus)
    conj_m, refl_m = symmetry_check(Zminus)
    assert conj_p and refl_p, "K8 FAILED: Z_+ not symmetric"
    assert conj_m and refl_m, "K8 FAILED: Z_- not symmetric"
    report.append("K8: PASS. Z_+ and Z_- both closed under rho->conj(rho) and rho->1-rho, with multiplicity.")

    return {
        "m": m, "t": ts, "T": T, "C": Cmat, "d": dvec, "det": det,
        "beta": beta, "R": R, "n": n, "M": M, "Cmat_rows": Cmat,
    }


def run_k7(inst2, report):
    """Adversarial mutation guard on the m=2 instance: replace n_1 by n_1+1
    and confirm the residual C n' + R d becomes nonzero and equals the
    first column of C."""
    Cmat, dvec, R, n = inst2["C"], inst2["d"], inst2["R"], inst2["n"]
    n_mut = list(n)
    n_mut[0] = n_mut[0] + 1
    Cn_mut = mat_vec(Cmat, [Fr(v) for v in n_mut])
    residual = [Cn_mut[j] + R * dvec[j] for j in range(len(dvec))]
    first_col = [Cmat[j][0] for j in range(len(Cmat))]
    assert residual != [Fr(0)] * len(residual), "K7 FAILED: mutated residual is still zero (vacuous check)"
    assert residual == first_col, (
        f"K7 FAILED: mutated residual {residual} != first column of C {first_col}"
    )
    report.append(f"K7: PASS. Mutated n' (n_1 -> n_1+1) gives C n' + R d = {residual} "
                  f"= first column of C = {first_col} (nonzero, as required).")
    return residual


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    report = []

    # Anchor instance
    inst1 = run_instance(2, [1, 2], 1, "1 (anchor: m=2,t=(1,2),T=1)", report)

    # Self-chosen second instance
    inst2b = run_instance(3, [1, 2, 3], 2, "2 (self-chosen: m=3,t=(1,2,3),T=2)", report)

    # K7 uses the m=2 (anchor) instance
    run_k7(inst1, report)

    # -----------------------------------------------------------------
    # Cross-check anchor numeric values against the request's stated
    # anchor block, for instance 1 only.
    # -----------------------------------------------------------------
    expected = {
        "C": [[Fr(8, 5), Fr(8, 17)], [Fr(128, 25), Fr(512, 289)]],
        "det": Fr(3072, 7225),
        "d": [Fr(1216, 425), Fr(1763072, 180625)],
        "beta": [Fr(-1426, 1275), Fr(-854, 375)],
        "R": 6375,
        "n": [-7130, -14518],
        "M": 14518,
    }
    assert inst1["C"] == expected["C"], f"Anchor mismatch C: {inst1['C']} vs {expected['C']}"
    assert inst1["det"] == expected["det"], f"Anchor mismatch det: {inst1['det']} vs {expected['det']}"
    assert inst1["d"] == expected["d"], f"Anchor mismatch d: {inst1['d']} vs {expected['d']}"
    assert inst1["beta"] == expected["beta"], f"Anchor mismatch beta: {inst1['beta']} vs {expected['beta']}"
    assert inst1["R"] == expected["R"], f"Anchor mismatch R: {inst1['R']} vs {expected['R']}"
    assert inst1["n"] == expected["n"], f"Anchor mismatch n: {inst1['n']} vs {expected['n']}"
    assert inst1["M"] == expected["M"], f"Anchor mismatch M: {inst1['M']} vs {expected['M']}"
    report.append("\nAnchor cross-check (instance 1 vs request's stated anchor block): PASS, all fields match exactly.")

    print("\n".join(report))
    print()
    print("ALL_CERTIFIED_CHECKS_PASSED")


if __name__ == "__main__":
    main()
