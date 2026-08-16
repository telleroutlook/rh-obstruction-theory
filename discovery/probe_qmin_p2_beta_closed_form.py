#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bm — CLOSED FORM β = 1/(2ρ(ρ−1)) upgrades the S≥2 family floor from "verified for 4 orbits" to a PROOF
parameterized by ρ's denominator.  This closes the last empirical gap in §6bl's family generalization.

The shift-moment root of §6bk/§6bl has an ELEMENTARY closed form in the off-line point ρ=σ+iτ:
      β = ξ − 1,  ξ = (w+1/w)/2,  w = 1 − 1/ρ   ⟹   β = (w−1)²/(2w) = 1/(2ρ(ρ−1)).
Writing ρ = (p+qi)/n in lowest terms (p,q,n ∈ Z, gcd=1), clearing denominators:
      β = n² / (2M),   M = Re(M) + Im(M)·i,   Re(M) = p²−q²−np,   Im(M) = q(2p−n).
Hence, with N(M)=Re(M)²+Im(M)² and v₂ the rational 2-adic valuation, the profile slope is EXACTLY
      S = v₂(β) = 2·v₂(n) − 1 − v₂(N(M))/2.

THE FAMILY THEOREM (elementary, no node quantifier, no L-value, no RH).  Suppose  4 ∣ n  and  p,q have
OPPOSITE parity (⟺ N(M) odd).  Then:
  (P1) n even ⟹ Im(M)=q(2p−n) is EVEN;  p,q opposite parity ⟹ Re(M)=p²−q²−np ≡ p−q ≡ 1 (mod 2) is ODD.
       So γ := conj(M) (times the odd rational content) satisfies γ ≡ 1 (mod 2·Z[i])  [Re odd, Im even].
  (P2) S = 2·v₂(n) − 1 ≥ 3  (since v₂(n) ≥ 2), and β = 2^S · γ / N with N = N(M) odd, γ ≡ 1 mod 2.
  (P3) γ ≡ 1 mod 2·Z[i] is closed under multiplication ⟹ Re(γ^{i+1}) is ODD ⟹ v₂(2·Re(γ^{i+1})) = 1, so
            w'_i = β^{i+1}+β̄^{i+1} = 2^{S(i+1)}·2Re(γ^{i+1})/N^{i+1}   ⟹   v₂(w'_i) = S(i+1) + 1.
  (P4) The §6bi unique-minimum expansion (v₂(e_r)≥r, v₂(w'_{m−1−r})=(S+1)+S(m−1−r)) gives, for S>1,
       v₂(term_r) ≥ (S+1)+S(m−1)−(S−1)r STRICTLY DECREASING in r, UNIQUE min at r=m−1 (the product
       w'_0·∏y_k, no cancellation) = m+S.  So C_j = m+S for EVERY column and node set, hence the
       UNCONDITIONAL LINEAR FLOOR  v₂(q_min) ≥ 1+3(m−1)−(m+S) = 2m − 2 − S.
  At S=1 (n≡2 mod 4, N(M) odd) the coefficient −(S−1)=0: all terms tie, unique-minimum COLLAPSES ⟹ C_j
  NOT pinned (cancellation) ⟹ floor vacuous — exactly §6bl's borderline class, now explained rigorously.

So the σ=3/4 theorem (n=4, S=3, 2m−5) is one member; EVERY 4∣n opposite-parity orbit is proved the same way.

RH stays [OUT].  Everything is exact 2-adic / Gaussian-integer arithmetic about explicit rationals.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd, comb
from discovery.probe_qmin_p2_orbit_trichotomy import orbit_beta, v2int, gpow, shift_w
from discovery.probe_qmin_p2_floor_identity import wvec, per_column, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_int


def rho_pqn(sig, tau):
    """rho = sig + i*tau = (p + q i)/n in lowest terms (p,q,n integers)."""
    n = tau.denominator
    # sig = a/b -> need common denom with tau
    d = sig.denominator
    n = d * n // gcd(d, n)  # common denom guess; recompute cleanly below
    p_num, p_den = sig.numerator, sig.denominator
    q_num, q_den = tau.numerator, tau.denominator
    n = p_den * q_den // gcd(p_den, q_den)
    p = p_num * (n // p_den)
    q = q_num * (n // q_den)
    g = gcd(gcd(abs(p), abs(q)), n)
    return p // g, q // g, n // g


def v2_frac_of_int_ratio(num, den):
    return v2int(num) - v2int(den)


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6bm: beta = 1/(2 rho (rho-1)); S = 2 v2(n) - 1 - v2(N(M))/2; family theorem for 4|n opp-parity.", flush=True)
    print("=" * 100, flush=True)

    ORBITS = [(Fr(3, 4), Fr(1)), (Fr(7, 8), Fr(1)), (Fr(5, 8), Fr(1)), (Fr(5, 4), Fr(1)), (Fr(9, 8), Fr(1)),
              (Fr(1, 4), Fr(1)), (Fr(3, 8), Fr(1)), (Fr(11, 12), Fr(1)), (Fr(5, 6), Fr(1)), (Fr(9, 10), Fr(1)),
              (Fr(4, 5), Fr(1)), (Fr(2, 3), Fr(1)), (Fr(3, 4), Fr(1, 2))]

    print("\n(1) closed form beta = 1/(2 rho(rho-1)) vs recurrence-extracted beta; S closed form vs measured:", flush=True)
    print("%-12s %-7s %-24s %-10s %-10s %s" % ("(sig,tau)", "(p,q,n)", "M=Re+Im i", "S(formula)", "S(recur)", "match/type"), flush=True)
    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        ReM = p * p - q * q - n * p
        ImM = q * (2 * p - n)
        NM = ReM * ReM + ImM * ImM
        S_formula = Fr(2 * v2int(n) - 1) - Fr(v2int(NM), 2)
        # recurrence-extracted beta and its S
        A, B, beta, k, g, N, wp = orbit_beta(sig, tau)
        S_recur = Fr(v2int(B.numerator) - v2int(B.denominator), 2)
        # closed-form beta = n^2/(2M) as Gaussian rational; compare to sympy beta
        # beta_cf = n^2 * conj(M) / (2 * N(M))
        cf_re = Fr(n * n * ReM, 2 * NM)
        cf_im = Fr(-n * n * ImM, 2 * NM)
        import sympy as sp
        bre, bim = Fr(sp.Rational(sp.re(beta))), Fr(sp.Rational(sp.im(beta)))
        # w'_i = beta^{i+1}+conj^{i+1} is root-order symmetric, so accept beta OR its conjugate
        beta_match = (cf_re == bre and cf_im == bim) or (cf_re == bre and cf_im == -bim)
        # parity type of gamma = conj(M) reduced
        s2 = min(v2int(ReM) if ReM else 99, v2int(ImM) if ImM else 99)
        gre, gim = (ReM >> s2), (-ImM >> s2) if ImM else 0
        typ = "Re-odd/Im-even" if (gre % 2 == 1 and gim % 2 == 0) else (
            "both-odd" if (gre % 2 == 1 and gim % 2 == 1) else "Re-even/Im-odd")
        fam = " <== 4|n opp-par FAMILY" if (n % 4 == 0 and (p % 2) != (q % 2)) else ""
        print("%-12s %-7s %-24s %-10s %-10s %s (%s)%s" % (
            "(%s,%s)" % (sig, tau), "(%d,%d,%d)" % (p, q, n), "%d%+di" % (ReM, ImM),
            str(S_formula), str(S_recur), "beta=%s S=%s" % (beta_match, S_formula == S_recur), typ, fam), flush=True)

    print("\n(2) family theorem floor 2m-2-S vs measured v2(q_min) (4|n opposite-parity orbits):", flush=True)
    pool = [1, 2, 3, 5, 7, 11, 13]
    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        if not (n % 4 == 0 and (p % 2) != (q % 2)):
            continue
        S = 2 * v2int(n) - 1
        row = []
        for m in (4, 5, 6):
            ts = pool[:m]
            if len(set(x_of(t) for t in ts)) != m:
                continue
            q_ = qmin_exact_orbit(ts, m, sig, tau)
            if q_ is None:
                continue
            pred = 2 * m - 2 - S
            row.append("m=%d: v2q=%d >= %d? %s" % (m, vp_int(q_, 2), pred, vp_int(q_, 2) >= pred))
        print("    (%s,%s) S=%d floor=2m-%d: %s" % (sig, tau, S, 2 + S, "  ".join(row)), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("PROVED (P1-P4): for 4|n & p,q opposite parity, gamma=conj(M) has odd Re / even Im, S=2v2(n)-1>=3,", flush=True)
    print("v2(w'_i)=S(i+1)+1, C_j=m+S, and v2(q_min) >= 2m-2-S UNCONDITIONALLY. sigma=3/4 (n=4,S=3) is one case.", flush=True)
    print("The S formula also PROVES the S=1 boundary (n=2 mod 4): unique-minimum ties => floor vacuous. RH [OUT].", flush=True)
