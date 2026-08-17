# OE-05 Biquadratic Follow-Up Review — Fixed-j / Quadratic-Twist Claim

**Date:** 2026-08-17  
**External claim:** The cube-factor equations reduce to a smooth intersection of two
quadrics with constant `j=148176/25`; the resulting quadratic twists all have rank zero,
so the `t>=2` case of NT-C is closed.  
**Verdict:** **REJECTED / NOT ESTABLISHED.** The determinant calculations, fixed-j
inference, Weierstrass model, and descent all contain exact errors. NT-C `t>=2` remains
OPEN.  
**Computational status:** `REPRODUCIBLE` via
`checker/audit_OE04_OE05_followup.py`.

---

## Missing normalization in the setup

The setup starts from Gaussian representations of `w+` and `w-` but omits the unit and
5-part normalization. In full,

```
w± = unit * 5-part * U± * alpha±^2.
```

The displayed real/imaginary equations assume a fixed unit and 5-part without listing
the cases. This may be repairable, but it is not an equivalence proof as written.

## The pencil determinants are wrong

From the displayed quadrics, the `(X,Y)` block of `lambda*Q+mu*P` is

```
[ lambda*v+mu*(u-v)      lambda*u-mu*(u+v) ]
[ lambda*u-mu*(u+v)     -lambda*v+mu*u     ].
```

Its determinant is not generally

```
-(u^2+v^2)*(lambda^2-2*lambda*mu+2*mu^2).
```

Exact counterexample: `u=2,v=1,lambda=2,mu=1` gives determinant `-1`, while the claimed
formula gives `-10`.

Similarly, the `(Z,W)` block is

```
[ -lambda*v+mu*u    -lambda*u-mu*v ]
[ -lambda*u-mu*v     lambda*v+mu*u ].
```

Its determinant is not generally `-(u^2+v^2)*(lambda^2+mu^2)`. At
`u=1,v=2,lambda=2,mu=1`, the determinant is `-31`, while the claimed formula gives
`-25`.

Therefore the four roots, the smoothness conclusion, the cross-ratio, and the claimed
constant `j` are not derived from the displayed equations.

## The claimed Weierstrass model has the wrong invariant

Even if the cross-ratio calculation `c=1/5` is accepted, it gives

```
j=256*(c^2-c+1)^3/(c^2*(c-1)^2)=148176/25.
```

But the submitted base curve

```
E0: Y^2=X^3-21X+10
```

has

```
j(E0)=98784/53,
```

not `148176/25`. The exact checker verifies the mismatch.

## The 2-descent is structurally invalid

The cubic

```
X^3-21X+10
```

has no rational root, so `E0(Q)[2]=0`. A map sending the `x`-coordinate to
`Q*/(Q*)^2` is the standard descent map attached to a rational 2-isogeny/rational
2-torsion setup, not to this curve as presented. No rational 2-torsion is available.

The statement that all relevant quadratic twists have

```
rank E^(d)(Q)=0
```

is not proved. Quadratic-twist ranks and 2-Selmer dimensions vary with `d`; local
conditions at 2 and 5 cannot by themselves annihilate all relevant twists. No explicit
twist parameter, covering space, Selmer element, or rank formula is supplied.

## The height argument is conceded to fail

The follow-up's own cross-check correctly notes that

```
h(P) ~ (1/2)log n,     h(E) ~ (1/3)log n
```

do not produce a contradiction from a Lang/Silverman lower bound of order
`c*h(E)`; `1/2 > (1/3)c` for any small absolute `c`. The later fixed-j/twist proposal
does not repair that failed height step.

## No pullback or torsion classification

No explicit birational map from the intersection curve to `E^(d)` is supplied, no twist
parameter is derived, and no torsion classification is given. The assertion that torsion
pulls back only to `X=Y=Z=W=0` trivial solutions is unsupported.

## Evidence table

| Claim | Assessment | Evidence / gap |
|---|---|---|
| Unit/5-part normalization handled | NOT ESTABLISHED | cases omitted |
| `det(B1)` normal form | REFUTED | exact sample gives `-1`, not `-10` |
| `det(B2)` normal form | REFUTED | exact sample gives `-31`, not `-25` |
| Fixed four roots / smooth genus-one model | NOT ESTABLISHED | determinant formulas fail |
| Constant `j=148176/25` | NOT ESTABLISHED | depends on invalid determinants |
| `E0:y^2=x^3-21x+10` has that `j` | REFUTED | `j(E0)=98784/53` |
| `x mod squares` 2-descent on `E0` | INVALID | `E0(Q)[2]=0` |
| All relevant twists have rank 0 | NOT ESTABLISHED | no Selmer/rank computation |
| Torsion pulls back only to trivial Row-3 points | NOT ESTABLISHED | no map or torsion calculation |
| NT-C `t>=2` closed | REJECTED | all decisive steps fail |

## Resulting status

The cube-factor case of NT-C remains **OPEN**. The fixed-j/twist idea is not currently
a theorem or even a well-defined reduction.
