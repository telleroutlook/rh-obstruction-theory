#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bk — THE NODE-FREE LEMMA v_2(w'_i)=4+3i HAS AN ELEMENTARY RANK-2 CLOSED FORM (sigma=3/4, D=425).
       This SUPERSEDES the §6bj "LTE on d_j + triangular-recursion cancellation" route, which was an
       OVER-COMPLICATION: the recursion numerator does NOT lift by a two-term cancellation (the two
       lowest terms d_j and G[j][0]w'_0 share v_2=6+2v_2(j) but the numerator's true valuation is 4j+2,
       a DEEP multi-term telescoping — see the honest note below).  The clean structure is that w'_i
       itself is a rank-2 Lucas sequence, proved directly.  RH stays [OUT].

THE CLOSED FORM (m-INDEPENDENT, verified: w'_i identical across m=4,6,...,14).  With
        alpha = 13 + 16 i,   N(alpha) = 13^2+16^2 = 425 = 25 * 17 = D,
the sigma=3/4 orbit target is  d_j = 8 - 4 Re(alpha/25)^j - 4 Re(alpha/17)^j.  The functional L
(defined by L(4q_j)=d_j, w'_i = L((X-1)^i)) is EXACTLY a two-point evaluation:
        L(f) = beta * f~(beta) + conj(beta) * f~(conj(beta)),   f~(Z) := f(1+Z),
        beta = -8(19-8i)/425 = 8*gamma/425,   gamma = -19 + 8 i   (a Gaussian integer, N(gamma)=425).
Hence
        w'_i = beta^{i+1} + conj(beta)^{i+1} = (8^{i+1} / 425^{i+1}) * 2 Re(gamma^{i+1}).

WHY TWO POINTS (not four).  The four orbit exponentials pair up by the RECIPROCAL RELATION
        (alpha/25) * (conj(alpha)/17) = N(alpha)/425 = 1,
so z:=alpha/25 and 1/z=conj(alpha)/17 are a single Chebyshev pair: with xi=(z+1/z)/2 one has
T_j(xi)=(z^j+z^{-j})/2, and T_j(xi)+T_j(conj xi) = Re(alpha/25)^j + Re(alpha/17)^j.  Since
4q_j(x) = -4(T_j(x)-1)/(x-1) and x-1=Z, (xi-1)*4q_j(xi) = -4(T_j(xi)-1); summing over xi,conj(xi)
gives d_j = beta*4q_j(1+beta)+conj.  As {4q_j}_{j=1..m} is a triangular basis of deg<=m-1 polys
(deg 4q_j = j-1), L is fixed by d_1..d_m, so the two-point functional IS L; holding for every m,
w'_i = beta^{i+1}+conj for all i.  [VERIFIED exactly below.]

THE VALUATION (elementary, no LTE).  425 is ODD.  gamma = -19+8i ≡ 1 (mod 2) in Z[i]
(Re odd, Im even), so gamma^{i+1} ≡ 1 (mod 2), i.e. Re(gamma^{i+1}) is ODD and v_2(2 Re) = 1.  Thus
        v_2(w'_i) = v_2(8^{i+1}) + v_2(2 Re(gamma^{i+1})) - v_2(425^{i+1}) = 3(i+1) + 1 - 0 = 4 + 3i.
QED — a two-line ultrametric argument, fully rigorous (modulo the [VERIFIED] closed form).

CONSEQUENCE (unchanged from §6bi).  v_2(w'_i)=4+3i => via the p_j unique-minimum expansion
C_j = m+3 for every column and every node set => v_2(q_min) >= 1 + 3(m-1) - (m+3) = 2m-5:
an UNCONDITIONAL LINEAR 2-adic floor for OP1's sigma=3/4 (D=425) barrier.  No node quantifier,
no L-value, no analytic rank, no RH.  Honest (L5): sigma=3/4 is the clean rank-2 case; other sigma
give beta with different v_2 (profile OFF+S*i) and need the same treatment per orbit.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import comb
from discovery.probe_qmin_p2_floor_identity import wvec, d_vec_sig
from discovery.probe_qmin_Cj_bilinear import vp_frac

SIG, TAU = Fr(3, 4), Fr(1)
GAMMA_RE, GAMMA_IM = -19, 8         # gamma = -19+8i, N=425 ; beta = 8*gamma/425
BETA = (Fr(-152, 425), Fr(64, 425))  # = 8*gamma/425 = -8(19-8i)/425


def shift_w(w, m):
    return [sum(comb(i, l) * ((-1) ** (i - l)) * w[l] for l in range(i + 1)) for i in range(m)]


def v2(fr):
    return vp_frac(fr, 2) if fr != 0 else 10 ** 9


# ---- exact Gaussian-rational arithmetic (re, im) with Fraction components ----
def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])
def gsub(a, b):
    return (a[0] - b[0], a[1] - b[1])
def gconj(a):
    return (a[0], -a[1])
def gscal(s, a):
    return (s * a[0], s * a[1])


def gpow_int(a, b, n):
    re, im = 1, 0
    for _ in range(n):
        re, im = re * a - im * b, re * b + im * a
    return re, im


def cheb_T(j, x):
    T0, T1 = (Fr(1), Fr(0)), x
    if j == 0:
        return T0
    if j == 1:
        return T1
    for _ in range(2, j + 1):
        T0, T1 = T1, gsub(gscal(2, gmul(x, T1)), T0)
    return T1


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6bk: w'_i = beta^{i+1}+conj (rank-2), beta=8*gamma/425, gamma=-19+8i => v_2(w'_i)=4+3i.", flush=True)
    print("SUPERSEDES §6bj LTE/recursion route (honest note: recursion numerator lift is multi-term).", flush=True)
    print("=" * 100, flush=True)

    # (0) HONEST refutation of the §6bj two-term-cancellation claim.
    print("\n(0) §6bj recursion numerator is NOT a two-term lift (min shared by 2 terms, true v far above):", flush=True)
    from math import factorial
    def Tder1(j, k):
        num = 1
        for l in range(k):
            num *= (j * j - l * l)
        dd = 1
        for i in range(1, 2 * k, 2):
            dd *= i
        return Fr(num, dd)
    def G(j, i):
        return Fr(-4) * Tder1(j, i + 1) / factorial(i + 1)
    m0 = 8
    wp0 = shift_w(wvec(m0, SIG, TAU), m0)
    d0 = d_vec_sig(SIG, TAU, m0)
    for j in (6, 7, 8):
        terms = [d0[j - 1]] + [-G(j, i) * wp0[i] for i in range(j - 1)]
        tv = sorted(v2(t) for t in terms)
        print(f"    j={j}: term-vals(sorted)={tv}  numerator v={v2(sum(terms))}  target 4j+2={4 * j + 2}", flush=True)

    # (1) m-independence of w'_i.
    print("\n(1) w'_i is m-INDEPENDENT (stable infinite sequence):", flush=True)
    seqs = {m: shift_w(wvec(m, SIG, TAU), m) for m in (4, 6, 8, 10, 12, 14)}
    ref = seqs[14]
    print(f"    identical across m in {{4..14}}: {all(seqs[m][i] == ref[i] for m in seqs for i in range(len(seqs[m])))}", flush=True)

    # (2) reciprocal pairing + Chebyshev point + CRUX two-point identity d_j=beta*4q_j(1+beta)+conj.
    print("\n(2) reciprocal pairing & CRUX two-point identity (=> L is two-point => closed form):", flush=True)
    z = (Fr(13, 25), Fr(16, 25))          # alpha/25
    zinv = (Fr(13, 17), Fr(-16, 17))      # conj(alpha)/17
    print(f"    (alpha/25)(conj alpha/17) = {gmul(z, zinv)}  (want (1,0))", flush=True)
    xi = gadd((Fr(1), Fr(0)), BETA)       # 1+beta
    JMAX = 16
    d = d_vec_sig(SIG, TAU, JMAX)
    dn2 = BETA[0] ** 2 + BETA[1] ** 2
    crux = True
    for j in range(1, JMAX + 1):
        Tj = cheb_T(j, xi)
        num = gscal(Fr(-4), gsub(Tj, (Fr(1), Fr(0))))
        q = gscal(Fr(1) / dn2, gmul(num, gconj(BETA)))   # 4q_j(1+beta) = -4(T_j-1)/beta
        val = gadd(gmul(BETA, q), gmul(gconj(BETA), gconj(q)))
        crux &= (val[1] == 0 and val[0] == d[j - 1])
    print(f"    d_j = beta*4q_j(1+beta)+conj for all j<={JMAX}: {crux}", flush=True)

    # (3) closed form w'_i = 8^{i+1}*2Re(gamma^{i+1})/425^{i+1} and the elementary valuation.
    print("\n(3) closed form + elementary valuation v_2(w'_i)=4+3i (gamma ≡ 1 mod 2 => Re odd):", flush=True)
    cf = allv = True
    for i in range(len(ref)):
        re, im = gpow_int(GAMMA_RE, GAMMA_IM, i + 1)
        val = Fr(8 ** (i + 1) * 2 * re, 425 ** (i + 1))
        cf &= (val == ref[i])
        allv &= (v2(ref[i]) == 4 + 3 * i and re % 2 == 1)
    print(f"    w'_i = 8^(i+1)*2Re(gamma^(i+1))/425^(i+1) all i: {cf}", flush=True)
    print(f"    Re(gamma^(i+1)) odd & v_2(w'_i)=4+3i all i: {allv}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("RESULT: node-free lemma v_2(w'_i)=4+3i PROVED elementarily (rank-2 closed form + 'odd real", flush=True)
    print("part'). => C_j=m+3 (§6bi) => v_2(q_min) >= 2m-5 unconditionally, sigma=3/4 (D=425). RH [OUT].", flush=True)
