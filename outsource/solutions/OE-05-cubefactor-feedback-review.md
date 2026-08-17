# OE-05 Cube-Factor Feedback Review — Bounded-Support/Baker Claim

**Date:** 2026-08-17  
**External claim:** Baker/Matveev linear forms in logarithms give an effective constant
`C(M)` depending only on the number `M` of supporting primes of the squarefree odd-power
cores, so all cube-factor Row-3 solutions with support cardinality at most `M` and
`n>C(M)` are excluded.  
**Verdict:** **NOT ESTABLISHED / INCONCLUSIVE.** It does not satisfy OE-05's confirmed
or partial acceptance criteria, and it does not provide the claimed precise localization.  
**Computational status:** `REPRODUCIBLE` for the exact scope checks in
`checker/audit_OE03_OE05_feedback.py`.

---

## What is valid

The feedback correctly identifies the central obstruction: Evertse-type S-unit and
Thue-Mahler bounds are uniform for a fixed actual support set, while the relevant split
primes for `A+` and `A-` are outside `5n` and are not a priori uniformly bounded.

It is also fair that the Frey-Hellegouarch route faces a conductor/level-growth problem.
This is a plausible research obstacle, but the feedback does not prove a theorem excluding
all Frey constructions, and no such exclusion is needed for OE-05.

The displayed discriminant is, in addition, not the discriminant of the stated cubic.
For `E: Y^2=X(X-w_+)(X+n)`, the roots are `0,w_+,-n`, so

```
Delta_E = 16*w_+^2*n^2*(w_+ + n)^2,
```

not `16*w_+*(-w_-)*n^2`. The exact audit checker samples `(a,n)=(1,4)` and confirms
the two complex values differ. Thus the conductor/level-lowering calculation is not
accepted as written.

## Blocking error 1: fixed support is confused with bounded support cardinality

Let the "support" be a fixed set of primes. Replacing it by the condition
`|S|<=M` is a strictly weaker condition: both the primes and their exponents may vary.

The exact audit checker exhibits the one-prime family

```
N_j = 13^(2j+3),   j=0,1,2,...
```

Every `N_j` is powerful away from 5 and has a nontrivial cube factor, but the family has
one supporting prime and unbounded height. Thus a constant depending only on `M` does not
control the heights of the algebraic numbers entering the logarithmic form.

To use Baker/Matveev, one must state which quantities are fixed. An actual fixed set
`S`, a fixed number field, fixed coefficients, and a fixed right-hand side give a
different (and much stronger) hypotheses than `|S|<=M` with primes, exponents, `u1/u2`,
`alpha`, `beta`, and `n` all varying.

## Blocking error 2: the displayed Baker inequality is not derived

The feedback starts from

```
Lambda = log(u1/u2) + 2*log(alpha/beta),
```

with an upper bound of polynomial size in `1/n`. A Matveev lower bound, however, involves
the number field, the number of logarithms, and the logarithmic heights of all algebraic
inputs. Those heights include `u1/u2`, `alpha`, and `beta`; they are not bounded by
`2^|S|`. Even with actual `S` fixed, exponents may make the heights grow.

Therefore the displayed implication

```
log(A-/n) <= C1 * 2^|S| * log(Apm)
```

is unsupported. The later reduction to

```
O(log n) <= constant * O(log log n)
```
 mixes two different hypotheses:

- if only `|S|<=M`, then the coefficient heights are not constant;
- if the actual support and all S-unit coefficients are fixed, then one must prove why
  the remaining Row-3 data still vary and how the bound depends on the right-hand side.

No effective constant `C(M)` is produced, and no source-verified Matveev theorem covering
the stated varying-support Gaussian family has been supplied in `baseline/`.

## Blocking error 3: the underlying quadratic family is not automatically Siegel/Faltings

The equation

```
u1*alpha^2 - u2*beta^2 = n
```

is a quadratic/Pell-type family (genus zero before imposing S-unit conditions), not a
curve of genus at least two. Faltings does not apply merely from this equation. Siegel's
finiteness statement for integral points is not the relevant effective enumeration, and
Pell-type equations can have infinite integral families before the S-unit and Row-3
constraints are imposed.

For a genuinely fixed actual `S` and fixed normalized right-hand side, Evertse-type
S-unit finiteness is available, but the feedback varies `S`, the coefficients, and the
right-hand side. That is precisely the OE-05 obstruction.

## Status of the asserted square subcase

The feedback calls the square subcase unconditional. The repository ledger is more
conservative:

- Theorem L is `PROOF-DRAFT` with an exact checker replay;
- Theorem M is `PROOF-DRAFT`, with an independent CAS check of its 2-isogeny descent
  explicitly recorded as a remaining Gate-A gap.

External prose cannot promote either item to `INDEPENDENTLY-CHECKED`.

## Evidence table

| Claim | Assessment | Reason |
|---|---|---|
| Growing actual support blocks direct Evertse/S-unit bounds | CONFIRMED | already recorded in OE-03/OE-05 |
| `|S|<=M` alone controls heights | REFUTED | `13^(2j+3)` has one supporting prime and unbounded height |
| Matveev yields the displayed `C1*2^|S|` upper bound | NOT ESTABLISHED | heights and number of logarithms are not controlled by cardinality |
| `C(M)` is effectively computable | NOT ESTABLISHED | no constants, no source-verified theorem scope, no derivation |
| Ordinary Frey curves are rigorously excluded | NOT ESTABLISHED | conductor-growth diagnosis is not a theorem covering all constructions |
| `t=1` case is already unconditional in this repo | OVERCLAIM | repository status remains `PROOF-DRAFT`; Theorem M has a recorded Gate-A gap |

## Resulting status

The cube-factor case of NT-C remains **OPEN**. A future bounded-support theorem must
distinguish explicitly between:

1. fixed actual support set `S` (with fixed field/coefficients/right-hand side scope);
2. a uniform bound over all support sets of cardinality at most `M`;
3. a uniform bound over Row-3 solutions after imposing `A+=a^2+n^2` and
   `A-=(n-a)^2+n^2`.

Only (3), with an independently replayed effective constant, would advance OE-05.

## Status-label mismatch

The reply calls its outcome "Acceptance Criteria 5 (Strong Partial / Precise
Localization)". OE-05 as shipped has no such criterion: criterion 5 is **REFUTED**
(supply a Row-3 counterexample), criterion 4 is **INCONCLUSIVE**, and the partial
criteria 2–3 require a proved subfamily obstruction or p³-gap identity. The submitted
reply meets none of 1–4 and supplies no counterexample for 5.
