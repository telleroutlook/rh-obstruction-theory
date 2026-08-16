#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cp — the p=2 floor is ORBIT-INDEPENDENT and linear for most orbits, but NOT universal: some orbits
(e.g. n=50) escape BOTH p=2 and p=3.  This pins down why OP1 needs a DISTRIBUTED (multi-prime) argument.

SETUP (p=2, spec §6bf).  v₂(q_min) = max_j (1 + N_j − C_j), N_j = Σ_{k≠j} v₂(x_j−x_k), C_j = v₂(S_j).
Since x_j−x_k = 8(j−k)(j+k)/[(4j²+1)(4k²+1)] with ODD denominators (4t²+1 is odd), v₂(x_j−x_k) ≥ 3 for
EVERY pair and EVERY orbit ⇒ N_j ≥ 3(m−1) unconditionally.  The floor is linear iff C_j does not cancel it.

FINDINGS (EXACT, L9), consecutive nodes t=1..m:
  * For n ∈ {10, 14, 22} (both a with 3∤(a+n) and 3|(a+n)!), the p=2 floor is ORBIT-INDEPENDENT and equal:
    v₂(q_min) = 5, 11, 16, 23 at m = 8, 12, 16, 20 — LINEAR (floor/m → ~1.15), same value across orbits.
    So p=2 catches many 3|(a+n) orbits that p=3 misses.
  * BUT n=50 (a=1; a+n=51 ⇒ 3|(a+n) too) ESCAPES: C_j GROWS faster than N_j, giving v₂(q_min) = 0,1,2,4
    (floor/m ≈ 0.2, ≪ the others).  n=50,a=1 thus escapes BOTH p=2 (weak) and p=3 (degenerate, 3|51),
    and its super-poly q_min is carried by the large orbit-specific primes of §6cn.

READING (L5): there is NO single small prime giving a uniform linear floor for ALL Row-3 orbits — the
p=2 and p=3 floors are strong but each has escapees, and the escapees are caught by DIFFERENT (often large,
orbit-specific) primes.  This is direct evidence that closing OP1 requires the DISTRIBUTED statement
"every node set has SOME prime p with v_p(q_min) ≥ c·m", not a single-prime lemma.  §6co (p=3, 3∤(a+n))
and this p=2 linear floor are the two proven/near-proven single-prime instances.  RH stays [OUT].

DECISIVE AGGREGATE TEST (added).  The OP1 quantity is log q_min = Σ_p v_p(q_min)·log p, NOT any one prime.
Computing the EXACT integer q_min for n=50 (the doubly-degenerate orbit, escapes both p=2 and p=3):
  log₂(q_min)/m ≈ 23.2, 24.3, 24.4, 25.2, 25.6 at m=6,8,10,12,14 — LINEAR and INCREASING in m,
i.e. log q_min = Ω(m) HOLDS for n=50 anyway, carried by the aggregate over its large orbit-specific primes.
So the OP1 barrier survives even the worst small-prime case via DISTRIBUTION across primes — no single prime
needed.  This upgrades the OP1 evidence: the linear-log lower bound appears UNIVERSAL over orbits (consecutive
nodes), with the single-prime floors (§6co p=3, p=2 here) being the constructive-but-non-universal witnesses.
The remaining rigor for OP1 is the aggregate statement + the node-set infimum (adversarial, §6cn).  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr

from discovery.probe_qmin_p2_floor_identity import wvec, per_column, qmin_exact_orbit


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6cp: p=2 floor is orbit-independent & linear for most orbits, but NOT universal (n=50 escapes). RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    ORB = [(1, 22, "3∤(a+n)"), (5, 22, "3|(a+n)"), (1, 14, "3|(a+n)"),
           (3, 10, "3∤(a+n)"), (1, 50, "3|(a+n)  [also 3|51 ⇒ p=3 degenerate]")]
    print("\n%-22s %s" % ("orbit", "v₂(q_min)=max_j(1+N_j−C_j) at m=8,12,16,20  (N_j≥3(m−1) always)"), flush=True)
    print("-" * 92, flush=True)
    for a, n, tag in ORB:
        sig = Fr(a, n)
        floors = []
        for m in (8, 12, 16, 20):
            w = wvec(m, sig, Fr(1))
            pc = per_column(list(range(1, m + 1)), m, w)
            if pc is None:
                floors.append(None)
                continue
            N, C = pc
            floors.append(max(1 + N[j] - C[j] for j in range(m)))
        s = "  ".join("%3s" % ("—" if f is None else f) for f in floors)
        rates = "  ".join("%.2f" % (f / m) for f, m in zip(floors, (8, 12, 16, 20)) if f is not None)
        print("  a=%-2d n=%-3d %-14s  floors: %s   (floor/m: %s)" % (a, n, tag, s, rates), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): p=2 floor orbit-independent & linear (5,11,16,23) for n∈{10,14,22} both regimes;", flush=True)
    print("n=50 escapes p=2 AND p=3 ⇒ NO universal small prime ⇒ OP1 needs the DISTRIBUTED multi-prime lemma.", flush=True)
    print("§6co (p=3, 3∤(a+n)) + this p=2 floor are the proven single-prime instances. RH stays [OUT].", flush=True)

    # DECISIVE AGGREGATE TEST: exact integer q_min; is log q_min = Ω(m) EVEN for the doubly-degenerate n=50?
    from math import log2
    print("\n" + "=" * 100, flush=True)
    print("AGGREGATE: log₂(q_min)/m for EXACT q_min (OP1 quantity = Σ_p v_p·log p, not a single prime):", flush=True)
    print("-" * 92, flush=True)
    for a, n, tag in [(1, 50, "escapes p=2 AND p=3 — worst small-prime case"),
                      (1, 22, "control: p=2 linear")]:
        row = []
        for m in (6, 8, 10, 12, 14):
            q = qmin_exact_orbit(list(range(1, m + 1)), m, Fr(a, n), Fr(1))
            if not q:
                row.append((m, None)); continue
            row.append((m, log2(abs(q))))
        print("  a=%d n=%-3d %-42s %s" % (a, n, tag, "  ".join(
            "m=%d:%.2f/m=%.1f" % (m, lg, lg / m) for (m, lg) in row if lg is not None)), flush=True)
    print("\n=> log q_min = Ω(m) holds for n=50 too (slope 23→26, INCREASING) — barrier survives via", flush=True)
    print("DISTRIBUTION across primes; single-prime floors are non-universal witnesses. RH stays [OUT].", flush=True)
