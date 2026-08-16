#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

DIAGNOSTIC for (PN).  probe_qmin_pernode_formula showed the naive
    v_p(q_min) =? max_j [v_p(W_j) - v_p(Psi(S_j))]
holds only ~83%.  Since cleared_columns scales EVERY column (incl. v_off) by one common Lden,
the per-node clearing factor cancels, and for p|q_min the max(0,.) floor cannot matter (lhs>=1).
So the residual mismatch means either U'/U is not a p-unit at odd p, or the Psi/W model of the
augmented minor is wrong.  This probe ISOLATES that: for each valid K=m collision and each odd
p|q_min it prints, per node j,
    actual_j := v_p(minor_j) - v_p(D_m(A))       [minor_j = |det([A drop j]|d)|, cleared ints]
    model_j  := v_p(Psi(S_j)) - v_p(W_j)
If actual_j == model_j + const (const = v_p(U'/U) global, equal across j) the model is right and
only bookkeeping was off; if they differ PER NODE, the Psi/W factorization is the culprit.
Exact integer + Gaussian-rational arithmetic (L9).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import vpf
import discovery.probe_leg3_affine as A
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows

SIG, TAU = Fr(3, 4), Fr(1)   # D=425


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


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("DIAGNOSE (PN): per-node actual v_p(minor_j)-v_p(D_m(A)) vs model v_p(Psi)-v_p(W). D=425.", flush=True)
    print("=" * 96, flush=True)
    rng = random.Random(1234567)
    shown = 0
    for m in [4, 5, 6]:
        for _ in range(400):
            if shown >= 8:
                break
            p0 = rng.choice([7, 11, 13]); ncls = rng.choice([2, 3])
            bn = class_node_bases(p0, ncls)
            if len(bn) < ncls:
                continue
            assign = [k % ncls for k in range(m)]; rng.shuffle(assign)
            ts = [bn[assign[k]] + p0 * rng.randrange(20) for k in range(m)]
            if len(set(ts)) != m or any(t == 0 for t in ts):
                continue
            oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
            if len(oc) != m or matrix_rank_int(oc, m) != m:
                continue
            q = qmin_fast(oc, vo)
            if not q:
                continue
            DmA = abs(int_det(cols_to_rows(oc, m)))
            minors = []
            aug = oc + [vo]
            for j in range(m):     # drop node column j, keep vo
                sub = [aug[k] for k in range(m + 1) if k != j]
                minors.append(abs(int_det(cols_to_rows(sub, m))))
            xs = [A.x_of(Fr(t)) for t in ts]
            W = [Wfactor(xs, j) for j in range(m)]
            PS = [psi_complement(SIG, TAU, xs, j) for j in range(m)]
            # look only where some odd p mismatches the naive formula
            bad = []
            for p in odd_prime_factors(q):
                naive = max(vpf(W[j], p) - vpf(PS[j], p) for j in range(m) if PS[j] != 0)
                if vpf(Fr(q), p) != naive:
                    bad.append(p)
            if not bad:
                continue
            shown += 1
            print(f"\n[{shown}] m={m} p0-cluster={p0} nodes={ts}", flush=True)
            print(f"    q_min={q}  v_p over MISMATCH primes {bad}", flush=True)
            print(f"    v_p(D_m(A)) at those p: " +
                  ", ".join(f"{p}:{vpf(Fr(DmA),p)}" for p in bad), flush=True)
            for p in bad:
                actual = [vpf(Fr(minors[j]), p) - vpf(Fr(DmA), p) for j in range(m)]
                model = [(vpf(PS[j], p) - vpf(W[j], p)) if PS[j] != 0 else None for j in range(m)]
                diff = [None if model[j] is None else actual[j] - model[j] for j in range(m)]
                print(f"      p={p}: v_p(q)={vpf(Fr(q),p)}  min_j actual={min(actual)} "
                      f"(so v_p(q) pred = {-min(0, min(actual))})", flush=True)
                print(f"         actual_j = {actual}", flush=True)
                print(f"         model_j  = {model}", flush=True)
                print(f"         actual-model = {diff}   (const across j ⇒ global unit only)", flush=True)
    print("\n" + "=" * 96, flush=True)
    print("READING: if 'actual-model' is a single constant per (config,p) ⇒ Psi/W model correct,", flush=True)
    print("mismatch was the missing max(0,.)+unit; if it VARIES across j ⇒ Psi/W factorization is", flush=True)
    print("the defect and must be re-derived.  Note v_p(q)=-min(0,min_j actual) is the EXACT law.", flush=True)
    print("RH stays [OUT].", flush=True)
