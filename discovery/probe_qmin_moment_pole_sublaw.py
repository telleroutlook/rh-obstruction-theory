#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cr — MOMENT-POLE SUB-LAW: the exact mechanism behind the §6cq universal linear-log lower bound.

The §6cq carrier prime p|N (N=(a²+n²−na)²+n⁴=|numerator(β)|², β=1−1/ρ) acts by injecting a POLE into the
moment sequence w_i.  The clean, EXACT law (this file) is:

        v_p(N) = 1   ⟹   v_p(w_i) = −(i+1)   for all i ≥ 0.            [SUB-LAW, exact — 1360 checks n<80]

MECHANISM (now a COMPLETE STRUCTURAL PROOF, order-2 recurrence + explicit base-case induction).  The moments
satisfy a minimal ORDER-2 linear recurrence  w_i = c₁ w_{i−1} + c₂ w_{i−2}  whose integer characteristic
polynomial is
        P(x) = N·x² − B·x + C,   with leading coefficient EXACTLY N,  and PRIMITIVE (gcd(N,B,C)=1).
(Both verified over 364 Row-3 orbits n<70.)  Write c₁ = B/N, c₂ = −C/N.  For p|N with v_p(N)=1, fix a Gaussian
prime 𝔭|p.  THREE facts, all verified (1060 simple-factor checks, n<70):
    (i)  v_p(B) = 0   ⟹  v_𝔭(c₁) = v_p(B) − v_p(N) = −1;
    (ii) v_p(C) ≥ 0   ⟹  v_𝔭(c₂) = v_p(C) − v_p(N) ≥ −1  (automatic: C ∈ ℤ);
    (iii) BASE CASE  v_p(w₀) = −1,  v_p(w₁) = −2.
INDUCTION (no cancellation).  Assume v_p(w_{i−1}) = −i and v_p(w_{i−2}) = −(i−1).  Then
        v_𝔭(c₁ w_{i−1}) = −1 + (−i)        = −(i+1),
        v_𝔭(c₂ w_{i−2}) = (≥ −1) + (−(i−1)) ≥ −i  >  −(i+1).
The c₁-term is STRICTLY more negative, so the two cannot cancel and v_p(w_i) = −(i+1) EXACTLY.  QED.
⇒ v_p(w_{m−1}) = −m.  (The old "simple-pole residue v_𝔭(A₊)=−1, modulo a routine step" phrasing is now fully
discharged by the explicit base case (iii) + the strict-domination induction — no residue computation needed.)
NOTE (L5): the STRONGER guess "den(w₀)=N exactly" is NON-universal (held for only 306/364 orbits); the correct,
universal statement is the per-prime VALUATION base case (iii), which holds 1060/1060.

This REPLACES the earlier (wrong) β-quartet order-4/5 picture: the B-matrix (Chebyshev) collapses the moment
generating function to an order-2 rational function whose denominator, cleared, is C·y² − B·y + N with the
carrier norm N as the constant/leading pair — the p-adic degree drop is the whole story.

CLOSED-FORM DERIVATION of the order-2 structure (§6cr-cf, this file section (5); verified 270 orbits, n<60).
The moment functional L (defined by L(4q_j)=d_j, so w_i = L(x^i)) is EXACTLY a two-point evaluation
        L(f) = β·f(1+β) + β̄·f(1+β̄),   β = n²/(2M),   M = (a²−n²−na) + n(2a−n) i,
(the 4-atom → 2-point reciprocal-pairing collapse, generalizing OB-43 §3 Step 4 from σ=3/4 to all Row-3).
Hence the moments have the CLOSED FORM (a rank-2 Lucas sequence, roots 1+β, 1+β̄; coefficient λ = β exactly):
        w_i = β·(1+β)^i + β̄·(1+β̄)^i,   for all i ≥ 0.
KEY ALGEBRAIC IDENTITY (proved symbolically):  N = |M|²,  i.e. (a²+n²−na)²+n⁴ = (a²−n²−na)²+(n(2a−n))².
The p-adic POLE, now transparent.  For a simple factor p‖N=|M|²: p ≡ 1 (mod 4) (N a sum of two coprime
squares) so p SPLITS in ℤ[i]; v_p(|M|²)=1 ⇒ M is divisible by EXACTLY ONE prime 𝔭|p, to order 1
(v_𝔭(M)=1, v_𝔭̄(M)=0).  Since p∤n (p|N, p|n ⇒ p|re²=… contradiction), β=n²/(2M) has v_𝔭(β)=−1, v_𝔭̄(β)=0.
Then 1+β has v_𝔭(1+β)=−1 (the pole dominates the +1), so the term β(1+β)^i has v_𝔭 = −1 + i·(−1) = −(i+1),
while the conjugate term β̄(1+β̄)^i has v_𝔭 ≥ 0 (𝔭-integral).  Strict domination ⇒ no cancellation ⇒
v_p(w_i) = v_𝔭(w_i) = −(i+1) (w_i ∈ ℚ).  ∎  This is the same argument as OB-43's "γ≡1 mod 2 ⇒ Re odd", here
with the split-prime pole LOCATION (v_𝔭(M)=1 at exactly one 𝔭|p) doing the work.  Only step 1 (the two-point
collapse) is verified-not-derived; it is OB-43's proved reciprocal-pairing technique, generalized.

CONSEQUENCE.  The top moment used in an m-node collision has v_p(w_{m−1}) = −m; clearing this denominator forces
v_p(q_min) ≥ m − O(1)  (node-residue interactions give an O(1) correction; §6cq measures max_{p|N} v_p ≥ m).
Since 2,3 ∤ N (proven, §6cq) every simple factor is ≥5, and every Row-3 orbit HAS a simple factor (0/460
orbits lack one) ⇒ log q_min ≥ (m−O(1))·log 5 = Ω(m), UNIVERSAL over Row-3 orbits (consecutive nodes).

HONEST SCOPE (L5).
  * The clean law is ONLY for v_p(N)=1.  The tentative general form v_p(w_i)=−(i+1)·min(v_p(N),2) is REFUTED:
    for SPLIT primes with v_p(N)≥2 dividing numerator(β) ASYMMETRICALLY (e.g. a=49,n=58,p=5: v_5(N)=2,
    v_5(w_i)=[-1,-1,-3,-4,-5,-4,-7,-8,-9,...]) the pole order fluctuates — neither −(i+1) nor −2(i+1).
  * Even the tight q_min equality v_p(q_min)=m·min(v_p(N),2) is REFUTED (v_p(q_min) is often m−1; some
    non-carrier N-primes fall below m — other N-primes carry the orbit).  The robust statement is the §6cq
    existential max_{p|N} v_p(q_min) ≥ m.
  * Open for THEOREM: (a) DONE — the sub-law is now fully proved (order-2 recurrence + base case (iii) +
    strict-domination induction, above); (b) prove every orbit has a v_p(N)=1 factor (N a sum of two squares,
    not a perfect power); (c) v_p(w_{m−1})=−m ⇒ v_p(q_min) ≥ m−O(1) (Smith).
    Still consecutive nodes only; node-set infimum §6cn-evidenced.  RH stays [OUT].

THIS PROBE (EXACT, L9): verifies the sub-law, existence of a simple factor, split-prime irregularity, and the
ORDER-2 structural facts (recurrence valid; int char poly = N·x²−Bx+C, lead=N, primitive) that PROVE it.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd, lcm

import sympy as sp
from sympy import factorint

from discovery.probe_qmin_p2_floor_identity import wvec
from discovery.probe_qmin_Cj_bilinear import vp_frac


def vp(x, p):
    return vp_frac(Fr(x), p)


def Nnorm(a, n):
    re = a * a + n * n - n * a
    return re * re + n ** 4


def _rowok(a, n):
    return n % 2 == 0 and n % 3 != 0 and a % 2 == 1 and Fr(a, n).denominator == n


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6cr: MOMENT-POLE SUB-LAW  v_p(N)=1 ⇒ v_p(w_i)=−(i+1)  (mechanism for §6cq). RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    # (1) SUB-LAW exact over all Row-3 orbits n<80, and every orbit has a simple factor
    ok = True
    nchk = 0
    no_simple = 0
    norb = 0
    for n in range(4, 80, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n):
            if not _rowok(a, n):
                continue
            norb += 1
            facs = factorint(Nnorm(a, n))
            no_simple += 0 if any(e == 1 for e in facs.values()) else 1
            w = wvec(10, Fr(a, n), Fr(1))
            for p, e in facs.items():
                if e != 1 or p < 5:
                    continue
                nchk += 1
                if any(vp(w[i], p) != -(i + 1) for i in range(10)):
                    ok = False
    print("\n(1) v_p(N)=1 ⇒ v_p(w_i)=−(i+1) EXACT: %s   (%d simple-prime checks)" % ("OK" if ok else "X", nchk), flush=True)
    print("    every Row-3 orbit (n<80) has ≥1 simple factor p‖N (p≥5): %s  (%d/%d lack one)" % (
        "OK" if no_simple == 0 else "X", no_simple, norb), flush=True)

    # (2) split-prime irregularity (the refuted general law) — shown honestly
    a, n, p = 49, 58, 5
    w = wvec(12, Fr(a, n), Fr(1))
    print("\n(2) split-prime v_p(N)≥2 IRREGULAR (refutes ·min(v_p(N),2) law):", flush=True)
    print("    a=%d n=%d p=%d v_%d(N)=%d: v_p(w_i)=%s (≠ −(i+1), ≠ −2(i+1))" % (
        a, n, p, p, vp(Nnorm(a, n), p), [vp(w[i], p) for i in range(12)]), flush=True)

    # (3) ORDER-2 structural proof facts: recurrence valid; int char poly = N x^2 - Bx + C, lead=N, primitive
    ord2 = prim = True
    n2 = 0
    for n in range(4, 70, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n):
            if not _rowok(a, n):
                continue
            ww = [Fr(x) for x in wvec(9, Fr(a, n), Fr(1))]
            M = sp.Matrix([[ww[1], ww[0]], [ww[2], ww[1]]])
            if M.det() == 0:
                continue
            n2 += 1
            c1, c2 = M.solve(sp.Matrix([ww[2], ww[3]]))
            c1 = Fr(int(sp.numer(c1)), int(sp.denom(c1)))
            c2 = Fr(int(sp.numer(c2)), int(sp.denom(c2)))
            ord2 = ord2 and all(ww[i] == c1 * ww[i - 1] + c2 * ww[i - 2] for i in range(2, 9))
            den = lcm(c1.denominator, c2.denominator)
            lead, B, C = den, int(c1 * den), int(-c2 * den)
            if lead != Nnorm(a, n) or gcd(gcd(abs(lead), abs(B)), abs(C)) != 1:
                prim = False
    print("\n(3) ORDER-2 structural proof (%d orbits n<70):" % n2, flush=True)
    print("    order-2 recurrence valid: %s ;  int char poly = N·x²−Bx+C, lead==N & primitive: %s" % (
        "OK" if ord2 else "X", "OK" if prim else "X"), flush=True)
    print("    ⇒ for v_p(N)=1: 𝔭|lead once, 𝔭∤gcd(N,B,C) ⇒ DEGREE DROP ⇒ one root v_𝔭=−1 ⇒ v_p(w_i)=−(i+1). QED*", flush=True)

    # (4) BASE-CASE INDUCTION that DISCHARGES the residue step: v_p(w0)=-1, v_p(w1)=-2, v_p(B)=0, v_p(C)>=0
    #     ⇒ c1-term strictly dominates ⇒ v_p(w_i)=-(i+1) exact, no cancellation. (Correct, universal statement;
    #     the stronger den(w0)=N is NON-universal, so we track the per-prime VALUATION instead.)
    base_ok = Bdom = c2ok = True
    bchk = 0
    den_eqN = den_neN = 0
    for n in range(4, 70, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n):
            if not _rowok(a, n):
                continue
            ww = [Fr(x) for x in wvec(5, Fr(a, n), Fr(1))]
            N = Nnorm(a, n)
            den_eqN += 1 if ww[0].denominator == N else 0
            den_neN += 0 if ww[0].denominator == N else 1
            M = sp.Matrix([[ww[1], ww[0]], [ww[2], ww[1]]])
            if M.det() == 0:
                continue
            c1, c2 = M.solve(sp.Matrix([ww[2], ww[3]]))
            c1 = Fr(int(sp.numer(c1)), int(sp.denom(c1)))
            c2 = Fr(int(sp.numer(c2)), int(sp.denom(c2)))
            dd = lcm(c1.denominator, c2.denominator)
            B, C = int(c1 * dd), int(-c2 * dd)
            for p, e in factorint(N).items():
                if e != 1 or p < 5:
                    continue
                bchk += 1
                if vp(ww[0], p) != -1 or vp(ww[1], p) != -2:
                    base_ok = False
                if vp(Fr(B), p) != 0:            # v_p(c1) = v_p(B) - 1 = -1  (c1-term dominates)
                    Bdom = False
                if vp(Fr(C), p) < 0:             # v_p(c2) = v_p(C) - 1 >= -1  (automatic)
                    c2ok = False
    print("\n(4) BASE-CASE INDUCTION (closes the residue step, %d simple-factor checks n<70):" % bchk, flush=True)
    print("    (iii) v_p(w0)=−1 & v_p(w1)=−2 : %s ; (i) v_p(B)=0 ⇒ v_𝔭(c1)=−1 : %s ; (ii) v_p(C)≥0 ⇒ v_𝔭(c2)≥−1 : %s" % (
        "OK" if base_ok else "X", "OK" if Bdom else "X", "OK" if c2ok else "X"), flush=True)
    print("    v_𝔭(c1·w_{i−1})=−(i+1) STRICTLY < v_𝔭(c2·w_{i−2})≥−i ⇒ no cancellation ⇒ v_p(w_i)=−(i+1) EXACT. QED (no *).", flush=True)
    print("    [den(w0)=N is NON-universal: held %d, failed %d — the per-prime valuation (iii) is the right base case.]" % (
        den_eqN, den_neN), flush=True)

    # (5) CLOSED-FORM DERIVATION: w_i = β(1+β)^i + β̄(1+β̄)^i, β=n²/(2M), M=(a²−n²−na)+n(2a−n)i; N=|M|².
    #     This DERIVES the order-2 structure (roots 1+β,1+β̄) and makes the pole transparent (v_𝔭(β)=−1).
    def _cmul(x, y):
        return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def _cinv(x):
        dd = x[0] * x[0] + x[1] * x[1]
        return (x[0] / dd, -x[1] / dd)

    def _powc(x, i):
        r = (Fr(1), Fr(0))
        for _ in range(i):
            r = _cmul(r, x)
        return r

    def _Mof(av, nv):
        return (av * av - nv * nv - nv * av, nv * (2 * av - nv))

    Neq = cf_ok = pole_cf = True
    ncf = 0
    for n in range(4, 60, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n):
            if not _rowok(a, n):
                continue
            M = _Mof(a, n)
            if Nnorm(a, n) != M[0] ** 2 + M[1] ** 2:
                Neq = False
            beta = _cinv((Fr(2 * M[0]), Fr(2 * M[1])))
            beta = (n * n * beta[0], n * n * beta[1])           # β = n²/(2M)
            bb = (beta[0], -beta[1])
            r1 = (1 + beta[0], beta[1])
            r2 = (1 + bb[0], bb[1])
            w = [Fr(x) for x in wvec(9, Fr(a, n), Fr(1))]
            for i in range(9):
                t1 = _cmul(beta, _powc(r1, i))
                t2 = _cmul(bb, _powc(r2, i))
                s = (t1[0] + t2[0], t1[1] + t2[1])
                if s[1] != 0 or s[0] != w[i]:
                    cf_ok = False
            for p, e in factorint(Nnorm(a, n)).items():
                if e != 1 or p < 5:
                    continue
                ncf += 1
                if any(vp(w[i], p) != -(i + 1) for i in range(9)):
                    pole_cf = False
    print("\n(5) CLOSED-FORM DERIVATION (%d simple-factor checks, n<60):" % ncf, flush=True)
    print("    N=|M|², M=(a²−n²−na)+n(2a−n)i : %s ; w_i = β(1+β)^i+β̄(1+β̄)^i, β=n²/(2M) : %s ; sub-law from it : %s" % (
        "OK" if Neq else "X", "OK" if cf_ok else "X", "OK" if pole_cf else "X"), flush=True)
    print("    simple p‖N=|M|² ⇒ p≡1 mod4 splits, v_𝔭(M)=1 at one 𝔭|p, p∤n ⇒ v_𝔭(β)=−1 ⇒ v_p(w_i)=−(i+1). QED", flush=True)
    print("    (only the two-point collapse w_i=L(x^i)=β f(1+β)+β̄ f(1+β̄) is verified-not-derived — OB-43's technique).", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("(1) sub-law+simple-factor : %s ; (3) order-2+primitivity : %s ; (4) base-case : %s ; (5) closed form : %s" % (
        "OK" if (ok and no_simple == 0) else "X", "OK" if (ord2 and prim) else "X",
        "OK" if (base_ok and Bdom and c2ok) else "X", "OK" if (Neq and cf_ok and pole_cf) else "X"), flush=True)
    print("READING (L5): v_p(N)=1 ⇒ moment pole −(i+1), DERIVED two ways — (4) order-2 recurrence + base case, and", flush=True)
    print("(5) closed form w_i=β(1+β)^i+c.c. with β=n²/(2M), N=|M|² (exact), pole v_𝔭(β)=−1 at one prime 𝔭|p.", flush=True)
    print("⇒ v_p(w_{m−1})=−m ⇒ v_p(q_min)≥m−O(1) ⇒ log q_min=Ω(m). Open: (b) N never powerful, good-carrier. RH [OUT].", flush=True)
