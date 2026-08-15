#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3: the PAIRWISE-SWAP lemma bounding min-psi by same-class rep distance.

LEMMA (candidate [THM]; verify per L9).  Work in a packed regime with a Phi=0 minimizer
structure (navail = m-1 distinct classes; K >= m nodes so some class has >= 2 reps).
Let a, b be two on-line nodes in the SAME x-class.  Dropping the OTHER node of that
class (resp.) from the full node set gives two (m-1)-subsets S ∋ a and S' ∋ b that are
BOTH Phi-minimizers (each keeps one rep per class => Phi=0) with the IDENTICAL complement
C = (the singletons).  By the affine identity (§6o), with alpha = a_k/b_k determined by C,
    psi(S)  = v_p(x_a - alpha),   psi(S') = v_p(x_b - alpha)   (SAME alpha).
If both were >= d+1 then x_a ≡ x_b ≡ alpha (mod p^{d+1}), contradicting v_p(x_a-x_b)=d.
Hence
    min( psi(S), psi(S') )  <=  v_p(x_a - x_b).
Therefore  min over Phi-minimizers of psi  <=  min over swappable same-class pairs of
v_p(x_a - x_b).  PIGEONHOLE: K >= m nodes in m-1 classes force a class with >= 2 reps;
if two of its reps have s-values (t = base + p s) differing by a p-unit then
v_p(x_a - x_b) = 1  =>  min-psi <= 1.

This probe verifies, on packed collision configs (K = m .. m+2):
  (P1) the inequality  min(psi(S), psi(S')) <= v_p(x_a - x_b)  for EVERY same-class
       swappable pair (a,b) of a Phi=0 minimizer;
  (P2) the global bound  min-over-Phi-min psi  <=  min_{swappable pairs} v_p(x_a-x_b);
  (P3) how often a same-class pair with v_p(x_a-x_b)=1 exists (=> min-psi<=1).

HONESTY (L5): verifies a bounding lemma; it caps min-psi by the closest same-class rep
distance, NOT yet by an absolute constant (that needs the distance itself bounded).
EVIDENCE + a rigorous handle.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
import random

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A


def psi_of_subset(u, tlist, S, p):
    v = A.vpf(A.Psi_val(u, [A.x_of(tlist[k]) for k in S]), p)
    return v if v is not None else 10**9


def phi_of_subset(tlist, S, p):
    return A.Phi([A.x_of(tlist[k]) for k in S], p)


def deep_pool(p, m, K, S, rng):
    r = m - 1
    if r < 1 or r >= p:
        return None
    bases = rng.sample(range(1, p), r)
    pool, seen = [], set()
    for b in bases:
        t = b + p * rng.randrange(S)
        if t != 0 and t not in seen:
            pool.append(Fr(t)); seen.add(t)
    guard = 0
    while len(pool) < K and guard < 3000:
        guard += 1
        b = rng.choice(bases)
        t = b + p * rng.randrange(S)
        if t != 0 and t not in seen:
            pool.append(Fr(t)); seen.add(t)
    return pool if len(pool) == K else None


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3: pairwise-swap lemma  min(psi(S),psi(S')) <= v_p(x_a - x_b)",
          flush=True)
    print("Orbit D=425 (split-only).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    sig, tau = Fr(3, 4), Fr(1)
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260815)

    p1_ok = True; p1_tested = 0
    p2_ok = True; p2_tested = 0
    have_unit_pair = 0; configs = 0
    minpsi_le1_via_bound = 0

    for p in (7, 11):
        for m in range(3, 6):
            for K in (m, m + 1, m + 2):
                for _ in range(300):
                    pool = deep_pool(p, m, K, 27, rng)
                    if pool is None:
                        continue
                    oc, vo = cleared_columns(pool, sig, tau, m)
                    if not qmin_fast(oc, vo):
                        continue
                    tl = [Fr(t) for t in pool]
                    n = len(tl)
                    # Phi-minimizers among (m-1)-subsets
                    subs = list(combinations(range(n), m - 1))
                    phis = [phi_of_subset(tl, S, p) for S in subs]
                    minPhi = min(phis)
                    mins = [S for S, ph in zip(subs, phis) if ph == minPhi]
                    psis = [psi_of_subset(u, tl, S, p) for S in mins]
                    minpsi = min(psis)
                    if minpsi <= 0:
                        continue
                    configs += 1
                    # same-class node pairs
                    cls = [A.xres(A.x_of(t), p) for t in tl]
                    pair_dists = []
                    for a in range(n):
                        for b in range(a + 1, n):
                            if cls[a] is None or cls[a] != cls[b]:
                                continue
                            d = A.vpf(A.x_of(tl[a]) - A.x_of(tl[b]), p)
                            d = d if d is not None else 10**9
                            pair_dists.append(d)
                            # (P1) find Phi-min S ∋ a (a-only among the pair) and S' ∋ b
                            Sa = next((S for S in mins if a in S and b not in S), None)
                            Sb = next((S for S in mins if b in S and a not in S), None)
                            if Sa is not None and Sb is not None and \
                               set(Sa) - {a} == set(Sb) - {b}:
                                pa = psi_of_subset(u, tl, Sa, p)
                                pb = psi_of_subset(u, tl, Sb, p)
                                p1_tested += 1
                                if min(pa, pb) > d:
                                    p1_ok = False
                    if pair_dists:
                        p2_tested += 1
                        if minpsi > min(pair_dists):
                            p2_ok = False
                        if min(pair_dists) == 1:
                            have_unit_pair += 1
                            if minpsi <= 1:
                                minpsi_le1_via_bound += 1

    print("\n" + "=" * 96, flush=True)
    print(f"(P1) min(psi(S),psi(S')) <= v_p(x_a-x_b) for swappable pairs "
          f"({p1_tested} pairs): {p1_ok}", flush=True)
    print(f"(P2) min-over-Phi-min psi <= min_pair v_p(x_a-x_b) "
          f"({p2_tested} configs): {p2_ok}", flush=True)
    print(f"(P3) positive-min-psi packed collision configs: {configs}", flush=True)
    print(f"     with a same-class pair at v_p(x_a-x_b)=1 (=> bound gives <=1): "
          f"{have_unit_pair}", flush=True)
    print(f"     of those, min-psi actually <=1: {minpsi_le1_via_bound}", flush=True)
    print("\nREADING (L5): the pairwise-swap lemma caps min-psi by the CLOSEST same-class", flush=True)
    print("rep distance.  With K>=m a repeated class exists; a unit-gap pair forces", flush=True)
    print("min-psi<=1.  Rigorous handle; bounding the distance itself is the residual", flush=True)
    print("open step.  EVIDENCE + a proved inequality.  split-only OP1 OPEN.  RH [OUT].",
          flush=True)
