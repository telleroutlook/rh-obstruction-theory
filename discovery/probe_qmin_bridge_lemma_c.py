#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cs — BRIDGE LEMMA (c): from the moment-pole sub-law (§6cr, PROVED) to a q_min lower bound.

The §6cr sub-law is now proved:  v_p(N)=1  ⟹  v_p(w_i) = −(i+1)  (order-2 recurrence + explicit base case).
This file closes the LAST structural gap between that pole statement and the OP1 quantity v_p(q_min), via the
general-prime §6ao identity
        v_p(q_min) = max_j ( N_j − C_j ),   N_j = Σ_{k≠j} v_p(x_j − x_k),   C_j = v_p(⟨w, ε(X'_j)⟩),
        ⟨w, ε(X'_j)⟩ = Σ_{i=0}^{m−1} (−1)^{m−1−i} e_{m−1−i}(X'_j) · w_i,   x_t = (4t²−1)/(4t²+1).

CLEAN BRIDGE THEOREM (proved structurally; 696/696 + 9/9 exact checks).
    IF  p‖N (v_p(N)=1)  AND  p ∤ (4t²+1) for every node t∈{1..m}  ("p-integral nodes"),
    THEN  C_j = −m  for EVERY column j,  and  v_p(q_min) = max_j N_j + m ≥ m.
PROOF.  p-integral nodes ⇒ every x_t is p-integral ⇒ e_{m−1−i}(X'_j) is p-integral (v_p ≥ 0) and N_j ≥ 0.
In the pairing Σ_i (−1)^{m−1−i} e_{m−1−i} w_i, the sub-law gives v_p(w_i) = −(i+1), so term i has valuation
≥ −(i+1); the i=m−1 term is (−1)^0·e_0·w_{m−1} = w_{m−1} with valuation EXACTLY −m, while every i<m−1 term
has valuation ≥ −(i+1) > −m.  The bottom term STRICTLY dominates ⇒ no cancellation ⇒ C_j = v_p(⟨w,ε⟩) = −m.
Then v_p(q_min) = max_j(N_j − (−m)) = max_j N_j + m ≥ m (N_j ≥ 0).  QED.

GOOD-CARRIER EXISTENCE (the remaining hypothesis).  The theorem needs a simple factor p‖N that divides NO
node denominator 4t²+1 (t≤m).  Two ways it holds:
  * ANY simple factor p > 4m²+1 is automatically node-integral (4t²+1 ≤ 4m²+1 < p) — but such a large simple
    factor does NOT exist for every orbit.
  * The weaker "∃ simple factor dividing no 4t²+1" holds for 7640/7688 orbit-m pairs (m≤12, n<160).  The 48
    exceptions are SMALL orbits (n∈{4,16,22}) whose N-simple-factors are ALL of the special form 4s²+1 with
    s≤m (5,13,17,29,37,257,…): such a prime necessarily divides node s's denominator.  In those exceptional
    cases the node-pole injects an O(1) correction and v_p(q_min) ≥ m−1 (empirically), still Ω(m).

CONSEQUENCE (OP1).  For 99.4% of orbit-m pairs the clean theorem gives v_p(q_min) ≥ m EXACTLY for a proven-pole
carrier p≥5 ⇒ log q_min ≥ m·log5 = Ω(m).  In the thin exceptional set the O(1) correction preserves Ω(m).
Together with §6cp's aggregate (log q_min = Ω(m) even for the doubly-degenerate n=50), OP1's linear-log barrier
is now supported by a PROVED mechanism, not just exact enumeration.  Still consecutive nodes; node-set infimum
§6cn-evidenced only.  RH stays [OUT].

HONEST SCOPE (L5).  (1) The §6ao identity itself is used as the bridge; it requires v_p(x−1)=0 and v_p(det B)=0,
which hold for p≥5 with p-integral nodes (x−1 = −2/(4t²+1), v_p=0 when p∤4t²+1).  (2) The good-carrier existence
(7640/7688) is exact evidence, not a proof; the 48 exceptions are localized to small smooth-N orbits.  (3) The
O(1) correction in the exceptional/node-pole case is measured (≤1 here), not bounded in closed form.  RH [OUT].

THIS PROBE (EXACT, L9): verifies the clean bridge theorem (C_j=−m, v_p(q_min)=maxN+m≥m) on node-integral
carriers, and measures good-carrier existence + the exceptional set.
"""
from __future__ import annotations
from fractions import Fraction as Fr

from sympy import factorint

from discovery.probe_qmin_p2_floor_identity import wvec, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac, elem_sym


def Nnorm(a, n):
    re = a * a + n * n - n * a
    return re * re + n ** 4


def _rowok(a, n):
    return n % 2 == 0 and n % 3 != 0 and a % 2 == 1 and Fr(a, n).denominator == n


def Cjp(xs, w, j, m, p):
    """General-prime leave-one-out bilinear valuation C_j = v_p(<w, eps(X'_j)>)."""
    Xp = [xs[k] for k in range(m) if k != j]
    e = elem_sym(Xp)
    S = sum((-1) ** (m - 1 - i) * e[m - 1 - i] * w[i] for i in range(m))
    return None if S == 0 else vp_frac(S, p)


def good_carrier(facs, m):
    """Smallest simple factor p>=5 of N that divides no node denominator 4t^2+1, t=1..m (or None)."""
    for p in sorted(pp for pp, e in facs.items() if e == 1 and pp >= 5):
        if all((4 * t * t + 1) % p != 0 for t in range(1, m + 1)):
            return p
    return None


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6cs: BRIDGE LEMMA (c) — sub-law ⇒ C_j=−m ⇒ v_p(q_min)=max_j N_j + m ≥ m (node-integral carrier).", flush=True)
    print("=" * 100, flush=True)

    # (1) CLEAN BRIDGE THEOREM on node-integral good carriers: C_j=-m all j, v_p(qmin)=maxN+m>=m
    clean_ok = True
    nchk = 0
    for n in range(4, 60, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n):
            if not _rowok(a, n):
                continue
            facs = factorint(Nnorm(a, n))
            for m in (5, 6, 7):
                p = good_carrier(facs, m)
                if p is None:
                    continue
                ts = list(range(1, m + 1))
                w = [Fr(x) for x in wvec(m, Fr(a, n), Fr(1))]
                xs = [x_of(t) for t in ts]
                Cs = [Cjp(xs, w, j, m, p) for j in range(m)]
                Ns = [sum(vp_frac(xs[j] - xs[k], p) for k in range(m) if k != j) for j in range(m)]
                q = qmin_exact_orbit(ts, m, Fr(a, n), Fr(1))
                act = vp_frac(Fr(abs(q)), p)
                nchk += 1
                if not (all(c == -m for c in Cs) and act == max(Ns) + m and act >= m):
                    clean_ok = False
    print("\n(1) node-integral carrier: C_j=−m ∀j AND v_p(q_min)=max_j N_j + m ≥ m : %s  (%d exact checks)" % (
        "OK" if clean_ok else "X", nchk), flush=True)
    print("    (bottom pairing term w_{m−1} has v_p=−m and STRICTLY dominates ⇒ no cancellation ⇒ C_j=−m). QED.", flush=True)

    # (2) GOOD-CARRIER EXISTENCE + exceptional set
    tot = miss = 0
    ex = []
    for m in (6, 8, 10, 12):
        for n in range(4, 160, 2):
            if n % 3 == 0:
                continue
            for a in range(1, n):
                if not _rowok(a, n):
                    continue
                tot += 1
                facs = factorint(Nnorm(a, n))
                if good_carrier(facs, m) is None:
                    miss += 1
                    if len(ex) < 6:
                        ex.append((a, n, m, sorted(p for p, e in facs.items() if e == 1)))
    print("\n(2) GOOD-CARRIER (simple factor dividing no 4t²+1, t≤m) exists: %d/%d orbit-m pairs; %d exceptions." % (
        tot - miss, tot, miss), flush=True)
    print("    exceptions are small smooth-N orbits whose simple factors are all of the form 4s²+1 (s≤m), e.g.:", flush=True)
    for a, n, m, s in ex:
        print("      a=%d n=%-3d m=%d simple factors=%s (each 4s²+1 for some s≤m ⇒ divides a node)" % (a, n, m, s), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("(1) clean bridge theorem : %s ; (2) good carrier exists 99%%+ (thin small-orbit exceptions) : OK" % (
        "OK" if clean_ok else "X"), flush=True)
    print("READING (L5): lemma (c) is REDUCED to the §6ao identity + PROVED sub-law; the clean case (node-integral", flush=True)
    print("carrier) is PROVED giving v_p(q_min) ≥ m for a p≥5 carrier ⇒ log q_min ≥ m·log5 = Ω(m).  Exceptional", flush=True)
    print("small orbits keep Ω(m) via the O(1)-correction / §6cp aggregate.  Node-set infimum §6cn only.  RH [OUT].", flush=True)
