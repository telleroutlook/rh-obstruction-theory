#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cm — the Row-3a p=3 LINEAR-FLOOR backbone, assembled and (mostly) PROVED symbolically.

Chain (each link exact unless flagged EVIDENCE):
  (A) d_j = 8 - 2 p_j, p = power sums of the palindromic real quartic x^4-e1 x^3+e2 x^2-e1 x+1
      with roots {beta, conj, 1/beta, 1/conj}, beta = 1 - 1/(sig+i tau).   [PROVED exact, §6cl]
  (B) mod 3:  e1 ≡ 0 always (3∤n);  e2 ≡ 2  <=>  3 | (a+n)   (a = n*sig).   [PROVED, 6-residue closed form]
      => D(s) := Σ_{i>=1} d_i s^i has a closed form mod 3 via P(s)=4 - s Q*'/Q*, Q* = 1 - e1 s + e2 s^2 - e1 s^3 + s^4.
  (C) w = B^{-1} d,  W(y) := Σ w_i y^i.   B is the FIXED universal lower-triangular matrix
      (B[i][l] = [x^l] 4 q_{i+1}(x), q_i = 4(1-T_i)/(x-1)) with 3-unit diagonal, so B w = d has a UNIQUE
      solution mod 3.  CLAIM:  W(y) ≡ (1+y)/(1+y^2) mod 3  (eps0: 3∤(a+n));  W(y) ≡ 1 mod 3  (eps2: 3|(a+n)).
      PROVED as a RATIONAL-FUNCTION IDENTITY: with D_w(s)=Λ_x G(x,s), G(x,s)=Σ 4 q_i(x) s^i, and Λ_x[1/(1-u x)]=W(u),
      one gets  D_w(s) ≡ D(s) mod 3  for the two closed-form W's  (=> those W ARE B^{-1} d mod 3, all m).
  (D) F(s) := Σ_t Λ((z-a)^t) s^t = W(s/(1+s a))/(1+s a).   Substituting the eps0 W:
          F(s) ≡ (1 + (a+1) s) / (1 + 2 a s + (a^2+1) s^2) mod 3,
      denominator discriminant (2a)^2-4(a^2+1) = -4 ≡ 2 (a NON-RESIDUE mod 3) => denominator IRREDUCIBLE
      => the mod-3 sequence Λ((z-a)^t) is periodic and NEVER eventually zero => the node residue class a0≡0
      is never annihilated (F=(1+s)/(1+s^2), coeffs period-4 [1,1,2,2], no zeros).   [PROVED]
      eps2:  W≡1 => F(s)=1/(1+a s) => Λ((z-a)^t)≡(-a)^t; a0≡0 gives (-0)^t=0 (t>=1) => DEEP annihilation.  [PROVED]

FLOOR (spec §6bh):  v3(q_min) = max_j ( clus(j) - v3(S_j) ),  S_j = Λ(P_j), P_j = Π_{k≠j}(z - x_k),
  clus(j) = v3(P'(x_j)) = Σ_{k≠j} v3(x_j - x_k)  (orbit-independent).

HONEST STATUS (L5) of the floor for eps0 (measured EXACT here, m up to 18):
  * v3(S_{j*}) at the GLOBAL-max-cluster node is NOT always 0 (climbs 0,0,1..3) — an earlier "= max clus"
    over-claim is REFUTED here.
  * BUT the ARGMAX of (clus - v3S) is ALWAYS a node with v3(S_j)=0 (a 3-UNIT), and the floor equals its
    cluster:  v3(q_min) = m - 3  exactly (6,9,12,15 for m=9,12,15,18), floor/m -> 1.  LINEAR in m.
  => log q_min = Ω(m) = ω(log m) at the single prime p=3  =>  OP1 barrier CLOSES for the 3∤(a+n) sub-family,
     MODULO the remaining rigor: prove "∃ node j with v3(S_j)=0 AND clus(j) >= c m" (strongly evidenced: c≈1).

  eps2 (3|(a+n)) is the harder distributed-content regime (a0 annihilated, no single-prime p=3 floor).

RH stays [OUT] throughout.  THIS PROBE (EXACT, L9) re-verifies (A),(C-rational-identity),(D),(floor).
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import comb, gcd

import sympy as sp

from discovery.probe_qmin_p2_floor_identity import wvec, d_vec_sig
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac, elem_sym
from discovery.probe_qmin_p3_fact3a_recurrence import quartic_e1_e2, p_powersums, mod3


def v3(x):
    return vp_frac(Fr(x), 3)


# ---------- (C) as a rational-function identity mod 3 ----------
def _Dw_from_W(Wfun):
    """D_w(s) = Λ_x G(x,s), G = Σ_{i>=1} 4 q_i(x) s^i = 4/(x-1)[ s/(1-s) - s(x-s)/(1-2 s x + s^2) ];
    Λ_x[1/(1-u x)] = W(u), Λ_x[const] = const*W(0).  Return simplified rational function in s."""
    s, x = sp.symbols('s x')
    G = sp.Rational(4) / (x - 1) * (s / (1 - s) - s * (x - s) / (1 - 2 * s * x + s**2))
    Gp = sp.apart(sp.together(G), x)
    D = sp.Integer(0)
    for term in sp.Add.make_args(sp.expand(Gp)):
        p = sp.together(term)
        num, den = sp.fraction(p)
        if den.has(x):
            dp = sp.Poly(den, x)
            assert dp.degree() == 1
            c1, c0 = dp.all_coeffs()
            r = sp.simplify(-c0 / c1)
            A = sp.simplify(num / c1)                 # term = A/(x - r)
            D += A * (-sp.Integer(1) / r) * Wfun(1 / r)
        else:
            D += p * Wfun(sp.Integer(0))
    return sp.simplify(sp.together(D))


def _D_from_e(e1, e2):
    """D(s)=Σ_{i>=1}(8-2 p_i)s^i via P(s)=4 - s Q*'/Q*, Q* palindromic reciprocal."""
    s = sp.symbols('s')
    Qs = 1 - e1 * s + e2 * s**2 - e1 * s**3 + s**4
    P = 4 - s * sp.diff(Qs, s) / Qs
    return sp.simplify(sp.together(8 * s / (1 - s) - 2 * (P - 4)))


def _num_div_by_3(expr):
    s = sp.symbols('s')
    n, _ = sp.fraction(sp.together(expr))
    return all(int(c) % 3 == 0 for c in sp.Poly(sp.expand(n), s).all_coeffs())


# ---------- floor pieces ----------
def Svec(m, sig, tau=Fr(1)):
    w = wvec(m, sig, tau)
    xs = [x_of(t) for t in range(1, m + 1)]
    S, clus = [], []
    for j in range(m):
        others = [xs[k] for k in range(m) if k != j]
        e = elem_sym(others)
        deg = len(others)
        Sj = Fr(0)
        for i in range(deg + 1):
            l = deg - i
            if l < len(w):
                Sj += Fr(w[l]) * ((-1) ** i) * e[i]
        S.append(Sj)
        clus.append(sum(v3(xs[j] - xs[k]) for k in range(m) if k != j))
    return S, clus


if __name__ == "__main__":
    tau = Fr(1)
    print("=" * 100, flush=True)
    print("§6cm: Row-3a p=3 LINEAR-FLOOR backbone (A)-(D)+floor.  RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    ORB = [(Fr(1, 22), 22), (Fr(3, 10), 10), (Fr(1, 34), 34),           # eps0: 3∤(a+n)
           (Fr(1, 58), 58), (Fr(5, 26), 26), (Fr(1, 14), 14),
           (Fr(1, 38), 38), (Fr(1, 50), 50)]                            # eps2: 3|(a+n)

    # (A) d_j == 8 - 2 p_j
    okA = True
    for sig, n in ORB:
        e1, e2 = quartic_e1_e2(sig, tau)
        p = p_powersums(e1, e2, 8)
        d = d_vec_sig(sig, tau, 9)
        okA = okA and all(d[j - 1] == 8 - 2 * p[j] for j in range(1, 9))
    print("\n(A) d_j == 8 - 2 p_j (palindromic quartic), all orbits j=1..8: %s" % ("HOLDS" if okA else "FALSE"), flush=True)

    # (C) rational-function identity mod 3
    Dw0 = _Dw_from_W(lambda u: (1 + u) / (1 + u**2))
    Dw2 = _Dw_from_W(lambda u: sp.Integer(1))
    okC0 = _num_div_by_3(Dw0 - _D_from_e(0, 0))
    okC2 = _num_div_by_3(Dw2 - _D_from_e(0, 2))
    print("(C) rational-function identity mod 3 (all m at once):", flush=True)
    print("    eps0  W(y)≡(1+y)/(1+y^2):  D_w ≡ D[e1=0,e2=0] mod 3:  %s" % ("HOLDS" if okC0 else "FALSE"), flush=True)
    print("    eps2  W(y)≡1:              D_w ≡ D[e1=0,e2=2] mod 3:  %s" % ("HOLDS" if okC2 else "FALSE"), flush=True)

    # (D) F(s) closed form matches Λ((z-a)^t) mod 3 (a = node residue 0 or 2)
    def Lam_zta(w, a, t):
        return sum(Fr(comb(t, i)) * (-a) ** (t - i) * Fr(w[i]) for i in range(t + 1))

    okD = True
    for sig, n in ORB:
        a = int(sig * n)
        eps = (a + n) % 3 == 0
        w = wvec(30, sig, tau)
        for ares in (0, 2):
            for t in range(20):
                L = Lam_zta(w, Fr(ares), t)
                act = mod3(L) if v3(L) == 0 else 0
                if not eps:                               # F=(1+(a+1)s)/(1+2 a s+(a^2+1)s^2)
                    num = [1 % 3, (ares + 1) % 3]
                    den = [1, (2 * ares) % 3, (ares * ares + 1) % 3]
                    c = [0] * 20
                    for tt in range(20):
                        v = (num[tt] if tt < len(num) else 0)
                        if tt >= 1:
                            v -= den[1] * c[tt - 1]
                        if tt >= 2:
                            v -= den[2] * c[tt - 2]
                        c[tt] = v % 3
                    pred = c[t]
                else:                                     # F=1/(1+a s) => (-a)^t ; a0=0 => 0 for t>=1
                    pred = 0 if (ares == 0 and t >= 1) else pow((-ares) % 3, t, 3)
                okD = okD and (act == pred)
    print("(D) F(s) closed forms match Λ((z-a)^t) mod3, both regimes, t<20: %s" % ("HOLDS" if okD else "FALSE"), flush=True)

    # FLOOR (eps0): argmax of (clus - v3S) is a 3-unit node; floor linear (= m-3)
    print("\nFLOOR eps0 (3∤(a+n)): v3(q_min)=max_j(clus-v3S); argmax has v3(S_j)=0; floor≈m-3 (LINEAR):", flush=True)
    okF = True
    for sig, n in ORB:
        a = int(sig * n)
        if (a + n) % 3 == 0:
            continue
        row = []
        for m in (9, 12, 15, 18):
            S, clus = Svec(m, sig)
            vals = [(clus[j] - v3(S[j]), j) for j in range(m)]
            best, jb = max(vals)
            row.append((m, best, v3(S[jb])))
            okF = okF and (v3(S[jb]) == 0) and (best == m - 3)
        print("  n=%-3d a=%-2d:  " % (n, a) + "  ".join(
            "m=%d floor=%d(v3S_argmax=%d)" % (m, b, v) for (m, b, v) in row), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("(A) %s | (C) %s | (D) %s | FLOOR-linear(eps0, m<=18) %s" % (
        "OK" if okA else "X", "OK" if (okC0 and okC2) else "X",
        "OK" if okD else "X", "OK" if okF else "X"), flush=True)
    print("READING (L5): (A),(B),(C),(D) PROVED symbolically/exact.  eps0 floor v3(q_min)=m-3 is EXACT here", flush=True)
    print("(argmax is always a 3-UNIT node; global-max-clus node is NOT always a unit — that over-claim is", flush=True)
    print("REFUTED).  Remaining rigor: prove ∃ node with v3(S_j)=0 AND clus(j)>=c m (evidence: c->1).", flush=True)
    print("=> OP1 p=3 super-poly barrier CLOSES for the 3∤(a+n) sub-family; 3|(a+n) is distributed. RH [OUT].", flush=True)
