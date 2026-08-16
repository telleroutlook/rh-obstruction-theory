#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

PER-NODE FORMULA for the aggregate barrier quantity.  §6y verified q_min = D_m(A)/D_m([A|d]).
Using the §6g factorization det[A_S]=(unit)*prod(x_k-1)*Vand(S) and the §6i augmented-minor
factorization det[A_{S_j}|d]=(unit)*prod_{k!=j}(x_k-1)*Vand(S_j)*Psi(S_j), the ratio collapses:
for K=m the j-th augmented minor is D_m(A)*Psi(S_j)/W_j (up to a global unit), W_j the confluent
factor of node j.  Hence for every ODD prime p (2 carries the 2^{j-1} leading-coeff unit and is
excluded here) this predicts the clean

        (PN)   v_p(q_min) = max_j [ v_p(W_j) - v_p(Psi(S_j)) ],
               W_j := (x_j - 1) * prod_{l!=j}(x_l - x_j),   Psi(S_j) := 2 Re[(u-1) prod_{l!=j}(u - x_l)],

i.e. q_min's p-part = max over nodes of (node j's Vandermonde ISOLATION minus the complement
orbit-sum's p-content).  This EXPLAINS §6w's prime-draining (v_p=0 for a prime p means: for that
p, EVERY node j has its isolation W_j p-adically cancelled by Psi(S_j)) and is AGGREGATE-friendly:
log q_min = sum_p log p * max_j[v_p(W_j)-v_p(Psi(S_j))].

This probe VERIFIES (PN) exactly on minimal valid collisions (K=m), all odd primes dividing
q_min, 3 orbits, cluster/spread/random adversaries.  Exact rational + Gaussian-rational
arithmetic (L9).  A single mismatch REFUTES (PN) and localizes a missing unit/term; 100% makes
(PN) a candidate [THM].  RH stays [OUT].
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
    seen, bases = set(), []
    c1 = A.xres(Fr(1), p)
    for t0 in range(1, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None and r != c1 and r not in seen:
            seen.add(r); bases.append(t0)
            if len(bases) >= want:
                break
    return bases


def gen_nodes(kind, m, rng):
    if kind == "cluster":
        p = rng.choice([7, 11, 13]); ncls = rng.choice([2, 3])
        bn = class_node_bases(p, ncls)
        if len(bn) < ncls:
            return None
        assign = [k % ncls for k in range(m)]; rng.shuffle(assign)
        return [bn[assign[k]] + p * rng.randrange(25) for k in range(m)]
    if kind == "spread":
        p = rng.choice([11, 13]); bn = class_node_bases(p, (p - 1) // 2)
        return [bn[k % len(bn)] + p * rng.randrange(25) for k in range(m)]
    return rng.sample(range(1, 400), m)


def psi_complement(u_re, u_tau, xs, j):
    """Psi(S_j) = 2 Re[(u-1) * prod_{l!=j}(u - x_l)], exact Fraction (Gaussian-rational)."""
    re, im = u_re - 1, u_tau                      # (u-1)
    for l in range(len(xs)):
        if l == j:
            continue
        ar, ai = u_re - xs[l], u_tau              # (u - x_l), x_l real
        re, im = re * ar - im * ai, re * ai + im * ar
    return 2 * re


def Wfactor(xs, j):
    """W_j = (x_j - 1) * prod_{l!=j}(x_l - x_j), exact Fraction."""
    w = xs[j] - 1
    for l in range(len(xs)):
        if l != j:
            w *= (xs[l] - xs[j])
    return w


def odd_prime_factors(n):
    fs, d = set(), 3
    n = abs(n)
    while d * d <= n:
        while n % d == 0:
            fs.add(d); n //= d
        d += 2
    if n > 2:
        fs.add(n)
    return fs


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("(PN)  v_p(q_min) = max_j [ v_p(W_j) - v_p(Psi(S_j)) ]  for odd p | q_min.  K=m.", flush=True)
    print("Verify exact; 3 orbits; cluster/spread/random.  DISCOVERY. No RH.", flush=True)
    print("=" * 96, flush=True)
    rng = random.Random(2718281)
    ok = tot = 0
    mism = []
    for name, sig, tau in ORBITS:
        for m in range(2, 9):
            got = 0
            for _ in range(300):
                if got >= 40:
                    break
                kind = rng.choice(["cluster", "cluster", "spread", "random"])
                ts = gen_nodes(kind, m, rng)
                if ts is None or any(t == 0 for t in ts) or len(set(ts)) != len(ts):
                    continue
                pool = [Fr(t) for t in ts]
                oc, vo = cleared_columns(pool, sig, tau, m)
                if len(oc) != m or matrix_rank_int(oc, m) != m:
                    continue
                q = qmin_fast(oc, vo)
                if not q:
                    continue
                xs = [A.x_of(Fr(t)) for t in ts]
                W = [Wfactor(xs, j) for j in range(m)]
                PS = [psi_complement(sig, tau, xs, j) for j in range(m)]
                got += 1
                for p in odd_prime_factors(q):
                    lhs = vpf(Fr(q), p)
                    rhs = max(vpf(W[j], p) - vpf(PS[j], p) for j in range(m)
                              if PS[j] != 0)
                    tot += 1
                    if lhs == rhs:
                        ok += 1
                    elif len(mism) < 6:
                        mism.append((name, m, p, lhs, rhs, ts))
            print(f"  {name} m={m}: checked (running total odd-prime checks={tot}, ok={ok})", flush=True)
    print("\n" + "=" * 96, flush=True)
    print(f"(PN) held EXACTLY on {ok}/{tot} odd-prime checks over valid K=m collisions.", flush=True)
    if mism:
        print("MISMATCHES (first few):", flush=True)
        for nm, m, p, lhs, rhs, ts in mism:
            print(f"   {nm} m={m} p={p}: v_p(q)={lhs} vs max_j[...]={rhs}  nodes={ts}", flush=True)
        print("READING (L5): (PN) FALSE as stated — a global unit/term at these p is missing;", flush=True)
        print("the witness localizes it. The identity q_min=D_m(A)/D_m([A|d]) (§6y) still stands.", flush=True)
    else:
        print("READING (L5): (PN) is a verified candidate [THM]: q_min's p-part = max over nodes", flush=True)
        print("of (Vandermonde isolation W_j) minus (complement orbit-sum Psi(S_j)), for odd p.", flush=True)
        print("Aggregate target log q_min = sum_p log p * max_j[v_p(W_j)-v_p(Psi(S_j))]; a prime is", flush=True)
        print("drained iff every node's isolation is cancelled by its complement orbit-sum there.", flush=True)
    print("RH stays [OUT].", flush=True)
