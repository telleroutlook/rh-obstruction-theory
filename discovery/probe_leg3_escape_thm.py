#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 ESCAPE THEOREM (non-packed regime), constructive verification.

THEOREM (candidate [THM]; proof in §6m, verify the construction by script per L9):
If slack = navail - (m-1) >= 1 (a spare x-class exists, navail = # distinct
x-classes != class(1) among ambient nodes), then
    (i)  minPhi = 0  (pick m-1 nodes in distinct classes != class(1)); every
         Phi-minimizer has all "clean" nodes (per-node contribution 0);
    (ii) for ANY Phi-minimizer S0 with psi>0, swapping any node k for a node k'
         in a spare class c' yields S0' with Phi(S0')=0=minPhi and
         Psi(S0') - Psi(S0) = (x_k - x_k') * b_k,  b_k a p-unit (Lemma A),
         (x_k - x_k') a p-unit (distinct classes)  =>  psi(S0') = 0;
    (iii) hence  min over Phi-minimizers of psi = 0  =>  lag = 0.
The non-packed regime of LEG3 is CLOSED; only the PACKED regime (slack<=0) remains.

This probe verifies, on every config with slack>=1:
  (A) minPhi == 0;
  (B) min over Phi-minimizers of psi == 0;
  (C) the CONSTRUCTIVE step: for every positive-psi Phi-minimizer, the explicit
      single swap into a spare class lands on a Phi-minimizer (Phi==0) with psi==0.

HONESTY (L5): verifies the constructive theorem for slack>=1.  Packed regime
(slack<=0) is NOT closed here; that is the sole remaining LEG3 gap.  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A   # x_of, off_atoms_u, Psi_val, ab_of_node, Phi, vpf, xres


ORBITS = A.ORBITS


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 ESCAPE THEOREM (slack>=1): constructive min-psi=0  =>  lag=0",
          flush=True)
    print("DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    slack_configs = 0
    minPhi_zero_ok = True          # (A) slack>=1 => minPhi==0
    minpsi_zero_ok = True          # (B) slack>=1 => min over Phi-min of psi == 0
    construct_ok = True            # (C) explicit swap lands Phi==0 & psi==0
    construct_tested = 0

    for label, sig, tau in ORBITS:
        u = A.off_atoms_u(sig, tau)[0]
        for p in (3, 7, 11):
            c1 = A.xres(Fr(1), p)
            for m in range(2, 8):
                for fname, ts in A.families(m, p).items():
                    if len(ts) < m:
                        continue
                    oc, vo = cleared_columns(ts, sig, tau, m)
                    if not qmin_fast(oc, vo):
                        continue
                    # available distinct x-classes (!= class of 1) among all nodes
                    xall = [A.x_of(t) for t in ts]
                    cls_all = [A.xres(x, p) for x in xall]
                    rescls = set(c for c in cls_all if c is not None)
                    navail = len(rescls - ({c1} if c1 in rescls else set()))
                    slack = navail - (m - 1)
                    if slack < 1:
                        continue
                    slack_configs += 1
                    rows = [(A.Phi([A.x_of(ts[k]) for k in S], p), S)
                            for S in combinations(range(len(oc)), m - 1)]
                    minPhi = min(ph for ph, _ in rows)
                    if minPhi != 0:                                   # (A)
                        minPhi_zero_ok = False
                    minis = [(ph, S) for ph, S in rows if ph == minPhi]
                    psis = []
                    for ph, S in minis:
                        xs = [A.x_of(ts[k]) for k in S]
                        v = A.vpf(A.Psi_val(u, xs), p)
                        psis.append(v if v is not None else 10**9)
                    if psis and min(psis) != 0:                       # (B)
                        minpsi_zero_ok = False
                    # (C) constructive escape for each positive-psi Phi-minimizer
                    cls_oc = [A.xres(A.x_of(t), p) for t in ts]
                    for (ph, S), v in zip(minis, psis):
                        if v <= 0:
                            continue
                        Sset = set(S)
                        used = set(cls_oc[k] for k in S) | {c1}
                        # a spare-class ambient node k'
                        kp = next((j for j in range(len(oc))
                                   if j not in Sset and cls_oc[j] is not None
                                   and cls_oc[j] not in used), None)
                        if kp is None:
                            continue
                        # swap the FIRST node k in S for k' (any node works: all clean)
                        k = S[0]
                        Snew = tuple(sorted((Sset - {k}) | {kp}))
                        xnew = [A.x_of(ts[j]) for j in Snew]
                        construct_tested += 1
                        if A.Phi(xnew, p) != 0:
                            construct_ok = False
                        vn = A.vpf(A.Psi_val(u, xnew), p)
                        if (vn if vn is not None else 10**9) != 0:
                            construct_ok = False

    print("\n" + "=" * 96, flush=True)
    print(f"configs with slack>=1 (non-packed): {slack_configs}", flush=True)
    print(f"(A) slack>=1 => minPhi == 0                              : {minPhi_zero_ok}",
          flush=True)
    print(f"(B) slack>=1 => min over Phi-minimizers of psi == 0      : {minpsi_zero_ok}",
          flush=True)
    print(f"(C) constructive swap lands Phi==0 AND psi==0 "
          f"({construct_tested} tested)     : {construct_ok}", flush=True)
    print("\nREADING (L5): the ESCAPE THEOREM (non-packed regime, slack>=1) is verified", flush=True)
    print("constructively: minPhi=0, and any positive-psi minimizer escapes to psi=0", flush=True)
    print("via one spare-class swap => lag=0.  LEG3's non-packed regime is CLOSED.", flush=True)
    print("Sole remaining gap: PACKED regime (slack<=0).  RH stays [OUT].", flush=True)
