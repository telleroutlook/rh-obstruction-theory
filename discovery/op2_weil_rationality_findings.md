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
done. Only test (1) yields a finding. Bounded-height PSLQ on one family = **evidence, not proof**.
