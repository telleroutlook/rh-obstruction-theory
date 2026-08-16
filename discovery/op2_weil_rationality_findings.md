# OP2 (Paper A Open Problem 2) — Weil-type observations and the rationality of the exact barrier

**Tier:** DISCOVERY / EVIDENCE only (program §12.1). Never imported into proofs. RH stays `[OUT]`.
**Probe:** `discovery/probe_op2_weil_rationality.py` (mpmath, PSLQ + precision-scaling discriminator).

## The question

Paper A Theorem A gives an *exact* information obstruction for the Li-type observations because
those observation values are **rational**, so "two zero-configurations with identical finite
observation" is a rational linear-algebra collision and the Chebyshev–Vandermonde reduction yields
an exact lattice index `q_min ≥ 1`. Open Problem 2 asks whether this extends to a fixed finite
family of Weil-type test functions `h_1..h_r`. The paper flags the obstacle: the observation values
are then **not guaranteed rational** and **no general transcendence statement is available**, so the
reduction does not apply.

## Exact observation values used (derived, real; Paley–Wiener, `ĥ` even & real)

- on-line pair `{½ ± iγ}`:  `Φ = 2·ĥ(γ)`.
- off-line quartet `{β ± ig₀, 1−β ± ig₀}`, `δ = β−½`:  arguments `(ρ−½)/i = ±g₀ ± iδ`, so
  `Φ_off = 4·Re ĥ(g₀ + iδ)`.
- Gaussian toy `ĥ_a(z) = exp(−a z²)`:  `Φ_a(γ) = 2e^{−aγ²}`,  `Φ_off = 4e^{−a(g₀²−δ²)}cos(2ag₀δ)`.

## Finding (EVIDENCE, L5-honest)

For a single Gaussian test function (`r=1`), the `1` off-line + `8` on-line observation reals
(anchored, harmlessly, at the first eight ζ-zero ordinates — a *generic-height* question, ordinates
are **not** an input) show **no genuine integer relation** up to coefficient height `10⁹` at
`250` decimal digits.

**Precision-scaling discriminator (the load-bearing check).** PSLQ at `40` dps *does* return a
relation with `max|coeff| = 20566` at maxcoeff `≥ 10⁶`, but re-evaluating that relation's residual
at `250` dps leaves it at `≈ 7.5e-31` (the found-precision floor) instead of collapsing to
`≈ 10^{-250}` — the signature of a **precision artifact**, not a true relation. A fresh PSLQ at
`250` dps finds **no relation** up to `10⁹`. So the `40`-dps "relations" are spurious.

**Reading.** The observation values are (empirically, bounded-height) **rationally independent**, so
the *exact* collision Theorem A relies on **does not exist** for this Weil family: the OP1 lattice-
index mechanism has **no arithmetic analogue** here. Extending Theorem A *exactly* to Weil-type
observations would require a **linear-independence / transcendence statement** about
`{Re ĥ(g₀+iδ), ĥ(γ_k)}` that is not currently available. This precisely **localizes** OP2's
difficulty: it is a *rationality* phenomenon, not a soft-analysis gap.

**What this probe does NOT establish (honesty note).** The exploratory "approximate-collision"
sweep (test 2, `r=3`) used a crude `q=1`-fixed integer least-squares; its residual is noisy
(`~0.07…0.27`, non-monotone) and does **not** demonstrate an "approximate obstruction shrinks with
`m`" claim. A genuine bounded-height minimum needs an LLL closest-vector search with `q` free; not
done. Only tests (1) and (3) yield findings. Bounded-height PSLQ on one family = **evidence, not proof**.

## Upgrade to a PROVED negative (Gaussian family) — Lindemann–Weierstrass

The empirical independence of test (1) becomes a **theorem** once the heights are algebraic. Key
algebraic identity (checked symbolically): with `β_± = −a(g₀²−δ²) ± i·2ag₀δ`,

```
Φ_off = 4·Re ĥ_a(g₀+iδ) = 4 e^{−a(g₀²−δ²)} cos(2ag₀δ) = 2( e^{β₊} + e^{β₋} ),
Φ(γ_k) = 2 e^{β_k},   β_k = −a γ_k².
```

So **every** observation value is `exp(exponent)`, and a nontrivial integer collision
`q·Φ_off = Σ_k c_k Φ(γ_k)` is exactly a nontrivial `Q̄`-linear relation

```
q·e^{β₊} + q·e^{β₋} − Σ_k c_k e^{β_k} = 0
```

among the exponentials `{e^{β₊}, e^{β₋}, e^{β_1}, …, e^{β_m}}`.

**Theorem (Gaussian Weil family, OP2-negative).** Fix `a ∈ Q̄, a≠0`; on-line heights `γ_k ∈ Q̄`
with the `γ_k²` distinct; off-line data `g₀, δ ∈ Q̄` with `g₀δ ≠ 0`. Then the exponents
`β_k = −aγ_k²` (real algebraic, distinct) and `β_± = −a(g₀∓iδ)²` (complex-conjugate algebraic,
non-real, hence `≠` every `β_k` and `≠` each other) are `m+2` **distinct algebraic** numbers. By
**Lindemann–Weierstrass**, `{e^{β_j}}` are linearly independent over `Q̄`, so the only integer
relation above is `q = 0` and all `c_k = 0`. **Hence no nontrivial exact collision exists**: the
Theorem-A collision mechanism provably does not port to this observation family.

Concrete verified instance (`a=1/5000`, `γ_k ∈ {10,13,17,21,25,30,35,40}`, `g₀=20`, `δ=1/5`):
`10` distinct algebraic exponents; cross-check PSLQ @250 dps, maxcoeff `10⁹` → **no relation**,
consistent with L–W.

**Scope / caveat (load-bearing honesty).** `ĥ_a = exp(−a z²)` corresponds to a **Gaussian** `h`
(Schwartz, **not** `C_c^∞`) — a legitimate analytic observation functional, but the compactly-
supported Paley–Wiener case (`ĥ` entire of exponential type) is **not** covered by Lindemann–
Weierstrass and stays **open**. This proves the OP2 negative **for the Gaussian family only**.

**Structural upshot.** The exact information barrier of Theorem A is intrinsically a **rationality**
phenomenon of the Li encoding: where OP1's Li observations are rational and *always* admit an exact
collision (lattice index `q_min ≥ 1`), the Gaussian Weil observations are provably `Q̄`-independent
and admit **none**. The two regimes are opposite, and the boundary is exactly the arithmetic nature
of the observation values.

## Generalization to a Schwartz-dense class (Hermite–Gaussian)

The L–W argument uses only that each value is `(algebraic)·exp(algebraic exponent)`. So it extends
verbatim to **any** even test function `ĥ(z) = P(z)·e^{−a z²}` with `P` a polynomial with algebraic
coefficients: then `Φ(γ_k) = 2 P(γ_k) e^{β_k}` and the off-line value is an algebraic combination of
`e^{β₊}, e^{β₋}`, all with algebraic coefficients. A nontrivial integer collision is
`Σ_j α_j e^{β_j} = 0` with `α_j` algebraic and **nonzero** (integer multiplicities times the nonzero
`P`-factors — require `P(γ_k) ≠ 0`, i.e. heights off the roots of `P`). L–W kills it, so **no exact
collision**. This covers the **Schwartz-dense algebra** `{P·Gaussian : P even, algebraic coeffs}`.

Verified instance: `ĥ = H_2(√a z) e^{−a z²}` (`a=1/5000`, same rational heights, `P`-factors
`4aγ_k²−2 ≠ 0`); cross-check PSLQ @250 dps, maxcoeff `10⁹` → **no relation**, consistent with L–W.

**Only genuinely open case:** true compact support `h ∈ C_c^∞` (as OP2 states it), where `ĥ` is
entire of exponential type and its values are **periods**, not `exp(algebraic)` — L–W does not apply.
So OP2 as literally posed (`C_c^∞`) remains open; but for the natural analytic/Schwartz families the
answer is a **provable NO**, which pins the difficulty of the open case precisely on the
arithmetic nature (period vs. `exp`-of-algebraic) of Paley–Wiener values.


