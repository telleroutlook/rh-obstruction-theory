#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs.
No RH / RH-equivalent input.

OP1 LEG3 (§6s localization): WHERE does the min-psi <= 2 cap come from in the NON-degenerate
navail = m-1 regime?

The pairwise-swap lemma (§6r) gives only  min-psi <= d := v_p(x_a - x_b)  for the doubled
class {a,b}.  But d can be made LARGE by choosing t_a,t_b with x_of very p-adically close.
Yet empirically min-psi <= 2.  So the true cap is the SECOND factor of §6s:

    psi(minimizer with swing node x) = v_p( (sigma - x) - tau*Im(H)/Re(H) ),  H = H(C),

and the adversary would need alpha(C) := sigma - tau*Im(H)/Re(H)  to satisfy
alpha ≡ x_a mod p^3 SIMULTANEOUSLY with a valid collision.  This probe measures, over
VALID navail=m-1 collisions (adversarial coordinate ascent), the TWO quantities

    d      = v_p(x_a - x_b)        (pairwise-swap ceiling)
    psi    = min over the 2 Phi-minimizers of v_p(x - alpha(C))   (actual lag)

and reports the JOINT distribution.  If  psi <= 2  while  d  ranges HIGH, the cap is the
alpha-alignment factor, NOT pairwise-swap -- i.e. a valid collision CANNOT tune C to align
alpha(C) with the doubled class beyond p^2.  That is the precise remaining LEG3 lemma to
prove.  Also directly checks the §6s identity psi == v_p((sigma-x) - tau*Im(H)/Re(H)).

HONESTY (L5): local search, small p,m, orbit D=425.  Localizes the mechanism; not a proof.
RH stays [OUT].
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


def cprod_list(zs):
    r = (Fr(1), Fr(0))
    for z in zs:
        r = A.cprod(r, z)
    return r


def alpha_via_ratio(u, xs_C, sig, tau, p):
    """alpha = sigma - tau*Im(H)/Re(H),  H = (u-1)*prod_{j in C}(u-x_j).  Returns Fr or None."""
    H = A.csub(u, (Fr(1), Fr(0)))
    for x in xs_C:
        H = A.cprod(H, A.csub(u, (x, Fr(0))))
    P, Q = H  # Re, Im
    if P == 0:
        return None
    return sig - tau * (Q / P)


def analyze(u, sig, tau, pool, m, p):
    """navail=m-1 pool: return (d, psi, ok_identity) or None if not navail=m-1."""
    tl = pool
    xs = [A.x_of(t) for t in tl]
    c1 = A.xres(Fr(1), p)
    classes = defaultdict(list)
    for k in range(len(tl)):
        r = A.xres(xs[k], p)
        if r is not None and r != c1:
            classes[r].append(k)
    navail = len(classes)
    if navail != m - 1:
        return None
    # find the doubled class
    doubled = [ks for ks in classes.values() if len(ks) >= 2]
    if len(doubled) != 1 or len(doubled[0]) != 2:
        return None
    a, b = doubled[0]
    d = A.vpf(xs[a] - xs[b], p)
    # Phi-minimizers
    rows = [(A.Phi([xs[k] for k in S], p), S) for S in combinations(range(len(tl)), m - 1)]
    minPhi = min(ph for ph, _ in rows)
    psi = None
    ok_id = True
    for ph, S in rows:
        if ph != minPhi:
            continue
        # swing node = the doubled-class member IN S (exactly one of a,b)
        swing = a if a in S else (b if b in S else None)
        v = A.vpf(A.Psi_val(u, [xs[k] for k in S]), p)
        v = v if v is not None else 10**9
        psi = v if psi is None else min(psi, v)
        # cross-check §6s identity on this minimizer
        if swing is not None and v < 10**9:
            C = [k for k in S if k != swing]
            al = alpha_via_ratio(u, [xs[k] for k in C], sig, tau, p)
            if al is not None:
                v2 = A.vpf(xs[swing] - al, p)
                v2 = v2 if v2 is not None else 10**9
                if v2 != v:
                    ok_id = False
    return (d, psi, ok_id)


def adv_search(u, sig, tau, p, m, S, rng, restarts):
    """Coordinate-ascent for VALID navail=m-1 collisions maximising psi; collect (d,psi)."""
    r = m - 1
    pairs = []
    id_ok = True
    for _ in range(restarts):
        bases = rng.sample(range(1, p), r)
        svec = [rng.randrange(S) for _ in range(m)]
        guard, improved, cur = 0, True, -1
        while improved and guard < 30:
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
                    res = analyze(u, sig, tau, pool, m, p)
                    if res is None:
                        continue
                    dval, psi, okid = res
                    val = psi if (psi is not None and psi < 10**9) else -1
                    if val > bj:
                        bj, bs = val, sj
                svec[j] = bs
                if bj > cur:
                    cur, improved = bj, True
            pool = build_pool(bases, svec, p)
            if pool is not None:
                oc, vo = cleared_columns(pool, sig, tau, m)
                if qmin_fast(oc, vo):
                    res = analyze(u, sig, tau, pool, m, p)
                    if res is not None:
                        dval, psi, okid = res
                        if psi is not None and psi < 10**9:
                            pairs.append((dval, psi))
                            id_ok = id_ok and okid
    return pairs, id_ok


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 (§6s): joint (d, psi) over VALID navail=m-1 collisions (K=m).", flush=True)
    print("d = v_p(x_a - x_b) [pairwise-swap ceiling];  psi = actual min-over-Phimin lag.", flush=True)
    print("Orbit D=425.  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)
    sig, tau = Fr(3, 4), Fr(1)
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260816)

    all_id_ok = True
    grand_maxpsi = -1
    grand_maxd = -1
    psi_when_d_high = defaultdict(lambda: -1)   # d -> max psi observed at that d
    for p in (7, 11):
        for m in (3, 4):
            if m - 1 >= p or (m - 1) > (p - 1) // 2:
                continue
            pairs, id_ok = adv_search(u, sig, tau, p, m, 81, rng, 6)
            all_id_ok = all_id_ok and id_ok
            if not pairs:
                continue
            maxd = max(d for d, _ in pairs)
            maxpsi = max(ps for _, ps in pairs)
            grand_maxpsi = max(grand_maxpsi, maxpsi)
            grand_maxd = max(grand_maxd, maxd)
            for d, ps in pairs:
                psi_when_d_high[d] = max(psi_when_d_high[d], ps)
            slack = (p - 1) // 2 - (m - 1)
            print(f"   p={p:>2} m={m} slack_x={slack}: n={len(pairs):>3}  "
                  f"max d={maxd}  max psi={maxpsi}  §6s-id={'OK' if id_ok else 'FAIL'}",
                  flush=True)

    print("\n" + "=" * 96, flush=True)
    print(f"§6s identity psi == v_p((sigma-x) - tau*Im(H)/Re(H)) over ALL minimizers: "
          f"{'HELD' if all_id_ok else 'FAILED'}", flush=True)
    print(f"GRAND: max d (pairwise-swap ceiling) = {grand_maxd},  "
          f"max psi (actual lag) = {grand_maxpsi}", flush=True)
    print(f"max psi per d value: {dict(sorted(psi_when_d_high.items()))}", flush=True)
    print("\nREADING (L5): if max psi <= 2 while max d ranges HIGHER, the cap is the", flush=True)
    print("alpha(C)-ALIGNMENT factor of §6s, NOT pairwise-swap -- a valid collision cannot", flush=True)
    print("tune the complement C to align alpha with the doubled class beyond p^2.  THAT is", flush=True)
    print("the precise remaining LEG3 lemma.  Localization, not a proof.  RH [OUT].", flush=True)
