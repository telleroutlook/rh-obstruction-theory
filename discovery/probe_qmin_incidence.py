#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 §6d FOLLOW-UP: attack the ONE surviving gap (§6c step iii) -- does the FIXED
off-line vector d attain near-top order in Z^m/L, UNIFORMLY over adversarial
on-line node choices?  Equivalently: is the incidence lag

        lag(A) := e_max(A) - v_p(q_min)  =  v_p(s_m(A)) - v_p(ord d-bar)

bounded by a SMALL CONSTANT over all node families and all split-only off-line
orbits?  If yes, then §6d's linear floor e_max >= ceil(2m/(p+1))-1 transfers to
        v_p(q_min) >= e_max - lag >= ceil(2m/(p+1)) - O(1)   (LINEAR),
closing the determinantal side of OP1 for split-only orbits (modulo the two
classical facts flagged in §6d).  If some adversary drives lag ~ e_max (d-bar rotated
into the LOW part of Z^m/L), the determinantal floor does NOT transfer and the gap is
real.

ADVERSARY MODEL.  The adversary controls the on-line node set (hence A and its Smith
decomposition); d is FIXED by the off-line orbit.  We give the adversary a rich pool
INCLUDING the families most likely to decouple d from the top factor:
  * single-class {t0 + p*i}: ONE confluent class => e_max ~ m-1 is huge; if d-bar
    misses that factor, lag would blow up -- the sharpest incidence stress test;
  * spread-p: even fill of all (p+1)/2 classes (the e_max-minimizer of §6d);
  * standard rational families of varied denominators.
Reported per (orbit, p, m): min v_p(q_min), the e_max on that same minimizing A, and
the MAX lag over ALL families (the adversary's best decoupling attempt).
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil

from discovery.probe_qmin_snf import (cleared_columns, qmin_index, det_divisor_r)


def vp(n, p):
    n = abs(int(n))
    if n == 0:
        return None
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def emax_of(on_cols, m, p):
    vDm = vp(det_divisor_r(on_cols, m, m), p) or 0
    vDm1 = vp(det_divisor_r(on_cols, m, m - 1), p) or 0
    return vDm - vDm1


def inert_primes_of_qmin(sigma, tau, m, p_list):
    pass  # (not needed; we track a fixed p_list)


def families(m, p):
    K = m + 3
    fams = {
        "half-int": [Fr(1, 2) + i for i in range(K)],
        "integer": [Fr(i) for i in range(1, K + 1)],
        "thirds": [Fr(a, 3) for a in range(1, K + 1)],
        "fifths": [Fr(a, 5) for a in range(1, K + 1)],
        "mixed": [Fr(1, 2), Fr(2), Fr(1, 3), Fr(3), Fr(2, 5), Fr(4),
                  Fr(1, 7), Fr(5), Fr(3, 4), Fr(6)][:K],
        "spread-p": _spread(p, m)[:K],
    }
    # single-class adversary (sharpest incidence stress test)
    for t0 in (1, 2):
        fams[f"single-cls@{t0}"] = [Fr(t0 + p * i) for i in range(K)]
    # cap every family at K nodes to bound minor count C(K, m-1)
    return {k: [t for t in v if t != 0][:K] for k, v in fams.items()}


def _spread(p, m):
    reps = list(range((p - 1) // 2 + 1))
    depth = ceil(2 * (m + 3) / (p + 1)) + 1
    return [Fr(c + p * i) for c in reps for i in range(depth) if (c + p * i) != 0]


ORBITS = [
    ("3/4+i   D=425", Fr(3, 4), Fr(1)),
    ("2/5+4/5 D=4",   Fr(2, 5), Fr(4, 5)),
    ("1+i/5   D=26",  Fr(1), Fr(1, 5)),
]

if __name__ == "__main__":
    print("=" * 90, flush=True)
    print("OP1 §6d gap (iii): is the incidence lag e_max - v_p(q_min) uniformly bounded?", flush=True)
    print("Strong adversary (incl. single-class & spread).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 90, flush=True)

    global_max_lag = 0
    for label, sigma, tau in ORBITS:
        print(f"\n{'='*90}\noff-line rho = {label}", flush=True)
        for p in (3, 7, 11):
            print(f"  p={p:>2} (inert): PH=ceil(2m/(p+1))-1", flush=True)
            print(f"    {'m':>3} | {'min vq (adv)':>12} {'e_max@that A':>12} "
                  f"| {'PH':>3} {'minvq>=PH?':>10} | {'MAX lag(all fam)':>16} "
                  f"{'worst fam':>14}", flush=True)
            print("    " + "-" * 84, flush=True)
            for m in range(2, 7):
                PH = ceil(2 * m / (p + 1)) - 1
                best_vq, best_em = None, None
                max_lag, worst = 0, ""
                for name, ts in families(m, p).items():
                    if len(ts) < m:
                        continue
                    try:
                        oc, vo = cleared_columns(ts, sigma, tau, m)
                        q = qmin_index(oc, vo, m)
                        if not q:
                            continue
                        vq = vp(q, p) or 0
                        em = emax_of(oc, m, p)
                    except Exception:
                        continue
                    lag = em - vq
                    if lag > max_lag:
                        max_lag, worst = lag, name
                    if best_vq is None or vq < best_vq:
                        best_vq, best_em = vq, em
                global_max_lag = max(global_max_lag, max_lag)
                ok = (best_vq is not None and best_vq >= PH)
                print(f"    {m:>3} | {str(best_vq):>12} {str(best_em):>12} "
                      f"| {PH:>3} {str(ok):>10} | {max_lag:>16} {worst:>14}",
                      flush=True)

    print("\n" + "=" * 90)
    print(f"GLOBAL MAX incidence lag e_max - v_p(q_min) over ALL orbits/families/m/p:"
          f"  {global_max_lag}")
    print("READING: if global max lag is a SMALL CONSTANT (and min vq >= PH holds),")
    print("then v_p(q_min) >= e_max - lag >= ceil(2m/(p+1)) - O(1) is LINEAR uniformly")
    print("=> §6d floor transfers to q_min => determinantal side of split-only OP1")
    print("closed (modulo the classical confluent-Vandermonde + off-by-one lemmas).")
    print("If lag ~ e_max for single-class, the fixed-vector incidence gap is REAL.")
