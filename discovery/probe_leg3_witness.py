#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs.
No RH / RH-equivalent input.

Verify a single WITNESS from probe_leg3_r2joint: reconstruct a p=7,m=4,K=m VALID collision
with min-over-Phi-min psi = 3, and CANONICALLY re-check it end to end, so the "min-psi can
reach 3 at K=m" finding is not a build_pool artifact.  Prints navail, minPhi, the full
Phi-minimizer psi list, and qmin_fast validity.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
import random

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A
from discovery.probe_leg3_r2joint import build_pool


def full_report(u, pool, m, p, sig, tau):
    tl = [Fr(t) for t in pool]
    xs = [A.x_of(t) for t in tl]
    c1 = A.xres(Fr(1), p)
    classes = {}
    for k, t in enumerate(tl):
        r = A.xres(xs[k], p)
        classes.setdefault(r, []).append(k)
    navail = len([r for r in classes if r is not None and r != c1])
    rows = [(A.Phi([xs[k] for k in S], p), S) for S in combinations(range(len(tl)), m - 1)]
    minPhi = min(ph for ph, _ in rows)
    psis = []
    for ph, S in rows:
        if ph != minPhi:
            continue
        v = A.vpf(A.Psi_val(u, [xs[k] for k in S]), p)
        psis.append((S, v if v is not None else None))
    oc, vo = cleared_columns(pool, sig, tau, m)
    valid = qmin_fast(oc, vo)
    minpsi = min(v for _, v in psis if v is not None)
    return dict(nodes=[int(t) for t in pool], navail=navail, m_minus_1=m - 1,
                minPhi=minPhi, minpsi=minpsi, valid=valid,
                phimin_psis=[(S, v) for S, v in psis])


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("WITNESS re-check: p=7,m=4,K=m valid collision with min-psi=3 (canonical)",
          flush=True)
    print("=" * 96, flush=True)
    sig, tau = Fr(3, 4), Fr(1)
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260816)
    p, m = 7, 4
    r = m - 1
    found = None
    for _ in range(200000):
        bases = rng.sample(range(1, p), r)
        svec = [rng.randrange(243) for _ in range(m)]
        pool = build_pool(bases, svec, p)
        if pool is None:
            continue
        oc, vo = cleared_columns(pool, sig, tau, m)
        if not qmin_fast(oc, vo):
            continue
        rep = full_report(u, pool, m, p, sig, tau)
        if rep["minpsi"] is not None and rep["minpsi"] >= 3:
            found = rep
            break
    if found is None:
        print("no min-psi>=3 valid witness found in random reconstruction "
              "(the coordinate-ascent hit may need the ascent to reproduce)", flush=True)
    else:
        print("WITNESS:", flush=True)
        for k, v in found.items():
            if k == "phimin_psis":
                print(f"  {k}:", flush=True)
                for S, psi in v:
                    print(f"      subset {S}: psi={psi}", flush=True)
            else:
                print(f"  {k}: {v}", flush=True)
        print("\nCONFIRMED: min-psi >= 3 occurs in a canonically-verified VALID collision",
              flush=True)
        print("at K=m.  The earlier swapdist 'max=2' was a random-sampling under-count;", flush=True)
        print("adversarial search recovers the §6h plateau (lag ~ 3).  RH [OUT].", flush=True)
