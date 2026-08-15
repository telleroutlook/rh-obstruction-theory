#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs.
No RH / RH-equivalent input.

OP1 LEG3 (§6s-main split): the lag decomposes UNCONDITIONALLY as
    psi = v_p(Ψ) = v_p(Re H) + v_p(x - alpha),   alpha = sigma - tau*Im(H)/Re(H),
with sigma,tau = Re(u),Im(u) of the off-line atom.  QUESTION: at the min-over-Phi-minimizer
(the actual lag), how is the lag split between the two terms, and -- crucially -- WHICH term
carries the extra +1 at the tight boundary slack_x = 0 (the x_of ±-degeneracy)?

For each VALID collision found by adversarial coordinate ascent (maximising the lag), record
at the achieving Phi-minimizer the pair (vReH, vxa) = (v_p(Re H), v_p(x - alpha)); bucket by
slack_x sign; report max lag, and max of each term separately.

HONESTY (L5): local search, orbit D=425 + cross-check D=4, small p,m.  Attributes the regime
split to the two terms; not a proof.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
from collections import defaultdict
import random

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A
from discovery.probe_leg3_r2joint import build_pool


def lag_split(u, sig, tau, tl, m, p):
    """Return (lag, vReH, vxa) at the Phi-minimizer achieving the min lag, else None."""
    sg, tu = u
    xs = [A.x_of(t) for t in tl]
    rows = [(A.Phi([xs[k] for k in S], p), S) for S in combinations(range(len(tl)), m - 1)]
    minPhi = min(ph for ph, _ in rows)
    best = None
    for ph, S in rows:
        if ph != minPhi:
            continue
        Psi = A.Psi_val(u, [xs[k] for k in S])
        lag = A.vpf(Psi, p)
        lag = lag if lag is not None else 10**9
        # attribute to the swing node whose (vReH+vxa) equals lag; report the min-lag minimizer
        if best is None or lag < best[0]:
            # compute term split for a representative swing node (first index of S)
            k = S[0]
            C = [xs[j] for j in S if j != k]
            H = A.cmul(A.csub(u, (Fr(1), Fr(0))), A.cprod(u, C))
            P, Q = H
            if P == 0:
                continue
            alpha = sg - tu * (Q / P)
            vReH = A.vpf(P, p); vReH = vReH if vReH is not None else 10**9
            vxa = A.vpf(xs[k] - alpha, p); vxa = vxa if vxa is not None else 10**9
            best = (lag, vReH, vxa)
    return best


def adv(u, sig, tau, p, m, S, rng, restarts):
    r = m - 1
    out = []
    for _ in range(restarts):
        bases = rng.sample(range(1, p), r)
        svec = [rng.randrange(S) for _ in range(m)]
        guard, improved, cur = 0, True, -1
        while improved and guard < 25:
            guard += 1
            improved = False
            for j in range(m):
                bj, bs = cur, svec[j]
                for sj in range(S):
                    svec[j] = sj
                    pool = build_pool(bases, svec, p)
                    if pool is None:
                        continue
                    oc, vo = cleared_columns(pool, sig, tau, m)
                    if not qmin_fast(oc, vo):
                        continue
                    res = lag_split(u, sig, tau, pool, m, p)
                    if res is None:
                        continue
                    val = res[0] if res[0] < 10**9 else -1
                    if val > bj:
                        bj, bs = val, sj
                svec[j] = bs
                if bj > cur:
                    cur, improved = bj, True
            pool = build_pool(bases, svec, p)
            if pool is not None:
                oc, vo = cleared_columns(pool, sig, tau, m)
                if qmin_fast(oc, vo):
                    res = lag_split(u, sig, tau, pool, m, p)
                    if res is not None and res[0] < 10**9:
                        out.append(res)
    return out


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 (§6s-main split): which TERM carries the lag / the slack_x=0 +1?", flush=True)
    print("lag = v_p(Re H) + v_p(x-alpha).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)
    rng = random.Random(20260816)
    for name, sig, tau in [("D=425", Fr(3, 4), Fr(1)), ("D=4", Fr(2, 5), Fr(4, 5))]:
        u = A.off_atoms_u(sig, tau)[0]
        print(f"\norbit {name}:", flush=True)
        agg = defaultdict(lambda: [0, 0, 0])   # slack_sign -> [max lag, max vReH, max vxa]
        for p in (7, 11):
            for m in (3, 4):
                if m - 1 >= p or (m - 1) > (p - 1) // 2:
                    continue
                slack = (p - 1) // 2 - (m - 1)
                sign = ">=1" if slack >= 1 else "=0"
                res = adv(u, sig, tau, p, m, 81, rng, 6)
                for lag, vReH, vxa in res:
                    a = agg[sign]
                    a[0] = max(a[0], lag); a[1] = max(a[1], vReH); a[2] = max(a[2], vxa)
                if res:
                    ml = max(r[0] for r in res)
                    print(f"   p={p:>2} m={m} slack_x={slack}({sign}): n={len(res):>3} "
                          f"max lag={ml}", flush=True)
        for sign, (ml, mr, mx) in sorted(agg.items()):
            print(f"   >> slack_x{sign}: max lag={ml}  max v_p(ReH)={mr}  "
                  f"max v_p(x-alpha)={mx}", flush=True)
    print("\nREADING (L5): compare the two terms' maxima across slack signs to see whether", flush=True)
    print("the slack_x=0 +1 lives in v_p(Re H) (a packing/real-part effect) or v_p(x-alpha)", flush=True)
    print("(the argument-ratio alignment).  Localizes the degeneracy.  Not a proof.  RH [OUT].",
          flush=True)
