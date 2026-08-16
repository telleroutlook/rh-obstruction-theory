#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

DECISIVE follow-up to the per-prime-floor REFUTATION.  probe_qmin_perprime_floor found valid
collisions at p=13, m in {9,10} with v_13(q_min)=0 while floor=ceil(2m/(p+3))-1=1 (slack -1):
the proved e_max floor does NOT transfer to q_min per-prime.  That KILLS the "sufficient"
per-prime route to OP1.  The ONLY question left that matters: at such a violation, is the
FULL integer q_min still huge (=> OP1's real target q_min->super-poly UNHARMED, only my
lemma was wrong), or does q_min itself collapse toward 1 (=> a genuine threat to OP1)?

This verifier re-finds a p=13,m=9 witness with v_13(q_min)=0, DUMPS its nodes, checks
validity by exact rank (C2) and finite qmin (C1), and prints the FULL q_min: bit length,
v_13, and small-prime factorization.  Exact arithmetic only (L9).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import emax_smith
import discovery.probe_leg3_affine as A


def class_node_bases(p, want):
    seen, bases = set(), []
    c1 = A.xres(Fr(1), p)
    for t0 in range(1, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None and r != c1 and r not in seen:
            seen.add(r); bases.append(t0)
            if len(bases) >= want:
                break
    return bases


def pool_of(bn, assign, depths, p):
    ts = [bn[assign[k]] + p * depths[k] for k in range(len(assign))]
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    return [Fr(t) for t in ts]


def vp(n, p):
    v = 0
    while n and n % p == 0:
        n //= p; v += 1
    return v


def small_factor(n, bound=200000):
    f, d = {}, 2
    while d * d <= n and d <= bound:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1   # residual (prime or large composite)
    return f


if __name__ == "__main__":
    p, m, ncls = 13, 9, 3
    sig, tau = Fr(3, 4), Fr(1)   # orbit D=425 anchor
    rng = random.Random(424242)
    bn = class_node_bases(p, ncls)
    print("=" * 96, flush=True)
    print(f"DECISIVE: p={p} m={m} — is the FULL q_min huge at a v_{p}(q_min)=0 violation?", flush=True)
    print(f"orbit D=425 (sig={sig}, tau={tau}); x-class base nodes={bn}", flush=True)
    print("=" * 96, flush=True)
    witness = None
    for _ in range(4000):
        assign = [k % ncls for k in range(m)]; rng.shuffle(assign)
        depths = [rng.randrange(40) for _ in range(m)]
        pool = pool_of(bn, assign, depths, p)
        if pool is None:
            continue
        oc, vo = cleared_columns(pool, sig, tau, m)
        q = qmin_fast(oc, vo)
        if not q:
            continue
        if vp(q, p) == 0:
            witness = (pool, assign, depths, oc, vo, q); break
    if witness is None:
        print("no v_p=0 witness re-found in budget (raise trials).", flush=True)
        raise SystemExit(0)
    pool, assign, depths, oc, vo, q = witness
    ts = [int(t) for t in pool]
    rk = matrix_rank_int(oc, m)
    em = emax_smith(oc, m, p)[0]
    xres = [A.xres(A.x_of(t), p) for t in pool]
    print(f"witness nodes t = {ts}", flush=True)
    print(f"x-residues mod {p} = {xres}   navail={len(set(xres))}", flush=True)
    print(f"validity: rank(A)={rk} (need {m}=m for C2)   qmin finite (C1) = True", flush=True)
    print(f"e_max (top p-Smith exponent) = {em}", flush=True)
    print("-" * 96, flush=True)
    print(f"FULL q_min = {q}", flush=True)
    print(f"   bit length (log2)     = {q.bit_length()}", flush=True)
    print(f"   decimal digits        = {len(str(q))}", flush=True)
    print(f"   v_{p}(q_min)           = {vp(q, p)}   (floor here = 1 -> VIOLATION confirmed)", flush=True)
    fac = small_factor(q)
    fac_str = " * ".join(f"{pr}^{e}" if e > 1 else f"{pr}" for pr, e in sorted(fac.items()))
    print(f"   factorization         = {fac_str}", flush=True)
    print("-" * 96, flush=True)
    print("READING (L5):", flush=True)
    if q.bit_length() >= 64:
        print(f"  q_min is ENORMOUS ({q.bit_length()} bits) despite v_{p}(q_min)=0.  The", flush=True)
        print("  per-prime e_max floor is REFUTED, but OP1's real target (full q_min super-", flush=True)
        print(f"  polynomial) is UNHARMED: the {p}-part vanished while other primes carry the", flush=True)
        print("  Vandermonde growth.  The sufficient per-prime route is dead; q_min-direct lives.", flush=True)
    else:
        print(f"  q_min is SMALL ({q.bit_length()} bits) — a genuine threat to OP1; the full", flush=True)
        print("  q_min itself was driven down, not just its p-part.  OP1 needs a narrower profile.", flush=True)
    print("RH stays [OUT].", flush=True)
