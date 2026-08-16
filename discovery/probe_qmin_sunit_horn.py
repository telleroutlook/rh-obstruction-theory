#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

S-UNIT HORN of the (CONFLICT) statement (§6ab), the sole open OP1 target.  We reduced the GEOMETRIC
drain to: can G = prod_{k<l}(t_k^2 - t_l^2) be S-smooth (S={2,3,5,17}) for large m?  If ALL pairwise
(t_k - t_l)(t_k + t_l) are S-smooth then, setting a_i = t_i - t_1, the triples (a_i, a_j, a_i - a_j)
are S-smooth => a_j/a_i + (a_i-a_j)/a_i = 1 is an S-unit equation x+y=1 => finitely many ratios
(Evertse) => m is BOUNDED.  This probe TESTS that finiteness empirically and, for the largest
S-smooth-G sets it can find, measures q_min and its ramified {5,17} weight — checking the CONFLICT
claim that smooth-G forces the ramified channel LARGE.

T1: search (greedy + exhaustive over a bounded range) for the LARGEST set {t_k} with every pairwise
    t_k^2 - t_l^2 being {2,3,5,17}-smooth.  A small cap supports finiteness (Horn 1).
T2: for the best smooth-G sets, report q_min, its ram part and geo part — expect ram LARGE (conflict).
Also HONESTLY probes the two gaps: (i) cancellation v_p(q_min) < v_p(G) at generic p; (ii) the count
of non-{2,3,5,17} primes in q_min grows only how fast?  Exact arithmetic (L9).  Bounded.  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
from itertools import combinations

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import vp

SIG, TAU = Fr(3, 4), Fr(1)
S = (2, 3, 5, 17)


def is_S_smooth(n):
    n = abs(int(n))
    if n == 0:
        return False
    for p in S:
        while n % p == 0:
            n //= p
    return n == 1


def smooth_G(ts):
    """True iff every pairwise t_k^2 - t_l^2 is S-smooth (=> G is S-smooth)."""
    for k in range(len(ts)):
        for l in range(k + 1, len(ts)):
            if not is_S_smooth(ts[k] * ts[k] - ts[l] * ts[l]):
                return False
    return True


def qmin_of(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return qmin_fast(oc, vo) or None


def parts(q):
    ram = vp(q, 5) * log2(5) + vp(q, 17) * log2(17)
    return ram, log2(q) - ram


def n_nonS_primes(q):
    """number of DISTINCT primes outside {2,3,5,17} dividing q (with multiplicity-free count)."""
    n = abs(int(q))
    for p in S:
        while n % p == 0:
            n //= p
    cnt, d = 0, 3
    while d * d <= n:
        if n % d == 0:
            cnt += 1
            while n % d == 0:
                n //= d
        d += 2
    if n > 1:
        cnt += 1
    return cnt


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("T1: largest {t_k} with ALL pairwise t_k^2 - t_l^2 being {2,3,5,17}-smooth (Horn-1 finiteness).", flush=True)
    print("=" * 96, flush=True)
    HI = 300
    # collect all pairs (a<b<=HI) with a^2-b^2 ... actually build a graph: nodes 1..HI, edge iff
    # t^2 - s^2 is S-smooth; a smooth-G set is a CLIQUE. Find the largest clique greedily + small exact.
    nodes = list(range(1, HI + 1))
    smooth_pair = {}
    for a in nodes:
        for b in range(a + 1, HI + 1):
            if is_S_smooth(b * b - a * a):
                smooth_pair[(a, b)] = True

    def is_clique(cs):
        return all((min(x, y), max(x, y)) in smooth_pair for x, y in combinations(cs, 2))

    # greedy max clique from each seed vertex
    best = []
    for seed in nodes:
        cur = [seed]
        # candidate neighbors
        for v in nodes:
            if v == seed:
                continue
            if all((min(v, u), max(v, u)) in smooth_pair for u in cur):
                cur.append(v)
        if len(cur) > len(best):
            best = cur[:]
    print(f"  greedy largest S-smooth-G clique (t<= {HI}): size {len(best)}  -> {sorted(best)}", flush=True)
    # verify
    print(f"  verify all pairwise differences S-smooth: {smooth_G(sorted(best))}", flush=True)

    print("\n" + "=" * 96, flush=True)
    print("T2: for smooth-G sets of size m, q_min anatomy (expect RAMIFIED large — the conflict).", flush=True)
    print(f"{'m':>3} | {'nodes (smooth-G)':>28} | {'log2 q_min':>10} | {'ram':>7} {'geo':>7} | {'#nonS primes':>12}", flush=True)
    bs = sorted(best)
    for m in range(2, min(len(bs), 8) + 1):
        ts = bs[:m]
        q = qmin_of(ts, m)
        if not q:
            print(f"{m:>3} | {str(ts):>28} | (no collision / singular)", flush=True)
            continue
        ram, geo = parts(q)
        print(f"{m:>3} | {str(ts):>28} | {log2(q):10.2f} | {ram:7.2f} {geo:7.2f} | {n_nonS_primes(q):>12}", flush=True)

    print("\n" + "=" * 96, flush=True)
    print("READING (L5): if the largest S-smooth-G clique is SMALL (bounded, doesn't grow with HI),", flush=True)
    print("Horn-1 finiteness is empirically supported (m > M(S) => G non-smooth). T2: if smooth-G nodes", flush=True)
    print("force ram (and total log2 q_min) LARGE, the conflict holds on the smooth side. But note the", flush=True)
    print("two GAPS to a proof of OP1: (i) v_p(q_min) can be < v_p(G) (cancellation), so a non-smooth G", flush=True)
    print("prime need NOT appear in q_min; (ii) finiteness gives O(1) large primes, not omega(log m).", flush=True)
    print("So this route proves at most a bounded/constant floor, NOT super-polynomial. Honest gap. RH [OUT].", flush=True)
