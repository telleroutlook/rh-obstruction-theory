# OB-44 reviewer response and execution roadmap

**Date:** 2026-08-17  
**Decision:** do not submit a paper version while these cores are open. The two
focused questions may be sent externally only after the local revisions below.

## 1. Response to the reviewer's main findings

| Finding | Response / change |
|---|---|
| A and B are clean problem statements but do not themselves advance OP1 unless their arithmetic cores are solved | Accepted. `PLAN.md` now has an open-problem execution register and puts Paper A v2 on publication hold. |
| Premises in OB-44B were not self-contained | Accepted. Revised OB-44B inlines the graded factorization, moment closed form, Lemma POLE, and Lemma BRIDGE. |
| Denominator normalization and `d` scaling were subtle | Accepted. OB-44B now fixes the reflection-doubled `d`, one common denominator `L`, and prohibits per-column or `d`-only scaling. |
| “Arbitrary rational nodes” was not handled precisely | Accepted. A rational node is `u/v`; poisoning is `p | 4u²+v²`; height is `max(|u|,v)`. |
| OB-44A's generic-sieve strategy was too vague | Accepted. The prompt now names the norm-type, abelian-root, and binary-family obstacles and asks for a concrete Gaussian/UFD descent or primitive-divisor route. |
| The `9856` scan did not state the simple-carrier rate | Accepted. The revised prompt states `9856/9856` simple carriers and `0/9856` powerful values in the scanned box. |
| A+B composition was implicit | Accepted. §2 below states the exact composition and failure modes. |
| `q_min>0` was too weak as PARTIAL | Accepted. OB-44B explicitly excludes it; PARTIAL requires super-logarithmic growth, an infinite family, or a height-refined theorem. |

## 2. A+B composition roadmap

The odd-carrier route closes only if both open cores hold in a compatible form.

```text
OP1-A (OB-44A):
    N(a,n) has a simple rational prime factor p.

OP1-B (OB-44B):
    Even when CRT rational-node choices poison every simple factor,
    q_min retains a super-logarithmic (ideally linear-log) floor.

Composition:
    OP1-A + OP1-B
        ⇒ resource-bounded finite Li-collision floor
        ⇒ log q_min = ω(log m), ideally Ω(m).
```

Failure modes:

1. **OP1-A false:** some Row-3 `N` is powerful, so no simple carrier exists.
2. **OP1-B false:** CRT poisoning gives configurations with `log q_min=o(m)`.
3. **OP1-A true, OP1-B open:** only the clean-carrier conditional theorem survives.
4. **Height-refined OP1-B only:** the result is useful but must state the node-height
   restriction; it cannot be marketed as an arbitrary-node-set bound.

## 3. Remaining genuinely external questions

1. **OB-44A:** powerful values of the explicit Row-3 binary quartic. This is a
   self-contained number-theory problem and remains externally worthy.
2. **OB-44B:** full relation-size lower bound after CRT poisoning. The clean
   unpoisoned theorem is now inlined; only the poisoned adversary core remains.

The Gaussian/Hermite-Gaussian no-collision theorem and the lattice-index identity
are internally tractable certification tasks, not paid mathematical-discovery
outsources.

## 4. Exact finite sanity replay

`checker/ob44b_prompt_anchor.py` independently checks, in exact rational
arithmetic:

1. the reflection-doubled `d` normalization;
2. `B w=d`;
3. the clean `m=3` valuations at `101` and `181`;
4. the CRT-poisoned `(17276,1)` configuration.

It is finite sanity evidence only and does not prove the open aggregate bound.

The checker also replays the sharper poisoned pair `(19286,26164)`: both simple
carriers are poisoned, `q_min=18`, and both carrier valuations vanish, but the
exact on-line coefficients have sup-norm `3292056116081922725`. OB-44B therefore
now targets full relation size, not `q_min` alone.

It also replays the rectangular configuration `(1005,7883,-10398)` with
`m=2,K=3`: every node poisons both carriers, `q_min=1`, and the exact full
relation has sup-norm `16156893919328`. This is a finite counterexample to any
`q_min`-only aggregate-floor formulation for `K>m`.

## 5. Addendum from second OB-44A reply

A second external reply found a material correction and simplification:

```
N=(a²+n²)((a−n)²+n²)=|a+ni|² |(a−n)+ni|².
```

It also corrected the relation

```
Re M = r−2n²
```

rather than `2r−n²`. Both facts are now incorporated in OB-44A. A local exact
replay in `checker/ob44a_factorization_scan.py` confirmed the factorization,
`gcd(a²+n²,(a−n)²+n²)∈{1,5}`, `0/75840` powerful values through `n<1000`, and
`0/1898236` through `n<5000`. The reported `n<10000` scan remains external
evidence, not a premise or theorem.

## 6. Addendum from the third reviewer round

The stale least-counterexample bound `n≥360` has been replaced by the deposited
`n≥5000` bound. The primitive-divisor route is now listed first and explicitly
covers both branches of the exact hard-case criterion, including the case
`v_5(A_+)+v_5(A_-)=1`.

An internal domain audit also found that the earlier wording `n positive, even`
accidentally admitted the critical-line orbit `(a,n)=(1,2)`, for which
`a/n=1/2` and `N=25`. The intended off-line Row-3 family has now been corrected
to `n≥4` (equivalently, `a/n≠1/2` under the remaining parity and coprimality
conditions). This is a domain correction, not a counterexample to the off-line
problem.

The OB-44B minor-identity objection exposed a real presentation omission: the
previous formula omitted the reduced Vandermonde factor `V'_j`. The diagnosis
that `w` must be a polynomial-evaluation vector is not correct — the identity is
linear in an arbitrary `w` — but the cofactor proof needed to say so explicitly.
OB-44B now states the exact identity with `V'_j`, proves it by column expansion
plus the classical alternant identity, and the checker replays it for an
arbitrary rational vector

```
w=(7/5,-3/2,11/7).
```

The `K>m` objection is handled as an explicit scope condition rather than a
silent extension: Lemma BRIDGE is labeled square-only, while CONFIRMED outcomes
for Problem B must handle `K≥m`, including `K=m+1` and unbounded extra nodes.
