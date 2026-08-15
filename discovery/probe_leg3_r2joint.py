#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 (§6r continuation): the DECISIVE (R2) experiment -- does the COLLISION-VALIDITY
constraint (q_min != 0) cap min-psi even at the HARDEST pool size K=m?

Why K=m is the adversary's best case.  With navail=m-1 classes and K=m nodes, exactly ONE
class has 2 reps {a,b}, the rest one each.  The ONLY Phi-minimizers are C∪{a} and C∪{b}
(C = the singletons), so
    min-psi = min( v_p(x_a - alpha), v_p(x_b - alpha) ),   alpha = alpha(C) fixed by C.
There is NO third minimizer to "undo" a deep alignment (unlike K>m).  The single-swing
probe (§6r-note2) showed a FREE swing reaches psi=6 against a fixed alpha.  So IF a valid
collision can put alpha deeply aligned with the {a,b} class, min-psi would be large and
LEG3 would fail.  This probe searches HARD (coordinate ascent, deep p-adic range, many
restarts) for a VALID collision (qmin_fast True) maximising min-psi at K=m.

CHECKS (orbit D=425, p in {7,11}, m=3..5):
  (J) max over VALID collisions (K=m) of min-psi, via coordinate ascent on all node
      s-offsets, restarts; deep range S up to 243.  Report max & the (p,m) it occurs at.
  (K) CONTROL: same search WITHOUT the validity filter (any packed pool) -- expected to
      grow (matches single-swing / K=m-1).  The GAP between (K) and (J) is the amount the
      collision constraint removes.

HONESTY (L5): local search, one orbit, small p,m.  If (J) stays <= 2 while (K) grows, the
q_min constraint is the (R2) ceiling mechanism -- strong EVIDENCE, not a proof.  A (J)
value >= 3 would be an honest THREAT to LEG3 (report it).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
import random

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A


def minpsi_over_phimin(u, tl, m, p):
    xs = [A.x_of(t) for t in tl]
    n = len(tl)
    rows = [(A.Phi([xs[k] for k in S], p), S) for S in combinations(range(n), m - 1)]
    minPhi = min(ph for ph, _ in rows)
    best = None
    for ph, S in rows:
        if ph != minPhi:
            continue
        v = A.vpf(A.Psi_val(u, [xs[k] for k in S]), p)
        v = v if v is not None else 10**9
        best = v if best is None else min(best, v)
    return best


def is_valid(pool, sig, tau, m):
    oc, vo = cleared_columns(pool, sig, tau, m)
    return qmin_fast(oc, vo)


def build_pool(bases, svec, p):
    """bases: m-1 class bases; svec: length-m s-offsets, last two share bases[repcls]."""
    # layout: node i (i<m-1) = bases[i] + p*svec[i]; node m-1 = bases[0] + p*svec[m-1]
    # so class 0 is the repeated class with reps svec[0], svec[m-1].
    ts = []
    for i in range(len(bases)):
        t = bases[i] + p * svec[i]
        ts.append(t)
    t_extra = bases[0] + p * svec[-1]
    ts.append(t_extra)
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    return [Fr(t) for t in ts]


def search(u, sig, tau, p, m, S, rng, restarts, require_valid):
    r = m - 1
    if r < 1 or r >= p:
        return 0
    best_overall = 0
    for _ in range(restarts):
        bases = rng.sample(range(1, p), r)
        svec = [rng.randrange(S) for _ in range(m)]
        pool = build_pool(bases, svec, p)
        cur = -1
        if pool is not None and (not require_valid or is_valid(pool, sig, tau, m)):
            v = minpsi_over_phimin(u, pool, m, p)
            cur = v if (v is not None and v < 10**9) else -1
        improved = True
        guard = 0
        while improved and guard < 40:
            guard += 1
            improved = False
            for j in range(m):
                bj = cur
                bs = svec[j]
                for sj in range(S):
                    svec[j] = sj
                    pool = build_pool(bases, svec, p)
                    if pool is None:
                        continue
                    if require_valid and not is_valid(pool, sig, tau, m):
                        continue
                    v = minpsi_over_phimin(u, pool, m, p)
                    v = v if (v is not None and v < 10**9) else -1
                    if v > bj:
                        bj, bs = v, sj
                svec[j] = bs
                if bj > cur:
                    cur, improved = bj, True
        best_overall = max(best_overall, cur)
    return best_overall


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 (§6r/R2): does q_min validity cap min-psi at the hardest K=m?",
          flush=True)
    print("Orbit D=425 (split-only).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    sig, tau = Fr(3, 4), Fr(1)
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260816)

    print(f"\n{'p':>3} {'m':>3}   " +
          "  ".join(f"S={S}:valid/ctrl" for S in (27, 81, 243)), flush=True)
    threat = False
    for p in (7, 11):
        for m in (3, 4, 5):
            if m - 1 >= p:
                continue
            cells = []
            for S in (27, 81, 243):
                jv = search(u, sig, tau, p, m, S, rng, restarts=12, require_valid=True)
                kc = search(u, sig, tau, p, m, S, rng, restarts=12, require_valid=False)
                cells.append((jv, kc))
                if jv >= 3:
                    threat = True
            print(f"{p:>3} {m:>3}   " +
                  "   ".join(f"{jv:>2}/{kc:>2}" for jv, kc in cells), flush=True)

    print("\n" + "=" * 96, flush=True)
    if threat:
        print("THREAT (L5): a VALID collision reached min-psi >= 3 at K=m -- the q_min", flush=True)
        print("constraint does NOT cap the lag by itself.  LEG3 O(1) needs a further", flush=True)
        print("argument (or narrower profile).  HONEST negative.  RH [OUT].", flush=True)
    else:
        print("READING (L5): every VALID collision (K=m) column stays <= 2 while the", flush=True)
        print("no-validity CONTROL grows -- the q_min collision constraint is exactly what", flush=True)
        print("caps min-psi (=lag) at a small constant.  This is the (R2) mechanism:", flush=True)
        print("deep alpha-alignment is incompatible with being a valid collision.", flush=True)
        print("Strong EVIDENCE, not a proof.  split-only OP1 OPEN.  RH [OUT].", flush=True)
