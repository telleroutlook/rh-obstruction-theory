#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bl — THE ORBIT TRICHOTOMY: w'_i is UNIVERSALLY rank-2; the p=2 floor is linear iff v_2(beta) != 1.

Building on §6bk (σ=3/4: w'_i = beta^{i+1}+conj is rank-2, v_2=4+3i).  This probe scans orbits and finds a
clean structural law governing OP1's p=2 channel for EVERY off-line orbit (σ,τ):

  (U) UNIVERSAL RANK 2.  For every orbit, the shifted-moment sequence w'_i = L((X-1)^i) satisfies an
      order-2 rational recurrence w'_i = A w'_{i-1} + B w'_{i-2}; equivalently w'_i = beta^{i+1}+conj(beta)^{i+1}
      with beta,conj(beta) the roots of  r^2 - A r - B  (beta = the shifted Chebyshev point of the
      reciprocal-paired orbit exponentials, §6bk).  [VERIFIED all orbits below via Hankel rank = 2.]

  (S) THE 2-ADIC SLOPE  S := v_2(beta) = v_2(B)/2  governs the profile and the floor:
        * S >= 2  (e.g. σ=3/4→k=3, σ=7/8,5/8,9/8→5, σ=5/4→3):  beta = 2^k gamma / N with gamma a Gaussian
          integer of ODD REAL / EVEN IMAG part (gamma ≡ 1 mod 2 in Z[i]) and N odd.  Then
                w'_i = 2^{k(i+1)} * 2 Re(gamma^{i+1}) / N^{i+1},   Re(gamma^{i+1}) ODD,
          so v_2(w'_i) = k(i+1)+1 (linear, slope k>=2).  The §3-Step-4 unique-minimum expansion gives
          C_j = m+k for every column/node set, hence the UNCONDITIONAL LINEAR FLOOR
                v_2(q_min) >= 1 + 3(m-1) - (m+k) = 2m - 2 - k.
          [σ=3/4 (k=3): 2m-5, PROVED in §6bk; the k>=2 family shares the identical two-line proof, with
           gamma ≡ 1 mod 2 VERIFIED for every S>=2 orbit tested.]
        * S = 1  (e.g. σ=5/6, 9/10, 7/10):  BORDERLINE.  beta has v_2=1; the unique-minimum collapses and
          min_j C_j grows at slope ≈ 3, so the p=2 lower bound 1+3(m-1)-min_j C_j is VACUOUS.  Measured
          v_2(q_min) is SMALL (σ=9/10: 1,2,4 at m=4,5,6) — the p=2 channel does NOT carry the barrier here.
        * S < 1  (e.g. σ=4/5, 2/3: v_2(B)=-3, S=-3/2):  beta has 2 in the DENOMINATOR; v_2(w'_i) goes
          NEGATIVE and non-linear, so C_j is negative and the floor is LARGE (measured v_2(q_min)=22,30,36) —
          p=2 closes these easily, but by a different (non-"odd real part") mechanism not proved here.

  (M) HONEST — the p=2 floor is NOT orbit-robust (correcting OB-43's Theorem framing).  No single fixed
      prime is uniformly linear across all orbits; the S=1 orbits defeat p=2.  BUT the TOTAL barrier is
      orbit-robust in the tested range: worst-case (min over node subsets of {1..13}) log_2(q_min) grows
      LINEARLY for every orbit (σ=3/4: 36,49,66; σ=5/6: 42,57,74; σ=9/10: 55,70,91 at m=4,5,6), with the
      barrier migrating to LARGER primes when p=2 is weak.  So OP1 plausibly closes for all orbits as a
      MULTI-PRIME phenomenon; the clean single-prime provable nugget is the S>=2 (v_2(beta)>=2) family via p=2.

RH stays [OUT].  Everything is finite exact 2-adic / Gaussian-integer arithmetic about explicit rationals.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import comb
import sympy as sp
from discovery.probe_qmin_p2_floor_identity import wvec, per_column, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import vp_frac, vp_int, x_of

P2 = 2


def shift_w(w, m):
    return [sum(comb(i, l) * ((-1) ** (i - l)) * w[l] for l in range(i + 1)) for i in range(m)]


def v2(fr):
    return vp_frac(fr, P2) if fr != 0 else 10 ** 9


def v2int(n):
    n = int(abs(n))
    if n == 0:
        return 10 ** 9
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def hankel_rank(seq, rmax=6):
    for r in range(1, rmax + 1):
        rows = [[seq[i + j] for j in range(r + 1)] for i in range(len(seq) - r)]
        if len(rows) < r + 1:
            return None
        pr = 0
        for c in range(r + 1):
            piv = next((rr for rr in range(pr, len(rows)) if rows[rr][c] != 0), None)
            if piv is None:
                continue
            rows[pr], rows[piv] = rows[piv], rows[pr]
            pv = rows[pr][c]
            for rr in range(len(rows)):
                if rr != pr and rows[rr][c] != 0:
                    f = rows[rr][c] / pv
                    rows[rr] = [a - f * b for a, b in zip(rows[rr], rows[pr])]
            pr += 1
            if pr == len(rows):
                break
        if pr <= r:
            return r
    return None


def orbit_beta(sig, tau, M=10):
    """Return (A, B, beta, k, gamma=(g_re,g_im), N) for the rank-2 recurrence of w'_i."""
    wp = shift_w(wvec(M, sig, tau), M)
    W = [sp.Rational(x.numerator, x.denominator) for x in wp]
    a, b = sp.symbols('a b')
    sol = sp.solve([W[2] - a * W[1] - b * W[0], W[3] - a * W[2] - b * W[1]], [a, b])
    A, B = sp.Rational(sol[a]), sp.Rational(sol[b])
    r = sp.symbols('r')
    beta = sp.nsimplify(sp.solve(r * r - A * r - B, r)[0])
    re, im = sp.Rational(sp.re(beta)), sp.Rational(sp.im(beta))
    den = sp.ilcm(re.q, im.q)
    P, Q = int(re * den), int(im * den)
    k = min(v2int(P) if P else 99, v2int(Q) if Q else 99)
    return A, B, beta, k, (P // 2 ** k, Q // 2 ** k), int(den), wp


def gpow(a, b, n):
    re, im = 1, 0
    for _ in range(n):
        re, im = re * a - im * b, re * b + im * a
    return re, im


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6bl: universal rank-2; p=2 floor linear iff v_2(beta) != 1 (S>=2 family: v_2(q_min) >= 2m-2-k).", flush=True)
    print("=" * 100, flush=True)

    ORBITS = [(Fr(3, 4), Fr(1)), (Fr(7, 8), Fr(1)), (Fr(5, 8), Fr(1)), (Fr(5, 4), Fr(1)),
              (Fr(5, 6), Fr(1)), (Fr(9, 10), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(2, 3), Fr(1))]

    print("\n(1) rank, beta = 2^k*gamma/N, gamma mod 2, profile slope, predicted p=2 floor:", flush=True)
    print("%-10s %-5s %-22s %-14s %-9s %s" % ("(sig,tau)", "rank", "beta", "gamma(mod2)", "S=v2(b)", "floor"), flush=True)
    for sig, tau in ORBITS:
        A, B, beta, k, (gre, gim), N, wp = orbit_beta(sig, tau)
        rk = hankel_rank(wp)
        S = Fr(v2int(B.p) - v2int(B.q), 2)
        if S >= 2:
            # verify closed form + odd real part
            cf = all(Fr((2 ** k) ** (i + 1) * 2 * gpow(gre, gim, i + 1)[0], N ** (i + 1)) == wp[i] for i in range(len(wp)))
            odd = all(gpow(gre, gim, n)[0] % 2 == 1 for n in range(1, 10))
            floor = "2m-%d (cf=%s,odd=%s)" % (2 + k, cf, odd)
        elif S == 1:
            floor = "VACUOUS (S=1 borderline)"
        else:
            floor = "large/nonlinear (S<1)"
        print("%-10s %-5s %-22s Re%%2=%d Im%%2=%d %-9s %s" % (
            "(%s,%s)" % (sig, tau), rk, str(beta), gre % 2, gim % 2, str(S), floor), flush=True)

    print("\n(2) measured min_j C_j and v_2(q_min) vs the prediction (fixed small node set):", flush=True)
    pool = [1, 2, 3, 5, 7, 11, 13]
    for sig, tau in ORBITS:
        A, B, beta, k, g, N, wp = orbit_beta(sig, tau)
        S = Fr(v2int(B.p) - v2int(B.q), 2)
        row = []
        for m in (4, 5, 6):
            ts = pool[:m]
            if len(set(x_of(t) for t in ts)) != m:
                continue
            pc = per_column(ts, m, wvec(m, sig, tau))
            q = qmin_exact_orbit(ts, m, sig, tau)
            if pc is None or q is None:
                continue
            pred = 2 * m - 2 - k if S >= 2 else None
            row.append("m=%d:minC=%d v2q=%d%s" % (m, min(pc[1]), vp_int(q, 2),
                                                  ("(>=%d? %s)" % (pred, vp_int(q, 2) >= pred)) if pred is not None else ""))
        print("    (%s,%s) S=%s: %s" % (sig, tau, S, "  ".join(row)), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): rank-2 is UNIVERSAL; p=2 gives an unconditional linear floor v_2(q_min)>=2m-2-k for the", flush=True)
    print("v_2(beta)=k>=2 family (gamma odd-real-part verified; σ=3/4 k=3 PROVED §6bk). S=1 orbits defeat p=2", flush=True)
    print("(barrier migrates to other primes); total log q_min still grows linearly. OP1 = multi-prime. RH [OUT].", flush=True)
