#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bj — THE TARGET LEMMA v_2(d_j) = 6 + 2 v_2(j) IS A LIFTING-THE-EXPONENT STATEMENT (sigma=3/4, D=425).

The node-free lemma of §6bi (v_2(w'_i)=4+3i) is fed by the triangular recursion d_j = sum_i G[j][i] w'_i.
Its base input is the 2-adic profile of the orbit target d_j.  This probe pins that down to a CLOSED FORM
and identifies the number-theoretic tool.  For sigma=3/4, tau=1 the orbit is rho in {3/4+-i, 1/4+-i}, and
    1 - 1/rho  =  (13 + 16 i)/25   (for rho=3/4+i)   and   (13 + 16 i)/17   (for rho=1/4+i),
with the Gaussian integer  alpha = 13 + 16 i,  N(alpha) = 13^2 + 16^2 = 425 = 25 * 17 = D,  alpha - conj = 32 i.
The orbit target is (verified to j=16, EXACT):
        d_j  =  4 * [ (1 - Re[(alpha/25)^j]) + (1 - Re[(alpha/17)^j]) ]
             =  4 * [ (25^j - Re[alpha^j])/25^j  +  (17^j - Re[alpha^j])/17^j ].
Since 25,17 are odd and Re[alpha^j] is ODD (v_2=0 always), v_2(d_j) = 2 + v_2( (25^j - Re) + (17^j - Re) ).
VERIFIED sub-valuations (LTE, p=2):
    v_2(25^j - Re[alpha^j]) = 2 + v_2(j),      v_2(17^j - Re[alpha^j]) = 2 + v_2(j),
        [base 2 = v_2(25-13)+v_2(25+13)-1 = 2+1-1; the Gaussian correction terms C(j,2k)13^{..}16^{2k}(-1)^k
         carry v_2 >= 7, deeper than 2+v_2(j)];
    and the SUM has v_2 = 4 + 2 v_2(j)  (a FURTHER cancellation, doubling the valuation), whose source is the
    conjugate relation  (alpha/25)(conj/17) = N(alpha)/425 = 1.
Hence  v_2(d_j) = 2 + (4 + 2 v_2(j)) = 6 + 2 v_2(j).  The imaginary companion v_2(Im[alpha^j]) = 4 + v_2(j)
is the textbook LTE (v_2(alpha^j - conj^j) = v_2(alpha - conj) + v_2(j) = 5 + v_2(j), /2i => 4 + v_2(j)).

This probe VERIFIES (exact, L9): the closed form for d_j, each LTE sub-valuation, the sum-doubling, and the
resulting v_2(d_j) = 6 + 2 v_2(j), to j = 24.  RH stays [OUT].  Honest (L5): the sub-valuation *formulas* are
verified numerically and each is a standard LTE identity; writing them as fully symbolic proofs (incl. the
sum-doubling from the conjugate relation) is the remaining step to close the §6bi lemma, hence OP1's 2-adic
channel, unconditionally for sigma=3/4.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from discovery.probe_qmin_p2_floor_identity import d_vec_sig

SIG, TAU = Fr(3, 4), Fr(1)
A_RE, A_IM = 13, 16          # alpha = 13 + 16 i, N(alpha) = 425 = 25 * 17


def v2int(n):
    if n == 0:
        return 10 ** 9
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def v2frac(fr):
    return v2int(fr.numerator) - v2int(fr.denominator)


def gpow(a, b, j):
    re, im = 1, 0
    for _ in range(j):
        re, im = re * a - im * b, re * b + im * a
    return re, im


if __name__ == "__main__":
    JMAX = 24
    d = d_vec_sig(SIG, TAU, JMAX)
    print("=" * 100, flush=True)
    print("§6bj: v_2(d_j) = 6 + 2 v_2(j) via LTE on alpha = 13+16i (N=425=25*17), sigma=3/4.", flush=True)
    print("=" * 100, flush=True)

    # (1) closed form d_j = 4[(1-Re[(a/25)^j]) + (1-Re[(a/17)^j])]
    form_ok = True
    for j in range(1, JMAX + 1):
        re, _ = gpow(A_RE, A_IM, j)
        val = 4 * ((Fr(1) - Fr(re, 25 ** j)) + (Fr(1) - Fr(re, 17 ** j)))
        form_ok &= (val == d[j - 1])
    print(f"\n(1) closed form d_j = 4[(1-Re[(a/25)^j])+(1-Re[(a/17)^j])] matches to j={JMAX}: {form_ok}", flush=True)

    # (2) LTE sub-valuations + sum doubling + final
    print("\n(2) sub-valuations:", flush=True)
    print(f"{'j':>3} {'v2(j)':>5} | {'v(25^j-Re)':>10} {'v(17^j-Re)':>10} | {'2+v2(j)':>8} | "
          f"{'v(sum)':>7} {'4+2v2(j)':>8} | {'v(d_j)':>7} {'6+2v2(j)':>8} | {'v(Im a^j)':>9} {'4+v2(j)':>8}", flush=True)
    all_ok = True
    for j in range(1, JMAX + 1):
        re, im = gpow(A_RE, A_IM, j)
        a25, a17 = 25 ** j - re, 17 ** j - re
        s = Fr(a25, 25 ** j) + Fr(a17, 17 ** j)
        v25, v17, vs = v2int(a25), v2int(a17), v2frac(s)
        vd, vim = v2frac(d[j - 1]), v2int(im)
        vj = v2int(j)
        row_ok = (v25 == 2 + vj and v17 == 2 + vj and vs == 4 + 2 * vj and vd == 6 + 2 * vj and vim == 4 + vj)
        all_ok &= row_ok
        print(f"{j:>3} {vj:>5} | {v25:>10} {v17:>10} | {2+vj:>8} | {vs:>7} {4+2*vj:>8} | "
              f"{vd:>7} {6+2*vj:>8} | {vim:>9} {4+vj:>8}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print(f"RESULT: closed-form {form_ok}, all LTE sub-valuations + v_2(d_j)=6+2v_2(j) to j={JMAX}: {all_ok}", flush=True)
    print("READING (L5): v_2(d_j)=6+2v_2(j) is LTE on 13+16i plus a conjugate-relation cancellation. Feeding this", flush=True)
    print("into the §6bi triangular recursion closes v_2(w'_i)=4+3i, hence C_j=m+3 and the linear floor", flush=True)
    print("v_2(q_min) >= 2m-5, unconditionally for sigma=3/4. Symbolic write-up of the LTE steps is the last mile.", flush=True)
