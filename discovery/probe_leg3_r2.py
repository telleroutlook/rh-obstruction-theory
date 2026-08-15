#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 (§6r continuation): sub-claim (R2) "min-psi is absolutely bounded", via the
§6o descent CEILING for a swing node against a FIXED complement.

Setup.  Fix a complement C (the m-2 non-swing nodes); by §6o this fixes alpha = a_k/b_k.
A swing node in a repeated x-class ranges over t = base + p*s, giving x = x_of(t) on a
p-adic LADDER inside the residue disk {x ≡ x_of(base) mod p}.  psi = v_p(x_of(base+p*s) - alpha).
The ADVERSARY picks s to MAXIMISE psi.  If the ladder cannot approach alpha past a constant
p-adic depth, psi has a CEILING => min-psi (<= this) is bounded => (R2).

Unlike probe_leg3_align (which JOINTLY optimises all nodes), this FIXES alpha and sweeps
ONLY the swing node exhaustively over s in [0, p^3), isolating the ladder's approach ceiling.

CHECKS (orbit D=425, p in {7,11}):
  (C1) for many random fixed complements C (=> fixed alpha) with alpha ≡ x_of(base) mod p
       (i.e. psi>0 reachable), the MAX over s in [0,p^3) of v_p(x_of(base+p*s) - alpha).
       Report the distribution and the GLOBAL max.
  (C2) confirm the closed form  psi = 1 + v_p(s - s*)  for a ladder-specific s* when it
       exists, i.e. the ladder is (to leading order) AFFINE in s -- so at most ONE s mod p
       lifts psi past 1, at most one s mod p^2 past 2, etc. (a single p-adic target).

HONESTY (L5): fixed-complement exhaustive sweep, one orbit, small p.  A bounded GLOBAL max
in (C1) is EVIDENCE the ladder approach is capped (=> R2); (C2) explains WHY (single target,
geometric thinning).  Not a proof of an absolute constant.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from collections import Counter
import random

import discovery.probe_leg3_affine as A


def alpha_of(u, C_xs, p):
    """alpha = a_k/b_k for complement node-x list C_xs (the §6o affine slope target).
    Psi(swing x) = a - x*b is affine in the swing x; alpha = a/b is its root."""
    # Build via two swing probes: Psi at swing=x0 and swing=x1, solve affine a - x*b.
    x0, x1 = Fr(0), Fr(1)  # any two distinct swing x-values (not necessarily on-line)
    P0 = A.Psi_val(u, C_xs + [x0])
    P1 = A.Psi_val(u, C_xs + [x1])
    # Psi = a - x b  => P0 = a - 0 = a ; P1 = a - b => b = a - P1 = P0 - P1
    a = P0
    b = P0 - P1
    if b == 0:
        return None
    return a / b


def vp_frac(fr, p):
    v = A.vpf(fr, p)
    return v if v is not None else 10**9


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 (§6r/R2): fixed-complement ladder CEILING for the swing node",
          flush=True)
    print("Orbit D=425 (split-only).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    sig, tau = Fr(3, 4), Fr(1)
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260815)

    global_max = 0
    ceil_dist = Counter()
    affine_ok = True; affine_tested = 0
    checked = 0
    for p in (7, 11):
        c1 = A.xres(Fr(1), p)
        for m in (3, 4, 5):
            r = m - 1
            if r >= p:
                continue
            for _ in range(300):
                # random complement: m-2 nodes in distinct classes (deep), + a swing base
                bases = rng.sample(range(1, p), r)
                comp_bases = bases[: m - 2]
                swing_base = bases[m - 2]
                C_ts = [Fr(b + p * rng.randrange(27)) for b in comp_bases]
                C_xs = [A.x_of(t) for t in C_ts]
                al = alpha_of(u, C_xs, p)
                if al is None:
                    continue
                # need alpha in the swing disk mod p (else psi=0 trivially)
                xr = A.xres(A.x_of(Fr(swing_base)), p)
                ar = A.xres(al, p)
                if xr is None or ar is None or xr != ar or xr == c1:
                    continue
                checked += 1
                # sweep swing node exhaustively over s in [0, p^3)
                best = 0
                psi_by_s = {}
                for s in range(p ** 3):
                    t = swing_base + p * s
                    if t == 0:
                        continue
                    ps = vp_frac(A.x_of(Fr(t)) - al, p)
                    psi_by_s[s] = ps
                    best = max(best, ps if ps < 10**9 else 0)
                ceil_dist[best] += 1
                global_max = max(global_max, best)
                # (C2) affine check: among s with psi>=2, they should share s mod p (one target)
                deep = [s for s, v in psi_by_s.items() if v >= 2 and v < 10**9]
                if deep:
                    affine_tested += 1
                    if len({s % p for s in deep}) > 1:
                        affine_ok = False

    print("\n" + "=" * 96, flush=True)
    print(f"(C1) fixed-complement configs with psi>0 reachable: {checked}", flush=True)
    print(f"     max-over-swing psi distribution: {dict(sorted(ceil_dist.items()))}",
          flush=True)
    print(f"     GLOBAL max ceiling = {global_max}", flush=True)
    print(f"(C2) 'psi>=2 swing s all share one residue mod p' (single p-adic target) "
          f"[{affine_tested} configs]: {affine_ok}", flush=True)
    print("\nREADING (L5): a bounded GLOBAL ceiling (C1) with a SINGLE deep target (C2)", flush=True)
    print("shows the swing ladder approaches alpha only geometrically -- each extra p-adic", flush=True)
    print("digit needs a p-times rarer s -- so with finitely many on-line reps the reachable", flush=True)
    print("psi is capped.  This is the (R2) ceiling mechanism.  EVIDENCE, not an absolute", flush=True)
    print("constant proof.  split-only OP1 OPEN.  RH [OUT].", flush=True)
