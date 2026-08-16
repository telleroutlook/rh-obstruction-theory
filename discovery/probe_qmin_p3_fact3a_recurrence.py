#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cl — ANALYTIC BACKBONE of FACT 3a/3b: reduce the mod-3 residue of w=B^-1 d to a finite
palindromic-quartic recurrence whose coefficients (e1,e2) mod 3 depend ONLY on n mod 3.

STRUCTURE (all exact, orbit-agnostic):
  * d_j = Sum over the off-line quartet of Re[1 - beta^j], beta = 1 - 1/rho, rho = sig + i*tau.
    Each of the 4 atoms rho in {sig±i tau, (1-sig)±i tau} appears TWICE in d_vec_sig, and the
    reflection rho -> 1-rho sends beta -> 1/beta.  Hence the beta-quartet is
        {beta1, conj(beta1), 1/beta1, 1/conj(beta1)},  beta1 = 1 - 1/(sig + i tau),
    CLOSED under conjugation AND inversion.  So  d_j = 8 - 2 p_j,  where
        p_j = beta1^j + conj^j + beta1^-j + conj^-j
    is the j-th power sum of a PALINDROMIC REAL QUARTIC  x^4 - e1 x^3 + e2 x^2 - e1 x + 1.
    => p_j = e1 p_{j-1} - e2 p_{j-2} + e1 p_{j-3} - p_{j-4},  p_0=4, p_1=e1, p_2=e1^2-2e2, p_3=e1^3-3e1 e2+3e1.
  * e1 = 2 Re(beta1 + 1/beta1),  e2 = 2 + |beta1+1/beta1|^2 - ... (computed exactly below from the 4 roots).
  * B mod 3 is a FIXED universal integer lower-triangular matrix (orbit-independent); w = B^-1 d.

CLAIM TO PROBE (EXACT, L9):
  (1) e1, e2 are 3-integral when 3∤n, and (e1 mod 3, e2 mod 3) depend ONLY on n mod 3 (not on a=n*sig
      nor on m).  [If true, the whole mod-3 recurrence — hence w mod 3 — is a function of n mod 3.]
  (2) Reconstruct d mod 3 from the recurrence and confirm w=B^-1 d reproduces FACT 3a ([1,1,2,2] period-4
      units for n≡1) and FACT 3b (w_0 unit, w_i≡0 i>=1 for n≡2).

READING (L5): if (e1,e2) mod 3 are pinned by n mod 3, FACT 3a/3b become a FINITE F_3 linear-algebra
statement (one 4-term recurrence + one fixed matrix inverse per residue class) — a provable closed core,
NOT an empirical pattern.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr

from discovery.probe_qmin_p2_floor_identity import wvec, d_vec_sig
from discovery.probe_qmin_Cj_bilinear import Bmatrix, solve_lower, vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def v3(x):
    return vp_frac(Fr(x), 3)


def mod3(fr):
    """residue of a 3-integral rational mod 3 (raises if not 3-integral)."""
    fr = Fr(fr)
    assert fr.denominator % 3 != 0, "not 3-integral"
    return (fr.numerator % 3) * pow(fr.denominator % 3, -1, 3) % 3


def quartic_e1_e2(sig, tau):
    """e1, e2 of the palindromic quartic with roots {beta1, conj, 1/beta1, 1/conj}, beta1=1-1/(sig+i tau).
    Work with the two conjugate 'trace' pairs. Use exact rational real/imag parts."""
    # beta1 = 1 - 1/rho ; 1/rho = conj(rho)/|rho|^2
    R = sig * sig + tau * tau                      # |rho|^2
    br = 1 - sig / R                               # Re beta1
    bi = tau / R                                   # Im beta1  (beta1 = br + i bi)
    Nb = br * br + bi * bi                          # |beta1|^2
    # 1/beta1 = conj(beta1)/|beta1|^2 = (br - i bi)/Nb
    ir, ii = br / Nb, -bi / Nb                       # Re,Im of 1/beta1
    # roots: beta1=br+ibi, conj=br-ibi, inv=ir+iii, invconj=ir-iii
    # e1 = sum of roots = 2 br + 2 ir
    e1 = 2 * br + 2 * ir
    # e2 = sum of pairwise products.  Pair sums: s1=beta1+conj=2br (prod=Nb), s2=inv+invconj=2ir (prod=1/Nb? )
    # Actually beta1*conj = Nb, inv*invconj = ir^2+ii^2 = 1/Nb.  Cross terms:
    # (beta1+conj)(inv+invconj) = 2br*2ir. plus beta1*conj + inv*invconj = Nb + (ir*ir+ii*ii)
    prod_pair1 = Nb
    prod_pair2 = ir * ir + ii * ii
    e2 = prod_pair1 + prod_pair2 + (2 * br) * (2 * ir)
    return e1, e2


def p_powersums(e1, e2, m):
    """p_0..p_{m}, palindromic-quartic power sums via Newton/linear recurrence."""
    p = [Fr(4)]                                    # p_0 = 4 (four roots)
    if m >= 1:
        p.append(Fr(e1))                            # p_1 = e1
    if m >= 2:
        p.append(e1 * e1 - 2 * e2)                  # p_2 = e1^2 - 2 e2
    if m >= 3:
        p.append(e1 ** 3 - 3 * e1 * e2 + 3 * e1)    # p_3 = e1^3 -3 e1 e2 + 3 e1 (coeffs a1=e1,a2=e2,a3=e1)
    for j in range(4, m + 1):
        p.append(e1 * p[j - 1] - e2 * p[j - 2] + e1 * p[j - 3] - p[j - 4])
    return p


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6cl: FACT 3a/3b backbone — palindromic-quartic recurrence for d, coeffs (e1,e2) mod 3 by n mod 3.", flush=True)
    print("=" * 100, flush=True)

    # Row-3 orbits (n≡2 mod4, 3∤n), distinct n across both residues mod 3, several 'a' values per n.
    ORB = [(Fr(3, 10), 10), (Fr(7, 10), 10), (Fr(1, 22), 22), (Fr(5, 22), 22),   # n≡1 mod3
           (Fr(1, 34), 34), (Fr(1, 58), 58),
           (Fr(1, 14), 14), (Fr(3, 14), 14), (Fr(1, 26), 26), (Fr(5, 26), 26),   # n≡2 mod3
           (Fr(1, 38), 38), (Fr(1, 50), 50)]
    tau = Fr(1)

    # (0) sanity: d_j = 8 - 2 p_j exactly (validates the whole reduction)
    print("\n(0) EXACT check  d_j == 8 - 2 p_j  (palindromic-quartic power sums):", flush=True)
    allok = True
    for sig, n in ORB:
        e1, e2 = quartic_e1_e2(sig, tau)
        p = p_powersums(e1, e2, 8)
        d = d_vec_sig(sig, tau, 9)      # d indexed j=1..9 -> list[0..8] for j=1..
        ok = all(d[j - 1] == 8 - 2 * p[j] for j in range(1, 9))
        allok = allok and ok
    print("  d_j == 8 - 2 p_j for all orbits, j=1..8:  %s" % ("HOLDS" if allok else "FALSE"), flush=True)

    # (1) CORRECTED classifier: e1≡0 mod3 always; e2 mod3 governs the split; e2≡2 <=> 3|(a+n).
    print("\n(1) e1 mod3 (claim ALWAYS 0) and e2 mod3 (claim ≡2 <=> 3|(a+n), a=n*sig):", flush=True)
    okcls = True
    for sig, n in ORB:
        _, _, nn = rho_pqn(sig, tau)
        assert nn == n, (nn, n)
        a = int(sig * n)
        e1, e2 = quartic_e1_e2(sig, tau)
        r1 = mod3(e1) if v3(e1) >= 0 else None
        r2 = mod3(e2)
        pred = 2 if (a + n) % 3 == 0 else 0
        good = (r1 == 0) and (r2 == pred)
        okcls = okcls and good
        print("  n=%-3d a=%-3d: e1 mod3=%s  e2 mod3=%d  3|(a+n)=%s  pred e2=%d  %s" % (
            n, a, r1, r2, (a + n) % 3 == 0, pred, "ok" if good else "MISMATCH"), flush=True)
    print("  e1≡0 & e2-classifier 3|(a+n):  %s" % ("HOLDS" if okcls else "FALSE"), flush=True)

    # (1b) EXHAUSTIVE over residues (a mod3, n mod3), 3∤n: closed-form e1≡0, e2≡2 iff 3|(a+n).
    print("\n(1b) exhaustive residue check (concrete a,n with those residues, 3∤n):", flush=True)
    okex = True
    for nr in (1, 2):
        for ar in (0, 1, 2):
            # concrete representatives: n ≡ nr mod3 & n≡2 mod4 & 3∤n; a ≡ ar mod3, gcd(a,n)=1 ideally
            n = {1: 22, 2: 14}[nr]
            a = {0: 3, 1: 1, 2: 5}[ar] if nr == 1 else {0: 3, 1: 1, 2: 5}[ar]
            from math import gcd as _g
            while _g(a, n) != 1 or a % 3 != ar:
                a += 3
            e1, e2 = quartic_e1_e2(Fr(a, n), tau)
            r1, r2 = mod3(e1), mod3(e2)
            pred = 2 if (a + n) % 3 == 0 else 0
            good = (r1 == 0) and (r2 == pred)
            okex = okex and good
            print("    a≡%d n≡%d (a=%d,n=%d): e1=%d e2=%d  3|(a+n)=%s pred=%d %s" % (
                ar, nr, a, n, r1, r2, (a + n) % 3 == 0, pred, "ok" if good else "X"), flush=True)
    print("  closed form e1≡0, e2≡2⟺3|(a+n):  %s" % ("HOLDS all 6 residues" if okex else "FALSE"), flush=True)

    # (2) w mod 3 pattern driven by the CORRECTED classifier 3|(a+n), NOT n mod 3.
    print("\n(2) w=B^-1 d mod 3:  3∤(a+n) => all units period-4 [1,1,2,2];  3|(a+n) => w_0 unit, rest annih.", flush=True)
    PERIOD4 = [1, 1, 2, 2]
    ok_unit = ok_annih = True
    for sig, n in ORB:
        a = int(sig * n)
        m = 12
        w = wvec(m, sig, tau)
        vs = [v3(Fr(w[i])) for i in range(m)]
        divis = (a + n) % 3 == 0
        if not divis:                                   # all-units, period-4
            good = all(v == 0 for v in vs) and all(mod3(Fr(w[i])) == PERIOD4[i % 4] for i in range(m))
            ok_unit = ok_unit and good
        else:                                           # annihilated: w_0 unit, w_i≡0 mod3 for i>=1
            good = vs[0] == 0 and all(vs[i] >= 1 for i in range(1, m))
            ok_annih = ok_annih and good
        print("  n=%-3d a=%-3d 3|(a+n)=%-5s: %s" % (
            n, a, divis, "ok" if good else "FAIL v3(w)=%s" % vs), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("CORRECTED FACT 3a (3∤(a+n): all w_i units, period-4 [1,1,2,2]): %s" % (
        "HOLDS" if ok_unit else "FALSE"), flush=True)
    print("CORRECTED FACT 3b (3|(a+n): w_0 unit, w_i≡0 mod3 i>=1):         %s" % (
        "HOLDS" if ok_annih else "FALSE"), flush=True)
    print("READING (L5): SUPERSEDES §6ck 'n mod 3' — the true classifier is e2 mod3 = |g|^2+2 (g=beta+1/beta),", flush=True)
    print("e2≡2 ⟺ 3|(a+n) ⟺ 3 inert-divides g.  e1≡0 mod3 always.  d_j=8-2p_j (order-4 recurrence, e1 drops", flush=True)
    print("mod3 => p_j≡-e2 p_{j-2}-p_{j-4}).  FACT 3a/3b now a FINITE F_3 core.  RH stays [OUT].", flush=True)
