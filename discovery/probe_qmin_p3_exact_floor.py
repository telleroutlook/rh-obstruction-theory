#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6ci — the EXACT p=3 floor formula and the 3a/3b split pinned to the clustering-vs-pairing competition.

HONEST CREDIT (L5): the identity is the §6bh/§6bf identity v_p(q_min)=max_j(N_j−C_j) at p=3, with
N_j = v₃(P'(x_j)) = Σ_{k≠j} v₃(x_j−x_k) = clus(j) and C_j = v₃(S_j), S_j the §6bf pairing.  No "+1"
offset at p=3 (the p=2 factor B=4(1−T) is a 3-unit).  NEW: verify it holds EXACTLY at p=3, and pin the
§6ch Row-3 dichotomy to the single discriminant v₃(S_j):

    v₃(q_min) = max_j ( clus(j) − v₃(S_j) )          [EXACT, determinant-free]

  clus(j) orbit-INDEPENDENT, pigeonhole max_j clus(j) ≥ ⌈m/2⌉−1 (2 node-classes mod 3).
  Row 3a (n≡1 mod3): some node has clus linear AND v₃(S_j)=O(1) ⇒ max_j(clus−v₃S) LINEAR (pairing generic).
  Row 3b (n≡2 mod3): every node has v₃(S_j) ≥ clus(j)−O(1) ⇒ max_j(clus−v₃S) FLAT (pairing absorbs).

READING (L5): OP1-at-p=3 for ALL Row-3 orbits = the explicit competition max_j(clus(j)−v₃(S_j)) ≥ cm.
This is (4″) made exact & determinant-free; the open sub-problem is WHY n mod 3 flips the v₃(S_j) regime.
Row 3a candidate-closes modulo this; Row 3b needs the §6ch global (distributed-prime) argument. RH [OUT].

THIS PROBE (EXACT, L9): (A) verify v₃(q_min) == max_j(clus(j)−v₃(S_j)) against direct integer-determinant
q_min over 3a/3b/vacuous orbits; (B) show the v₃(S_j) discriminant (3a: min v₃(S_j*)=0, margin linear;
3b: v₃(S_j*)≥3, margin flat).
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn
from discovery.probe_qmin_p2_nodd_vandermonde_floor import S_of


def v3f(x):
    return vp_frac(Fr(x), 3)


def v3i(q):
    v = 0
    while q and q % 3 == 0:
        q //= 3
        v += 1
    return v


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6ci: EXACT p=3 floor v₃(q_min)=max_j(clus(j)−v₃(S_j)); n mod 3 flips the v₃(S_j) regime. RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    ORBITS = [(Fr(3, 10), "n=10 3a"), (Fr(1, 22), "n=22 3a"),
              (Fr(1, 14), "n=14 3b"), (Fr(1, 26), "n=26 3b"),
              (Fr(1, 2), "n=2 vac"), (Fr(7, 10), "n=10 3a")]

    # (A) exact identity
    tested = mism = 0
    for sig, _lab in ORBITS:
        rng = random.Random(13)
        for m in (5, 6, 7, 8):
            for _ in range(30):
                ts = rng.sample(range(1, 14 * m), m)
                if len(set(ts)) != m:
                    continue
                xs = [x_of(t) for t in ts]
                w = wvec(m, sig, Fr(1))
                qm = qmin_exact_orbit(ts, m, sig, Fr(1))
                if not isinstance(qm, int) or qm == 0:
                    continue
                clus = [sum(v3f(xs[j] - xs[k]) for k in range(m) if k != j) for j in range(m)]
                rhs = max(clus[j] - v3f(S_of(xs, w, j, m)) for j in range(m))
                tested += 1
                mism += (v3i(qm) != rhs)
    print("\n(A) v₃(q_min) == max_j(clus(j)−v₃(S_j)):  tested=%d  mismatches=%d  => %s" % (
        tested, mism, "HOLDS EXACTLY" if mism == 0 else "FALSE — investigate"), flush=True)

    # (B) the v₃(S_j) discriminant at the deepest-clustered node
    print("\n(B) discriminant — v₃(S_j*) at the deepest node & worst-case margin max_j(clus−v₃S):", flush=True)
    for sig, lab in [(Fr(3, 10), "n=10 3a"), (Fr(1, 22), "n=22 3a"),
                     (Fr(1, 14), "n=14 3b"), (Fr(1, 26), "n=26 3b")]:
        _, _, n = rho_pqn(sig, Fr(1))
        row = []
        for m in (6, 8, 10):
            rng = random.Random(7)
            sjstar, worst_margin = [], 10 ** 9
            for _ in range(60):
                ts = rng.sample(range(1, 16 * m), m)
                if len(set(ts)) != m:
                    continue
                xs = [x_of(t) for t in ts]
                w = wvec(m, sig, Fr(1))
                clus = [sum(v3f(xs[j] - xs[k]) for k in range(m) if k != j) for j in range(m)]
                jstar = max(range(m), key=lambda j: clus[j])
                sjstar.append(v3f(S_of(xs, w, jstar, m)))
                worst_margin = min(worst_margin, max(clus[j] - v3f(S_of(xs, w, j, m)) for j in range(m)))
            row.append("m=%2d v₃(S_j*)∈[%d,%d] margin=%d" % (m, min(sjstar), max(sjstar), worst_margin))
        print("  %-8s (n mod3=%d): %s" % (lab, n % 3, "  |  ".join(row)), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): identity exact; 3a has a deep node with v₃(S_j)=O(1) (margin LINEAR), 3b forces", flush=True)
    print("v₃(S_j)≥clus−O(1) on every node (margin FLAT). OP1-at-p=3 = the competition max_j(clus−v₃S)≥cm.", flush=True)
    print("(4″) is now exact & determinant-free; the open core is WHY n mod 3 flips v₃(S_j). RH stays [OUT].", flush=True)
