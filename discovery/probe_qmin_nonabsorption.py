#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE NON-ABSORPTION TEST (§6ad) — the SOLE remaining rigorous input for OP1 (per §6ac / task #10).

Setup (all exact, L9).  q_min = D_m(A) / D_m([A|d]) (IDENT, verified §6x).  For a prime p,
    v_p(q_min) = v_p(D_m(A)) - v_p(D_m([A|d])),   and by Cramer (K=m) the m-minors of [A|d] are
    { det A } ∪ { det(A, col j -> d) = D_m(A)*x_j }, so
    v_p(D_m([A|d])) = min( v_p(D_m(A)),  min_j v_p(minor_j) ),   minor_j := det(A col j -> d).
Hence, whenever some minor_j is p-smaller than det A,
    v_p(q_min) = v_p(det A) - min_j v_p(minor_j).                       (RESIDUAL)

§6g proves a NUMERATOR floor v_p(det A) >= confluence depth (full m-1 on a SINGLE p-class).
The open question (the "augmented-gcd absorption"): on nodes CLUSTERED mod p (max numerator floor),
does the off-line d-column drive some min_j v_p(minor_j) DOWN (so the floor SURVIVES into q_min,
RESIDUAL large  => non-absorption, OP1 floor holds) or does d share the same p-adic confluence
(min_j v_p(minor_j) == v_p(det A)  => q_min p-part = 0, ABSORBED, OP1 danger)?

This probe, for p in {5,17}, D=425:
  T1  MAX-CLUSTER family {t0 + p*i : i<m} (single x-class mod p, full confluence): report
      v_p(det A), min_j v_p(minor_j), v_p(q_min), and the §6g floor ceil(2m/(p+3))-1.  Cross-check
      v_p(q_min) against qmin_fast (independent SNF).  Non-absorption <=> v_p(q_min) grows.
  T2  Does the ADVERSARY, restricted to nodes clustered mod p, get v_p(q_min) -> 0?  Coordinate
      descent over single-class node choices minimizing v_p(q_min); report the floor it hits.
  T3  Contrast: SPREAD family (distinct x-classes) — expect v_p(q_min) drainable (matches §6z-note).
The verdict distinguishes "aggregate floor provable via a per-p clustered non-absorption lemma"
from "gcd absorbs even on clustered nodes, so the floor is purely aggregate (two-channel)".
Exact integer arithmetic only.  Bounded search (evidence, not proof).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2, ceil
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows
from discovery.probe_leg3_pushm import vp
import discovery.probe_leg3_affine as A

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17
RAM = (5, 17)


def build(ts, m):
    """Return (on-line columns oc as list of m int-vectors length m, off-line d-vector vo) or None."""
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def minor_valuations(oc, vo, m, p):
    """v_p(det A), min_j v_p(minor_j) where minor_j = det(A, col j -> d), and v_p(q_min)=RESIDUAL."""
    Arows = cols_to_rows(oc, m)                       # A as rows, columns = oc
    detA = int_det(Arows)
    if detA == 0:
        return None
    vdet = vp(detA, p)
    vmins = []
    for j in range(m):
        cols = [oc[k] if k != j else vo for k in range(m)]
        mnr = int_det(cols_to_rows(cols, m))
        vmins.append(vp(mnr, p) if mnr != 0 else None)
    finite = [v for v in vmins if v is not None]
    vmin_minor = min(finite) if finite else None
    return vdet, vmin_minor, vmins


def vp_qmin(oc, vo, p):
    q = qmin_fast(oc, vo)
    return (vp(q, p) if q else None), q


def single_class_bases(p):
    """all residues t0 in 1..p-1 whose x-class is a finite on-line class (usable cluster seeds)."""
    c1 = A.xres(Fr(1), p)
    outs = []
    for t0 in range(1, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None:
            outs.append((t0, r))
    return outs


def spread_bases(p, want):
    seen, bases, c1 = set(), [], A.xres(Fr(1), p)
    for t0 in range(1, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None and r not in seen:
            seen.add(r); bases.append(t0)
            if len(bases) >= want:
                break
    return bases


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("NON-ABSORPTION TEST (§6ad): does clustering nodes mod p in {5,17} force v_p(q_min) large?", flush=True)
    print("RESIDUAL: v_p(q_min) = v_p(detA) - min_j v_p(minor_j). §6g floor = ceil(2m/(p+3))-1.", flush=True)
    print("=" * 100, flush=True)

    for p in RAM:
        print(f"\n########## p = {p}  (D=425) ##########", flush=True)
        # pick the cluster seed t0 whose x-class admits the deepest confluence (try each, keep best)
        seeds = single_class_bases(p)
        print("\n--- T1: MAX-CLUSTER family {t0 + p*i}, single x-class (full numerator confluence) ---", flush=True)
        print(f"{'m':>3} | {'floor':>5} | {'v_p(detA)':>9} | {'min v_p(minor)':>14} | {'v_p(q_min)':>10} "
              f"| {'xcheck':>6} | {'seed':>5}", flush=True)
        for m in range(2, 9):
            floor = max(0, ceil(2 * m / (p + 3)) - 1)
            best = None                       # maximize v_p(q_min) over seeds (the confluent optimum)
            for (t0, _r) in seeds:
                ts = [t0 + p * i for i in range(m)]
                b = build(ts, m)
                if not b:
                    continue
                oc, vo = b
                mv = minor_valuations(oc, vo, m, p)
                if mv is None:
                    continue
                vdet, vmin_minor, _ = mv
                resid = vdet - vmin_minor if vmin_minor is not None else vdet
                vq, q = vp_qmin(oc, vo, p)
                if best is None or (vq or 0) > best[3]:
                    best = (t0, vdet, vmin_minor, vq or 0, resid, vq == resid)
            if best is None:
                print(f"{m:>3} | {floor:>5} | (no valid single-class collision)", flush=True)
                continue
            t0, vdet, vmin_minor, vq, resid, ok = best
            print(f"{m:>3} | {floor:>5} | {vdet:>9} | {str(vmin_minor):>14} | {vq:>10} | "
                  f"{str(ok):>6} | {t0:>5}", flush=True)

        print("\n--- T2: ADVERSARY on single-class nodes — can descent drive v_p(q_min) -> 0? ---", flush=True)
        rng = random.Random(20260816 + p)
        print(f"{'m':>3} | {'min v_p(q_min) over clustered nodes':>36}", flush=True)
        for m in range(2, 9):
            best = None
            # enumerate single-class seed t0, and shift the p-adic offsets y_i (nodes t0+p*y_i)
            for (t0, _r) in seeds:
                for _ in range(60):
                    ys = rng.sample(range(0, 40), m)
                    ts = [t0 + p * y for y in ys]
                    b = build(ts, m)
                    if not b:
                        continue
                    oc, vo = b
                    vq, q = vp_qmin(oc, vo, p)
                    if vq is not None and (best is None or vq < best):
                        best = vq
            print(f"{m:>3} | {str(best):>36}", flush=True)

        print("\n--- T3: SPREAD family (distinct x-classes) — contrast, expect drainable (§6z-note) ---", flush=True)
        print(f"{'m':>3} | {'v_p(q_min) spread':>18}", flush=True)
        sb = spread_bases(p, 8)
        for m in range(2, min(len(sb), 8) + 1):
            ts = [sb[i] + p * i for i in range(m)]   # distinct classes, mild spread in the expansion
            b = build(ts, m)
            if not b:
                print(f"{m:>3} | (singular)", flush=True)
                continue
            oc, vo = b
            vq, q = vp_qmin(oc, vo, p)
            print(f"{m:>3} | {str(vq):>18}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if T1 v_p(q_min) GROWS (tracks the §6g floor) on clustered nodes AND T2's", flush=True)
    print("adversary CANNOT drive it to 0, the augmented gcd does NOT absorb the confluence floor at", flush=True)
    print("that p — a per-p clustered NON-ABSORPTION lemma, the missing rigorous input for OP1's", flush=True)
    print("floor. If T2 -> 0 even on clustered nodes, the gcd absorbs per-p and the floor is PURELY", flush=True)
    print("aggregate (two-channel, §6ab), needing the harder joint argument. T3 is the spread control.", flush=True)
    print("Bounded search, one orbit (D=425). Evidence, not proof. RH stays [OUT].", flush=True)
