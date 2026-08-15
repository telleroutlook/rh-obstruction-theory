#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3: does the min-over-Phi-minimizers psi stay bounded under DEEP tuning once
K >= m (the collision-valid regime)?

Pivot (this session).  probe_leg3_align showed that with the TIGHTEST packing K=m-1
(a SINGLE Phi-minimizer, no subset competition) deep p-adic tuning grows psi (p=11,m=3:
2->4 at S=81).  But that regime is NOT a valid OP1 collision: a collision needs the m-th
determinantal divisor D_m(A) != 0, i.e. an m x m minor, i.e. at least m on-line columns.
So K >= m ALWAYS for a genuine collision, and then there are C(K, m-1) >= m competing
Phi-minimizers.  §6j's load-bearing quantity is the MIN over them.  This probe tests
whether that MIN resists deep adversarial tuning in the valid regime K in {m, m+1}.

CHECKS:
  (V) collision-validity boundary: over random pools, does qmin_fast ever hold with
      K = m-1 on-line nodes?  (Expected: never -- collisions require K >= m.)
  (G) growth test: for K in {m-1 (invalid, control), m, m+1}, max over deeply-tuned
      packed pools of [min over Phi-minimizers of psi], as the tuning depth S grows.
      Expected: K=m-1 grows (control, matches align); K>=m stays a small constant.

HONESTY (L5): random+coordinate search, one orbit, small p,m -- EVIDENCE that the
collision-valid regime caps the lag; the invalid K=m-1 growth is a non-collision
artifact.  Not a proof.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
import random

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A


def minpsi_over_phimin(u, tlist, m, p):
    xs = [A.x_of(t) for t in tlist]
    rows = [(A.Phi([xs[k] for k in S], p), S)
            for S in combinations(range(len(tlist)), m - 1)]
    if not rows:
        return None
    minPhi = min(ph for ph, _ in rows)
    best = None
    for ph, S in rows:
        if ph != minPhi:
            continue
        v = A.vpf(A.Psi_val(u, [xs[k] for k in S]), p)
        v = v if v is not None else 10**9
        best = v if best is None else min(best, v)
    return best


def deep_pool(p, m, K, S, rng):
    """K nodes over r=m-1 classes, each rep tuned deeply in [0,S)."""
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
    print("OP1 LEG3: min-over-Phi-min psi under DEEP tuning, by pool size K (valid: K>=m)",
          flush=True)
    print("Orbit D=425 (split-only).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    sig, tau = Fr(3, 4), Fr(1)
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260815)

    # (V) collision-validity boundary: can K=m-1 ever be a collision?
    print("\n(V) collision-validity: does qmin_fast hold at various K?  (need K>=m)",
          flush=True)
    for p in (7, 11):
        for m in range(3, 6):
            counts = {}
            for K in (m - 1, m, m + 1):
                nfound = 0
                for _ in range(400):
                    pool = deep_pool(p, m, K, 12, rng)
                    if pool is None:
                        continue
                    oc, vo = cleared_columns(pool, sig, tau, m)
                    if qmin_fast(oc, vo):
                        nfound += 1
                counts[K] = nfound
            print(f"   p={p} m={m}: collisions found  "
                  + "  ".join(f"K={K}:{counts[K]}" for K in (m - 1, m, m + 1)),
                  flush=True)

    # (G) growth test: max over deeply-tuned pools of min-psi, vs depth S
    print("\n(G) max over deeply-tuned packed pools of [min-over-Phi-min psi] vs depth S:",
          flush=True)
    print(f"{'p':>3} {'m':>3} {'K':>4}   " + "  ".join(f"S={S}" for S in (9, 27, 81, 243)),
          flush=True)
    for p in (7, 11):
        for m in (3, 4, 5):
            if m - 1 >= p:
                continue
            for K in (m - 1, m, m + 1):
                row = []
                for S in (9, 27, 81, 243):
                    best = 0
                    for _ in range(400):
                        pool = deep_pool(p, m, K, S, rng)
                        if pool is None or len(pool) < m - 1:
                            continue
                        v = minpsi_over_phimin(u, pool, m, p)
                        if v is not None and v < 10**9:
                            best = max(best, v)
                    row.append(best)
                tag = "  (K=m-1 INVALID control)" if K == m - 1 else ""
                print(f"{p:>3} {m:>3} {K:>4}   " + "   ".join(f"{v:>3}" for v in row) + tag,
                      flush=True)

    print("\n" + "=" * 96, flush=True)
    print("READING (L5): if (V) shows collisions only at K>=m, and (G) shows the K>=m", flush=True)
    print("rows FLAT (no growth with depth S) while the K=m-1 control grows, then the", flush=True)
    print("earlier psi-growth is a NON-collision artifact: in every valid collision the", flush=True)
    print("subset competition caps min-psi => lag=O(1).  EVIDENCE, not proof.  RH [OUT].",
          flush=True)
