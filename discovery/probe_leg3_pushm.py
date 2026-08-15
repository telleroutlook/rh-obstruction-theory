#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 (the sole remaining gap after §6f/§6g proved the e_max linear floor):
is the fixed-vector incidence lag

        lag(A) := e_max(A) - v_p(q_min)  =  v_p(s_m(A)) - v_p(ord d-bar in Z^m/L)

UNIFORMLY bounded by a SMALL CONSTANT, so that the proved linear floor
e_max >= ceil(2m/(p+3))-1 transfers to v_p(q_min)?  §6e reached lag<=3 but only
for m<=6 (minor-enumeration wall), leaving "lag=O(1) vs slow growth" UNSETTLED.

This probe breaks the m<=6 wall with an SNF/DVR pipeline that is O(m^3), not
O(C(K,m)) minors, and pushes split-only orbits to m~10 against the sharpest
adversaries.

RIGOR of the two quantities (both exact, no floats):
  * v_p(q_min): qmin_fast (SNF; memory-calibrated == trusted minor-gcd qmin_index).
  * e_max     : p-adic Smith exponents via MIN-VALUATION-PIVOT elimination over the
                DVR Z_(p).  Standard fact: over a DVR, choosing a pivot of minimal
                valuation makes it divide every other entry, so field elimination
                reproduces integral Smith form; the sorted pivot valuations are the
                elementary-divisor exponents e_1<=...<=e_r.  e_max = e_r; and
                sum(e_i) = v_p(D_r) is cross-checked against the SNF product.
Both are cross-validated at m<=6 against the TRUSTED det_divisor_r / qmin_index.

HONESTY (L5): this is EVIDENCE, not proof.  A bounded lag out to m~10 strengthens
"lag=O(1)"; any upward creep would expose LEG3 as genuinely open/false.  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil, gcd

import discovery.probe_overdetermined_collision as P
from discovery.probe_covolume_floor import O_orbit_direct
from discovery.probe_qmin_snf import cleared_columns, det_divisor_r, qmin_index
from discovery.qmin_snf_fast import qmin_fast, _snf_invariant_product


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


def padic_smith_exponents(cols, m, p):
    """Sorted p-adic elementary-divisor exponents e_1<=...<=e_r of the m x K
    integer matrix whose columns are `cols`.  Min-valuation-pivot elimination
    over the DVR Z_(p) (exact rationals).  Returns list of ints (length = rank)."""
    K = len(cols)
    A = [[Fr(cols[j][i]) for j in range(K)] for i in range(m)]   # m x K
    exps = []
    t = 0
    while t < min(m, K):
        # pick entry in A[t:, t:] of minimal finite p-valuation
        best = None
        for i in range(t, m):
            for j in range(t, K):
                if A[i][j] != 0:
                    v = vpf(A[i][j], p)
                    if best is None or v < best[0]:
                        best = (v, i, j)
        if best is None:
            break                                   # rest is zero -> done
        bv, bi, bj = best
        A[t], A[bi] = A[bi], A[t]
        for row in A:
            row[t], row[bj] = row[bj], row[t]
        piv = A[t][t]
        for i in range(t + 1, m):
            if A[i][t] != 0:
                f = A[i][t] / piv
                for j in range(t, K):
                    A[i][j] -= f * A[t][j]
        for j in range(t + 1, K):
            if A[t][j] != 0:
                f = A[t][j] / piv
                for i in range(t + 1, m):
                    A[i][j] -= f * A[i][t]
        exps.append(bv)
        t += 1
    return sorted(exps)


def emax_smith(cols, m, p):
    """e_max = top p-adic elementary divisor exponent = v_p(D_r) - v_p(D_{r-1})."""
    e = padic_smith_exponents(cols, m, p)
    return e[-1] if e else 0, e


def families(m, p):
    K = m + 4
    fams = {
        "half-int": [Fr(1, 2) + i for i in range(K)],
        "integer": [Fr(i) for i in range(1, K + 1)],
        "thirds": [Fr(a, 3) for a in range(1, K + 1)],
        "spread-p": _spread(p, m)[:K],
    }
    # single-class adversary at EVERY class base t0 (sharpest decoupling attempt)
    for t0 in range(1, (p + 1) // 2 + 1):
        fams[f"single@{t0}"] = [Fr(t0 + p * i) for i in range(K)]
    # p-adically clustered single class (nodes congruent mod p^2, p^3 -> deep
    # confluence, tries to inflate same-class v_p differences)
    fams["deep-cluster"] = [Fr(1 + p * p * i) for i in range(K)]
    return {k: [t for t in v if t != 0][:K] for k, v in fams.items()}


def _spread(p, m):
    reps = list(range((p - 1) // 2 + 1))
    depth = ceil(2 * (m + 4) / (p + 1)) + 1
    return [Fr(c + p * i) for c in reps for i in range(depth) if (c + p * i) != 0]


ORBITS = [
    ("3/4+i    D=425", Fr(3, 4), Fr(1)),
    ("2/5+4/5i D=4",   Fr(2, 5), Fr(4, 5)),
    ("1+i/5    D=26",  Fr(1), Fr(1, 5)),
]

MMAX = 10


def cross_validate():
    """At m<=6 confirm SNF/DVR pipeline == trusted minor-gcd path."""
    print("CROSS-VALIDATION (SNF/DVR vs trusted det_divisor_r / qmin_index), m<=6:",
          flush=True)
    ok = True
    for label, sig, tau in ORBITS:
        for p in (3, 7, 11):
            for m in range(2, 7):
                for name, ts in families(m, p).items():
                    if len(ts) < m:
                        continue
                    oc, vo = cleared_columns(ts, sig, tau, m)
                    # trusted
                    q_t = qmin_index(oc, vo, m)
                    if q_t is None:
                        continue
                    vDm = vp(det_divisor_r(oc, m, m), p) or 0
                    vDm1 = vp(det_divisor_r(oc, m, m - 1), p) or 0
                    em_t = vDm - vDm1
                    vq_t = vp(q_t, p) or 0
                    # fast
                    q_f = qmin_fast(oc, vo)
                    vq_f = vp(q_f, p) or 0
                    em_f, exps = emax_smith(oc, m, p)
                    # sum of exps == v_p(D_r) (SNF product) sanity
                    dM, _ = _snf_invariant_product(
                        [[oc[k][i] for k in range(len(oc))] for i in range(m)])
                    if (q_f != q_t or vq_f != vq_t or em_f != em_t
                            or sum(exps) != (vp(dM, p) or 0)):
                        ok = False
                        print(f"  MISMATCH {label} p={p} m={m} {name}: "
                              f"q {q_t}/{q_f} em {em_t}/{em_f} vq {vq_t}/{vq_f} "
                              f"sumexp {sum(exps)} vDr {vp(dM, p)}", flush=True)
    print(f"  cross-validation clean: {ok}", flush=True)
    return ok


if __name__ == "__main__":
    print("=" * 94, flush=True)
    print("OP1 LEG3: push m to ~10 on split-only orbits — is the incidence lag O(1)?",
          flush=True)
    print("SNF/DVR pipeline (O(m^3)).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 94, flush=True)

    cv = cross_validate()

    global_max_lag = 0
    lag_at_m = {}
    for label, sig, tau in ORBITS:
        print(f"\n{'='*94}\noff-line rho = {label}", flush=True)
        for p in (3, 7, 11):
            print(f"  p={p:>2} (inert): PH = ceil(2m/(p+3))-1", flush=True)
            print(f"    {'m':>3} | {'min vq (adv)':>12} {'e_max@min':>9} "
                  f"{'MAXlag':>6} {'worst fam':>12} | {'PH':>3} {'vq>=PH':>7}",
                  flush=True)
            print("    " + "-" * 78, flush=True)
            for m in range(2, MMAX + 1):
                PH = ceil(2 * m / (p + 3)) - 1
                best_vq, em_at, max_lag, worst = None, None, 0, ""
                for name, ts in families(m, p).items():
                    if len(ts) < m:
                        continue
                    oc, vo = cleared_columns(ts, sig, tau, m)
                    q = qmin_fast(oc, vo)
                    if not q:
                        continue
                    vq = vp(q, p) or 0
                    em, _ = emax_smith(oc, m, p)
                    lag = em - vq
                    if lag > max_lag:
                        max_lag, worst = lag, name
                    if best_vq is None or vq < best_vq:
                        best_vq, em_at = vq, em
                global_max_lag = max(global_max_lag, max_lag)
                lag_at_m[m] = max(lag_at_m.get(m, 0), max_lag)
                ok = (best_vq is not None and best_vq >= PH)
                print(f"    {m:>3} | {str(best_vq):>12} {str(em_at):>9} "
                      f"{max_lag:>6} {worst:>12} | {PH:>3} {str(ok):>7}", flush=True)

    print("\n" + "=" * 94, flush=True)
    print(f"cross-validation (SNF==trusted) : {cv}", flush=True)
    print(f"GLOBAL MAX incidence lag (all orbits/p/families, m up to {MMAX}): "
          f"{global_max_lag}", flush=True)
    print("  lag vs m (max over everything):", flush=True)
    for m in sorted(lag_at_m):
        print(f"    m={m:>2}: max lag = {lag_at_m[m]}", flush=True)
    print("READING: flat/bounded lag as m grows => strong evidence lag=O(1) and the", flush=True)
    print("proved linear e_max floor transfers to v_p(q_min); upward creep => LEG3", flush=True)
    print("genuinely open. EVIDENCE ONLY (L5). RH stays [OUT].", flush=True)
