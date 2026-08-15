#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 ADVERSARIAL test: can the node-set adversary grow min-psi with m?

OP1 quantifies over ALL rational on-line node sets {t_k} (the adversary picks them to
minimise q_min, i.e. maximise the incidence lag).  By §6j lag <= min over Phi-minimizers
of psi = v_p(Psi).  §6m closed the non-packed regime; the packed regime is where the
adversary would push.  §6o recast psi = v_p(x_k - a_k/b_k) (a p-adic distance), so to
force min-psi >= C the adversary must p-adically ALIGN x_k to the target alpha to depth
C across EVERY Phi-minimizer simultaneously -- a rigid over-constrained demand.

This probe lets the adversary TRY: for the split-only orbit D=425 and p ∈ {3,7,11}, it
searches packed node pools (few t-classes, deliberately deep p-adic clustering to force
alignment) and records the MAXIMUM over pools of [min over Phi-minimizers of psi].  If
that max stays a small constant as m grows, the adversary CANNOT grow the lag -> strong
evidence LEG3 holds adversarially.  If it grows with m, LEG3 is in trouble (report L5).

Search = seeded-random packed pools + a structured "deep-align" adversary (all reps of
each class at t = base + p^2 * j, forcing within-class v_p=2).

HONESTY (L5): EVIDENCE from a bounded adversarial search (not exhaustive); a growing
trend would REFUTE, a flat plateau SUPPORTS but does not prove.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
import random

import discovery.probe_leg3_affine as A   # x_of, off_atoms_u, Psi_val, Phi, vpf, xres


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


def random_packed_pool(p, m, K, rng, DEPTH=8):
    """K nodes over exactly r=m-1 t-classes, random p-adic depths (wide range)."""
    r = m - 1
    if r < 1 or r >= p:
        return None
    bases = rng.sample(range(1, p), r)
    pool, seen = [], set()
    # ensure >=1 per class
    for b in bases:
        a, c = rng.randint(0, DEPTH), rng.randint(0, DEPTH)
        t = b + p * a + p * p * c
        if t != 0 and t not in seen:
            pool.append(Fr(t)); seen.add(t)
    guard = 0
    while len(pool) < K and guard < 2000:
        guard += 1
        b = rng.choice(bases)
        a, c = rng.randint(0, DEPTH), rng.randint(0, DEPTH)
        t = b + p * a + p * p * c
        if t != 0 and t not in seen:
            pool.append(Fr(t)); seen.add(t)
    return pool if len(pool) >= m else None


def deep_align_pool(p, m, K):
    """Structured adversary: r=m-1 classes, all reps at base + p^2 * j (v_p=2 within)."""
    r = m - 1
    if r < 1 or r >= p:
        return None
    bases = list(range(1, r + 1))
    pool, seen = [], set()
    j = 0
    while len(pool) < K:
        for b in bases:
            t = b + p * p * j
            if t != 0 and t not in seen:
                pool.append(Fr(t)); seen.add(t)
            if len(pool) >= K:
                break
        j += 1
    return pool


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 ADVERSARIAL: max over packed pools of [min-over-Phi-min psi] vs m",
          flush=True)
    print("Orbit D=425 (split-only).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    sig, tau = Fr(3, 4), Fr(1)                 # D=425 split-only orbit
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260815)              # fixed seed (reproducible)
    N_RANDOM = 200

    print(f"{'p':>3} {'m':>3} {'K':>4} {'max-min-psi(rand)':>18} {'deep-align':>11}",
          flush=True)
    global_max = 0
    worst = None
    for p in (3, 7, 11):
        for m in range(2, 9):
            if m - 1 >= p:                     # need >= m-1 available classes < p
                continue
            # ADVERSARY sweeps pool size: K=m-1 (no spare reps) is the tightest packing
            for K in (m - 1, m, m + 1, m + 3):
                if K < m - 1 or K < 1:
                    continue
                best_rand = 0
                for _ in range(N_RANDOM):
                    pool = random_packed_pool(p, m, K, rng)
                    if pool is None or len(pool) < m - 1 or len(pool) < K:
                        continue
                    v = minpsi_over_phimin(u, pool, m, p)
                    if v is not None and v < 10**9:
                        best_rand = max(best_rand, v)
                da = deep_align_pool(p, m, K)
                v_da = minpsi_over_phimin(u, da, m, p) if da and len(da) >= m - 1 else None
                v_da = v_da if (v_da is not None and v_da < 10**9) else 0
                mx = max(best_rand, v_da)
                if worst is None or mx > worst[0]:
                    worst = (mx, p, m, K)
                global_max = max(global_max, mx)
                print(f"{p:>3} {m:>3} {K:>4} {best_rand:>18} {v_da:>11}", flush=True)

    print("\n" + "=" * 96, flush=True)
    print(f"GLOBAL max over all searched packed pools of min-over-Phi-min psi: {global_max}",
          flush=True)
    if worst:
        print(f"   attained at p={worst[1]}, m={worst[2]}, K={worst[3]}", flush=True)
    print("\nREADING (L5): if this stays a small constant as m grows, the node-set", flush=True)
    print("adversary CANNOT grow the incidence lag => strong evidence LEG3 holds", flush=True)
    print("adversarially (lag=O(1)).  A growing trend would REFUTE.  Bounded search,", flush=True)
    print("EVIDENCE not proof.  split-only OP1 OPEN; RH stays [OUT].", flush=True)
