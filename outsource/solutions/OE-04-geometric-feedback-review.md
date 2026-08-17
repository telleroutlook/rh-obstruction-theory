# OE-04 Geometric Feedback Review — Symmetric Quartic / Vojta Claim

**Date:** 2026-08-17  
**External claim:** The symmetric quartic reduces the square case to a rank-zero
elliptic curve, and Darmon-Granville plus Vojta gives a conditional proof for the
general powerful case, thereby confirming OE-04.  
**Verdict:** **REJECTED as a CONFIRMED result.** The symmetric algebra is partly
correct, but the square argument is not a new NT-D result and the general geometric
argument does not establish the stated conditional theorem. A useful salvage is that
`4=2^2` and `8=2^3` already refute a gap-only version of NT-D.  
**Computational status:** `REPRODUCIBLE` via
`checker/audit_OE04_OE05_followup.py`.

---

## What is correct

With `n=2m` and `u=a-m`,

```
A+ = (u+m)^2 + 4m^2 = u^2+2um+5m^2,
A- = (m-u)^2 + 4m^2 = u^2-2um+5m^2,
```
and hence

```
A+A- = (u^2+5m^2)^2-(2um)^2
      = u^4+6m^2u^2+25m^4.
```

The exact checker verifies this identity on several primitive samples. The reduction
`u=0 => a=m => gcd(a,2m)=m=1 => n=2` is also elementary.

## Defect 1: the two supplied elliptic models are not interchangeable

The first version multiplies the conic by `x` and uses

```
E1: v^2 = x^3+6x^2+25x.
```

The second version invokes Cassels' quartic Jacobian and uses

```
E2: Y^2 = X(X+4)(X-16)=X^3-12X^2-64X.
```

These curves have different rational `j`-invariants:

```
j(E1) = 237276/625,
j(E2) = 148176/25.
```

Thus the two rank discussions are not two presentations of one proved reduction. The
first descent also computes only one image and omits the dual-isogeny image; the second
asserts a full 2-Selmer computation without giving the covering spaces or local maps.
Its attempted local obstruction for the class `2` even exhibits a soluble value mod 5
and then claims a contradiction without a valuation calculation.

The square case is already covered by Theorem L in this repository. No new NT-D
statement follows from rederiving it.

## Defect 2: fixed cube factors give genus one, not genus >1

For fixed `z1,z2`, the submitted system is

```
u^2+2um+5m^2 = z1^3*y1^2,
u^2-2um+5m^2 = z2^3*y2^2.
```

For fixed nonzero `z1,z2`, this is two quadratic equations in projective
3-space with coordinates `(u:m:y1:y2)`. A smooth complete intersection of two
quadrics in `P^3` has genus one, not genus at least two.

For example, at `z1=z2=1`, the pencil determinant is, up to a nonzero scalar,

```
lambda*mu*(lambda^2+3*lambda*mu+mu^2),
```

with four distinct roots. The checker verifies this representative. Therefore invoking
Faltings to get finiteness of all rational points on each fixed-`(z1,z2)` curve is a
genus error: genus-one curves can have positive rank.

## Defect 3: Darmon-Granville is not supplied in the needed scope

No Darmon-Granville paper or theorem statement is present in `baseline/`. The external
reply does not state a theorem number or verify the hypotheses. Moreover, the relevant
Darmon-Granville-type results concern fixed generalized-Fermat exponents (typically with
reciprocal sum below one), not a varying powerful decomposition

```
F(u,m)=Y^2Z^3
```

where `Z` is another unknown. The signature `(4,2,3)` has reciprocal sum

```
1/4+1/2+1/3=13/12>1,
```
so it is not the hyperbolic regime named in the common formulations. The reply does not
explain how any source theorem covers this varying-`Z` problem.

| Claim as used | Source check | Verdict | Impact |
|---|---|---|---|
| Darmon-Granville finitely covers `F(u,m)=Y^2Z^3` with variable `Z` | no source in `baseline/`; no theorem number in reply | `source-unavailable / hypotheses-missing` | blocks the general powerful case |
| Vojta gives an absolute height bound from alleged ampleness | no source in `baseline/`; no `(V,D)` or `K_V+D` computation | `not-found / hypotheses-missing` | blocks the claimed conditional criterion |

## Defect 4: the Vojta step is overclaimed

The reply neither computes the variety `V`, its boundary, nor `K_V+D`, and does not
prove log-general type. It replaces this by slogans about "two independent ramified
conditions".

Even the standard Lang-Vojta-type conclusion for a log-general-type variety is
Zariski non-density (or containment in a proper closed subset), not an absolute height
bound for all integral points. The claimed implication

```
K_V ample  ==>  max(|u|,|m|)<C
```

is not a statement of Vojta's conjecture as supplied. Kodaira dimension `>0` is also
weaker than general type.

## Salvage: NT-D as a gap-only approach is refuted

The pair

```
4=2^2,   8=2^3
```

consists of powerful-away-from-5 integers with

```
A2-A1=4 ~ A1.
```

Thus no theorem saying "two powerful-away-from-5 numbers cannot have a gap comparable
to their size" can be true. This satisfies the OE-04 REFUTED-approach criterion for the
gap-only route, but it says nothing about the Row-3 family and does not prove the core
conjecture.

## Evidence table

| Claim | Assessment | Evidence / gap |
|---|---|---|
| Symmetric quartic identity | CONFIRMED | exact checker |
| `E1` rank-0 proof | NOT ESTABLISHED | one descent image only; wrong/incomplete descent |
| `E2` rank-0 proof | NOT ESTABLISHED | Selmer computation asserted, not supplied |
| Square case implies NT-D | NO | already Theorem L; powerful case omitted |
| Fixed `(z1,z2)` curve has genus >1 | REFUTED | fixed system is genus one |
| Darmon-Granville closes varying `Z` | NOT ESTABLISHED | no source/scope; non-hyperbolic signature |
| Vojta gives absolute height bound | NOT ESTABLISHED | wrong conjecture scope; no `K_V+D` computation |
| Gap-only route | REFUTED | exact pair `4,8` |

## Resulting status

OE-04's gap-only approach is **REFUTED** by `4,8`; the Row-3-specific core remains
OPEN. The submitted geometric/conditional proof is not accepted.
