# Statement — Theorem I (Gaussian Weil no-collision)

**Theorem ID:** I-gaussian-weil-no-collision  
**Mathematical status:** PROOF-DRAFT (prepared for Gate-A review; not independently checked)  
**Computational status:** REPRODUCIBLE finite quadratic-witness replay; no finite computation certifies the analytic theorem
**Program ref:** Paper A Open Problem 2 / observation-encoding arithmetic  
**Paper target:** Paper A v2

---

## §0. What is proved

For a natural algebraic Gaussian/Hermite-Gaussian test function, an off-line symmetric
quartet cannot be exactly compensated by on-line pairs with integer multiplicities.
This is the opposite of the rational Li collision in Theorem B2. It is a statement about
finite observation vectors only; it assumes and implies nothing about RH or the zeros of
`ζ`.

## §1. Objects

Let `Qbar` denote the field of algebraic numbers and `Qbar_R = Qbar ∩ R`.
Fix:

- an integer `m ≥ 1`;
- `a ∈ Qbar_R`, `a > 0`;
- distinct on-line heights `γ_1,...,γ_m ∈ Qbar_R` such that `γ_j ≠ 0` and
  `γ_1^2,...,γ_m^2` are pairwise distinct;
- an off-line quartet parameterized by `g ∈ Qbar_R`, `g > 0`, and
  `δ ∈ Qbar_R`, `δ ≠ 0`;
- a nonzero even polynomial `P ∈ Qbar_R[x]` such that
  `P(γ_k) ≠ 0` for every `k` and `P(g+iδ) ≠ 0`.

Define the even Gaussian-type test function

```
G(z) = P(z) exp(-a z^2).
```

For the on-line pair `L(γ) = {1/2+iγ, 1/2-iγ}` and the off-line quartet
`Q(g,δ) = {1/2+δ ± ig, 1/2-δ ± ig}`, use the finite Weil-type observation

```
Φ_G(Z) = sum_{rho in Z} G((rho-1/2)/i).
```

The evenness of `P` and the identities `G(-z)=G(z)` and
`G(bar z)=overline{G(z)}`
give

```
Φ_G(L(γ_k)) = 2 P(γ_k) exp(-a γ_k^2),
Φ_G(Q(g,δ))
  = 2 P(g+iδ) exp(-a(g+iδ)^2)
    + 2 P(g-iδ) exp(-a(g-iδ)^2).
```

## §2. Theorem

**Theorem I (algebraic Gaussian no-collision).** Under the hypotheses in §1,
there is no nonzero integer vector `(q,c_1,...,c_m) ∈ Z^{m+1}` satisfying

```
q Φ_G(Q(g,δ)) = sum_{k=1}^m c_k Φ_G(L(γ_k)).
```

Equivalently, the `m+2` observation terms associated with the exponents

```
β_+ = -a(g+iδ)^2,
β_- = -a(g-iδ)^2,
β_k = -a γ_k^2                         (k=1,...,m)
```

are collectively immune to a nontrivial integer balancing relation.

The same argument applies to a finite family of distinct off-line quartets
provided the corresponding unordered exponent pairs `{β_+,β_-}` are disjoint
and the designated polynomial `P` is nonvanishing at every participating
on-line and off-line argument. It also applies to a finite family of test
functions whenever at least one member satisfies the nonvanishing hypotheses.

## §3. Explicit non-degeneracy requirement

The hypotheses `P(γ_k)≠0` and `P(g+iδ)≠0` are necessary. If, for example,
`P(g+iδ)=0`, then conjugacy gives `P(g-iδ)=0`, so the off-line quartet is
invisible to `G`; `(q,c_1,...,c_m)=(1,0,...,0)` is then a degenerate integer
relation. This is not a failure of the no-collision argument: it means the
chosen test function annihilates the distinction being observed.

### Normalization audit

The observation coordinate is `(rho-1/2)/i`. Thus an on-line point
`1/2+i gamma` maps to `gamma`, while `1/2+delta+i g` maps to `g-i delta` and
`1/2-delta+i g` maps to `g+i delta`. Since the quartet contains both signs of
`delta`, the displayed unordered pair `P(g+i delta), P(g-i delta)` is exactly
the reconstructed pair; the labels `+/-` alone carry no convention-dependent
meaning.

## §4. Status boundary

This theorem does **not** cover:

1. compactly supported real `h ∈ C_c^∞(R)`;
2. general Paley-Wiener Fourier transforms of compactly supported test functions;
3. approximate bounded-height collisions;
4. any claim about the actual Riemann zero set;
5. any claim about RH, or about an RH-equivalent criterion.
