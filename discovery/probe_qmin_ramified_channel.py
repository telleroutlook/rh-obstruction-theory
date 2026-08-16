#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

TWO-CHANNEL DECOMPOSITION of q_min (from the (PN) refutation, §6z).  The confluent-Vandermonde
per-node model captures q_min's p-part ONLY at "geometric" primes (node clustering => Vandermonde
content); at the ORBIT-RAMIFIED primes p | D_orbit it predicts 0 yet v_p(q_min) is large and
GROWS with m (probe_pn_goodprime: p=17, D=425=5^2*17, v_17(q)=3,4,5 at m=3,4,5 with nodes generic
mod 17).  So

    log q_min = [ GEOMETRIC channel: sum_{p geometric} v_p log p ]  (node-clustering, §6g Vandermonde)
              + [ RAMIFIED channel: sum_{p | D_orbit} v_p log p ]    (orbit d-vector arithmetic, node-blind)

The danger q_min -> 1 needs BOTH channels drained.  The Vandermonde floor (§6g) governs only the
geometric channel; the ramified channel is a SEPARATE positive source tied to D_orbit.  This probe
tests whether the RAMIFIED channel can be drained by the node adversaries (cluster/spread/random)
or whether it holds a node-independent floor that GROWS with m.  For D=425 the ramified odd primes
are {5,17}.  We adversarially MINIMIZE the ramified-part log2 (= v_5*log2(5)+v_17*log2(17)) and,
separately, the geometric-part, over m=2..9, reporting both minima vs m.

If min(ramified part) stays positive and rises ~linearly while the geometric adversary is free to
crush its own channel, the ramified channel is a genuine node-independent lower-bound ingredient
for the AGGREGATE OP1 target.  Exact integer arithmetic (L9).  Bounded search (evidence). RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import vp
import discovery.probe_leg3_affine as A

SIG, TAU, RAMIFIED = Fr(3, 4), Fr(1), (5, 17)   # D=425 = 5^2 * 17


def class_node_bases(p, want):
    seen, bases, c1 = set(), [], A.xres(Fr(1), p)
    for t0 in range(1, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None and r != c1 and r not in seen:
            seen.add(r); bases.append(t0)
            if len(bases) >= want:
                break
    return bases


def qmin_of(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    q = qmin_fast(oc, vo)
    return q or None


def parts(q):
    """(ramified log2 part, geometric log2 part)."""
    ram = 0
    n = q
    for p in RAMIFIED:
        e = vp(n, p)
        ram += e * log2(p)
    return ram, log2(q) - ram


def gen(kind, m, rng):
    if kind == "cluster":
        p = rng.choice([7, 11, 13]); ncls = rng.choice([2, 3])
        bn = class_node_bases(p, ncls)
        if len(bn) < ncls:
            return None
        assign = [k % ncls for k in range(m)]; rng.shuffle(assign)
        return [bn[assign[k]] + p * rng.randrange(25) for k in range(m)]
    if kind == "spread":
        p = 13; bn = class_node_bases(p, (p - 1) // 2)
        return [bn[k % len(bn)] + p * rng.randrange(25) for k in range(m)]
    return rng.sample(range(1, 400), m)


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("TWO-CHANNEL q_min (D=425, ramified odd primes {5,17}).  Adversarially MINIMIZE each", flush=True)
    print("channel's log2 over cluster/spread/random.  Can node geometry drain the RAMIFIED part?", flush=True)
    print("=" * 96, flush=True)
    print(f"{'m':>3} | {'min RAMIFIED log2':>18} | {'min GEOMETRIC log2':>19} | {'min TOTAL log2':>15}", flush=True)
    rng = random.Random(58585)
    for m in range(2, 10):
        best_ram = best_geo = best_tot = None
        for _ in range(900):
            kind = rng.choice(["cluster", "cluster", "spread", "random"])
            ts = gen(kind, m, rng)
            if ts is None:
                continue
            q = qmin_of(ts, m)
            if not q:
                continue
            ram, geo = parts(q)
            tot = ram + geo
            best_ram = ram if best_ram is None else min(best_ram, ram)
            best_geo = geo if best_geo is None else min(best_geo, geo)
            best_tot = tot if best_tot is None else min(best_tot, tot)
        if best_ram is None:
            continue
        print(f"{m:>3} | {best_ram:18.2f} | {best_geo:19.2f} | {best_tot:15.2f}", flush=True)
    print("\n" + "=" * 96, flush=True)
    print("READING (L5): if 'min RAMIFIED log2' stays > 0 and RISES with m while the geometric", flush=True)
    print("adversary can crush its own channel, then the ramified channel is a node-INDEPENDENT", flush=True)
    print("lower-bound ingredient the §6g Vandermonde floor does not touch — a NEW positive source", flush=True)
    print("for the aggregate OP1 target. If it can be driven to 0, the channel is drainable and the", flush=True)
    print("aggregate bound must rest on the geometric channel alone. Bounded search. RH [OUT].", flush=True)
