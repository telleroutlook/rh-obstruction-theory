#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3: can DEEP p-adic tuning of the tightest packing push psi past a constant?

Group recast (§6p continuation).  Psi = Tr(w), w = (u-1) prod_k (u - x_k) a p-UNIT
(Norm a p-unit, §6k).  psi = v_p(2 Re w) = the p-adic depth to which w/wbar = -1, where
w/wbar = eta(1) * prod_k eta(x_k), eta(x) = (u - x)/(ubar - x) in the norm-1 subgroup.
The node-set adversary tunes each on-line node t_k within its residue class (t_k =
base_k + p*s_k) to ALIGN w/wbar to -1 to high depth.  With the TIGHTEST packing
K = m-1 (one rep per class => a single Phi-minimizer = the whole set), min-psi = psi of
that set, and the adversary has r = m-1 independent tuning knobs s_k.

QUESTION: does deeper tuning (larger s-range S) let the adversary grow psi?  If max psi
PLATEAUS as S grows, the alignment has a p-adic CEILING => psi (=lag) is bounded even
under deep adversarial tuning.  If it grows with S, LEG3 is threatened (report L5).

METHOD: coordinate-ascent maximisation of psi over s_k in [0,S) with several random
restarts (exact rational arithmetic).  Report max psi found per (p,m,S).

HONESTY (L5): a LOCAL-search maximiser (coordinate ascent + restarts), not a global
proof of the ceiling; a flat max across growing S SUPPORTS a bounded lag.  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

import discovery.probe_leg3_affine as A   # x_of, off_atoms_u, Psi_val, vpf


def psi_of(u, ts, p):
    v = A.vpf(A.Psi_val(u, [A.x_of(t) for t in ts]), p)
    return v if v is not None else 10**9


def coord_ascent(u, bases, p, S, rng, restarts):
    """Maximise psi over t_k = base_k + p*s_k, s_k in [0,S), by coordinate ascent."""
    r = len(bases)
    best_overall = -1
    for _ in range(restarts):
        s = [rng.randrange(S) for _ in range(r)]
        ts = [Fr(bases[k] + p * s[k]) for k in range(r)]
        cur = psi_of(u, ts, p)
        improved = True
        while improved:
            improved = False
            for k in range(r):
                bk, bs = cur, s[k]
                for sk in range(S):
                    tk = bases[k] + p * sk
                    if tk == 0:
                        continue
                    ts[k] = Fr(tk)
                    v = psi_of(u, ts, p)
                    if v > bk:
                        bk, bs = v, sk
                s[k] = bs
                ts[k] = Fr(bases[k] + p * bs)
                if bk > cur:
                    cur, improved = bk, True
        best_overall = max(best_overall, cur)
    return best_overall


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3: max psi under DEEP p-adic tuning of tightest packing (K=m-1)",
          flush=True)
    print("Orbit D=425 (split-only).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    sig, tau = Fr(3, 4), Fr(1)
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260815)

    print(f"{'p':>3} {'m':>3} {'r=m-1':>6}  " +
          "  ".join(f"S={S}" for S in (3, 9, 27, 81)), flush=True)
    for p in (7, 11):
        for m in range(3, 7):
            r = m - 1
            if r >= p:
                continue
            bases = list(range(1, r + 1))          # r distinct classes 1..r
            row = []
            for S in (3, 9, 27, 81):
                mx = coord_ascent(u, bases, p, S, rng, restarts=6)
                row.append(mx)
            print(f"{p:>3} {m:>3} {r:>6}  " + "   ".join(f"{v:>3}" for v in row),
                  flush=True)

    print("\n" + "=" * 96, flush=True)
    print("READING (L5): each row shows max psi as the adversary tunes nodes deeper", flush=True)
    print("(S = p-adic search range).  A FLAT row => deep tuning does NOT grow psi =>", flush=True)
    print("a p-adic alignment CEILING => lag bounded even under deep adversarial tuning.", flush=True)
    print("A rising row would threaten LEG3.  Local search, EVIDENCE not proof.  RH [OUT].",
          flush=True)
