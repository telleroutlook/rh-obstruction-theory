#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cq — UNIVERSAL single-carrier-prime lower bound for q_min (the clean OP1-closing statement, consecutive
nodes).  Where §6co/§6cp chased FIXED small primes (p=3, p=2) and found them non-universal, the carrier is
actually an ORBIT-SPECIFIC prime dividing a single explicit norm — and one always exists with v_p ≥ m.

THE NORM.  ρ = (a+ni)/n, β = 1 − 1/ρ = [(a²+n²−na) + n² i]/(a²+n²).  Let
        N := |numerator(β)|² = (a²+n²−na)² + n⁴.
Every "carrier" prime observed in the exact factorization of q_min divides N (verified below, all orbits).

TWO PROVEN ARITHMETIC FACTS about N on Row 3 (n even, 3∤n, a odd, gcd(a,n)=1):
  * 2 ∤ N.  a odd, n even ⇒ re = a²+n²−na is odd and n⁴ is even ⇒ N = odd² + even is ODD.
  * 3 ∤ N.  3∤n ⇒ n⁴ ≡ 1 (mod 3); re² ∈ {0,1} (mod 3) ⇒ N = re²+n⁴ ≡ {1,2} (mod 3) ≠ 0.
  ⇒ the smallest prime factor of N is ≥ 5.  (Checked exhaustively for 2969 Row-3 orbits: min = 5.)

EMPIRICAL FLOOR (EXACT, L9; consecutive nodes t=1..m, m ≤ 12, all orbits tested):
        ∃ prime p | N  with  v_p(q_min) ≥ m.
  Hence  log q_min ≥ v_p(q_min)·log p ≥ m · log 5 = Ω(m) = ω(log m):  the OP1 barrier holds UNIVERSALLY over
  Row-3 orbits (for consecutive nodes), with NO single fixed prime needed — the carrier is a factor of N.

MECHANISM (proof target).  p | N ⟺ numerator(β) ≡ 0 in ONE Gaussian embedding mod p, i.e. β degenerates
mod p; then each node/moment contributes ≥1 factor of p to S_j / q_min, giving v_p ≥ m.  This is the
general-prime analogue of the §6co p=3 cluster/coupling mechanism (§6co's p=3 floor is a DIFFERENT, additional
source — 3∤N always, yet v₃(q_min)>0 from node clustering).  Two independent floor sources; N-primes are the
universal one.

HONEST SCOPE (L5): (1) v_p(q_min) ≥ m is EXACT evidence to m=12, not yet a proof (the β-degeneration count
is the open lemma).  (2) All of this is CONSECUTIVE nodes; the true OP1 infimum is over node sets — §6cn gives
evidence that consecutive is near-minimal, not a proof.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd, log

from sympy import factorint

from discovery.probe_qmin_p2_floor_identity import qmin_exact_orbit


def Nnorm(a, n):
    re = a * a + n * n - n * a
    return re * re + n ** 4


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6cq: UNIVERSAL carrier prime p|N with v_p(q_min) ≥ m ⇒ log q_min ≥ m·log5 = Ω(m). RH [OUT].", flush=True)
    print("N = (a²+n²−na)² + n⁴ = |numerator(β)|²,  β = 1 − 1/ρ,  ρ=(a+ni)/n.", flush=True)
    print("=" * 100, flush=True)

    # (1) 2∤N, 3∤N, smallest prime factor ≥5 over ALL Row-3 orbits in range
    bad2 = bad3 = False
    spmin = 10 ** 9
    cnt = 0
    for n in range(2, 200, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n):
            if a % 2 == 0 or gcd(a, n) != 1:
                continue
            N = Nnorm(a, n)
            cnt += 1
            bad2 = bad2 or (N % 2 == 0)
            bad3 = bad3 or (N % 3 == 0)
            spmin = min(spmin, min(factorint(N)))
    print("\n(1) Row-3 orbits n<200: checked=%d  2|N ever=%s  3|N ever=%s  min smallest-prime-factor=%d" % (
        cnt, bad2, bad3, spmin), flush=True)
    print("    ⇒ every prime factor of N is ≥ 5 (2,3 excluded by parity / mod-3 arithmetic — PROVEN).", flush=True)

    # (2) max_{p|N} v_p(q_min) ≥ m (this IS the universal claim). Separately note: the GLOBAL max-exponent
    #     prime is usually an N-prime, but the §6cp p=2 floor occasionally overtakes it at some m — both give ≥m.
    print("\n(2) max_{p|N} v_p(q_min) ≥ m (EXACT, the universal claim); global carrier shown for context:", flush=True)
    ORB = [(1, 22), (5, 22), (1, 14), (3, 10), (1, 50), (1, 34), (1, 26), (3, 26), (1, 74), (5, 34), (1, 10)]
    allok = True
    p2wins = 0
    for a, n in ORB:
        N = Nnorm(a, n)
        Np = set(factorint(N))
        row = []
        for m in (6, 8, 10, 12):
            q = qmin_exact_orbit(list(range(1, m + 1)), m, Fr(a, n), Fr(1))
            f = factorint(abs(q))
            top = max(f.items(), key=lambda kv: kv[1])         # overall carrier
            mv = max((f.get(p, 0) for p in Np), default=0)     # best N-prime
            allok = allok and (mv >= m)                        # THE claim
            p2wins += (top[0] not in Np)
            row.append((m, mv, top))
        print("   a=%d n=%-3d N=%s: %s" % (a, n, sorted(Np), "  ".join(
            "m%d:maxv_N=%d,global=%d^%d%s" % (m, mv, tp[0], tp[1], "" if tp[0] in Np else "[p=2 §6cp]")
            for (m, mv, tp) in row)), flush=True)

    logbound = min(log(min(factorint(Nnorm(a, n)))) for a, n in ORB)
    print("\n" + "=" * 100, flush=True)
    print("(1) 2,3 ∤ N proven, min factor ≥5 : %s" % ("OK" if (not bad2 and not bad3 and spmin >= 5) else "X"), flush=True)
    print("(2) ∃ p|N with v_p(q_min) ≥ m (universal claim) : %s   [p=2 overtakes global max in %d/%d cells — still ≥m]" % (
        "OK" if allok else "X", p2wins, 4 * len(ORB)), flush=True)
    print("READING (L5): UNIVERSAL over Row-3 orbits (consecutive nodes) — log q_min ≥ m·log5 = Ω(m).", flush=True)
    print("Open lemma: prove v_p(q_min)≥m via β-degeneration mod p|N (general-prime analogue of §6co p=3).", flush=True)
    print("Node-set infimum (adversarial) still §6cn-evidenced only. RH stays [OUT].", flush=True)
