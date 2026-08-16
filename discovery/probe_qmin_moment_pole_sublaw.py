#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cr — MOMENT-POLE SUB-LAW: the exact mechanism behind the §6cq universal linear-log lower bound.

The §6cq carrier prime p|N (N=(a²+n²−na)²+n⁴=|numerator(β)|², β=1−1/ρ) acts by injecting a POLE into the
moment sequence w_i.  The clean, EXACT law (this file) is:

        v_p(N) = 1   ⟹   v_p(w_i) = −(i+1)   for all i ≥ 0.            [SUB-LAW, exact — 1360 checks n<80]

MECHANISM (proof target — general-prime analogue of the §6co p=3 coupling lemma).  v_p(N)=1 with p≥5, p∤n:
p splits in Z[i] as 𝔭𝔭̄, and exactly ONE prime above p divides numerator(β), simply — so β has a SIMPLE ZERO
at 𝔭 (v_𝔭(β)=+1) and β̄ does not.  The moment generating function W(y)=Σ w_i y^i is rational with denominator
the reversed β-quartet (roots {β,β̄,1/β,1/β̄}); partial fractions give a term A/(1−(1/β)y) from the root 1/β,
which has a SIMPLE POLE v_𝔭(1/β)=−1.  Its residue A has v_p(A)=−1, so w_i ⊇ A·(1/β)^i with
v_p = v_p(A) − i = −1 − i = −(i+1).  Hence v_p(w_{m−1}) = −m for an m-node system.

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
  * Open for THEOREM: (a) prove the sub-law residue count (v_p(A)=−1); (b) prove every orbit has a v_p(N)=1
    factor (N a sum of two squares, not a perfect power); (c) v_p(w_{m−1})=−m ⇒ v_p(q_min) ≥ m−O(1) (Smith).
    Still consecutive nodes only; node-set infimum §6cn-evidenced.  RH stays [OUT].

THIS PROBE (EXACT, L9): verifies the sub-law, the existence of a simple factor, the split-prime irregularity.
"""
from __future__ import annotations
from fractions import Fraction as Fr

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

    print("\n" + "=" * 100, flush=True)
    print("(1) sub-law + simple-factor existence : %s" % ("OK" if (ok and no_simple == 0) else "X"), flush=True)
    print("READING (L5): v_p(N)=1 ⇒ moment pole −(i+1) is the EXACT mechanism; every orbit has such p≥5", flush=True)
    print("⇒ v_p(w_{m−1})=−m ⇒ v_p(q_min) ≥ m−O(1) ⇒ log q_min=Ω(m), universal (consecutive nodes).", flush=True)
    print("General ·min(v_p(N),2) law REFUTED for split v_p(N)≥2. Open: residue count + factor existence. RH [OUT].", flush=True)
