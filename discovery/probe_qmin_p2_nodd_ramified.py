#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bp — ROW 2 (n ODD) ATTACK: lift the §6bi/§6bm unique-minimum machinery to the ramified prime (1+i).

§6bm PROVED the p=2 floor v_2(q_min) >= 2m-2-S ONLY for the 4|n opposite-parity family, where gamma=conj(M)
is Re-odd/Im-even (gamma ≡ 1 mod 2 in Z[i], a 2-adic unit) so v_2(w'_i)=S(i+1)+1 is LINEAR and the §6bi
term-valuation has a UNIQUE minimum pinning C_j=m+S node-independently.

§6bl(S) observed that for n ODD, gamma is BOTH-ODD (gamma ≡ 1+i mod 2), v_2(w'_i) "goes negative and
non-linear", floor LARGE but "by a mechanism NOT proved here".  THIS PROBE isolates that mechanism.

THEORY UNDER TEST.  both-odd gamma is divisible by the ramified prime pi=1+i EXACTLY once (N(gamma) ≡ 2
mod 4 ⟹ v_pi(gamma)=1).  Write c_j := gamma^j + conj(gamma)^j (a rational integer = the trace).  Since
mod pi the residue field is F_2 (conjugation trivial, i ≡ 1), one shows v_pi(c_j) >= j+1 ALWAYS.  If this
is TIGHT (v_pi(c_j) exactly j+1 up to a bounded/periodic correction), then v_2(w'_i)=v_pi(c_{i+1})/2 - 2(i+1)
is AFFINE-ON-AVERAGE with slope ~ S+1/2 (a Beatty/floor-linear profile, NOT the "unstructured non-linear"
the notes feared).  A floor-linear profile with a definite average slope should STILL give the §6bi term
minimum a controlled (node-independent) C_j, hence a provable LINEAR floor for Row 2.

WHAT THIS PROBE MEASURES (all EXACT integer / Gaussian-integer arithmetic, L9):
  (1) gamma = both-odd primitive Gaussian numerator of beta; confirm v_pi(gamma)=1 (both-odd).
  (2) v_pi(c_j) for j=1..14 — is it exactly j+1?  extract the correction a_j := v_pi(c_j) - (j+1).
  (3) the profile P_i := v_2(w'_i) directly from wp, and cross-check P_i == v_pi(c_{i+1})/2 - 2(i+1).
      Fit an affine model P_i ~ round((S+1/2)(i+1)) + const and report residuals.
  (4) DOWNSTREAM: is per-column C_j node-INDEPENDENT for n-odd orbits (adversary min & max over node sets)?
      If min_j C_j = (affine in m, node-independent), the floor 1+3(m-1)-min_j C_j is provably linear.

READING (L5): if (2) shows v_pi(c_j) affine and (4) shows C_j node-independent affine, Row 2 becomes a
PROVABLE single-prime floor via a (1+i)-adic unique-minimum — the same proof shape as §6bm, one prime up.
Descent = one-sided bound.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_orbit_trichotomy import orbit_beta, v2int, shift_w
from discovery.probe_qmin_p2_floor_identity import wvec, per_column, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_int, vp_frac


def vpi_gauss(a, b):
    """v_pi(a+bi) at the ramified prime pi=1+i in Z[i].  Divide by (1+i) repeatedly.
    (a+bi)/(1+i) = ((a+b) + (b-a)i)/2 — integral iff a,b same parity."""
    a, b = int(a), int(b)
    if a == 0 and b == 0:
        return 10 ** 9
    v = 0
    while (a % 2) == (b % 2):          # a,b same parity <=> divisible by (1+i)
        a, b = (a + b) // 2, (b - a) // 2
        v += 1
    return v


def vpi_int(n):
    """v_pi of a rational integer = 2 * v_2(n) (pi ramified, e=2)."""
    return 2 * v2int(n)


def beta_gauss_numer(beta):
    """Return (gamma_re, gamma_im, den2) with beta = (gre+gim i)/(2^den2 * odd), gamma primitive at 2."""
    import sympy as sp
    re, im = sp.Rational(sp.re(beta)), sp.Rational(sp.im(beta))
    den = sp.ilcm(re.q, im.q)
    gre, gim = int(re * den), int(im * den)
    # strip common factor of (1+i): reduce until not both-even-parity-collapsible at 2
    g = 1
    # factor out powers of 2 from the pair
    while gre % 2 == 0 and gim % 2 == 0:
        gre //= 2
        gim //= 2
        g += 1
    return gre, gim, int(den)


def rho_pqn(sig, tau):
    pn, pd = sig.numerator, sig.denominator
    qn, qd = tau.numerator, tau.denominator
    from math import gcd
    n = pd * qd // gcd(pd, qd)
    p = pn * (n // pd)
    q = qn * (n // qd)
    g = gcd(gcd(abs(p), abs(q)), n)
    return p // g, q // g, n // g


def trace_seq(gre, gim, jmax):
    """c_j = gamma^j + conj(gamma)^j via the integer recurrence c_j = 2Re(g) c_{j-1} - N(g) c_{j-2}."""
    tr = 2 * gre
    nm = gre * gre + gim * gim
    c = [2, tr]
    for _ in range(2, jmax + 1):
        c.append(tr * c[-1] - nm * c[-2])
    return c


def adversary_C(m, sig, tau, w, rng, maximize, restarts=18, rounds=6):
    """One-sided adversary on min_j C_j: maximize (upper bound) or minimize (lower bound)."""
    best = None
    for _ in range(restarts):
        ts = rng.sample(range(1, 200), m)
        pc = per_column(ts, m, w)
        if pc is None:
            continue
        cur = min(pc[1])
        for _rnd in range(rounds):
            improved = False
            for i in range(m):
                for _ in range(8):
                    cand = ts[:]
                    cand[i] = rng.randrange(1, 200)
                    if len(set(cand)) != m:
                        continue
                    pc2 = per_column(cand, m, w)
                    if pc2 is None:
                        continue
                    v = min(pc2[1])
                    better = (v > cur) if maximize else (v < cur)
                    if better:
                        ts, cur, improved = cand, v, True
            if not improved:
                break
        if best is None or (cur > best if maximize else cur < best):
            best = cur
    return best


if __name__ == "__main__":
    print("=" * 104, flush=True)
    print("§6bp: Row 2 (n odd) — ramified-prime (1+i) profile of v_2(w'_i) and C_j node-independence.", flush=True)
    print("=" * 104, flush=True)

    # n-odd orbits (both-odd gamma, S<0).  Plus one 4|n control (S>=3) to confirm v_pi machinery.
    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(1, 3), Fr(1)), (Fr(3, 5), Fr(1)),
              (Fr(3, 4), Fr(1))]  # last = 4|n control (Re-odd/Im-even, S=3)

    print("\n(1)+(2)+(3): gamma parity, v_pi(c_j), and the v_2(w'_i) profile.", flush=True)
    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        A, B, beta, k, (P, Q), den, wp = orbit_beta(sig, tau, M=16)
        gre, gim, den2 = beta_gauss_numer(beta)
        par = "both-odd" if (gre % 2 and gim % 2) else (
            "Re-odd/Im-even" if (gre % 2 and gim % 2 == 0) else "Re-even/Im-odd")
        vpi_g = vpi_gauss(gre, gim)
        S = Fr(v2int(B.numerator) - v2int(B.denominator), 2)
        c = trace_seq(gre, gim, 15)
        # v_pi(c_j) and correction a_j = v_pi(c_j) - (j+1)
        vpic = [vpi_int(c[j]) for j in range(1, 15)]        # v_pi at j=1..14
        acorr = [vpic[j - 1] - (j + 1) for j in range(1, 15)]
        # profile P_i = v_2(w'_i), and predicted v_pi(c_{i+1})/2 - 2*den2*(i+1)? use direct + cross-check
        prof = [vp_frac(Fr(wp[i]), 2) if wp[i] != 0 else None for i in range(len(wp))]
        print("\n  orbit (%s,%s) (p,q,n)=(%d,%d,%d): gamma=%d%+di [%s], v_pi(gamma)=%d, S=%s, N=%d" % (
            sig, tau, p, q, n, gre, gim, par, vpi_g, str(S), den), flush=True)
        print("    v_pi(c_j) j=1..14 : %s" % vpic, flush=True)
        print("    a_j = v_pi(c_j)-(j+1): %s  %s" % (
            acorr, "[EXACT j+1]" if all(a == 0 for a in acorr) else "[has correction]"), flush=True)
        print("    v_2(w'_i) i=0..15  : %s" % prof, flush=True)
        # affine fit of profile on average slope
        diffs = [prof[i + 1] - prof[i] for i in range(len(prof) - 1) if prof[i] is not None and prof[i + 1] is not None]
        avg = Fr(sum(diffs), len(diffs)) if diffs else None
        print("    avg slope of v_2(w'_i) = %s  (predicted S+1/2 = %s)" % (str(avg), str(S + Fr(1, 2))), flush=True)

    print("\n" + "=" * 104, flush=True)
    print("(4) C_j node-independence: adversary MIN and MAX of min_j C_j over node sets (m=4..6).", flush=True)
    print("    If [min-adv, max-adv] is a TIGHT interval affine in m, C_j is pinned -> provable floor.", flush=True)
    rng = random.Random(20260817)
    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        cells = []
        for m in (4, 5, 6):
            w = wvec(m, sig, tau)
            lo = adversary_C(m, sig, tau, w, rng, maximize=False)
            hi = adversary_C(m, sig, tau, w, rng, maximize=True)
            # measured floor at a sample node set
            ts = rng.sample(range(1, 60), m)
            qv = qmin_exact_orbit(ts, m, sig, tau)
            fl = vp_int(qv, 2) if qv else None
            cells.append("m=%d:C in[%s,%s] q2=%s" % (m, lo, hi, fl))
        print("  (%s,%s) n=%d: %s" % (sig, tau, n, "  ".join(cells)), flush=True)

    print("\n" + "=" * 104, flush=True)
    print("READING (L5): both-odd gamma => v_pi(gamma)=1; if v_pi(c_j)=j+1 exactly and v_2(w'_i) is affine with", flush=True)
    print("slope S+1/2, the profile is (1+i)-adically LINEAR. If C_j is then node-independent & affine in m,", flush=True)
    print("Row 2 gets the SAME §6bm-style unique-minimum floor proof, one prime up. Adversary one-sided. RH [OUT].", flush=True)
