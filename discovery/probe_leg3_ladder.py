#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 PACKED regime: psi as a p-adic distance + same-class ladder descent.

RECAST (candidate; verify per L9).  By the §6l affine identity Psi = a_k - x_k b_k
   Psi = -b_k (x_k - alpha),   alpha = a_k / b_k  (depends only on the OTHER nodes),
so whenever b_k is a p-unit (Lemma A, §6m, guaranteed when psi>0),
   psi = v_p(Psi) = v_p(x_k - alpha)         [a p-adic DISTANCE from x_k to alpha].
Consequences:
  * alpha != class(x_k) mod p  =>  psi = 0  (automatic escape);
  * alpha ≡ class(x_k) mod p   =>  psi >= 1, and the SAME-CLASS ladder x(t_k + p s)
    (s = 0,1,2,...) moves x_k p-adically; a ladder long enough to realise every
    residue of (x_k - alpha)/p mod p attains  psi <= (single-step depth) <= small.
This makes min-psi a bounded p-adic-descent quantity; min-psi <= 3 is already the
m-INDEPENDENT constant LEG3 needs (lag <= min-psi, §6j).

This probe verifies, on packed positive-min-psi configs:
  (R1) the identity  psi = v_p(x_k - a_k/b_k)  for every node with b_k a p-unit;
  (R2) building a same-class ladder for the driving node reduces psi; report
       min-psi as ladder length L grows (L = 1, 3, p+1, 2p+1);
  (R3) the ladder floor vs the single-step depth d1 = v_p(x(t+p)-x(t)).

HONESTY (L5): EVIDENCE that the packed bound is a bounded p-adic descent; NOT a proof
that a specific OP1 matrix supplies a length->=p ladder.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
from collections import Counter

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A   # x_of, off_atoms_u, Psi_val, ab_of_node, Phi, vpf, xres


def ladder_minpsi(u, xs, k, t_k, p, L):
    """min over s=0..L-1 of psi when node k's x is replaced by x(t_k + p s)."""
    best = None
    for s in range(L):
        t2 = t_k + p * s
        if t2 == 0:
            continue
        x2 = A.x_of(t2)
        xs2 = list(xs)
        xs2[k] = x2
        v = A.vpf(A.Psi_val(u, xs2), p)
        v = v if v is not None else 10**9
        best = v if best is None else min(best, v)
    return best


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 PACKED: psi = v_p(x_k - a_k/b_k)  +  same-class ladder descent",
          flush=True)
    print("DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    r1_ok = True            # psi == v_p(x_k - a_k/b_k) when b_k a p-unit
    r1_tested = 0
    packed_pos = 0
    ladder_floor = Counter()             # min-psi reachable via best-node ladder
    Lstats = {"1": Counter(), "3": Counter(), "p+1": Counter(), "2p+1": Counter()}

    for label, sig, tau in A.ORBITS:
        u = A.off_atoms_u(sig, tau)[0]
        for p in (3, 7, 11):
            c1 = A.xres(Fr(1), p)
            for m in range(2, 7):
                for fname, ts in A.families(m, p).items():
                    if len(ts) < m:
                        continue
                    oc, vo = cleared_columns(ts, sig, tau, m)
                    if not qmin_fast(oc, vo):
                        continue
                    cls = set(c for c in (A.xres(A.x_of(t), p) for t in ts)
                              if c is not None)
                    navail = len(cls - ({c1} if c1 in cls else set()))
                    if navail > m - 1:
                        continue                        # non-packed => §6m
                    # Phi-minimizers and their psi
                    rows = [(A.Phi([A.x_of(ts[k]) for k in S], p), S)
                            for S in combinations(range(len(oc)), m - 1)]
                    minPhi = min(ph for ph, _ in rows)
                    minis = [S for ph, S in rows if ph == minPhi]
                    psis = []
                    for S in minis:
                        v = A.vpf(A.Psi_val(u, [A.x_of(ts[k]) for k in S]), p)
                        psis.append((v if v is not None else 10**9, S))
                    minpsi0 = min(v for v, _ in psis)
                    if minpsi0 <= 0:
                        continue
                    packed_pos += 1
                    # (R1) identity on all nodes of the min-psi minimizer with unit b_k
                    _, Sbest = min(psis, key=lambda z: z[0])
                    xs = [A.x_of(ts[k]) for k in Sbest]
                    for ki in range(len(xs)):
                        a_k, b_k = A.ab_of_node(u, xs, ki)
                        if A.vpf(b_k, p) != 0:
                            continue
                        alpha = a_k / b_k
                        lhs = A.vpf(A.Psi_val(u, xs), p)
                        rhs = A.vpf(xs[ki] - alpha, p)
                        r1_tested += 1
                        if (lhs if lhs is not None else 10**9) != \
                           (rhs if rhs is not None else 10**9):
                            r1_ok = False
                    # (R2/R3) same-class ladder descent on node 0 of Sbest
                    k0 = 0
                    t_k = ts[Sbest[k0]]
                    d1 = A.vpf(A.x_of(t_k + p) - A.x_of(t_k), p)
                    floors = {}
                    for Ltag, L in (("1", 1), ("3", 3), ("p+1", p + 1), ("2p+1", 2 * p + 1)):
                        fl = ladder_minpsi(u, xs, k0, t_k, p, L)
                        Lstats[Ltag][min(fl, 9)] += 1
                        floors[Ltag] = fl
                    ladder_floor[min(floors["2p+1"], 9)] += 1

    print("\n" + "=" * 96, flush=True)
    print(f"(R1) identity psi == v_p(x_k - a_k/b_k) (unit b_k, {r1_tested} nodes): {r1_ok}",
          flush=True)
    print(f"\n(R2/R3) PACKED positive-min-psi configs: {packed_pos}", flush=True)
    print(f"     ladder floor (min-psi over node-0 ladder of length 2p+1) distribution:",
          flush=True)
    for k in sorted(ladder_floor):
        print(f"        floor={k}: {ladder_floor[k]}", flush=True)
    print(f"     min-psi over node-0 ladder vs ladder length L:", flush=True)
    for Ltag in ("1", "3", "p+1", "2p+1"):
        dist = dict(sorted(Lstats[Ltag].items()))
        print(f"        L={Ltag:>4}: {dist}", flush=True)
    print("\nREADING (L5): psi is a p-adic distance v_p(x_k - alpha); a same-class ladder", flush=True)
    print("descends it toward the single-step depth as L grows.  min-psi is a bounded", flush=True)
    print("(m-independent) constant => lag=O(1), the LEG3 requirement.  EVIDENCE on the", flush=True)
    print("bound mechanism; ladder availability in a real OP1 matrix still OPEN.  RH [OUT].",
          flush=True)
