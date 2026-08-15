#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 sharpened reduction: CLEAN bound  lag <= psi(S0)  for ANY Phi-minimizing
subset S0.

Derivation (exact, from §6i):
    lag = min_{S'} [Phi(S') + psi(S')] - min_{S'} Phi(S').
Let S0 in argmin Phi.  Using S0 as a feasible point for the first min:
    lag <= [Phi(S0) + psi(S0)] - min Phi = psi(S0).
So the ENTIRE incidence lag is bounded by psi = v_p(Psi) evaluated at a
Phi-minimizer -- the "Phi-near-optimality" leg of §6i is unnecessary.  LEG3 now
reduces to a SINGLE quantity:  is  min_{S0 in argmin Phi} psi(S0)  bounded by a
small constant, uniformly in m and over adversarial node sets?

Psi(S') = sum_{off-line atoms u_a} (u_a - 1) prod_{k in S'} (u_a - x_k), an
orbit-sum over the FIXED (<=8) off-line atoms of P_{S'}(X)=(X-1)prod(X-x_k).
psi(S') = v_p(Psi(S')) = v_p(det[A_{S'}|d]) - Phi(S')  (computed convention-free).

This probe:
  (A) verifies the clean bound  lag <= min_{S0 in argmin Phi} psi(S0);
  (B) reports min & max psi over Phi-minimizers, and whether psi=0 is attainable;
  (C) computes the number of DISTINCT off-line atom residues mod p (in F_{p^2}),
      the structural reason a short orbit-sum resists high p-valuation.

HONESTY (L5): EVIDENCE + reduction, not a proof.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil
from itertools import combinations

import discovery.probe_overdetermined_collision as P
from discovery.probe_covolume_floor import bareiss_det
from discovery.probe_qmin_snf import cleared_columns, det_divisor_r
from discovery.qmin_snf_fast import qmin_fast


def vp(n, p):
    n = abs(int(n))
    if n == 0:
        return None
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def vpf(fr, p):
    if fr == 0:
        return None
    return (vp(fr.numerator, p) or 0) - (vp(fr.denominator, p) or 0)


def x_of(t):
    t = Fr(t)
    return (4 * t * t - 1) / (4 * t * t + 1)


# ---- Q(i) arithmetic (a + b i, a,b in Q) --------------------------------
def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def cinv(z):
    d = z[0] * z[0] + z[1] * z[1]
    return (z[0] / d, -z[1] / d)


def csub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def off_atoms_u(sigma, tau):
    """Distinct u = (w + 1/w)/2, w = 1 - 1/rho, over the orbit
    {sigma+-i tau, 1-sigma +- i tau}.  Returns list of Q(i) points."""
    rhos = [(sigma, tau), (sigma, -tau), (1 - sigma, tau), (1 - sigma, -tau)]
    us = []
    for rho in rhos:
        w = csub((Fr(1), Fr(0)), cinv(rho))       # 1 - 1/rho
        u = tuple((a + b) / 2 for a, b in zip(w, cinv(w)))   # (w + 1/w)/2
        us.append(u)
    # dedupe exact Q(i)
    uniq = []
    for u in us:
        if all(u != v for v in uniq):
            uniq.append(u)
    return uniq


def vp_qi(z, p):
    """v_p of a Q(i) element for INERT p (unramified): min of component v_p."""
    a = vpf(z[0], p)
    b = vpf(z[1], p)
    if a is None and b is None:
        return None
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def atom_residues_modp(us, p):
    """distinct residues in F_{p^2} = F_p[i] of the (p-integral) atoms."""
    res = set()
    ok = True
    for (a, b) in us:
        if (vpf(a, p) or 0) < 0 or (vpf(b, p) or 0) < 0:
            ok = False
            continue
        ar = (a.numerator % p) * pow(a.denominator % p, p - 2, p) % p
        br = (b.numerator % p) * pow(b.denominator % p, p - 2, p) % p
        res.add((ar, br))
    return len(res), ok


def Phi(S_ts, p):
    xs = [x_of(t) for t in S_ts]
    s = sum((vpf(x - 1, p) or 0) for x in xs)
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            s += (vpf(xs[j] - xs[i], p) or 0)
    return s


def families(m, p):
    K = m + 3
    fams = {
        "half-int": [Fr(1, 2) + i for i in range(K)],
        "integer": [Fr(i) for i in range(1, K + 1)],
        "thirds": [Fr(a, 3) for a in range(1, K + 1)],
        "spread-p": _spread(p, m)[:K],
    }
    for t0 in range(1, (p + 1) // 2 + 1):
        fams[f"single@{t0}"] = [Fr(t0 + p * i) for i in range(K)]
    return {k: [t for t in v if t != 0][:K] for k, v in fams.items()}


def _spread(p, m):
    reps = list(range((p - 1) // 2 + 1))
    depth = ceil(2 * (m + 3) / (p + 1)) + 1
    return [Fr(c + p * i) for c in reps for i in range(depth) if (c + p * i) != 0]


ORBITS = [
    ("3/4+i    D=425", Fr(3, 4), Fr(1)),
    ("2/5+4/5i D=4",   Fr(2, 5), Fr(4, 5)),
    ("1+i/5    D=26",  Fr(1), Fr(1, 5)),
]


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3: clean bound lag <= psi(S0) (S0 = Phi-minimizer).  Bound psi?",
          flush=True)
    print("DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    bound_ok = True
    max_lag = 0
    max_minpsi = 0          # max over configs of min_{Phi-min} psi
    psi0_attained = 0       # configs where some Phi-minimizer has psi<=0
    total_pos = 0

    for label, sig, tau in ORBITS:
        us = off_atoms_u(sig, tau)
        print(f"\n{'='*96}\noff-line rho = {label}   (#distinct atoms u = {len(us)})",
              flush=True)
        for p in (3, 7, 11):
            natom, ok = atom_residues_modp(us, p)
            print(f"  p={p:>2}: #distinct atom residues mod p (in F_p^2) = {natom}"
                  f"{'' if ok else '  (some atom non-p-integral!)'}", flush=True)
            print(f"    {'fam':>10} {'m':>2} | {'lag':>3} | {'minPhi':>6} "
                  f"{'#Phimin':>7} {'min psi0':>8} {'max psi0':>8} | {'lag<=minpsi0':>12}",
                  flush=True)
            print("    " + "-" * 78, flush=True)
            for m in range(2, 8):
                for fname, ts in families(m, p).items():
                    if len(ts) < m:
                        continue
                    oc, vo = cleared_columns(ts, sig, tau, m)
                    q = qmin_fast(oc, vo)
                    if not q:
                        continue
                    vq = vp(q, p) or 0
                    vDm = vp(det_divisor_r(oc, m, m), p) or 0
                    vDm1 = vp(det_divisor_r(oc, m, m - 1), p) or 0
                    lag = (vDm - vDm1) - vq
                    # Phi over all (m-1)-subsets; collect argmin, their psi=V-Phi
                    rows = []
                    for S in combinations(range(len(oc)), m - 1):
                        ph = Phi([ts[k] for k in S], p)
                        rows.append((ph, S))
                    minPhi = min(ph for ph, _ in rows)
                    psis = []
                    for ph, S in rows:
                        if ph != minPhi:
                            continue
                        cols = [oc[k] for k in S] + [vo]
                        M = [[cols[c][r] for c in range(m)] for r in range(m)]
                        dv = bareiss_det(M)
                        if dv == 0:
                            continue
                        psis.append((vp(dv, p) or 0) - ph)
                    if not psis:
                        continue
                    minpsi0, maxpsi0 = min(psis), max(psis)
                    okrow = (lag <= minpsi0)
                    bound_ok = bound_ok and okrow
                    max_lag = max(max_lag, lag)
                    max_minpsi = max(max_minpsi, minpsi0)
                    if lag > 0:
                        total_pos += 1
                        if minpsi0 <= 0:
                            psi0_attained += 1
                    if lag > 0 or not okrow:   # informative rows
                        print(f"    {fname:>10} {m:>2} | {lag:>3} | {minPhi:>6} "
                              f"{len(psis):>7} {minpsi0:>8} {maxpsi0:>8} | "
                              f"{str(okrow):>12}{'' if okrow else '  <<<'}", flush=True)

    print("\n" + "=" * 96, flush=True)
    print(f"clean bound  lag <= min_(Phi-min) psi(S0)  holds everywhere : {bound_ok}",
          flush=True)
    print(f"max lag = {max_lag}   max over configs of min_(Phi-min) psi = {max_minpsi}",
          flush=True)
    print(f"positive-lag configs: {total_pos};  of these, a Phi-minimizer with "
          f"psi<=0 exists in {psi0_attained}", flush=True)
    print("READING: lag <= psi(S0) collapses LEG3 to ONE quantity -- v_p of the fixed", flush=True)
    print("orbit-sum Psi over a Phi-minimizer.  A bounded number of atom residues (few", flush=True)
    print("F_p^2 points) is the structural reason psi resists growth.  EVIDENCE (L5). RH [OUT].",
          flush=True)
