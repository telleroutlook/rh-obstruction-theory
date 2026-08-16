#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

STRUCTURAL REFORMULATION of the corrected (aggregate) OP1 target.  §6x gave direct evidence
that inf log q_min grows ~linearly.  To get a RIGOROUS handle we test the clean determinantal
identity

        (IDENT)   q_min  =  D_m(A) / D_m([A|d])                 (both determinantal divisors)

where D_r(X)=gcd of r x r minors of X.  If (IDENT) holds exactly, then

        log q_min  =  log D_m(A)  -  log D_m([A|d]),

decoupling the aggregate barrier quantity into a NUMERATOR channel (D_m(A), the confluent-
Vandermonde/product growth of §6c-6g, PROVABLY large) MINUS a DENOMINATOR channel
(D_m([A|d]), the adversary's only tool: augmenting with the off-line d can only shrink the
gcd).  The aggregate target log q_min super-poly becomes: the adversary cannot make
log D_m([A|d]) track log D_m(A) to within o(growth).

This probe, on MINIMAL valid collisions (K=m, so D_m(A)=|det A| is one m x m determinant and
D_m([A|d]) is the gcd of the m+1 m-minors of the m x (m+1) augmented matrix — both cheap):
  (1) VERIFIES (IDENT) exactly against qmin_fast (independent SNF), across 3 orbits / adversaries;
  (2) tabulates log2 D_m(A), log2 D_m([A|d]), and their difference = log2 q_min, vs m, to show
      HOW the two channels grow and that the gap (=log q_min) grows while both channels do.

Exact integer arithmetic only (L9).  Bounded search (evidence, not proof).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2, gcd
from itertools import combinations
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
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


def int_det(M):
    """exact integer determinant of a square integer matrix (fraction-free Bareiss)."""
    n = len(M)
    M = [[Fr(x) for x in row] for row in M]
    det = Fr(1)
    for i in range(n):
        piv = None
        for r in range(i, n):
            if M[r][i] != 0:
                piv = r; break
        if piv is None:
            return 0
        if piv != i:
            M[i], M[piv] = M[piv], M[i]; det = -det
        det *= M[i][i]
        inv = M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / inv
            if f:
                for c in range(i, n):
                    M[r][c] -= f * M[i][c]
    assert det.denominator == 1
    return int(det)


def cols_to_rows(cols, m):
    return [[cols[j][i] for j in range(len(cols))] for i in range(m)]


def Dm_A(oc, m):
    """K=m: D_m(A) = |det of the single m x m matrix|."""
    rows = cols_to_rows(oc, m)                 # m x m
    return abs(int_det(rows))


def Dm_Ad(oc, vo, m):
    """D_m([A|d]) = gcd of all m-minors of the m x (m+1) augmented matrix (drop-one-column)."""
    aug = oc + [vo]                            # m+1 columns
    g = 0
    for drop in range(len(aug)):
        sub = [aug[j] for j in range(len(aug)) if j != drop]   # m columns
        rows = cols_to_rows(sub, m)
        g = gcd(g, abs(int_det(rows)))
    return g


def build(sig, tau, ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    pool = [Fr(t) for t in ts]
    oc, vo = cleared_columns(pool, sig, tau, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def gen_nodes(kind, sig, tau, m, rng):
    if kind == "cluster":
        p = rng.choice([7, 11, 13]); ncls = rng.choice([2, 3])
        bn = class_node_bases(p, ncls)
        if len(bn) < ncls:
            return None
        assign = [k % ncls for k in range(m)]; rng.shuffle(assign)
        return [bn[assign[k]] + p * rng.randrange(30) for k in range(m)]
    if kind == "spread":
        p = rng.choice([11, 13]); bn = class_node_bases(p, (p - 1) // 2)
        if len(bn) < min(m, len(bn)):
            return None
        return [bn[k % len(bn)] + p * rng.randrange(30) for k in range(m)]
    return rng.sample(range(1, 400), m)


if __name__ == "__main__":
    print("=" * 98, flush=True)
    print("IDENT  q_min = D_m(A)/D_m([A|d])  — verify exact + decompose the aggregate channels.", flush=True)
    print("Minimal valid collisions K=m; 3 orbits; cluster/spread/random adversaries. No RH.", flush=True)
    print("=" * 98, flush=True)
    rng = random.Random(31415)
    ident_ok = ident_tot = 0
    for name, sig, tau in ORBITS:
        print(f"\norbit {name}:  m :  log2 D_m(A) | log2 D_m([A|d]) | diff = log2 q_min   (min over adversaries)", flush=True)
        for m in range(2, 10):
            best = None   # minimize q_min
            for _ in range(240):
                kind = rng.choice(["cluster", "cluster", "spread", "random"])
                ts = gen_nodes(kind, sig, tau, m, rng)
                if ts is None:
                    continue
                b = build(sig, tau, ts, m)
                if b is None:
                    continue
                oc, vo = b
                q = qmin_fast(oc, vo)
                if not q:
                    continue
                dA = Dm_A(oc, m)
                dAd = Dm_Ad(oc, vo, m)
                ident_tot += 1
                if dAd and dA % dAd == 0 and dA // dAd == q:
                    ident_ok += 1
                if best is None or q < best[0]:
                    best = (q, dA, dAd)
            if best is None:
                continue
            q, dA, dAd = best
            print(f"          {m:>2} : {log2(dA):10.2f}  | {log2(dAd):12.2f}   | {log2(q):8.2f}", flush=True)
    print("\n" + "=" * 98, flush=True)
    print(f"IDENT q_min == D_m(A)/D_m([A|d]) held EXACTLY on {ident_ok}/{ident_tot} valid collisions.", flush=True)
    print("READING (L5): if 100%, (IDENT) is a verified determinantal reformulation of the", flush=True)
    print("aggregate barrier quantity: log q_min = log D_m(A) - log D_m([A|d]). The numerator", flush=True)
    print("channel is the confluent-Vandermonde growth (PROVABLE, §6c-6g); the aggregate target", flush=True)
    print("reduces to: the d-augmented gcd cannot track it. Exact identity; bound still open.", flush=True)
    print("RH stays [OUT].", flush=True)
