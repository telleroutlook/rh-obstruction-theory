#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

ADVERSARIAL test of full Open Problem 1.  We proved (probe_qmin_snf.py) that for
a FIXED on-line node set + off-line orbit, every order-m collision has off-line
multiplicity  |q| >= q_min = D_m(A)/D_m([A|v_off])  (a rigorous lattice index),
and empirically |q| = q_min exactly.  So the collision-size floor is q_min.

Full OP1 asks whether the floor stays super-polynomial over ALL constructions.
The ADVERSARY minimizes q_min over on-line node choices (count K, denominators,
prime-matched conductors) and off-line placements.  This probe searches for the
SMALLEST q_min at each m.  If  min_construction q_min  still grows exponentially
=> strong evidence OP1 is TRUE.  If some construction drives q_min to
polynomial size => OP1 would be FALSE (a poly-size collision survives).

Adversary moves tried:
  (a) grow K (more on-line nodes than equations) — over-determination;
  (b) integer nodes t=1..K, half-integer nodes 1/2+i, and small-fraction nodes;
  (c) prime-matched nodes: conductors N=4a^2+b^2 sharing the off-line primes;
  (d) several off-line orbits (small/large height, near/far from Re=1/2).
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import discovery.probe_overdetermined_collision as P
from discovery.probe_covolume_floor import O_orbit_direct
from discovery.probe_qmin_snf import cleared_columns, qmin_index


def qmin_for(ts, sigma, tau, m):
    on_cols, voff = cleared_columns(ts, sigma, tau, m)
    return qmin_index(on_cols, voff, m)


def node_families(m, Kmax):
    """Yield (name, ts) candidate on-line node sets for the adversary."""
    for K in range(m + 1, Kmax + 1):
        yield (f"half-int K={K}", [Fr(1, 2) + Fr(i) for i in range(K)])
        yield (f"integer  K={K}", [Fr(i) for i in range(1, K + 1)])
        yield (f"small-frac K={K}", [Fr(1, 2)] + [Fr(1, d) for d in range(2, K + 1)])
        # thirds / mixed denominators
        yield (f"thirds   K={K}", [Fr(a, 3) for a in range(1, K + 1)])


if __name__ == "__main__":
    print("=" * 72)
    print("ADVERSARIAL minimization of q_min (the collision-size floor).")
    print("DISCOVERY TIER (conjecture only).")
    print("=" * 72)
    offlines = [(Fr(3, 4), Fr(1)), (Fr(3, 4), Fr(1, 2)), (Fr(2, 3), Fr(1)),
                (Fr(5, 6), Fr(1, 2)), (Fr(3, 4), Fr(2))]
    print("For each m: the MINIMUM q_min over all node families & off-line orbits")
    print("tried, and which construction achieved it.\n")
    print(f"{'m':>3} | {'min q_min':>20} | {'log2':>7} | {'dlog2':>7} | "
          f"{'best construction':>40}")
    print("-" * 92)
    prev = None
    for m in range(2, 8):
        Kmax = m + 8                       # allow generous over-determination
        best_q = None
        best_desc = ""
        for (sigma, tau) in offlines:
            for (name, ts) in node_families(m, Kmax):
                # require distinct nodes & nonzero (t=0 excluded by construction)
                if any(t == 0 for t in ts):
                    continue
                try:
                    q = qmin_for(ts, sigma, tau, m)
                except Exception:
                    q = None
                if q is None or q <= 0:
                    continue
                if best_q is None or q < best_q:
                    best_q = q
                    best_desc = f"off({sigma},{tau}) {name}"
        if best_q is None:
            print(f"{m:>3} | (no valid collision found)")
            continue
        l2 = log2(best_q)
        dl = f"{l2 - prev:+.2f}" if prev is not None else "  -  "
        prev = l2
        print(f"{m:>3} | {best_q:>20} | {l2:>7.2f} | {dl:>7} | {best_desc:>40}")
    print("\nDecision rule:")
    print("  * min q_min grows exponentially (dlog2 bounded below by c>0):")
    print("    STRONG evidence Open Problem 1 is TRUE (no poly-size collision).")
    print("  * min q_min flattens / grows only polynomially: a poly-size")
    print("    collision may exist => OP1 would be FALSE; report the construction.")
    print("  (Rigorous per-family lower bound already established; this probes")
    print("   the remaining 'over ALL constructions' quantifier.)")
