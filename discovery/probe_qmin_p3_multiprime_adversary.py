#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cn — MULTI-PRIME extension of the §6cm floor + adversarial (node-set) robustness of OP1.

Motivation: §6cm proves the p=3 LINEAR floor only for the sub-family 3∤(a+n).  OP1's infimum is
controlled by the OTHER sub-family 3|(a+n) (p=3 annihilates the a0 class).  Two questions:
  (Q1) Do 3|(a+n) orbits still get a super-poly q_min, via some OTHER prime?
  (Q2) OP1's node set is adversary-chosen to MINIMIZE q_min.  Does the floor survive the minimizer?

FINDINGS (EXACT, L9):
  * GENERAL prime classifier (from the palindromic-quartic reduction §6cl, valid for every prime p∤n):
    the mod-p pole/floor is non-degenerate iff  1 + e2 s^2 + s^4  stays separable mod p, i.e.
        e2 ≢ ±2 (mod p)   [z^2 - e2 z + 1 has distinct roots  ⟺  e2^2 - 4 ≢ 0].
    e2 = |g|^2 + 2 is a FIXED rational per orbit ⇒ only FINITELY many "degenerate" primes (those p |
    numerator of e2∓2).  So every orbit is non-degenerate at all but finitely many p — a candidate
    MULTI-PRIME route to a uniform floor.
  * FACTORIZATION of q_min at the consecutive node set t=1..m shows, for 3|(a+n) orbits, LINEAR-exponent
    primes exist (large orbit-specific primes from the node denominators 4t^2+1, plus v_2), so
    log q_min = Ω(m) EVEN when p=3 is degenerate.  (n=14,a=1: 73,197 grow ~m; n=22,a=5: 509,773.)
  * ADVERSARIAL trend: minimizing log2 q_min over random node sets gives values LARGER than the
    consecutive set t=1..m — i.e. consecutive is near the minimizer, and it is already linear (~20/node),
    for BOTH 3∤(a+n) and 3|(a+n).  Random spreading raises q_min (you cannot dodge clustering at every
    prime at once — the distributed-pigeonhole intuition of §6ch).

HONEST SCOPE (L5):
  - This is EVIDENCE, not proof, for OP1's infimum.  "min over random sets" is not the true adversarial
    infimum over STRUCTURED node sets; and §6cm's exact floor is proved for the consecutive node set only.
  - The clean open lemma to close OP1: "for EVERY node set, some prime p gives v_p(q_min) >= c m"
    (a distributed/pigeonhole statement, §6ch), of which §6cm (p=3, 3∤(a+n)) is the single-prime instance.
  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import math
import random

from sympy import factorint

from discovery.probe_qmin_p2_floor_identity import qmin_exact_orbit
from discovery.probe_qmin_p3_fact3a_recurrence import quartic_e1_e2


def e2_mod_p(e2, p):
    """e2 mod p if 3-integral at p, else None."""
    if e2.denominator % p == 0:
        return None
    return e2.numerator % p * pow(e2.denominator % p, -1, p) % p


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6cn: multi-prime floor (general classifier e2≢±2 mod p) + adversarial node-set robustness. RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    ORBITS = [(1, 22, "3∤(a+n)  [p=3 floor, §6cm]"),
              (5, 22, "3|(a+n)  [p=3 degenerate → other primes]"),
              (1, 14, "3|(a+n)")]

    print("\n(1) GENERAL classifier e2 mod p; DEG ⟺ e2≡±2 (mod p) ⟺ p degenerate for the p-floor:", flush=True)
    for a, n, tag in ORBITS:
        e1, e2 = quartic_e1_e2(Fr(a, n), Fr(1))
        cells = []
        for p in (3, 5, 7, 11, 13):
            if n % p == 0:
                cells.append("p=%d:n|n" % p)
                continue
            r = e2_mod_p(e2, p)
            if r is None:
                cells.append("p=%d:—" % p)
                continue
            deg = (r == 2 % p or r == (-2) % p)
            cells.append("p=%d:e2=%d%s" % (p, r, "[DEG]" if deg else "[ok]"))
        print("  a=%-2d n=%-3d %-32s  %s" % (a, n, tag, "  ".join(cells)), flush=True)

    print("\n(2) FACTOR q_min at consecutive t=1..m: linear-exponent primes exist for 3|(a+n) too:", flush=True)
    for a, n, tag in ORBITS:
        sig = Fr(a, n)
        line = "  a=%-2d n=%-3d: " % (a, n)
        facs = {}
        for m in (8, 10):
            q = qmin_exact_orbit(list(range(1, m + 1)), m, sig, Fr(1))
            facs[m] = factorint(q) if (q and q > 0) else {}
        primes = sorted(set(facs[8]) | set(facs[10]))
        growth = [(p, facs[8].get(p, 0), facs[10].get(p, 0)) for p in primes]
        lin = [p for (p, e8, e10) in growth if e10 - e8 >= 2]            # exponent grows ~ with m
        print(line + "linear-exponent primes (e10-e8>=2): %s" % lin, flush=True)
        print("           full m=10 factor: " + " * ".join("%d^%d" % (p, e) for p, e in sorted(facs[10].items())), flush=True)

    print("\n(3) ADVERSARIAL: min log2 q_min over random node sets vs consecutive t=1..m (per-node in parens):", flush=True)
    rng = random.Random(2027)
    for a, n, tag in ORBITS[:2]:
        sig = Fr(a, n)
        print("  a=%-2d n=%-3d %s" % (a, n, tag), flush=True)
        for m in (6, 8):
            qc = qmin_exact_orbit(list(range(1, m + 1)), m, sig, Fr(1))
            lqc = math.log2(qc) if qc and qc > 0 else -1
            best = None
            for _ in range(60):
                ts = rng.sample(range(1, 90), m)
                q = qmin_exact_orbit(ts, m, sig, Fr(1))
                if q and q > 0 and (best is None or q < best):
                    best = q
            lqm = math.log2(best) if best else -1
            print("    m=%2d: consecutive=%6.1f   min/60 random=%6.1f (%.1f/node)  => random NOT smaller" % (
                m, lqc, lqm, lqm / m), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): 3|(a+n) orbits keep log q_min=Ω(m) via large orbit-primes + p=2; consecutive nodes", flush=True)
    print("are near the minimizer and already linear for BOTH regimes. EVIDENCE for OP1 infimum, not proof.", flush=True)
    print("Clean open lemma: 'every node set has some prime p with v_p(q_min)>=c m' (distributed, §6ch).", flush=True)
    print("§6cm (p=3, 3∤(a+n)) is its proved single-prime instance. RH stays [OUT].", flush=True)
