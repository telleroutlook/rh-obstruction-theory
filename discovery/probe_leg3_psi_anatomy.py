#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 anatomy: DECOMPOSE the incidence lag into its two arithmetic sources,
to see WHICH one produces the observed lag<=3 plateau (§6h) and whether either is
provably bounded.

Exact lag identity (from q_min = D_m(A)/D_m([A|d]) and D_{m-1}(A) | D_m([A|d]) |
D_m(A), all rigorous):
    lag = v_p(D_m([A|d])) - v_p(D_{m-1}(A)).
Since v_p(D_m(A)) is large, v_p(D_m([A|d])) = min over (m-1)-subsets S' of on-line
nodes of  V(S') := v_p(det[A_{S'} | d])  (the d-augmented m-minors), when that min
is < v_p(D_m(A)).  §6g's factorization C_j=(x-1)g_j gives, for the PURE on-line
(m-1)-minor with top rows,
    Phi(S') := sum_{k in S'} v_p(x_k - 1) + sum_{k<l in S'} v_p(x_l - x_k)
             = v_p(det of top-(m-1)-rows minor on S').
Define the d-RESIDUAL  psi(S') := V(S') - Phi(S').  Then
    lag = min_{S'} [Phi(S') + psi(S')] - v_p(D_{m-1})
        = [Phi(S*) - v_p(D_{m-1})] + psi(S*)   at the V-minimizing S*.

TWO candidate drivers of the lag:
  (I)  Phi-slack   := Phi(S*) - v_p(D_{m-1})   (S* not the D_{m-1}-minimizer);
  (II) d-residual  := psi(S*)                  (fixed off-line d meets the nodes).
This probe reports both, checks the identity lag == lag_via_minors (consistency
vs the trusted SNF lag), and tests the sub-lemma
    v_p(D_{m-1}(A)) == min_{S'} Phi(S')   (is D_{m-1} realized by TOP-row minors?).

HONESTY (L5): EVIDENCE/insight, not proof.  RH stays [OUT].
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


def Phi(S_ts, p):
    """Phi(S') = sum v_p(x_k-1) + sum_{k<l} v_p(x_l-x_k) over on-line nodes S'."""
    xs = [x_of(t) for t in S_ts]
    s = 0
    for x in xs:
        s += (vpf(x - 1, p) or 0)
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
    print("OP1 LEG3 anatomy: lag = (Phi-slack) + (d-residual psi).  Which drives lag<=3?",
          flush=True)
    print("DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    ident_ok = sublemma_ok = True
    max_phislack = max_psi = max_lag = 0
    # aggregate: how often each driver is the nonzero one
    from collections import Counter
    driver = Counter()

    for label, sig, tau in ORBITS:
        print(f"\n{'='*96}\noff-line rho = {label}", flush=True)
        for p in (3, 7, 11):
            print(f"  p={p:>2}: lag = [Phi(S*)-vD_(m-1)] + psi(S*)   (S* = V-minimizing subset)",
                  flush=True)
            print(f"    {'fam':>10} {'m':>2} | {'lag':>3} {'lagMin':>6} {'vD_m1':>5} "
                  f"{'minPhi':>6} {'subL':>4} | {'Phi(S*)':>7} {'psi(S*)':>7} "
                  f"{'Phi-slk':>7} | driver", flush=True)
            print("    " + "-" * 88, flush=True)
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
                    emax = vDm - vDm1
                    lag = emax - vq
                    # enumerate (m-1)-subsets S' of on-line columns; V(S') and Phi(S')
                    Vmin, minPhi, Sstar = None, None, None
                    for S in combinations(range(len(oc)), m - 1):
                        cols = [oc[k] for k in S] + [vo]
                        M = [[cols[c][r] for c in range(m)] for r in range(m)]
                        dv = bareiss_det(M)
                        if dv == 0:
                            continue
                        V = vp(dv, p) or 0
                        ph = Phi([ts[k] for k in S], p)
                        if minPhi is None or ph < minPhi:
                            minPhi = ph
                        if Vmin is None or V < Vmin:
                            Vmin, Sstar = V, (S, ph)
                    if Vmin is None:
                        continue
                    lag_min = Vmin - vDm1
                    phi_star = Sstar[1]
                    psi_star = Vmin - phi_star
                    phi_slack = phi_star - vDm1
                    # checks
                    if lag_min != lag:
                        ident_ok = False
                    if minPhi != vDm1:
                        sublemma_ok = False
                    max_lag = max(max_lag, lag)
                    max_phislack = max(max_phislack, phi_slack)
                    max_psi = max(max_psi, psi_star)
                    if lag > 0:
                        if phi_slack > 0 and psi_star > 0:
                            driver["both"] += 1
                        elif phi_slack > 0:
                            driver["Phi-slack"] += 1
                        elif psi_star > 0:
                            driver["psi"] += 1
                        else:
                            driver["neither?!"] += 1
                    if lag > 0:   # only print the informative (nonzero-lag) rows
                        drv = ("both" if phi_slack > 0 and psi_star > 0 else
                               "Phi-slk" if phi_slack > 0 else
                               "psi" if psi_star > 0 else "??")
                        idflag = "" if (lag_min == lag and minPhi == vDm1) else " <<<"
                        print(f"    {fname:>10} {m:>2} | {lag:>3} {lag_min:>6} {vDm1:>5} "
                              f"{minPhi:>6} {str(minPhi==vDm1):>4} | {phi_star:>7} "
                              f"{psi_star:>7} {phi_slack:>7} | {drv}{idflag}", flush=True)

    print("\n" + "=" * 96, flush=True)
    print(f"identity  lag == min_S' V(S') - v_p(D_(m-1))            : {ident_ok}", flush=True)
    print(f"sub-lemma v_p(D_(m-1)) == min_S' Phi(S') (top-row real.): {sublemma_ok}", flush=True)
    print(f"max lag = {max_lag}   max Phi-slack = {max_phislack}   max psi(S*) = {max_psi}",
          flush=True)
    print(f"lag>0 driver counts: {dict(driver)}", flush=True)
    print("READING: if the lag is driven ENTIRELY by a bounded psi (d-residual) with", flush=True)
    print("Phi-slack==0, the proof reduces to bounding psi(S*)=v_p of a divided", flush=True)
    print("difference of the fixed d over the nodes.  EVIDENCE ONLY (L5).  RH [OUT].", flush=True)
