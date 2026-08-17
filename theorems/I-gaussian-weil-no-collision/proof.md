# Proof — Theorem I (Gaussian Weil no-collision)

**Status:** PROOF-DRAFT. The argument is separated into an analytic/algebraic
identity (Step A) and one external theorem (Step B). No finite computation is
used as proof.

## Step A — Reduce an integer collision to an algebraic linear relation among exponentials

Keep the notation of `statement.md`. Put

```
β_+ = -a(g+iδ)^2,   β_- = -a(g-iδ)^2,   β_k = -a γ_k^2.
```
All three kinds of exponent are algebraic. Since `γ_k^2` are distinct, the
`β_k` are distinct real algebraic numbers. Since `gδ ≠ 0` and `a > 0`, the
imaginary parts of `β_+` and `β_-` are nonzero and opposite; hence `β_+` and
`β_-` are distinct non-real conjugates. Consequently

```
β_+, β_-, β_1,...,β_m
```

are `m+2` distinct algebraic numbers.

Because `P` is even, the two atoms of an on-line pair give the same Gaussian
value; because its coefficients are real, complex conjugation gives the paired
off-line term. The observation identities therefore take the form

```
Φ_G(Q(g,δ))
  = 2P(g+iδ)e^{β_+} + 2P(g-iδ)e^{β_-},
Φ_G(L(γ_k)) = 2P(γ_k)e^{β_k}.
```

Suppose integers `q,c_1,...,c_m` satisfy

```
qΦ_G(Q(g,δ)) = Σ_k c_k Φ_G(L(γ_k)).
```

Dividing by `2` and moving all terms to one side yields

```
qP(g+iδ)e^{β_+}
  + qP(g-iδ)e^{β_-}
  - Σ_k c_kP(γ_k)e^{β_k}
  = 0.
```

This is a `Qbar`-linear relation among `{e^{β_+},e^{β_-},e^{β_1},...,e^{β_m}}`.

## Step B — Apply Lindemann-Weierstrass

By the Lindemann-Weierstrass theorem in its linear-independence form, the
exponentials of distinct algebraic numbers are linearly independent over
`Qbar`. Therefore every coefficient in the relation from Step A is zero:

```
qP(g+iδ)=0,   qP(g-iδ)=0,   c_kP(γ_k)=0 (k=1,...,m).
```

The stated nonvanishing hypotheses force `q=0` and `c_1=...=c_m=0`. Thus no
nontrivial integer collision exists.

## Finite families and multiple quartets

For several even polynomial test functions, the equality of each coordinate gives the preceding
relation for the same integer vector. If at least one designated test function
satisfies the nonvanishing hypotheses, that coordinate alone forces all
integers to vanish.

For several quartets with parameters `(g_l,δ_l)`, each quartet contributes
two exponents `-a(g_l±iδ_l)^2`. For `g_l>0`, `δ_l≠0`, the unordered pair is
determined by `(g_l^2-δ_l^2, 2g_lδ_l)`; hence genuinely distinct quartets give
disjoint exponent pairs. Repeating Step A produces one Lindemann-Weierstrass
relation with coefficients `q_lP(g_l±iδ_l)`. Distinct exponents force every
`q_l=0`, and then the on-line coefficients vanish.

## What is not proved

The proof uses the special form `(algebraic polynomial)·exp(algebraic exponent)`.
It gives no statement for compactly supported `h`, whose Fourier transform is
Paley-Wiener rather than Gaussian, and it gives no quantitative bound on
approximate bounded-height relations.
