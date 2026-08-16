#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

The DECISIVE test of full Open Problem 1: minimize the TRUE collision size
(= max|coeff| over the whole integer relation, on-line c_k AND off-line q) over
all constructions.  (probe_adversarial_qmin.py minimized only q_min, the
off-line-multiplicity partial bound; when q_min=1 the size can still be forced
large by the on-line coefficients.  Here we minimize the actual size via exact
LLL shortest relation.)

If  min_construction size(m)  grows super-polynomially in m  =>  STRONG evidence
OP1 is TRUE (no poly-size Li-collision survives, over all constructions tried).
If some construction drives size to polynomial  =>  OP1 would be FALSE; the
construction is reported as a candidate counterexample for follow-up.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
from discovery.probe_covolume_floor import O_orbit_direct, shortest_rel_custom


def size_for(ts, sigma, tau, m):
    """max|coeff| of the shortest integer collision relation (q!=0), or None."""
    best = shortest_rel_custom(ts, O_orbit_direct(sigma, tau, m), m)
    if best is None:
        return None
    nc, q, mc = best
    return max(max(abs(x) for x in nc), abs(q))


def node_families(m, Kmax):
    for K in range(m + 1, Kmax + 1):
        yield (f"half-int K={K}", [Fr(1, 2) + Fr(i) for i in range(K)])
        yield (f"integer  K={K}", [Fr(i) for i in range(1, K + 1)])
        yield (f"small-frac K={K}", [Fr(1, 2)] + [Fr(1, d) for d in range(2, K + 1)])
        yield (f"thirds   K={K}", [Fr(a, 3) for a in range(1, K + 1)])


if __name__ == "__main__":
    print("=" * 72)
    print("DECISIVE OP1 test: minimize TRUE collision size over constructions.")
    print("DISCOVERY TIER (conjecture only).")
    print("=" * 72)
    offlines = [(Fr(3, 4), Fr(1)), (Fr(3, 4), Fr(1, 2)), (Fr(2, 3), Fr(1)),
                (Fr(5, 6), Fr(1, 2)), (Fr(3, 4), Fr(2))]
    print("min over node families & off-line orbits of the shortest-relation")
    print("max|coeff| (the true collision-size floor).\n")
    print(f"{'m':>3} | {'min size':>22} | {'log2':>7} | {'dlog2':>7} | "
          f"{'best construction':>36}")
    print("-" * 90)
    prev = None
    for m in range(2, 8):
        Kmax = m + 6
        best_s = None
        best_desc = ""
        for (sigma, tau) in offlines:
            for (name, ts) in node_families(m, Kmax):
                if any(t == 0 for t in ts):
                    continue
                try:
                    s = size_for(ts, sigma, tau, m)
                except Exception:
                    s = None
                if s is None or s <= 0:
                    continue
                if best_s is None or s < best_s:
                    best_s = s
                    best_desc = f"off({sigma},{tau}) {name}"
        if best_s is None:
            print(f"{m:>3} | (no valid collision found)")
            continue
        l2 = log2(best_s)
        dl = f"{l2 - prev:+.2f}" if prev is not None else "  -  "
        prev = l2
        print(f"{m:>3} | {best_s:>22} | {l2:>7.2f} | {dl:>7} | {best_desc:>36}")
    print("\nDecision: min TRUE size growing exponentially (dlog2 bounded below)")
    print("=> strong evidence OP1 TRUE.  Flattening to polynomial => OP1 FALSE")
    print("(report the construction).  This is the actual OP1 quantity, unlike")
    print("the q_min partial bound.")
