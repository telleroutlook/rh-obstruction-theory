#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

PIN the GEOMETRIC IDENTITY behind q_min (bridge to a theorem).  probe_qmin_resultant_anatomy showed
v_p(q_min) tracks v_p(num DISC) for odd primes p outside the off-line set {5,17}, with p=3 leaking.
Since x_k - x_l = 8(t_k^2 - t_l^2)/[(4t_k^2+1)(4t_l^2+1)], the odd part of num DISC is the odd part of
    G := prod_{k<l} (t_k^2 - t_l^2)   (a Vandermonde in t^2, a nonzero integer for distinct t_k>0).
This probe measures the EXACT law: for each odd prime p, the distribution of
    delta_p := v_p(q_min) - v_p(G)
over many node sets and m, classified by prime type (off-line {5,17}; p=3; generic geometric).  The
aim is to state precisely:  for generic primes p (p != 2,3 and p not an off-line norm prime),
    v_p(q_min) = v_p(G)   identically (delta_p == 0),
which would make  log q_min  >=  sum_{p generic} v_p(G) log p  =  log( G / (2,3,5,17-part of G) ).
Then the adversary minimizing log q_min must make G a {2,3,5,17}-UNIT (all prime factors in that
fixed set) — an S-unit/smoothness constraint that fails for large m (finiteness of S-unit values),
forcing a floor.  This is the rigorous nugget.  Exact arithmetic (L9).  Bounded (evidence). RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import lcm
from collections import Counter, defaultdict
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2*17
OFFLINE = {5, 17}                   # odd prime factors of numerators of sigma^2+tau^2, (1-sigma)^2+tau^2


def qmin_of(ts, m):
    if len(set(ts)) != len(ts) or any(t == 0 for t in ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return qmin_fast(oc, vo) or None


def Gvander(ts):
    """G = prod_{k<l} (t_k^2 - t_l^2)  (integer)."""
    G = 1
    for k in range(len(ts)):
        for l in range(k + 1, len(ts)):
            G *= (ts[k] * ts[k] - ts[l] * ts[l])
    return abs(G)


def vp(n, p):
    n = abs(int(n))
    if n == 0:
        return 0
    e = 0
    while n % p == 0:
        n //= p; e += 1
    return e


def odd_primes(n):
    n = abs(int(n))
    while n % 2 == 0 and n > 1:
        n //= 2
    ps, d = set(), 3
    while d * d <= n:
        while n % d == 0:
            ps.add(d); n //= d
        d += 2
    if n > 1:
        ps.add(n)
    return ps


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("GEOMETRIC IDENTITY test: delta_p = v_p(q_min) - v_p(G),  G = prod(t_k^2 - t_l^2), D=425.", flush=True)
    print("Classify primes: OFFLINE {5,17}; p=3; GENERIC (all others).  Want delta_p==0 for GENERIC.", flush=True)
    print("=" * 96, flush=True)
    rng = random.Random(31415926)
    for m in (3, 4, 5, 6):
        dist_generic = Counter()      # delta_p distribution over generic primes
        dist_3 = Counter()
        dist_off = defaultdict(Counter)
        n_sets = 0
        exceptions = []               # (ts, p, delta) for generic p with delta != 0
        for _ in range(240):
            ts = rng.sample(range(1, 60), m)
            q = qmin_of(ts, m)
            if not q:
                continue
            G = Gvander(ts)
            n_sets += 1
            ps = odd_primes(q) | odd_primes(G) | OFFLINE
            for p in ps:
                dq, dG = vp(q, p), vp(G, p)
                delta = dq - dG
                if p in OFFLINE:
                    dist_off[p][delta] += 1
                elif p == 3:
                    dist_3[delta] += 1
                else:
                    dist_generic[delta] += 1
                    if delta != 0 and len(exceptions) < 12:
                        exceptions.append((ts[:], p, dq, dG))
        print(f"\n----- m={m}  ({n_sets} valid node sets) -----", flush=True)
        tot_g = sum(dist_generic.values())
        zero_g = dist_generic.get(0, 0)
        print(f"  GENERIC primes: delta_p distribution {dict(sorted(dist_generic.items()))}", flush=True)
        print(f"     -> delta==0 fraction = {zero_g}/{tot_g} = {(zero_g/tot_g if tot_g else 0):.3f}", flush=True)
        print(f"  p=3    : delta distribution {dict(sorted(dist_3.items()))}", flush=True)
        for p in sorted(dist_off):
            print(f"  p={p:<3}: delta=v_p(q)-v_p(G) distribution {dict(sorted(dist_off[p].items()))} "
                  f"(G rarely has {p}; so ~ v_p(q) itself)", flush=True)
        if exceptions:
            print(f"  GENERIC-prime exceptions (delta!=0), up to 12: ", flush=True)
            for (ts, p, dq, dG) in exceptions[:12]:
                print(f"     p={p} v_p(q)={dq} v_p(G)={dG}  ts={ts}", flush=True)
    print("\n" + "=" * 96, flush=True)
    print("READING (L5): if GENERIC delta==0 fraction is ~1.0 (only rare small-delta exceptions),", flush=True)
    print("the identity v_p(q_min)=v_p(G) holds for generic p ⇒ log q_min >= log(G with {2,3,5,17}", flush=True)
    print("removed). Minimizing q_min forces G to be {2,3,5,17}-smooth across ALL pairs (t_k^2-t_l^2),", flush=True)
    print("an S-unit constraint that fails for large m — the rigorous floor mechanism. Exceptions", flush=True)
    print("localize the exact exceptional set (leading Chebyshev coeffs / gcd with 4t^2+1). RH [OUT].", flush=True)
