#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE p=2 FLOOR IDENTITY and its reduction to a single leave-one-out bilinear bound (§6bf).

At p=2 the clean §6ao identity (v(q_min)=max_j(N_j-C_j)) does NOT transfer verbatim, because there
v(x-1)=0 and v(det B)=0 were used, both FALSE at p=2 (v_2(x-1)=1, v_2(det B)=m(m+3)/2).  But the SAME
linear-algebra factorization A = B · V · diag(x_k - 1) and d = B·w (w = B^{-1}d) gives an EXACT p=2 identity
with two corrections:

    v_2(q_min) = max_j ( 1 + N_j^(2) - C_j^(2) ),
        N_j^(2) = sum_{k != j} v_2(x_j - x_k)  >= 3(m-1)   [UNCONDITIONAL: v_2(x_j-x_k) = 3 + v_2(t_j^2-t_k^2) >= 3],
        C_j^(2) = v_2( <w, eps(X'_j)> ),   eps(X'_j)_i = (-1)^{m-1-i} e_{m-1-i}(other x-values),  w = B^{-1} d.

The "+1" is v_2(x_j - 1) (=1 for every node); the base 3(m-1) of N_j is UNIFORM across ALL columns j (unlike
p=3, where N_j was large only on clustered columns via pigeonhole).  CONSEQUENCE: since N_j >= 3(m-1) for EVERY
j, taking the column j0 that minimizes C_j gives

    v_2(q_min) >= 1 + 3(m-1) - min_j C_j^(2).

So the ENTIRE p=2 open core reduces to a SINGLE clean statement about the off-line pairing:
    (CORE-2)  min_j C_j^(2) <= (3 - c) m + O(1)   for some absolute c > 0   [enough: min_j C_j = O(1)].
i.e. among the m leave-one-out bilinear valuations, at least one is not too 2-adically deep.

This probe: (1) VERIFIES the identity across several orbits (structural, should be orbit-free); (2) MEASURES
min_j C_j^(2) under an adversary that MAXIMIZES it (= minimizes the floor) -- is min_j C_j^(2) bounded/O(1),
or can it be driven ~ 3m (which would kill the reduction)?  Exact (L9).  Adversary one-sided (L5).  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows
from discovery.probe_qmin_Cj_bilinear import x_of, vp_int, vp_frac, Bmatrix, solve_lower, elem_sym
import discovery.probe_overdetermined_collision as PO
from math import gcd

P2 = 2


def qmin_exact_orbit(ts, m, sig, tau):
    if any(t == 0 for t in ts) or len(set(ts)) != m:
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], sig, tau, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    detA = int_det(cols_to_rows(oc, m))
    if detA == 0:
        return None
    g = abs(detA)
    for j in range(m):
        cols = [list(oc[k]) for k in range(m)]
        cols[j] = list(vo)
        g = gcd(g, int_det(cols_to_rows(cols, m)))
    if g == 0:
        return None
    return abs(detA) // g


def Cj2(xs, w, j, m):
    Xp = [xs[k] for k in range(m) if k != j]
    e = elem_sym(Xp)                                  # e[0..m-1]
    S = sum((-1) ** (m - 1 - i) * e[m - 1 - i] * w[i] for i in range(m))
    return None if S == 0 else vp_frac(S, P2)


def per_column(ts, m, w):
    """Return (Nlist, Clist) or None."""
    xs = [x_of(t) for t in ts]
    Ns, Cs = [], []
    for j in range(m):
        Ns.append(sum(vp_frac(xs[j] - xs[k], P2) for k in range(m) if k != j))
        c = Cj2(xs, w, j, m)
        if c is None:
            return None
        Cs.append(c)
    return Ns, Cs


def d_vec_sig(sig, T, m):
    """General-orbit target d for orbit {sig +- iT, 1-sig +- iT}, reusing the orbit-agnostic phi.
    (PO.d_vec hardcodes sig=3/4; this parameterizes sig for the cross-orbit identity check.)"""
    T = Fr(T)
    atoms = [(sig, T), (sig, -T), (1 - sig, T), (1 - sig, -T)]
    out = []
    for j in range(1, m + 1):
        s = Fr(0)
        for (re, im) in atoms:
            for (r2, i2) in ((re, im), (1 - re, im)):
                s += PO._phi_re(j, r2, i2)
        out.append(s)
    return out


def wvec(m, sig, tau):
    return solve_lower(Bmatrix(m), d_vec_sig(sig, tau, m), m)


def adversary_maximize_minC(m, sig, tau, w, rng, restarts=20, rounds=6):
    """Maximize min_j C_j^(2) (= minimize the floor). Return best (largest) min_j C_j seen."""
    best = -1
    for _ in range(restarts):
        ts = rng.sample(range(1, 300), m)
        pc = per_column(ts, m, w)
        if pc is None:
            continue
        cur = min(pc[1])
        for _rnd in range(rounds):
            improved = False
            for i in range(m):
                for _ in range(8):
                    cand = ts[:]
                    cand[i] = rng.choice([rng.randrange(1, 300), rng.randrange(1, 40),
                                          (ts[(i + 1) % m] + rng.choice([-2, 2, 4, -4, 6, -6]))
                                          if ts[(i + 1) % m] > 6 else rng.randrange(1, 300)])
                    if len(set(cand)) != m:
                        continue
                    pc2 = per_column(cand, m, w)
                    if pc2 is None:
                        continue
                    v = min(pc2[1])
                    if v > cur:
                        ts, cur, improved = cand, v, True
            if not improved:
                break
        best = max(best, cur)
    return best


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6bf: EXACT p=2 floor identity  v_2(q_min) = max_j(1 + N_j - C_j),  N_j >= 3(m-1) unconditional.", flush=True)
    print("Reduction:  v_2(q_min) >= 1 + 3(m-1) - min_j C_j^(2).  Core-2: is min_j C_j^(2) = O(1) (or <= (3-c)m)?", flush=True)
    print("=" * 100, flush=True)

    orbits = [("3/4 (D=425)", Fr(3, 4), Fr(1)),
              ("7/8 (p3 dies)", Fr(7, 8), Fr(1)),
              ("4/5 (p3 dies)", Fr(4, 5), Fr(1))]

    print("\n(1) IDENTITY CHECK across orbits (should hold structurally, orbit-free):", flush=True)
    print(f"{'orbit':>16} | {'m':>3} | {'#cfg':>5} | {'identity matches':>16}", flush=True)
    print("-" * 52, flush=True)
    rng = random.Random(2026)
    for name, sig, tau in orbits:
        for m in (4, 6):
            w = wvec(m, sig, tau)
            cnt = match = tries = 0
            while cnt < 40 and tries < 3000:
                tries += 1
                ts = rng.sample(range(1, 150), m)
                q = qmin_exact_orbit(ts, m, sig, tau)
                if q is None:
                    continue
                pc = per_column(ts, m, w)
                if pc is None:
                    continue
                cnt += 1
                pred = max(1 + pc[0][j] - pc[1][j] for j in range(m))
                if vp_int(q, P2) == pred:
                    match += 1
            print(f"{name:>16} | {m:>3} | {cnt:>5} | {f'{match}/{cnt}':>16}", flush=True)

    print("\n(2) ADVERSARY maximizing min_j C_j^(2) (= minimizing floor). Is min_j C_j bounded / << 3m?", flush=True)
    print(f"{'orbit':>16} | {'m=4':>4} {'m=5':>4} {'m=6':>4} {'m=7':>4} | {'3(m-1)@m=7':>10} | {'bounded?':>8}", flush=True)
    print("-" * 62, flush=True)
    for name, sig, tau in orbits:
        row = []
        for m in (4, 5, 6, 7):
            w = wvec(m, sig, tau)
            row.append(adversary_maximize_minC(m, sig, tau, w, rng))
        bounded = max(row) <= 8            # heuristic: stays small, not growing ~3m
        print(f"{name:>16} | {row[0]:>4} {row[1]:>4} {row[2]:>4} {row[3]:>4} | {3*6:>10} | {str(bounded):>8}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if the identity matches everywhere AND the adversary cannot push min_j C_j^(2) beyond", flush=True)
    print("O(1) (<< 3m), then v_2(q_min) >= 3m - O(1) reduces to CORE-2 (min_j C_j = O(1)) -- a single clean", flush=True)
    print("leave-one-out bilinear statement, orbit-free. If min_j C_j grows ~ 3m, the reduction fails and the", flush=True)
    print("floor needs the full joint bound. Adversary = one-sided upper bound on the true max. RH stays [OUT].", flush=True)
