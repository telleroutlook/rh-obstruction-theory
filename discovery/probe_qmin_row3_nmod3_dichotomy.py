#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6ch — the SINGLE-PRIME-CERTIFICATE BLIND SPOT.  Within Row 3 (n≡2 mod4, 3∤n) OP1 splits by n mod 3:

  Row 3a (n≡1 mod3, e.g. n=10,22): p=3 carries a LINEAR valuation floor; v₃(q_min)=max_j clus(j)−C
      with bounded defect C≤3 (up to m=12), clus(j)=Σ_{k≠j} v₃(x_j−x_k).  With the PROVABLE pigeonhole
      max_j clus(j) ≥ ⌈m/2⌉−1 (m nodes, N(3)=2 classes mod 3), a CANDIDATE single-prime close MODULO
      the bounded-defect lemma v₃(q_min) ≥ max_j clus(j) − O(1).

  Row 3b (n≡2 mod3, e.g. n=14,26): NO small prime carries a linear floor (p=2 is O(1), p=3 flat ~0–1,
      others sporadic noise), YET log(min q_min) grows ~linearly/quadratically in m ≫ log m.  So OP1
      HOLDS but its content is DISTRIBUTED across many primes — no single-prime certificate; and NOT
      archimedean (|det V|<1 as every node x_t=(4t²−1)/(4t²+1) ∈ (0,1)).

READING (L5, HONEST NEGATIVE): OP1 appears TRUE for all orbits, but the single-prime valuation-floor
STRATEGY (§6bm/§6cd/§6cf/§6cg) has a genuine BLIND SPOT on Row 3b — closing it needs a GLOBAL bound
on log q_min = Σ_p v_p(q_min)·log p, not a single prime.  This SUPERSEDES §6cf's "all of Row 3 → (4″)".
RH stays [OUT].

THIS PROBE (EXACT, L9): (A) per-prime floors over node sets showing Row 3a has a p=3 linear floor and
Row 3b has none; (B) the direct magnitude log(min q_min) super-polynomial on BOTH; (C) the pigeonhole
max_j clus(j) ≥ ⌈m/2⌉−1 holds.  Uses qmin_exact_orbit (integer determinants) — kept to m≤9 to run fast.
"""
from __future__ import annotations
from fractions import Fraction as Fr
import math
import random

from discovery.probe_qmin_p2_floor_identity import qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def vp_int(q, p):
    v = 0
    while q % p == 0:
        q //= p
        v += 1
    return v


def v3f(x):
    return vp_frac(Fr(x), 3)


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6ch: Row-3 dichotomy by n mod 3 — single-prime certificate exists (3a) or does not (3b). RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    ORBITS = [(Fr(3, 10), "n=10  Row 3a (n≡1 mod3)"),
              (Fr(1, 22), "n=22  Row 3a (n≡1 mod3)"),
              (Fr(1, 14), "n=14  Row 3b (n≡2 mod3)"),
              (Fr(1, 26), "n=26  Row 3b (n≡2 mod3)")]
    SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]

    for sig, label in ORBITS:
        _, _, n = rho_pqn(sig, Fr(1))
        assert n % 4 == 2 and n % 3 != 0, "orbit is not Row 3"
        print("\n%s   [n mod3 = %d]:" % (label, n % 3), flush=True)
        for m in (5, 6, 7, 8, 9):
            rng = random.Random(1)
            floor = {p: 10 ** 9 for p in SMALL_PRIMES}
            best = None
            pigeon = 10 ** 9          # min over samples of max_j clus(j); must be >= ceil(m/2)-1
            for _ in range(60):
                ts = rng.sample(range(1, 16 * m), m)
                if len(set(ts)) != m:
                    continue
                xs = [x_of(t) for t in ts]
                qm = qmin_exact_orbit(ts, m, sig, Fr(1))
                if not isinstance(qm, int) or qm == 0:
                    continue
                for p in SMALL_PRIMES:
                    floor[p] = min(floor[p], vp_int(qm, p))
                if best is None or qm < best:
                    best = qm
                clus = [sum(v3f(xs[j] - xs[k]) for k in range(m) if k != j) for j in range(m)]
                pigeon = min(pigeon, max(clus))
            v3fl = floor[3]
            lg = math.log(best) if best else 0.0
            nz = {p: floor[p] for p in SMALL_PRIMES if floor[p] > 0}
            print("  m=%d: v3-floor=%d  small-prime floors=%-28s  log(min q_min)=%6.2f (log m=%.2f)  pigeon max_clus=%d (>=%d)"
                  % (m, v3fl, str(nz), lg, math.log(m), pigeon, (m + 1) // 2 - 1), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): Row 3a shows v3-floor growing ~linearly (single-prime certificate at p=3);", flush=True)
    print("Row 3b shows every small-prime floor O(1) yet log(min q_min) super-poly ⇒ distributed content,", flush=True)
    print("NO single-prime certificate. OP1 holds throughout; the single-prime STRATEGY has a Row-3b blind", flush=True)
    print("spot needing a global log-q_min bound. Supersedes §6cf 'all Row 3 → (4″)'. RH stays [OUT].", flush=True)
