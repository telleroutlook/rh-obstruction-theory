#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 (§6r continuation): the pairwise-swap lemma (probe_leg3_pairswap, P1)
PROVES   min-over-Phi-min psi  <=  min over SWAPPABLE same-class pairs of v_p(x_a - x_b),
where a pair (a,b) is SWAPPABLE iff there exist Phi-minimizers S ∋ a, S' ∋ b with the
identical complement S∖{a} = S'∖{b}.  (The naive closest same-class pair need NOT be
swappable -- pairswap P2 was False -- so pigeonhole on raw distance is insufficient.)

RESIDUAL GAP, now sharp: is  D_swap := min over swappable pairs of v_p(x_a - x_b)
bounded by an absolute constant under a DEEP p-adic adversary in the valid regime K>=m?
If D_swap stays bounded, then min-psi (= lag) is bounded => LEG3 / O(1) lag.

CHECKS on deep-tuned valid collisions (K = m .. m+2, tuning depth S up to 243):
  (D) max over configs of D_swap, per (p,m,K) and per depth S.  Also report the max over
      configs of the ACTUAL min-psi, to confirm min-psi <= D_swap and both stay bounded.
  (E) fraction of valid collisions that HAVE at least one swappable same-class pair
      (if some have none, the lemma is vacuous there and needs a separate argument).

HONESTY (L5): deep random search, one orbit, small p,m -- EVIDENCE that D_swap (hence
lag) is bounded, plus the honest caveat that a swappable pair must be shown to exist.
Not a proof.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
import random

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A


def analyze(u, tl, m, p):
    """Return (minpsi, D_swap, has_swappable) over Phi-minimizers of an m-1 subset family."""
    xs = [A.x_of(t) for t in tl]
    n = len(tl)
    subs = list(combinations(range(n), m - 1))
    phis = [A.Phi([xs[k] for k in S], p) for S in subs]
    minPhi = min(phis)
    mins = [S for S, ph in zip(subs, phis) if ph == minPhi]
    psis = []
    for S in mins:
        v = A.vpf(A.Psi_val(u, [xs[k] for k in S]), p)
        psis.append(v if v is not None else 10**9)
    minpsi = min(psis) if psis else 10**9
    cls = [A.xres(xs[k], p) for k in range(n)]
    Dswap = None
    minset = [set(S) for S in mins]
    for a in range(n):
        for b in range(a + 1, n):
            if cls[a] is None or cls[a] != cls[b]:
                continue
            # swappable: some Phi-min S with a in S, b out, and S∖a ∪ b also Phi-min
            ok = False
            for S in minset:
                if a in S and b not in S and (S - {a}) | {b} in minset:
                    ok = True
                    break
            if not ok:
                continue
            d = A.vpf(xs[a] - xs[b], p)
            d = d if d is not None else 10**9
            Dswap = d if Dswap is None else min(Dswap, d)
    return minpsi, Dswap, (Dswap is not None)


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
    print("OP1 LEG3 (§6r): swappable-pair distance floor D_swap under DEEP tuning",
          flush=True)
    print("Orbit D=425 (split-only).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    sig, tau = Fr(3, 4), Fr(1)
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260815)

    print("\n(D) max over valid collisions of  [D_swap]  and  [min-psi], vs depth S:",
          flush=True)
    print(f"{'p':>3} {'m':>3} {'K':>3}   " +
          "  ".join(f"S={S}(Dsw/mps)" for S in (27, 81, 243)), flush=True)
    tot = 0; with_swap = 0; viol = 0
    global_D = 0; global_mps = 0
    for p in (7, 11):
        for m in (3, 4, 5):
            if m - 1 >= p:
                continue
            for K in (m, m + 1, m + 2):
                cells = []
                for S in (27, 81, 243):
                    maxD = 0; maxmps = 0
                    for _ in range(400):
                        pool = deep_pool(p, m, K, S, rng)
                        if pool is None:
                            continue
                        oc, vo = cleared_columns(pool, sig, tau, m)
                        if not qmin_fast(oc, vo):
                            continue
                        tl = [Fr(t) for t in pool]
                        mps, Dsw, has = analyze(u, tl, m, p)
                        if mps <= 0 or mps >= 10**9:
                            continue
                        tot += 1
                        if has:
                            with_swap += 1
                            if mps > Dsw:
                                viol += 1
                            maxD = max(maxD, Dsw)
                        maxmps = max(maxmps, mps)
                    cells.append((maxD, maxmps))
                    global_D = max(global_D, maxD)
                    global_mps = max(global_mps, maxmps)
                print(f"{p:>3} {m:>3} {K:>3}   " +
                      "   ".join(f"{d:>2}/{mp:>2}" for d, mp in cells), flush=True)

    print("\n" + "=" * 96, flush=True)
    print(f"(E) positive-min-psi valid collisions: {tot};  with a swappable same-class "
          f"pair: {with_swap}  ({tot - with_swap} without)", flush=True)
    print(f"    lemma violations (min-psi > D_swap): {viol}   "
          f"(must be 0 by pairswap P1)", flush=True)
    print(f"    GLOBAL max D_swap = {global_D}   GLOBAL max min-psi = {global_mps}",
          flush=True)
    print("\nREADING (L5): if D_swap and min-psi both stay a small constant as depth S", flush=True)
    print("grows (no m- or S-growth), the swappable-pair bound caps the lag => O(1).", flush=True)
    print("The residual is configs WITHOUT a swappable pair (need a separate argument).", flush=True)
    print("EVIDENCE + proved inequality (P1).  split-only OP1 OPEN.  RH [OUT].", flush=True)
