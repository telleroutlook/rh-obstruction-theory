#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE p=3 SINGLE-PRIME FLOOR (§6al) — is OP1 reducible to one prime?

§6ak found prime 3 (smallest x-image, N(3)=2 classes) resists drainage: min v_3(q_min)=2,4,5 at m=4,6,7,
GROWING while the drainable primes 5,7,17 hit 0.  If v_3(q_min) has a UNIFORM linear floor c*m that the
adversary can NEVER zero, then log q_min >= v_3*log3 >= c*m*log3 by ITSELF -- OP1 reduces to a classical
single-prime pigeonhole+confluence statement mod 3, self-contained and provable.

This probe stress-tests that: for each m it runs MANY (NREST) coordinate descents that AGGRESSIVELY
MINIMIZE v_3(q_min) from random starts, plus structured starts (nodes packed into / spread across the two
x-classes mod 3), and reports the SMALLEST v_3 found (an UPPER bound on the adversary's achievable min),
whether ANY config reached v_3=0, and the total log2 q_min there.  Reasoning (L5): descent is *trying* to
make v_3 small; if its BEST effort still cannot reach 0 and tracks a linear trend, that is evidence (not
proof) of a positive floor -- more restarts only strengthen it.  Compared against the pigeonhole prediction
PH3 = ceil(2m/(p+3))-1 = ceil(m/3)-1 and a confluence guess.  Exact (L9). One orbit (D=425). RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17
P = 3


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def vp_int(n, p):
    v = 0
    while n and n % p == 0:
        n //= p; v += 1
    return v


def v3_of(ts, m):
    b = build(ts, m)
    if not b:
        return None, None
    q = qmin_fast(*b)
    if not q or q < 2:
        return None, None
    return vp_int(q, P), q


def descent_v3(ts, m, rng, rounds=25):
    best_ts = ts[:]
    v, _ = v3_of(best_ts, m)
    best = v if v is not None else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(10):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 400)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                v, _ = v3_of(cand, m)
                if v is None:
                    continue
                if v < best:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best_ts


def xclass_mod3(t):
    """x = (4t^2-1)/(4t^2+1) mod 3, as the residue of numerator*inverse(den) when den invertible mod 3."""
    num = (4 * t * t - 1) % 3
    den = (4 * t * t + 1) % 3
    if den == 0:
        return None
    return (num * pow(den, -1, 3)) % 3


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("p=3 SINGLE-PRIME FLOOR (§6al): aggressively MINIMIZE v_3(q_min); does it ever reach 0, or grow", flush=True)
    print("~linearly? A uniform v_3 >= c*m would reduce OP1 to a classical mod-3 pigeonhole+confluence bound.", flush=True)
    print("=" * 96, flush=True)
    # show the two x-classes mod 3
    seen = {}
    for t in range(1, 60):
        c = xclass_mod3(t)
        seen.setdefault(c, []).append(t)
    print("x-classes mod 3 (t -> x mod3):", {k: v[:6] for k, v in seen.items()}, flush=True)
    print(f"\n{'m':>3} | {'min v_3 found':>13} | {'reached 0?':>10} | {'PH3=ceil(m/3)-1':>15} | "
          f"{'log2 q there':>12} | {'restarts':>8}", flush=True)
    print("-" * 84, flush=True)
    rng = random.Random(20260816)
    for m in range(3, 10):
        NREST = 40 if m <= 7 else 24
        best_v3, best_q, hit0 = None, None, False
        for r in range(NREST):
            # mix random and structured starts
            if r % 3 == 0:
                # spread across both x-classes mod 3 as evenly as possible
                pool = [t for t in range(1, 400) if xclass_mod3(t) is not None]
                s0 = rng.sample(pool, m)
            else:
                s0 = rng.sample(range(1, 400), m)
            ts = descent_v3(s0, m, rng)
            v, q = v3_of(ts, m)
            if v is None:
                continue
            if v == 0:
                hit0 = True
            if best_v3 is None or v < best_v3:
                best_v3, best_q = v, q
        ph3 = -(-m // 3) - 1
        lq = log2(best_q) if best_q else 0.0
        print(f"{m:>3} | {str(best_v3):>13} | {str(hit0):>10} | {ph3:>15} | {lq:12.2f} | {NREST:>8}",
              flush=True)
    print("\n" + "=" * 96, flush=True)
    print("READING (L5): if 'reached 0?' is False for all m and 'min v_3 found' grows ~linearly (and >= PH3),", flush=True)
    print("prime 3 carries a per-prime floor the adversary cannot drain => candidate SINGLE-PRIME reduction", flush=True)
    print("of OP1 (log q_min >= v_3 log3 >= c*m). If v_3 reaches 0 at some m, prime 3 is drainable after all", flush=True)
    print("and the floor is irreducibly aggregate (back to §6ak). Descent gives an UPPER bound on the", flush=True)
    print("achievable min v_3; failing to reach 0 despite many restarts is EVIDENCE, not proof. RH [OUT].", flush=True)
