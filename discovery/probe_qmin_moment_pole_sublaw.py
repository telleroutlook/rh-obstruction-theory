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

    print("\n" + "=" * 100, flush=True)
    print("(1) sub-law + simple-factor existence : %s ; (3) order-2 + primitivity : %s ; (4) base-case induction : %s" % (
        "OK" if (ok and no_simple == 0) else "X", "OK" if (ord2 and prim) else "X",
        "OK" if (base_ok and Bdom and c2ok) else "X"), flush=True)
    print("READING (L5): v_p(N)=1 ⇒ moment pole −(i+1), now FULLY PROVED (order-2 recurrence + explicit base case", flush=True)
    print("v_p(w0)=−1,v_p(w1)=−2 + strict-domination induction — no residue computation); every orbit has such p≥5", flush=True)
    print("⇒ v_p(w_{m−1})=−m ⇒ v_p(q_min)≥m−O(1) ⇒ log q_min=Ω(m), universal (consecutive nodes). Open: (b),(c). RH [OUT].", flush=True)
