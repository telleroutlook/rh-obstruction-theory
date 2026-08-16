#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs.
No RH / RH-equivalent input.

FOLLOW-UP to the OB-41 refutation (§6u).  The referee's clustering attack (navail<<m-1)
broke the "lag = O(1)" lemma in the LARGE-p regime (p>=2m-1), where the e_max floor is
trivial.  The barrier's PROVED input (e_max >= ceil(2m/(p+3))-1, §6g) is only nontrivial
in the SMALL-p regime p <= 2m-1.  DECISIVE QUESTION for OP1: does the SAME clustering
attack, run where the floor is ACTIVE, drive the barrier quantity v_p(q_min) BELOW the
floor?  (Recall lag = e_max - v_p(q_min); the barrier survives iff v_p(q_min) >= floor -
O(1), i.e. the proved e_max floor TRANSFERS to q_min.)

This probe:
  * works ONLY in p <= 2m-1 (floor = ceil(2m/(p+3))-1 >= 1);
  * builds genuinely CLUSTERED valid collisions (nodes packed into c << m-1 x-classes as
    distinct large rationals base+p*depth), NOT the navail=m-1 pools that build_pool forces;
  * adversarially MINIMIZES v_p(q_min) by coordinate descent over per-node depths, for
    several class-counts c;
  * reports, per (p,m): floor, min v_p(q_min) achieved by the adversary, the e_max there,
    and whether v_p(q_min) >= floor (i.e. the barrier's floor transfer SURVIVES the attack).

HONESTY (L5): bounded coordinate-descent search, small p, one orbit family per call; this
DETECTS a floor break if one exists in range, and is evidence (not proof) of survival if
none is found.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil
import random

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import emax_smith, vpf
import discovery.probe_leg3_affine as A


def class_bases(p, want):
    """Return up to `want` distinct nonzero-t x-class base residues mod p (t in 1..p-1)."""
    seen, bases = set(), []
    c1 = A.xres(Fr(1), p)
    for t0 in range(1, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None and r != c1 and r not in seen:
            seen.add(r)
            bases.append(t0)          # store the *node* base t0 (its x-residue is the class)
            if len(bases) >= want:
                break
    return bases


def clustered_pool(base_nodes, assign, depths, p):
    """node k = base_nodes[assign[k]] + p*depths[k]  (same x-class per assign, distinct rationals)."""
    ts = []
    for k in range(len(assign)):
        t = base_nodes[assign[k]] + p * depths[k]
        ts.append(t)
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    return [Fr(t) for t in ts]


def vpq_of(pool, sig, tau, m, p):
    """v_p(q_min) for a VALID collision, else None."""
    oc, vo = cleared_columns(pool, sig, tau, m)
    q = qmin_fast(oc, vo)
    if not q:
        return None
    v = 0
    qq = q
    while qq % p == 0:
        qq //= p
        v += 1
    return v


def emax_of(pool, sig, tau, m, p):
    oc, _ = cleared_columns(pool, sig, tau, m)
    em, _ = emax_smith(oc, m, p)
    return em


def adv_min_vpq(sig, tau, p, m, ncls, S, rng, trials):
    """Random sampling of clustered valid collisions with ncls classes; return the pool
    achieving the SMALLEST v_p(q_min) (the adversary's floor-break attempt), else None."""
    bn = class_bases(p, ncls)
    if len(bn) < ncls:
        return None
    best = None
    for _ in range(trials):
        assign = [k % ncls for k in range(m)]
        rng.shuffle(assign)
        depths = [rng.randrange(S) for _ in range(m)]
        pool = clustered_pool(bn, assign, depths, p)
        if pool is None:
            continue
        vq = vpq_of(pool, sig, tau, m, p)
        if vq is None:
            continue
        if best is None or vq < best[0]:
            em = emax_of(pool, sig, tau, m, p)
            best = (vq, em, list(assign), list(depths))
            if vq == 0:
                break   # cannot go lower; floor-break candidate found
    return best


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("OP1 §6u follow-up: does the CLUSTERING attack break the e_max->q_min floor in", flush=True)
    print("the ACTIVE regime p <= 2m-1?   Adversary MINIMIZES v_p(q_min) over clustered", flush=True)
    print("valid collisions.  Barrier SURVIVES iff min v_p(q_min) >= floor=ceil(2m/(p+3))-1.", flush=True)
    print("Orbit D=425 (rho=3/4+i).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 100, flush=True)
    sig, tau = Fr(3, 4), Fr(1)
    rng = random.Random(20260817)
    # floor-active regime: p <= 2m-1  <=>  m >= (p+1)/2.  Keep m modest so SNF stays fast.
    CASES = [(5, 6), (5, 8), (7, 8), (7, 10), (11, 12)]
    worst_break = None
    for (p, m) in CASES:
        if p > 2 * m - 1:
            continue
        floor = ceil(2 * m / (p + 3)) - 1
        row_min = None
        for ncls in (2, (p - 1) // 2):    # clustered (navail=2) AND max-spread ((p-1)/2 classes)
            if ncls < 2 or ncls > m:
                continue
            res = adv_min_vpq(sig, tau, p, m, ncls, 40, rng, 250)
            if res is None:
                continue
            vq, em, assign, depths = res
            navail = len(set(assign))
            tag = "OK" if vq >= floor else "**BELOW FLOOR**"
            print(f"  p={p:>2} m={m:>2} floor={floor}  ncls={ncls} navail={navail}: "
                  f"min v_p(q_min)={vq}  e_max={em}  lag={em - vq}  -> {tag}", flush=True)
            if row_min is None or vq < row_min:
                row_min = vq
        if row_min is not None:
            gap = row_min - floor
            print(f"    >> p={p} m={m}: adversarial MIN v_p(q_min)={row_min}, floor={floor}, "
                  f"gap={gap}  {'FLOOR HOLDS' if gap >= 0 else 'FLOOR BROKEN'}", flush=True)
            if worst_break is None or gap < worst_break[0]:
                worst_break = (gap, p, m, row_min, floor)
    print("\n" + "=" * 100, flush=True)
    if worst_break:
        gap, p, m, rm, fl = worst_break
        print(f"WORST case: gap = min_vpq - floor = {gap}  (p={p}, m={m}, min_vpq={rm}, floor={fl})",
              flush=True)
        if gap >= 0:
            print("READING (L5): in the ACTIVE regime the clustering attack did NOT push", flush=True)
            print("v_p(q_min) below the proved e_max floor => the barrier's floor TRANSFER", flush=True)
            print("survives the attack that killed the (large-p) lag lemma.  Evidence, not proof.", flush=True)
        else:
            print("READING (L5): the clustering attack DID break the floor transfer in the", flush=True)
            print("active regime => the e_max->q_min route needs repair (a genuine new gap).", flush=True)
    print("RH stays [OUT].", flush=True)
