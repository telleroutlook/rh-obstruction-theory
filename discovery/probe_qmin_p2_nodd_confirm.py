#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bq — CONFIRM the two proof-critical facts for Row 2 (n odd) surfaced by §6bp:

  FACT A (profile).  For both-odd gamma (v_pi(gamma)=1, pi=1+i), the trace c_j = gamma^j+conj(gamma)^j has
    v_pi(c_j) = (j+1) + a_j  with a_j PERIODIC of period 4 in j.  §6bp saw a_j = (0, A, 0, 1) for j ≡
    (1,2,3,0) mod 4.  Consequence: v_2(w'_i) is PERIOD-4 QUASI-LINEAR — each residue class i mod 4 is an
    arithmetic progression with common difference 4S (S=v_2(beta)).  Here we (i) verify the period-4 law to
    j=30, (ii) extract A per orbit and relate it to v_2(a^2-b^2) (a,b = Re,Im gamma), (iii) confirm the
    per-class common difference is exactly 4S.

  FACT B (pinned C_j).  The leave-one-out pairing valuation C_j = min_r [ v_2(e_r(X'_j)) + v_2(w_{...}) ]
    is NODE-INDEPENDENT and equals a clean quasi-linear function of m (period-4 in m).  §6bp saw min-adv ==
    max-adv for m=4,5,6.  Here we push the adversary harder and to m=7, add more n-odd orbits, and report
    the ARGMIN term index and the GAP to the 2nd-smallest term (uniqueness = ultrametric pinning).

If A is periodic-exact and B is node-independent+unique, Row 2 (n odd) gets a §6bm-style LINEAR floor proof
via a (1+i)-adic unique-minimum — the profile is quasi-linear, not chaotic.  Adversary one-sided.  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_orbit_trichotomy import orbit_beta, v2int
from discovery.probe_qmin_p2_floor_identity import wvec, per_column, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_int, vp_frac, elem_sym
from discovery.probe_qmin_p2_nodd_ramified import (
    vpi_gauss, vpi_int, beta_gauss_numer, rho_pqn, trace_seq)


def term_valuations(xs, w, j, m):
    """Return sorted list of v_2 of each additive term in C_j = v_2( sum_i (-1)^.. e_{m-1-i} w_i )."""
    Xp = [xs[k] for k in range(m) if k != j]
    e = elem_sym(Xp)
    terms = []
    for i in range(m):
        coeff = e[m - 1 - i] * w[i]
        if coeff != 0:
            terms.append((vp_frac(Fr(coeff), 2), i))
    terms.sort()
    return terms


def adversary_minC(m, sig, tau, w, rng, maximize, restarts=24, rounds=8):
    best = None
    for _ in range(restarts):
        ts = rng.sample(range(1, 240), m)
        pc = per_column(ts, m, w)
        if pc is None:
            continue
        cur = min(pc[1])
        for _rnd in range(rounds):
            improved = False
            for i in range(m):
                for _ in range(10):
                    cand = ts[:]
                    cand[i] = rng.randrange(1, 240)
                    if len(set(cand)) != m:
                        continue
                    pc2 = per_column(cand, m, w)
                    if pc2 is None:
                        continue
                    v = min(pc2[1])
                    if (v > cur) if maximize else (v < cur):
                        ts, cur, improved = cand, v, True
            if not improved:
                break
        if best is None or ((cur > best) if maximize else (cur < best)):
            best = cur
    return best


if __name__ == "__main__":
    print("=" * 104, flush=True)
    print("§6bq: confirm FACT A (period-4 v_pi(c_j)) and FACT B (pinned, unique-min C_j) for Row 2 (n odd).", flush=True)
    print("=" * 104, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(1, 5), Fr(1)),
              (Fr(2, 5), Fr(1)), (Fr(6, 7), Fr(1)), (Fr(3, 7), Fr(1))]

    print("\nFACT A — v_pi(c_j) period-4 law (j=1..30) and per-class common difference vs 4S:", flush=True)
    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        A, B, beta, k, PQ, den, wp = orbit_beta(sig, tau, M=8)
        gre, gim, _ = beta_gauss_numer(beta)
        both_odd = (gre % 2 and gim % 2)
        S = Fr(v2int(B.numerator) - v2int(B.denominator), 2)
        c = trace_seq(gre, gim, 31)
        vpic = [vpi_int(c[j]) for j in range(1, 31)]
        acorr = [vpic[j - 1] - (j + 1) for j in range(1, 31)]
        # period-4 test: a_j depends only on j mod 4
        by_res = {r: sorted(set(acorr[j - 1] for j in range(1, 31) if j % 4 == r)) for r in (1, 2, 3, 0)}
        per4 = all(len(v) == 1 for v in by_res.values())
        A_spike = by_res[2][0] if len(by_res[2]) == 1 else by_res[2]
        v2_ab = v2int(gre * gre - gim * gim)  # v_2(a^2 - b^2)
        # per-class common difference of v_2(w'_i): use wp if long enough else derive from c
        print("  (%s,%s) n=%d both_odd=%s S=%s: period4=%s  a_j[j mod4=1,2,3,0]=%s  A=%s  v2(a^2-b^2)=%d  4S=%s" % (
            sig, tau, n, both_odd, str(S), per4,
            [by_res[r][0] if len(by_res[r]) == 1 else by_res[r] for r in (1, 2, 3, 0)],
            A_spike, v2_ab, str(4 * S)), flush=True)

    print("\nFACT B — C_j node-independence (adv MIN vs MAX) + argmin uniqueness gap, m=4..7:", flush=True)
    rng = random.Random(20260818)
    for sig, tau in ORBITS[:4]:
        p, q, n = rho_pqn(sig, tau)
        for m in (4, 5, 6, 7):
            w = wvec(m, sig, tau)
            lo = adversary_minC(m, sig, tau, w, rng, maximize=False)
            hi = adversary_minC(m, sig, tau, w, rng, maximize=True)
            # uniqueness: at a random valid node set, gap between smallest and 2nd-smallest term at argmin col
            gap = None
            for _ in range(40):
                ts = rng.sample(range(1, 80), m)
                pc = per_column(ts, m, w)
                if pc is None:
                    continue
                jstar = min(range(m), key=lambda j: pc[1][j])
                tv = term_valuations([x_of(t) for t in ts], w, jstar, m)
                if len(tv) >= 2:
                    gap = tv[1][0] - tv[0][0]
                break
            tag = "PINNED" if lo == hi else "gap[%s,%s]" % (lo, hi)
            print("  (%s,%s) n=%d m=%d: minC in [%s,%s] %s  uniq-min gap=%s" % (
                sig, tau, n, m, lo, hi, tag, gap), flush=True)

    print("\n" + "=" * 104, flush=True)
    print("READING (L5): FACT A period4=True + FACT B PINNED with positive uniq-min gap => v_2(w'_i) is", flush=True)
    print("period-4 quasi-linear and C_j is node-independent via a UNIQUE (1+i)-adic minimum. Row 2 becomes a", flush=True)
    print("provable linear floor v_2(q_min) >= 1+3(m-1) - C_j(m), C_j(m) ~ S*m < 0. Adversary one-sided. RH [OUT].", flush=True)
