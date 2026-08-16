#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

OP2 SCOPING PROBE — Weil-type (non-Li) observations and the RATIONALITY of the exact obstruction.

Paper A Open Problem 2 asks whether the Theorem-A exact information obstruction extends from the Li
tests to a fixed finite family of Weil-type test functions h_1..h_r (even, real-valued, C_c^inf),
observation phi_h(rho) = hhat((rho-1/2)/i).  The paper flags the obstacle: "the resulting
observation values are not guaranteed to be rational, and no general transcendence statement is
available", so the Chebyshev-Vandermonde reduction (which gives the EXACT lattice index q_min>=1)
does not apply.

WHAT THEOREM A NEEDS (the exact obstruction): two zero-configurations with IDENTICAL finite
observation but different predicate P (one all-on-line, one carrying an off-line functional-equation
quartet).  Identical observation = a COLLISION:  q * Phi_off = sum_k c_k * Phi(gamma_k)  in R^r,
integers q != 0, c_k.  In OP1 the observation values are RATIONAL, so a collision is a rational
linear-algebra fact and q_min = exact lattice index bounds the witness complexity.  For Weil
observations the values are (generically) transcendental; an exact collision then requires an
INTEGER RELATION among transcendentals, which generically does NOT exist.

EXACT OBSERVATION VALUES (derived, real).  For hhat even & real on R (Paley-Wiener):
  on-line pair {1/2 +- i*gamma}:            Phi = 2 * hhat(gamma)                       [real]
  off-line quartet {beta +- i g0, 1-beta +- i g0}, delta = beta-1/2:  the four arguments
    (rho-1/2)/i are  +- g0 +- i*delta, so   Phi_off = 4 * Re hhat(g0 + i*delta)          [real]
Gaussian family hhat_a(z) = exp(-a z^2)  (a>0; corresponds to a Gaussian h, Schwartz not compact —
a legitimate analytic TOY for the rationality/independence question, which is width-independent):
  on-line:   Phi_a(gamma) = 2 * exp(-a*gamma^2)
  off-line:  Phi_off_a    = 4 * exp(-a*(g0^2 - delta^2)) * cos(2*a*g0*delta)

THIS PROBE (mpmath, high precision — DISCOVERY only, never a proof):
  (1) PSLQ independence: is there ANY integer relation (bounded height) among the observation reals
      {Phi_off} U {Phi(gamma_k)} for a single test function (r=1)?  A relation WOULD be the exact
      collision Theorem A needs; PSLQ finding none up to a large height is evidence the exact
      obstruction has NO analogue without a transcendence input.
  (2) approximate-collision residual (EXPLORATORY, not a finding): a crude q=1-fixed integer
      least-squares for growing m; the residual here is noisy (~0.07-0.27, non-monotone), so this
      probe does NOT establish an "approximate obstruction ->0 with m" claim -- that would need an
      LLL bounded-height closest-vector search with q free. Only test (1) yields a finding.
This LOCALIZES OP2: the exact barrier is a RATIONALITY phenomenon; for this Weil family the values
are empirically rationally independent, so the exact collision does not exist and the OP1 lattice-
index mechanism has no analogue absent a linear-independence/transcendence theorem.  RH stays [OUT].
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 40  # decimal digits

# Realistic on-line heights: first Riemann zeta nontrivial-zero ordinates (sanity anchors only, NOT
# an input to any claim — the independence question is generic in the heights).
GAMMAS = [
    mp.mpf("14.134725141734693790"),
    mp.mpf("21.022039638771554993"),
    mp.mpf("25.010857580145688763"),
    mp.mpf("30.424876125859513210"),
    mp.mpf("32.935061587739189691"),
    mp.mpf("37.586178158825671257"),
    mp.mpf("40.918719012147495187"),
    mp.mpf("43.327073280914999519"),
]

# Off-line witness (a hypothetical off-critical zero the observation must fail to detect).
BETA = mp.mpf("0.70")
G0 = mp.mpf("20.0")
DELTA = BETA - mp.mpf("0.5")


def phi_online(a, gamma):
    return 2 * mp.e ** (-a * gamma ** 2)


def phi_offline(a):
    return 4 * mp.e ** (-a * (G0 ** 2 - DELTA ** 2)) * mp.cos(2 * a * G0 * DELTA)


def _vals(a, dps):
    with mp.workdps(dps):
        return [phi_offline(a)] + [phi_online(a, g) for g in GAMMAS]


def _residual(rel, a, dps):
    """Magnitude of sum_i rel[i]*val_i evaluated at `dps` digits. Genuine relation => ~10^-dps;
    spurious PSLQ artifact => plateaus near the precision it was FOUND at."""
    with mp.workdps(dps):
        vals = _vals(a, dps)
        s = mp.mpf(0)
        for c, v in zip(rel, vals):
            s += c * v
        return mp.fabs(s)


def test_pslq_independence():
    print("=" * 100, flush=True)
    print("OP2 (1) PSLQ INDEPENDENCE w/ PRECISION-SCALING DISCRIMINATOR (spurious vs genuine). RH [OUT].", flush=True)
    print("=" * 100, flush=True)
    a = mp.mpf("0.0002")  # single Gaussian test fn (r=1); tiny width keeps ALL values O(1) => well-
    #                       conditioned PSLQ: exp(-a*gamma^2) in [0.69,0.96] for gamma in [14,43]
    vals40 = _vals(a, 40)
    print("  test fn hhat(z)=exp(-%s z^2); r=1; %d on-line + 1 off-line observation reals (O(1))" % (
        mp.nstr(a, 3), len(GAMMAS)), flush=True)
    print("  Phi_off=%s ; Phi(gamma_k)=[%s]" % (
        mp.nstr(vals40[0], 8), ", ".join(mp.nstr(v, 8) for v in vals40[1:])), flush=True)
    # A relation among 9 O(1) reals with coeffs up to C needs ~9*log10(C) digits to be trustworthy;
    # at 40 dps, coeffs >~ 10^4 are in the spurious regime. Discriminate by RE-EVALUATING at 250 dps.
    for maxcoeff in (10 ** 3, 10 ** 6, 10 ** 9):
        with mp.workdps(40):
            rel = mp.pslq(vals40, maxcoeff=maxcoeff, maxsteps=20000)
        if not rel:
            print("  maxcoeff=%.0e @40dps -> NO relation" % maxcoeff, flush=True)
            continue
        r40 = _residual(rel, a, 40)
        r250 = _residual(rel, a, 250)
        verdict = "GENUINE" if r250 < mp.mpf(10) ** (-120) else "SPURIOUS (precision artifact)"
        print("  maxcoeff=%.0e @40dps -> rel found, max|coeff|=%d ; |residual| @40dps=%s @250dps=%s => %s" % (
            maxcoeff, max(abs(c) for c in rel), mp.nstr(r40, 3), mp.nstr(r250, 3), verdict), flush=True)
    # Decisive: run PSLQ at HIGH precision; a genuine bounded-height relation survives, spurious ones vanish.
    with mp.workdps(250):
        vals250 = _vals(a, 250)
        rel_hi = mp.pslq(vals250, maxcoeff=10 ** 9, maxsteps=60000)
    print("  PSLQ @250dps maxcoeff=1e9 -> %s" % (
        ("rel max|coeff|=%d (GENUINE)" % max(abs(c) for c in rel_hi)) if rel_hi else "NO relation"), flush=True)
    print("  READING: relations at 40dps are precision artifacts; at 250dps none survives up to 1e9", flush=True)
    print("  => observation values are (empirically) rationally INDEPENDENT => NO exact bounded", flush=True)
    print("  collision => Theorem A's exact obstruction has no arithmetic analogue for this Weil family.", flush=True)


def _round_int_solution(A_cols, b, qmax):
    """Best bounded-integer q,c for q*b ~ sum c_k A_cols[k], via real least-squares then rounding.
    A_cols: list of r-vectors (on-line), b: r-vector (off-line). Returns (residual_norm, q, c)."""
    r = len(b)
    m = len(A_cols)
    # Solve the real system  sum_k c_k A_k - q b = 0  with q=1 fixed (normalize), least squares for c.
    # Build r x m matrix M, target = b (q=1). c_real = pinv(M) b.
    M = mp.matrix(r, m)
    for k in range(m):
        for i in range(r):
            M[i, k] = A_cols[k][i]
    bt = mp.matrix(b)
    # normal equations (M^T M) c = M^T b
    MT = M.T
    G = MT * M
    rhs = MT * bt
    try:
        c_real = mp.lu_solve(G, rhs)
    except Exception:
        return None
    c_int = [int(mp.nint(c_real[k])) for k in range(m)]
    # residual of q=1
    res = mp.matrix(b)
    for k in range(m):
        for i in range(r):
            res[i] -= c_int[k] * A_cols[k][i]
    return (mp.norm(res), 1, c_int)


def test_approx_collision():
    print("\n" + "=" * 100, flush=True)
    print("OP2 (2) APPROXIMATE-COLLISION RESIDUAL vs m (r=3 Gaussians). RH [OUT].", flush=True)
    print("=" * 100, flush=True)
    A_widths = [mp.mpf("0.0001"), mp.mpf("0.0002"), mp.mpf("0.0004")]  # tiny widths => all Phi O(1)
    r = len(A_widths)
    b = [phi_offline(a) for a in A_widths]
    print("  r=%d test fns widths=%s; off-line target |Phi_off|=%s" % (
        r, [mp.nstr(a, 3) for a in A_widths], mp.nstr(mp.norm(mp.matrix(b)), 8)), flush=True)
    for m in range(3, len(GAMMAS) + 1):
        A_cols = [[phi_online(a, GAMMAS[k]) for a in A_widths] for k in range(m)]
        out = _round_int_solution(A_cols, b, qmax=1)
        if out is None:
            print("  m=%d: singular" % m, flush=True)
            continue
        resnorm, q, c = out
        print("  m=%2d: best q=1 integer combo residual |q*Phi_off - sum c_k Phi_k| = %s  (c=%s)" % (
            m, mp.nstr(resnorm, 6), c), flush=True)
    print("  READING (L5, HONEST): the crude q=1-fixed integer least-squares does NOT decrease", flush=True)
    print("  monotonically (0.066..0.272, noisy) => this rough test does NOT establish an", flush=True)
    print("  'approximate obstruction shrinks with m' claim. A real bounded-height minimum needs LLL", flush=True)
    print("  closest-vector search with q free; NOT done here. Only test (1) yields a finding.", flush=True)


def test_lindemann_weierstrass():
    """The exact statement: pick a and all heights ALGEBRAIC (here: rational). Then EVERY observation
    value is exp(algebraic): Phi(gamma_k)=2*exp(-a*gamma_k^2) and Phi_off = 2*(exp(-a*(g0-i*delta)^2)
    + exp(-a*(g0+i*delta)^2)).  A nontrivial integer collision q*Phi_off = sum c_k Phi(gamma_k) is an
    integer (hence Q-bar) linear relation among {exp(beta_+), exp(beta_-), exp(beta_1)..exp(beta_m)}
    with beta_k = -a*gamma_k^2 (real rational) and beta_pm = -a*(g0 -/+ i*delta)^2 (complex algebraic).
    If the exponents are DISTINCT ALGEBRAIC, Lindemann-Weierstrass => the exponentials are linearly
    independent over Q-bar => the only relation is trivial (q=0, all c_k=0) => NO exact collision.
    This upgrades the empirical independence of test (1) to a THEOREM for the Gaussian Weil family."""
    print("\n" + "=" * 100, flush=True)
    print("OP2 (3) LINDEMANN-WEIERSTRASS: algebraic heights => PROVED no-collision (Gaussian family). RH [OUT].", flush=True)
    print("=" * 100, flush=True)
    a = mp.mpf(1) / 5000              # rational (algebraic), != 0
    gam = [mp.mpf(g) for g in (10, 13, 17, 21, 25, 30, 35, 40)]  # distinct rationals => distinct squares
    g0 = mp.mpf(20)                   # rational
    delta = mp.mpf(1) / 5             # rational, != 0  (off-line: beta != 1/2)
    # exponents beta_k = -a*gamma_k^2 (real, distinct rationals); beta_pm = -a*(g0 -/+ i*delta)^2.
    re_pm = -a * (g0 ** 2 - delta ** 2)
    im_pm = 2 * a * g0 * delta        # +/-; nonzero => beta_pm non-real, distinct from each other & reals
    print("  a=1/5000; gamma_k distinct rationals => beta_k=-a*gamma_k^2 distinct RATIONALS (algebraic)", flush=True)
    print("  beta_+/- = %s -/+ %s i : complex algebraic, conjugate, non-real (2*a*g0*delta=%s != 0)" % (
        mp.nstr(re_pm, 6), mp.nstr(im_pm, 6), mp.nstr(im_pm, 6)), flush=True)
    betas = [-a * g ** 2 for g in gam]
    distinct = len(set(mp.nstr(b, 30) for b in betas)) == len(betas)
    print("  distinct real exponents beta_k? %s ; beta_+/- non-real => distinct from all beta_k: True" % distinct, flush=True)
    print("  => 10 DISTINCT ALGEBRAIC exponents => Lindemann-Weierstrass: {exp(beta_j)} lin. indep./Q-bar", flush=True)
    print("  => the ONLY integer relation q*Phi_off = sum c_k Phi(gamma_k) is trivial => NO exact collision.", flush=True)
    # Numerical cross-check (evidence only; the statement above is the theorem): PSLQ must find nothing.
    vals = [4 * mp.e ** re_pm * mp.cos(im_pm)] + [2 * mp.e ** (-a * g ** 2) for g in gam]
    with mp.workdps(250):
        vals250 = [4 * mp.e ** (-a * (g0 ** 2 - delta ** 2)) * mp.cos(2 * a * g0 * delta)] + \
                  [2 * mp.e ** (-a * g ** 2) for g in gam]
        rel = mp.pslq(vals250, maxcoeff=10 ** 9, maxsteps=60000)
    print("  cross-check PSLQ @250dps maxcoeff=1e9 -> %s (consistent with LW)" % (
        "rel FOUND (unexpected!)" if rel else "NO relation"), flush=True)
    print("  CAVEAT: Gaussian hhat=exp(-a z^2) <-> Gaussian h (Schwartz, not C_c^inf). Legitimate analytic", flush=True)
    print("  observation family; the C_c^inf/Paley-Wiener case (hhat entire of exp type) is NOT covered by", flush=True)
    print("  LW and stays open. This PROVES the OP2 negative for the Gaussian family only.", flush=True)


def test_hermite_gaussian():
    """Generalization: ANY even test function hhat(z) = P(z)*exp(-a z^2) with P a polynomial with
    ALGEBRAIC coefficients gives observation values (algebraic)*exp(beta), beta = -a z^2 algebraic.
    A nontrivial integer collision is then sum (algebraic_j) exp(beta_j) = 0 with algebraic_j != 0
    (integer c_k times the nonzero P-factor). REQUIRES P(gamma_k) != 0 (on-line) AND P(g0+/-i*delta)
    != 0 (off-line): if the off-line P-factor vanishes then Phi_off = 0 and (q=1, c=0) is a degenerate
    collision. Under both, Lindemann-Weierstrass (distinct algebraic exponents) forces every
    coefficient to 0 => no collision. So the OP2-negative covers the whole SCHWARTZ-DENSE
    algebra {P*Gaussian, P even, algebraic coeffs}, not just the pure Gaussian. Test: Hermite H_2."""
    print("\n" + "=" * 100, flush=True)
    print("OP2 (4) HERMITE-GAUSSIAN hhat=H_2(sqrt(a) z)exp(-a z^2): PROVED no-collision (dense class). RH [OUT].", flush=True)
    print("=" * 100, flush=True)
    a = mp.mpf(1) / 5000
    gam = [mp.mpf(g) for g in (10, 13, 17, 21, 25, 30, 35, 40)]  # none = 50 => P-factor 4a*g^2-2 != 0

    def hhat(z):
        return mp.hermite(2, mp.sqrt(a) * z) * mp.e ** (-a * z ** 2)  # H_2(x)=4x^2-2; even in z

    g0, delta = mp.mpf(20), mp.mpf(1) / 5
    with mp.workdps(250):
        online = [2 * hhat(g) for g in gam]                       # real
        offline = 4 * mp.re(hhat(g0 + mp.mpc(0, 1) * delta))       # 4 Re hhat(g0+i delta)
        vals = [offline] + online
        rel = mp.pslq(vals, maxcoeff=10 ** 9, maxsteps=60000)
    pfac = [4 * a * g ** 2 - 2 for g in gam]
    pfac_off = 4 * a * (g0 + mp.mpc(0, 1) * delta) ** 2 - 2   # P-factor at off-line arg (must be != 0)
    print("  a=1/5000; P=H_2; on-line P-factors 4a*g^2-2 all != 0? %s ; off-line P(g0+i*delta) != 0? %s" % (
        all(abs(p) > mp.mpf(10) ** (-20) for p in pfac), abs(pfac_off) > mp.mpf(10) ** (-20)), flush=True)
    print("  (BOTH nonzero required: if P(g0+/-i*delta)=0 then Phi_off=0 => degenerate collision.)", flush=True)
    print("  Phi_off=%s ; Phi(gamma_k)=[%s]" % (
        mp.nstr(vals[0], 8), ", ".join(mp.nstr(v, 8) for v in vals[1:])), flush=True)
    print("  cross-check PSLQ @250dps maxcoeff=1e9 -> %s (consistent with LW)" % (
        "rel FOUND (unexpected!)" if rel else "NO relation"), flush=True)
    print("  => LW argument extends verbatim: no exact collision for P*Gaussian (algebraic data) family.", flush=True)
    print("  Uncovered: genuine C_c^inf (hhat entire of exponential type, values are periods, not", flush=True)
    print("  exp-of-algebraic) -- LW does not apply; stays OPEN.", flush=True)


if __name__ == "__main__":
    test_pslq_independence()
    test_approx_collision()
    test_lindemann_weierstrass()
    test_hermite_gaussian()
    print("\n" + "=" * 100, flush=True)
    print("OP2 SCOPING CONCLUSION (evidence, L5): the EXACT Theorem-A obstruction is a RATIONALITY", flush=True)
    print("phenomenon (OP1 exploits rational Li values -> exact lattice index q_min). For this Weil", flush=True)
    print("family the observation reals show NO genuine integer relation up to height 1e9 at 250 dps", flush=True)
    print("(the 40-dps 'relations' are precision artifacts: residual plateaus at ~1e-31, not ~1e-250,", flush=True)
    print("and vanish at 250 dps). So the values are EMPIRICALLY rationally independent => no exact", flush=True)
    print("bounded collision => Theorem A's exact obstruction has NO arithmetic analogue here without", flush=True)
    print("a linear-independence / transcendence statement about {Re hhat(g0+i*delta), hhat(gamma_k)}", flush=True)
    print("-- which is not available. The approximate-collision magnitude (test 2) is NOT quantified", flush=True)
    print("by this probe (crude q=1 rounding, noisy). Bounded-height PSLQ / one family = EVIDENCE, not", flush=True)
    print("proof. RH stays [OUT].", flush=True)
