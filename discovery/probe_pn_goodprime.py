#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

CONFIRM the good/bad-prime split of (PN).  Diagnostic probe_pn_diagnose showed the confluent-
Vandermonde per-node model
    model_j := v_p(Psi(S_j)) - v_p(W_j),   actual_j := v_p(minor_j) - v_p(D_m(A))
matches (actual_j - model_j constant across j) at GOOD primes but VARIES across j exactly at the
orbit-ramified primes and the clustering prime.  Hypothesis to confirm:

    (PN-good)  for every odd prime p that is GOOD for the config
               [ p does not divide any node denominator 4t_k^2+1, all x_k distinct mod p,
                 all x_k != 1 mod p, and u reduces mod p ],
               the EXACT law gives  v_p(q_min) = max(0, max_j[v_p(W_j) - v_p(Psi(S_j))]),
    while at BAD (degenerate) primes the model may fail.

We tabulate, over many valid K=m collisions: among all odd p | q_min, how many are GOOD, and of
those how many satisfy (PN-good); and how many BAD primes exist and how many of THOSE mismatch.
If GOOD primes are 100% and mismatches are confined to BAD primes, (PN) is a partial [THM] whose
scope EXCLUDES precisely the mass-carrying degenerate primes.  Exact arithmetic (L9). RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import vpf
import discovery.probe_leg3_affine as A

ORBITS = [("D=425", Fr(3, 4), Fr(1)), ("D=4", Fr(2, 5), Fr(4, 5)), ("D=26", Fr(1), Fr(1, 5))]


def class_node_bases(p, want):
    seen, bases, c1 = set(), [], A.xres(Fr(1), p)
    for t0 in range(1, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None and r != c1 and r not in seen:
            seen.add(r); bases.append(t0)
            if len(bases) >= want:
                break
    return bases


def psi_complement(u_re, u_tau, xs, j):
    re, im = u_re - 1, u_tau
    for l in range(len(xs)):
        if l == j:
            continue
        ar, ai = u_re - xs[l], u_tau
        re, im = re * ar - im * ai, re * ai + im * ar
    return 2 * re


def Wfactor(xs, j):
    w = xs[j] - 1
    for l in range(len(xs)):
        if l != j:
            w *= (xs[l] - xs[j])
    return w


def odd_prime_factors(n):
    fs, d, n = set(), 3, abs(n)
    while d * d <= n:
        while n % d == 0:
            fs.add(d); n //= d
        d += 2
    if n > 2:
        fs.add(n)
    return fs


def redmod(fr, p):
    """Fraction mod p, or None if denominator not invertible mod p."""
    from math import gcd
    if gcd(fr.denominator, p) != 1:
        return None
    return (fr.numerator * pow(fr.denominator, -1, p)) % p


def is_good_prime(p, ts, xs, sig, tau):
    if redmod(sig, p) is None or redmod(tau, p) is None:
        return False
    xr = []
    for t in ts:
        den = 4 * t * t + 1
        if den % p == 0:
            return False
    for x in xs:
        r = redmod(x, p)
        if r is None or r == 1 % p:
            return False
        xr.append(r)
    return len(set(xr)) == len(xr)


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("(PN-good): (PN) holds at GOOD odd primes; may fail at BAD (degenerate) primes. 3 orbits.", flush=True)
    print("=" * 96, flush=True)
    rng = random.Random(9090909)
    good_ok = good_tot = bad_mis = bad_tot = 0
    good_fail_examples = []
    for name, sig, tau in ORBITS:
        got = 0
        for _ in range(4000):
            if got >= 120:
                break
            m = rng.choice([3, 4, 5])
            p0 = rng.choice([7, 11, 13]); ncls = rng.choice([2, 3])
            bn = class_node_bases(p0, ncls)
            if len(bn) < ncls:
                continue
            assign = [k % ncls for k in range(m)]; rng.shuffle(assign)
            ts = [bn[assign[k]] + p0 * rng.randrange(20) for k in range(m)]
            if len(set(ts)) != m or any(t == 0 for t in ts):
                continue
            oc, vo = cleared_columns([Fr(t) for t in ts], sig, tau, m)
            if len(oc) != m or matrix_rank_int(oc, m) != m:
                continue
            q = qmin_fast(oc, vo)
            if not q:
                continue
            got += 1
            xs = [A.x_of(Fr(t)) for t in ts]
            W = [Wfactor(xs, j) for j in range(m)]
            PS = [psi_complement(sig, tau, xs, j) for j in range(m)]
            for p in odd_prime_factors(q):
                if any(PS[j] == 0 for j in range(m)):
                    continue
                pred = max(0, max(vpf(W[j], p) - vpf(PS[j], p) for j in range(m)))
                match = (vpf(Fr(q), p) == pred)
                if is_good_prime(p, ts, xs, sig, tau):
                    good_tot += 1
                    if match:
                        good_ok += 1
                    elif len(good_fail_examples) < 8:
                        good_fail_examples.append((name, m, p, vpf(Fr(q), p), pred, ts))
                else:
                    bad_tot += 1
                    if not match:
                        bad_mis += 1
        print(f"  {name}: sampled {got} valid collisions "
              f"(good {good_ok}/{good_tot}, bad-mismatch {bad_mis}/{bad_tot})", flush=True)
    print("\n" + "=" * 96, flush=True)
    print(f"GOOD primes: (PN) held {good_ok}/{good_tot}.", flush=True)
    print(f"BAD  primes: mismatched {bad_mis}/{bad_tot} (model expected to fail here).", flush=True)
    if good_fail_examples:
        print("GOOD-prime FAILURES (refine the 'good' predicate):", flush=True)
        for nm, m, p, lhs, pred, ts in good_fail_examples:
            print(f"   {nm} m={m} p={p}: v_p(q)={lhs} pred={pred} nodes={ts}", flush=True)
        print("READING (L5): 'good' predicate incomplete — a degeneracy is unaccounted.", flush=True)
    else:
        print("READING (L5): (PN) is EXACT at all sampled GOOD primes ⇒ partial [THM]: the confluent-", flush=True)
        print("Vandermonde per-node law v_p(q_min)=max(0,max_j[v_p(W_j)-v_p(Psi(S_j))]) holds off the", flush=True)
        print("degenerate primes. But it is p-adically BLIND at the ramified/collision primes, which", flush=True)
        print("carry q_min's mass (§6w/§6z) ⇒ (PN) cannot be the lower-bound vehicle; the barrier is", flush=True)
        print("genuinely aggregate + ramification-driven, not Vandermonde-isolation-driven.", flush=True)
    print("RH stays [OUT].", flush=True)
