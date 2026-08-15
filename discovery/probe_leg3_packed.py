#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 PACKED regime (slack<=0): is min-psi<=3 a finite-K artifact?

MECHANISM (candidate; verify by script per L9).  In the packed regime the only
remaining freedom is REPRESENTATIVE choice within each x-class (t -> t+p keeps the
class, hence keeps Phi).  With  x(t) = 1 - 2/(4t^2+1),
    x(t') - x(t) = -8 (t-t')(t+t') / [(4t^2+1)(4t'^2+1)].
For p ≡ 3 mod 4 the denominators are p-units (4c^2+1 != 0 since -1 is a non-residue),
so a single step t' = t+p gives  v_p(x(t')-x(t)) = 1  (exactly, generically).  By
Lemma A (§6m) the affine slope b_k is a p-UNIT when psi>0, so swapping one node to a
same-class one-step neighbour changes Psi by  -b_k*Δx  of v_p EXACTLY 1.  Hence from
ANY psi>=2 minimizer, if a same-class deeper representative is AVAILABLE, psi drops.
=> min-psi>1 should occur ONLY when the finite ambient family lacks the needed
representative.  If so, the empirical "min-psi<=3" is a finite-K edge effect, and
augmenting each used class with deeper reps should push min-psi down toward <=1.

This probe tests, on collision configs (focus: PACKED, positive min-psi):
  (H1) v_p(x(t+p)-x(t)) == 1 for same-class one-step pairs (p ≡ 3 mod 4);
  (H2) AUGMENTING the ambient node set with deeper same-class reps (t+p, t+2p; same
       classes => Phi & packing unchanged) reduces min over Phi-minimizers of psi;
  (H3) how low min-psi goes under augmentation (toward <=1?).

HONESTY (L5): EVIDENCE about the SOURCE of the packed-regime bound, not a proof.
Augmentation adds candidate representatives to probe representative-depth dependence;
it does not assert those columns occur in a specific OP1 matrix.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
from collections import Counter

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A   # x_of, off_atoms_u, Psi_val, Phi, vpf, xres


def minpsi_over_phimin(u, tlist, m, p):
    """min over (m-1)-subsets that are Phi-minimizers of psi = v_p(Psi)."""
    xs_all = [A.x_of(t) for t in tlist]
    rows = []
    for S in combinations(range(len(tlist)), m - 1):
        rows.append((A.Phi([xs_all[k] for k in S], p), S))
    if not rows:
        return None
    minPhi = min(ph for ph, _ in rows)
    best = None
    for ph, S in rows:
        if ph != minPhi:
            continue
        v = A.vpf(A.Psi_val(u, [xs_all[k] for k in S]), p)
        v = v if v is not None else 10**9
        best = v if best is None else min(best, v)
    return best


def augment(tlist, p, extra):
    """Add deeper same-class reps t+p*j (j=1..extra) for each present class."""
    out = list(tlist)
    seen = set(tlist)
    for t in tlist:
        for j in range(1, extra + 1):
            t2 = t + p * j
            if t2 != 0 and t2 not in seen:
                out.append(t2)
                seen.add(t2)
    return out


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 PACKED regime: is min-psi<=3 a finite-K artifact of representatives?",
          flush=True)
    print("DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    # (H1) same-class one-step depth
    h1_ok = True
    h1_vals = Counter()
    for p in (3, 7, 11):
        for c in range(0, p):
            t = Fr(c if c != 0 else p)      # a representative of class c (avoid 0)
            v = A.vpf(A.x_of(t + p) - A.x_of(t), p)
            h1_vals[v] += 1
            if v != 1:
                h1_ok = False

    # (H2/H3) augmentation on PACKED positive-min-psi configs
    packed_pos = 0
    reduced = 0
    to_le1 = 0
    before_after = Counter()   # (min-psi before, min-psi after augmentation)

    for label, sig, tau in A.ORBITS:
        u = A.off_atoms_u(sig, tau)[0]
        for p in (3, 7, 11):
            c1 = A.xres(Fr(1), p)
            for m in range(2, 7):                 # cap m for augmented combinatorics
                for fname, ts in A.families(m, p).items():
                    if len(ts) < m:
                        continue
                    oc, vo = cleared_columns(ts, sig, tau, m)
                    if not qmin_fast(oc, vo):
                        continue
                    cls = set(c for c in (A.xres(A.x_of(t), p) for t in ts)
                              if c is not None)
                    navail = len(cls - ({c1} if c1 in cls else set()))
                    if navail > m - 1:            # non-packed: handled by §6m
                        continue
                    mp0 = minpsi_over_phimin(u, ts, m, p)
                    if mp0 is None or mp0 <= 0:
                        continue
                    packed_pos += 1
                    ts_aug = augment(ts, p, 2)
                    mp1 = minpsi_over_phimin(u, ts_aug, m, p)
                    before_after[(min(mp0, 9), min(mp1, 9))] += 1
                    if mp1 < mp0:
                        reduced += 1
                    if mp1 <= 1:
                        to_le1 += 1

    print("\n" + "=" * 96, flush=True)
    print(f"(H1) v_p(x(t+p)-x(t)) for same-class one-step (p ≡ 3 mod 4): all==1 = {h1_ok}",
          flush=True)
    print(f"     depth distribution: {dict(h1_vals)}", flush=True)
    print(f"\n(H2/H3) PACKED positive-min-psi configs: {packed_pos}", flush=True)
    print(f"     augmenting with deeper same-class reps REDUCES min-psi in: {reduced}",
          flush=True)
    print(f"     reaches min-psi <= 1 after augmentation: {to_le1}", flush=True)
    print(f"     (min-psi before -> after) counts:", flush=True)
    for k in sorted(before_after):
        print(f"       {k[0]} -> {k[1]}: {before_after[k]}", flush=True)
    print("\nREADING (L5): if (H1) holds and augmentation drives min-psi toward <=1,", flush=True)
    print("the packed-regime min-psi<=3 is a FINITE-K edge effect: with enough same-", flush=True)
    print("class representatives (large observation families) min-psi<=1 => lag<=1.", flush=True)
    print("EVIDENCE on the bound's source, not a proof.  RH stays [OUT].", flush=True)
