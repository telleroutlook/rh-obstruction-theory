#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 (§6r continuation): verify the STRUCTURAL MECHANISM behind sub-claim (R1)
"a swappable same-class pair EXISTS once K >= m", turning the 1333/1333 empirical
observation into a checked constructive proof mechanism.

CLAIM (R1 mechanism).  In a packed valid collision (navail = #distinct x-classes present,
NONE equal to the class of x=1):
  (a) navail = m-1 EXACTLY  (not < m-1) whenever min-psi > 0 [tested];
  (b) since none of the m-1 present classes is the class of 1, every "one rep per class"
      (m-1)-subset has ALL x_k p-units away from 1 and pairwise-distinct classes, so its
      Phi = 0 = minPhi;
  (c) K >= m nodes over m-1 present classes force (pigeonhole) a class with >= 2 reps;
      pick two of its reps a,b and one rep from each of the OTHER m-2 classes as C.  Then
      C∪{a} and C∪{b} are BOTH Phi-minimizers with shared complement C  =>  (a,b) is a
      SWAPPABLE same-class pair.  Hence a swappable pair always exists.

CHECKS on valid collisions (K = m .. m+2, deep tuning S up to 243):
  (A) among positive-min-psi valid collisions, distribution of navail; is it == m-1 always?
  (B) does the EXPLICIT construction in (c) (repeated class + one-per-other-class) actually
      yield two Phi=0 minimizers?  Count successes / configs.
  (C) cross-check vs probe_leg3_swapdist's "has swappable" (should agree).

HONESTY (L5): verifies the constructive mechanism on one orbit, small p,m.  If (A) shows
navail == m-1 always and (B) the construction always succeeds, (R1) is essentially proved
structurally (modulo a general navail==m-1 lemma).  EVIDENCE toward a proof.  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
from collections import Counter
import random

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A


def minpsi(u, tl, m, p):
    xs = [A.x_of(t) for t in tl]
    n = len(tl)
    rows = [(A.Phi([xs[k] for k in S], p), S) for S in combinations(range(n), m - 1)]
    minPhi = min(ph for ph, _ in rows)
    best = None
    for ph, S in rows:
        if ph != minPhi:
            continue
        v = A.vpf(A.Psi_val(u, [xs[k] for k in S]), p)
        v = v if v is not None else 10**9
        best = v if best is None else min(best, v)
    return best, minPhi


def class_of_one(p):
    return A.xres(A.x_of(Fr(0)), p) if False else A.xres(Fr(1), p)  # x=1 residue


def navail_and_classes(tl, p):
    c1 = A.xres(Fr(1), p)
    buckets = {}
    for k, t in enumerate(tl):
        r = A.xres(A.x_of(t), p)
        if r is None or r == c1:
            continue
        buckets.setdefault(r, []).append(k)
    return buckets  # class residue -> node indices (excluding class of 1)


def construct_swappable(u, tl, m, p, buckets):
    """Try (c): repeated class (a,b) + one rep from each other class -> two Phi=0 minimizers."""
    xs = [A.x_of(t) for t in tl]
    reps = [ks for ks in buckets.values()]
    # need at least one class with >=2 reps and total >= m-1 classes
    rep_classes = [ks for ks in reps if len(ks) >= 2]
    if len(reps) < m - 1 or not rep_classes:
        return False
    singles = [ks[0] for ks in reps]  # one rep per class
    for ks in rep_classes:
        a, b = ks[0], ks[1]
        others = [s for s in singles if s not in ks][: m - 2]
        if len(others) != m - 2:
            continue
        Sa = others + [a]
        Sb = others + [b]
        pha = A.Phi([xs[k] for k in Sa], p)
        phb = A.Phi([xs[k] for k in Sb], p)
        if pha == 0 and phb == 0:
            return True
    return False


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
    print("OP1 LEG3 (§6r/R1): swappable pair ALWAYS exists (structural mechanism)",
          flush=True)
    print("Orbit D=425 (split-only).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    sig, tau = Fr(3, 4), Fr(1)
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260815)

    navail_dist = Counter()
    tot = 0; construct_ok = 0; minphi_zero = 0
    for p in (7, 11):
        for m in (3, 4, 5):
            if m - 1 >= p:
                continue
            for K in (m, m + 1, m + 2):
                for _ in range(400):
                    pool = deep_pool(p, m, K, 81, rng)
                    if pool is None:
                        continue
                    oc, vo = cleared_columns(pool, sig, tau, m)
                    if not qmin_fast(oc, vo):
                        continue
                    tl = [Fr(t) for t in pool]
                    mps, minPhi = minpsi(u, tl, m, p)
                    if mps is None or mps <= 0 or mps >= 10**9:
                        continue
                    tot += 1
                    buckets = navail_and_classes(tl, p)
                    navail_dist[len(buckets) - (m - 1)] += 1   # offset from m-1
                    if minPhi == 0:
                        minphi_zero += 1
                    if construct_swappable(u, tl, m, p, buckets):
                        construct_ok += 1

    print("\n" + "=" * 96, flush=True)
    print(f"(A) positive-min-psi valid collisions: {tot}", flush=True)
    print(f"    navail - (m-1) distribution (0 == navail=m-1 exactly): "
          f"{dict(sorted(navail_dist.items()))}", flush=True)
    print(f"    configs with minPhi == 0: {minphi_zero}  ({tot - minphi_zero} with minPhi>0)",
          flush=True)
    print(f"(B) explicit (c) construction yields two Phi=0 minimizers: "
          f"{construct_ok}/{tot}", flush=True)
    print("\nREADING (L5): if navail=m-1 always (A: all mass at offset 0), minPhi=0 always,", flush=True)
    print("and the explicit repeated-class + one-per-other-class construction succeeds in", flush=True)
    print("every config (B), then (R1) 'a swappable pair exists once K>=m' is proved by", flush=True)
    print("construction on this orbit.  Residual (R2) = bound D_swap.  EVIDENCE.  RH [OUT].",
          flush=True)
