#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bw — DECIDE the Row 2 FACT B proof route: is the depth ceiling a PURE 2-adic IMAGE fact, or does it
require the GLOBAL collision competition?

§6bv reduced FACT B to a 2-adic distance: at m≡2 mod4 the tie's cancellation depth is
      depth = v₂(τ − σ),   τ = w_{m−1}/w_{m−2}  (fixed odd orbit target),   σ = Σ_{k≠j} x_k  (a node-sum).
§6bu found depth ≤ A ≤ 2 uniformly under the ACTUAL collision constraint.  Two mechanisms could cause the
ceiling, and they demand DIFFERENT proofs:
  (1) PURE IMAGE — the set {x_t = (4t²−1)/(4t²+1)} is 2-adically restricted enough that EVEN UNCONSTRAINED,
      a sum of m−1 of them cannot approach τ past depth A.  ⇒ Row 2 closes via a clean 2-adic image lemma.
  (2) GLOBAL COMPETITION — unconstrained, σ COULD approach τ deeply, but being the argmin column of a valid
      collision (all other columns pinned) forbids it.  ⇒ needs the harder global minimax argument.

THIS PROBE (EXACT, L9) measures, for n-odd orbits and m∈{6,10,14}:
  • UNCONSTRAINED max depth: over (m−1)-subsets of a node pool (hill-climb to maximize v₂(τ−σ)), the deepest
    2-adic approximation of τ by ANY node-sum — a clean UPPER bound on what σ-tuning alone can do.
  • the achievable residue set U_K = { x_t mod 2^K } sizes for K=4..10 — is the image O(1) or growing?
DECISION RULE (L5):
  unconstrained max depth BOUNDED ≈ A  ⇒ mechanism (1): the ceiling is pure image structure → clean lemma.
  unconstrained max depth GROWS with m ⇒ mechanism (2): the ceiling needs the global collision argument.
Adversary one-sided (hill-climb gives a LOWER bound on the true unconstrained max ⇒ if it already grows, (2)
is forced; if it stays flat, (1) is strongly indicated).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def target_tau(m, sig, tau):
    """The fixed odd 2-adic target τ = w_{m−1}/w_{m−2} (both fixed, node-independent)."""
    w = wvec(m, sig, tau)
    return Fr(w[m - 1]) / Fr(w[m - 2]), w


def depth_of_subset(ts, tau_t):
    """depth = v₂(τ − σ), σ = Σ x_t over the chosen node set (size m−1)."""
    sigma = sum(x_of(t) for t in ts)
    return vp_frac(tau_t - sigma, 2)


def adv_max_depth(mm1, tau_t, rng, restarts, rounds, pool):
    """Hill-climb over (m−1)-subsets to MAXIMIZE v₂(τ−σ) — a lower bound on the true unconstrained max."""
    best = None
    for _ in range(restarts):
        ts = rng.sample(range(1, pool), mm1)
        cur = depth_of_subset(ts, tau_t)
        for _rnd in range(rounds):
            improved = False
            for i in range(mm1):
                for _ in range(12):
                    cand = ts[:]
                    cand[i] = rng.randrange(1, pool)
                    if len(set(cand)) != mm1:
                        continue
                    v = depth_of_subset(cand, tau_t)
                    if v > cur:
                        ts, cur, improved = cand, v, True
            if not improved:
                break
        if best is None or cur > best:
            best = cur
    return best


def image_sizes(Ks, pool):
    """|U_K| = number of distinct residues of x_t mod 2^K over t=1..pool (x_t is a 2-adic unit fraction)."""
    out = []
    for K in Ks:
        mod = 1 << K
        seen = set()
        for t in range(1, pool):
            x = x_of(t)
            num, den = x.numerator, x.denominator     # den odd (4t²+1), so x is a 2-adic integer
            seen.add((num * pow(den, -1, mod)) % mod)
        out.append(len(seen))
    return out


if __name__ == "__main__":
    print("=" * 104, flush=True)
    print("§6bw: is the Row 2 depth ceiling a PURE 2-adic image fact (1) or the GLOBAL competition (2)?", flush=True)
    print("=" * 104, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1))]
    MS = [6, 10, 14]
    rng = random.Random(20260823)

    print("\nImage sizes |U_K| = #{ x_t mod 2^K : t=1..400 }  (K=4..10):", flush=True)
    Ks = list(range(4, 11))
    print("  K:            " + "  ".join("%4d" % K for K in Ks), flush=True)
    print("  |U_K|:        " + "  ".join("%4d" % s for s in image_sizes(Ks, 400)), flush=True)
    print("  (2^{K}):      " + "  ".join("%4d" % (1 << K) for K in Ks), flush=True)

    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        print("\norbit (%s,%s) n=%d:" % (sig, tau, n), flush=True)
        for m in MS:
            tau_t, w = target_tau(m, sig, tau)
            vt = vp_frac(tau_t, 2)          # τ must be an odd 2-adic unit for the tie identity to apply
            restarts = 60 if m <= 10 else 40
            rounds = 12 if m <= 10 else 9
            md = adv_max_depth(m - 1, tau_t, rng, restarts, rounds, pool=max(160, 16 * m))
            print("  m=%2d: v₂(τ)=%d  UNCONSTRAINED max depth over (m−1)-subsets = %s" % (m, vt, md), flush=True)

    print("\n" + "=" * 104, flush=True)
    print("DECISION (L5): if UNCONSTRAINED max depth stays flat (≈ A, small) as m grows ⇒ mechanism (1): the", flush=True)
    print("ceiling is pure 2-adic image structure, Row 2 closes via a clean image lemma.  If it GROWS with m ⇒", flush=True)
    print("mechanism (2): the ceiling needs the global collision competition.  Hill-climb one-sided. RH [OUT].", flush=True)
