# OE-03 Geometric Feedback Review — Quadric Model

**Date:** 2026-08-17  
**External claim:** The NT-A growing-support problem is reduced unconditionally to
three explicit genus-one curves (four 5-adic types, modulo symmetry), so only a finite
Mordell-Weil/Chabauty computation remains.  
**Verdict:** **REFUTED as a reduction of NT-A. PARTIAL only for the previously known
square-based `t=1` sublocus.**  
**Computational status:** `REPRODUCIBLE` via `checker/audit_OE03_OE05_feedback.py`.

---

## What the feedback gets right

The submitted algebraic substitutions are correct. The exact audit checker verifies:

1. For `(e1,e2)=(0,0)`,
   `x=(m^2-1)/(2m)` gives
   `(x-1)^2+1 = (m^4-4m^3+6m^2+4m+1)/(2m)^2`.
2. For `(e1,e2)=(1,0)`,
   `x=(1+2k-k^2)/(1-k^2)` gives
   `x^2+1 = 2(k^4-2k^3+2k+1)/(1-k^2)^2`;
   with `W=5u(1-k^2)`, this yields
   `W^2=10k^4-20k^3+20k+10`.
3. For `(e1,e2)=(1,1)`,
   `x=(-10k^2+10k-2)/(1-5k^2)` gives
   `((x-1)^2+1)(1-5k^2)^2 =
   10(5k^4-10k^3+12k^2-6k+1)`;
   with `Omega=v(1-5k^2)`, this yields
   `Omega^2=10k^4-20k^3+24k^2-12k+2`.
4. The proposed anchor `k=1` maps to `x=1/2`, hence `(a,n)=(1,2)`, and both original
   values equal `5=5^1*1^2`. It is excluded by the Row-3 boundary condition `n>=4`.

Thus the model is a valid birational treatment of the restricted system

```
A+ = 5^e1 * X^2,   A- = 5^e2 * Y^2.
```

## Fatal scope error: this is not the powerful locus

The system `Apm = 5^e * square` is the **square-based, `t=1` sublocus** of
powerful-away-from-5 integers. The full definition allows a prime `p!=5` to occur with
any exponent at least two, in particular an odd exponent at least three.

An exact counterexample to the claimed equivalence is

```
13^3 = 2197.
```

It is powerful away from 5, because its only nonzero non-5 exponent is `3>=2`, but it is
not of the form `5^e * square`, because the exponent of 13 is odd. The same phenomenon
occurs in the Gaussian model:

```
(3+2i)^3 = -9+46i,   N(-9+46i)=13^3.
```

Consequently, points on the three submitted quartics cover only the cases where every
non-5 exponent is even. They do **not** cover Gaussian factors `U*alpha^2` with `U`
having split-prime exponents `3,5,7,...`. No rank computation on these three curves can
close NT-A or the cube-factor part of NT-C.

This restricted square-based case is already the subject of Theorems L and M
(both remain `PROOF-DRAFT` in the repository ledger; Theorem M additionally records an
independent CAS descent check as a Gate-A gap).

## The proposed rank protocol is also overclaimed

Even on a fixed genus-one curve:

- rank 0 plus exact torsion can give all rational points, but the rank calculation must
  itself be independently established, not merely reported by an external solver;
- Chabauty-Coleman requires rank at most one (and an explicit Mordell-Weil setup);
- rank greater than one is not handled by the proposed protocol;
- Siegel's integral-point finiteness is non-effective and does not by itself enumerate
  the points;
- Mordell-Weil finite generation alone is not an effective enumeration algorithm.

The feedback's statement that the problem has been "reduced to a completely standard
algorithm" or is at a "perfect path" is therefore not accepted.

## Evidence table

| Claim | Assessment | Evidence / gap |
|---|---|---|
| Three quartic equations are correctly derived | CONFIRMED | exact polynomial checks in `checker/audit_OE03_OE05_feedback.py` |
| `k=1` anchor maps to `(1,2)` | CONFIRMED | exact check in the same checker |
| Restricted model captures `Apm=5^e*square` | CONFIRMED | direct rational substitution |
| Restricted model captures powerful-away-from-5 | REFUTED | `13^3` and `(3+2i)^3` |
| Computing three Mordell-Weil groups closes NT-A | REFUTED | cube-factor points are absent from the model |
| Rank protocol handles all positive-rank cases | NOT ESTABLISHED | Chabauty rank condition/effectivity overclaimed |

## Resulting status

OE-03 remains **OPEN**. The useful geometric content is a duplicate/rederivation of the
known `t=1` reduction and may be used as a sanity model, but it must not be cited as a
premise for the full powerful problem.
