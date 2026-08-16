#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — replay of an EXTERNAL referee's REFUTED claim on OB-41.
NOT imported into proofs.  No RH / RH-equivalent input.

The referee asserts a VALID collision (rank A = m, so C1+C2) at slack_x = 1 (the "good"
regime where OB-41 claims lag <= 2) with lag = 6, using the DOCUMENT'S OWN anchor orbit
rho = 3/4 + i (D = 425), by CLUSTERING the on-line nodes into only navail = 2 x-residue
classes mod p.  L9 discipline: verify every load-bearing number by exact arithmetic here.

Checks, all exact (Fraction / Gaussian-rational):
  (a) atom u == 273/425 - (64/425) i                         [reproduce §6]
  (b) x-residues mod p match the referee's stated pattern
  (c) navail (distinct finite x-classes) and slack_x
  (d) rank(A) over Q  (C2)  -- exact Gaussian elimination on the cleared integer columns
  (e) collision validity via qmin_fast (C1 in-span + C2 rank=m)
  (f) Phi-minimizers, psi at each, and lag = min over Phi-minimizers of psi
Reports whether the referee's (lag) reproduces and whether the config is a VALID collision.
RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations

import discovery.probe_leg3_affine as A
from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast


def qrank(cols):
    """Exact rank over Q of a list of integer column vectors (each length m)."""
    if not cols:
        return 0
    m = len(cols[0])
    # build rows = the columns as rational vectors, row-reduce
    M = [[Fr(c[i]) for c in cols] for i in range(m)]  # m x K
    rank = 0
    ncol = len(cols)
    pr = 0
    for c in range(ncol):
        piv = None
        for r in range(pr, m):
            if M[r][c] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[pr], M[piv] = M[piv], M[pr]
        pivval = M[pr][c]
        M[pr] = [v / pivval for v in M[pr]]
        for r in range(m):
            if r != pr and M[r][c] != 0:
                f = M[r][c]
                M[r] = [M[r][k] - f * M[pr][k] for k in range(ncol)]
        pr += 1
        rank += 1
        if pr == m:
            break
    return rank


def run_case(name, sig, tau, p, m, tl):
    print("=" * 96, flush=True)
    print(f"CASE {name}: rho params (sig,tau)=({sig},{tau})  p={p}  m={m}  K={len(tl)}", flush=True)
    u = A.off_atoms_u(sig, tau)[0]
    print(f"  (a) atom u = {u[0]} + ({u[1]}) i", flush=True)

    xs = [A.x_of(t) for t in tl]
    c1res = A.xres(Fr(1), p)
    residues = [A.xres(x, p) for x in xs]
    print(f"  (b) x-residues mod {p} = {residues}", flush=True)
    classes = {}
    for r in residues:
        if r is not None and r != c1res:
            classes[r] = classes.get(r, 0) + 1
    navail = len(classes)
    slack = (p - 1) // 2 - (m - 1)
    print(f"  (c) navail (distinct finite x-classes) = {navail}   "
          f"slack_x = (p-1)/2-(m-1) = {slack}", flush=True)

    # (d) exact rank of cleared columns
    on_cols, voff = cleared_columns(tl, sig, tau, m)
    rk = qrank(on_cols)
    print(f"  (d) rank(A) over Q (exact) = {rk}   (need = m = {m} for C2)", flush=True)

    # (e) collision validity via qmin (C1 in-span + C2)
    q = qmin_fast(on_cols, voff)
    print(f"  (e) qmin_fast = {q}   -> {'VALID collision (C1+C2 hold)' if q else 'INVALID'}", flush=True)

    # (f) Phi-minimizers, psi, lag
    rows = [(A.Phi([xs[k] for k in S], p), S) for S in combinations(range(len(tl)), m - 1)]
    minPhi = min(ph for ph, _ in rows)
    mins = [S for ph, S in rows if ph == minPhi]
    psis = []
    for S in mins:
        v = A.vpf(A.Psi_val(u, [xs[k] for k in S]), p)
        psis.append(v if v is not None else 10**9)
    lag = min(psis)
    print(f"  (f) #Phi-minimizers = {len(mins)} (of {len(rows)} subsets), minPhi = {minPhi}", flush=True)
    print(f"      psi over Phi-minimizers = {psis}", flush=True)
    print(f"      lag = min over Phi-minimizers of psi = {lag}", flush=True)

    verdict_valid = (rk == m and q is not None)
    print(f"  VERDICT: valid_collision={verdict_valid}  lag={lag}  slack_x={slack}  "
          f"(claim: lag<=2 if slack_x>=1)", flush=True)
    if verdict_valid and slack >= 1 and lag > 2:
        print("  >>> REFUTATION CONFIRMED: valid collision, slack_x>=1, lag>2.", flush=True)
    elif verdict_valid and slack == 0 and lag > 3:
        print("  >>> REFUTATION CONFIRMED: valid collision, slack_x=0, lag>3.", flush=True)
    elif not verdict_valid:
        print("  >>> NOT a valid collision -> NOT a refutation of the stated theorem.", flush=True)
    else:
        print("  >>> Within the claimed bound -> NOT a refutation.", flush=True)
    return verdict_valid, lag, slack, navail


def build_clustered(p, m, resA, resB, seedshift=0):
    """Build m nodes clustered into exactly TWO x-residue classes (resA,resB) mod p,
    as DISTINCT rationals (t = base + k*p share x-residue mod p but differ over Q).
    Returns a node list with exact rank(A)=m if one is found by a short deterministic
    sweep, else None.  navail=2, far below m-1 -> the referee's clustering regime."""
    # nodes with t ≡ base (mod p) all have the same x-residue as base; find bases hitting resA/resB
    def bases_for(res):
        out = []
        for t0 in range(1, p):
            if A.xres(A.x_of(Fr(t0)), p) == res:
                out.append(t0)
        return out
    bA, bB = bases_for(resA), bases_for(resB)
    if not bA or not bB:
        return None
    # split m nodes ~half/half; use distinct multiples to keep rationals distinct
    nA = m // 2
    tl = []
    k = seedshift
    while len([x for x in tl]) < nA:
        tl.append(Fr(bA[0] + k * p)); k += 1
    k = seedshift
    while len(tl) < m:
        tl.append(Fr(bB[0] + k * p)); k += 1
    # verify rank; if deficient, spread across more multiples
    on_cols, _ = cleared_columns(tl, Fr(3, 4), Fr(1), m)
    if qrank(on_cols) != m:
        # retry with larger stride
        tl = []
        for i in range(nA):
            tl.append(Fr(bA[0] + (i + 1) * p))
        for i in range(m - nA):
            tl.append(Fr(bB[0] + (i + 1) * p))
        on_cols, _ = cleared_columns(tl, Fr(3, 4), Fr(1), m)
        if qrank(on_cols) != m:
            return None
    return tl


if __name__ == "__main__":
    sig, tau = Fr(3, 4), Fr(1)  # the D=425 anchor orbit
    # 1) Referee's cleanest explicit case -- exact replay:
    t14 = [1823, 2113, 4433, 2838, 6608, 201, 6900, 7886, 5276, 7915, 8037, 1019, 6993, 5949]
    run_case("referee m=14 p=29", sig, tau, 29, 14, [Fr(t) for t in t14])

    # 2) My OWN independently-constructed clustered valid collisions at other (p,m),
    #    slack_x >= 1 throughout, to show the refutation is a GENUS not a fluke.
    print("\n\n########## INDEPENDENT clustered constructions (2 x-classes, slack_x>=1) ##########",
          flush=True)
    for (p, m) in [(17, 8), (23, 10), (23, 12), (31, 14)]:
        slack = (p - 1) // 2 - (m - 1)
        if slack < 1:
            continue
        # pick the two smallest nonzero x-residues present
        seen = []
        for t0 in range(1, p):
            r = A.xres(A.x_of(Fr(t0)), p)
            if r is not None and r != A.xres(Fr(1), p) and r not in seen:
                seen.append(r)
        if len(seen) < 2:
            continue
        tl = build_clustered(p, m, seen[0], seen[1])
        if tl is None:
            print(f"  (p={p},m={m}) could not build rank-m clustered config; skip", flush=True)
            continue
        run_case(f"constructed p={p} m={m} (navail=2)", sig, tau, p, m, tl)
