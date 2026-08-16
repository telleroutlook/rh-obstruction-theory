#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

RESIDUE PRIME CONTENT of the adversarial-minimum q_min (§6aj) — WHICH channel carries the floor?

§6ai localized OP1's floor to a top-heavy residue (q_min ~ order of [d] in the top Smith factor) and
§6ah/§6af reframed it as the un-absorbable LINEAR piece of log|det A|.  §6ae had already shown the
RAMIFIED primes {5,17} are INDIVIDUALLY drainable to v_p=0 by the adversary.  If that is right, then at
the adversarial MINIMUM the surviving q_min must be carried by the OTHER channel -- generic ("geometric")
primes coming from the Vandermonde discriminant G = prod_{k<l}(t_k^2 - t_l^2), NOT by 5 or 17.  This
probe MEASURES that, which decides the proof toolkit for the nucleus:
   * if the min-q residue is SMOOTH / carried by MANY small generic primes  -> a Vandermonde/discriminant
     lower bound (height-of-a-fixed-vector-mod-a-lattice) is the target;
   * if it is dominated by a FEW LARGE primes -> an S-unit / Baker-type statement;
   * if 5 and 17 still dominate DESPITE §6ae -> §6ae's per-prime drain does not survive joint min-q
     (report honestly, L5, would REOPEN the ramified route).

Method (exact, L9): coordinate-descent to min log2 q_min (m=3..7), factor q_min by trial division up to a
bound B, split into (i) ramified part 5^a 17^b, (ii) smooth generic part (primes <= B, excl 5/17),
(iii) large cofactor (> B, i.e. one/few big primes).  Report each part's bit-share, #distinct generic
primes, largest prime, and whether the cofactor is prime.  Bounded search, one orbit (D=425).  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2, isqrt
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17
RAMIFIED = (5, 17)


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def descent_minq(ts, m, rng, rounds=20):
    best_ts = ts[:]
    b = build(best_ts, m)
    best = log2(qmin_fast(*b)) if b and qmin_fast(*b) else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(8):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 320)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                b = build(cand, m)
                if not b:
                    continue
                q = qmin_fast(*b)
                if not q or q < 2:
                    continue
                v = log2(q)
                if v < best - 1e-9:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best_ts


def factor_upto(n, B):
    """Trial-divide n by primes up to B.  Returns (factors dict for p<=B, cofactor > 1 that has no
    factor <= B).  Cofactor is either 1, a prime > B, or a product of such (rare here)."""
    f = {}
    d = 2
    while d <= B and d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    # any remaining prime factor <= B (when n itself <= B after divisions)
    if 1 < n <= B:
        f[n] = f.get(n, 0) + 1
        n = 1
    return f, n            # n is the large cofactor (>B) or 1


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2; r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def bits(x):
    return log2(x) if x > 1 else 0.0


if __name__ == "__main__":
    B = 100000
    print("=" * 104, flush=True)
    print(f"RESIDUE PRIME CONTENT (§6aj): factor the ADVERSARIAL-MIN q_min (trial div <= {B}). Which", flush=True)
    print("channel survives -- ramified {5,17}, smooth generic (Vandermonde), or a few large primes?", flush=True)
    print("=" * 104, flush=True)
    rng = random.Random(20260816)
    hdr = (f"{'m':>3} | {'log2 q':>7} | {'ram 5^a17^b':>11} | {'ram bits':>8} | "
           f"{'#gen p':>6} | {'gen bits':>8} | {'largest p':>10} | {'cofac bits':>10} | {'cof prime':>9}")
    print(hdr, flush=True)
    print("-" * len(hdr), flush=True)
    for m in range(3, 8):
        # take the best of several descents (harder adversary)
        best_ts, best_q = None, None
        for _ in range(6):
            s0 = rng.sample(range(1, 320), m)
            ts = descent_minq(s0, m, rng)
            b = build(ts, m)
            if not b:
                continue
            q = qmin_fast(*b)
            if q and q >= 2 and (best_q is None or q < best_q):
                best_q, best_ts = q, ts
        if best_q is None:
            print(f"{m:>3} | (no valid)", flush=True)
            continue
        q = best_q
        f, cof = factor_upto(q, B)
        a, bpow = f.pop(5, 0), f.pop(17, 0)
        ram = 5 ** a * 17 ** bpow
        rambits = bits(ram)
        gen_primes = sorted(f)                      # generic small primes (excl 5,17), <= B
        genbits = sum(f[p] * log2(p) for p in gen_primes)
        largest = max(gen_primes) if gen_primes else 1
        cofbits = bits(cof)
        cofp = is_prime(cof) if cof > 1 else False
        # largest prime overall (cofactor may exceed largest small generic)
        big = cof if cof > 1 else largest
        print(f"{m:>3} | {log2(q):7.2f} | {str((a, bpow)):>11} | {rambits:8.2f} | "
              f"{len(gen_primes):>6} | {genbits:8.2f} | {big:>10} | {cofbits:10.2f} | {str(cofp):>9}",
              flush=True)
    print("\n" + "=" * 104, flush=True)
    print("READING (L5): compare ram bits vs generic bits vs cofactor bits in the MIN-q row.", flush=True)
    print("  * ram bits ~ 0  => §6ae confirmed jointly: adversary drains 5,17; the floor is NON-ramified.", flush=True)
    print("  * generic bits dominate with MANY small primes => Vandermonde/discriminant LB is the target.", flush=True)
    print("  * a big prime cofactor dominates => S-unit/Baker flavor.  ram bits large => §6ae REOPENS.", flush=True)
    print("Trial division bounded; a large cofactor is left unfactored (its bit-size is exact). One orbit", flush=True)
    print("(D=425). Bounded search. Evidence, not proof. RH stays [OUT].", flush=True)
