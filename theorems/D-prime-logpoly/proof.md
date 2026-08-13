# Proof — Theorem D' (D-prime-logpoly)

**Status:** ESCAPE-ROUTE-REFINED (OB-01 + OB-16 external reviews, 2026-08-11): the
`𝒞_logpoly` escape computation below was REFUTED; the escape class is a
log-*weighted* symbol class, and the exact model is itself refuted. See statement.md
§3–§7 for the current verdict.  
**Analytic / finite separation:** purely analytic.

---

## §0. Correction notice (two rounds: OB-16, then OB-31)

**Round 1 (OB-16).** The original file tried to make `𝒞_logpoly` the escape class by fitting a
**leading** `t^{-1}log(1/t)` log-coefficient `c_{0,1}=(2π)^{-1}`. REFUTED: the genuine escape
class is the log-*weighted* `S^{1,-1}` class (§2), not finite-log-degree `𝒞_logpoly`.

**Round 2 (OB-31, Gate-A BLOCKED).** The *repaired* claim — "every finite-log-degree
`𝒞_logpoly` has a pure-power leading term, hence is covered by D" — is **also false as a
universal**: the class omits **ellipticity**. Counterexample `H=(I−Δ_x)(I−Δ_y)` on `𝕋⁴`
(positive, self-adjoint, classical, log-degree 0, **non-elliptic**) has `N_H~π²Λ log Λ` and a
**leading** `t⁻¹log(1/t)`. The defensible statement is only over the **narrowed**
`𝒞_logpoly^{sub,ell}` (positive elliptic classical principal symbol + strictly-lower-order
finite log) — see §1, where it is proved (mechanism script-verified) and marked PENDING
re-review. Also (OB-31): the `A=I,j=0` Lesch argument is for a classical *elliptic* generator
`P`, and does not transfer to a log-*generator* `H` without ellipticity; and Lesch `CL^{m,k}`
permits a top-order log.

The corrected escape analysis (log-weighted class; exact-model refutation) is in §2 and
statement.md §0/§3–§7.

---

## §1. Leading heat-trace singularity — the NARROWED lemma (OB-31-corrected)

**OB-31 correction.** The earlier universal claim — "*every* finite-log-degree
`H ∈ 𝒞_logpoly` has a pure-power leading heat trace" — is **FALSE**: the class as defined
omits ellipticity. Counterexample `H=(I−Δ_x)(I−Δ_y)` on `𝕋⁴` is positive, self-adjoint,
classical (log-degree 0), non-elliptic, and has `N_H(Λ)~π²Λ log Λ`, `Z_H(t)~π²t⁻¹log(1/t)` —
a **leading log**. So Lesch's `A=I` argument does **not** apply to a general (log-)generator
`H`; it applies to a *classical elliptic* generator `P`. The corrected, defensible statement
is over the narrowed class:

**Lemma (`𝒞_logpoly^{sub,ell}` — leading term is a pure power).** Fix a closed smooth
`d`-manifold `M` (`d ≥ 1`), a positive smooth density `dμ`, a smooth norm `|·|` on `T*M`,
and `K ∈ ℕ₀`. Let `H` be the self-adjoint closure in `L²(M, dμ)` of a scalar formally
self-adjoint elliptic ΨDO of order `m > 0`, with `H ≥ −C` and compact resolvent, whose
symbol has the expansion
```
σ(H)(x,ξ) ~ h_m(x,ξ) + Σ_{j≥1} Σ_{ℓ=0}^{K} h_{m−j,ℓ}(x,ξ) (log|ξ|)^ℓ   (|ξ| → ∞),
```
where each `h_{m−j,ℓ}` is smooth for `ξ ≠ 0` and homogeneous of degree `m−j` for `|ξ| ≥ 1`,
and for every `J ≥ 1` and `ε > 0` the remainder after subtracting `h_m` and the `1 ≤ j < J`
terms satisfies the symbol estimates of `S^{m−J+ε}_{1,0}`; and `h_m` is a **uniformly positive
classical elliptic principal symbol**: `h_m(x,ξ) ≥ c|ξ|^m` for `|ξ| ≥ 1`, `c > 0`. Then:
```
N_H(Λ) ~ C_H Λ^{d/m},   Z_H(t) = a_0 t^{-d/m} + o(t^{-d/m}),   a_0 = Γ(d/m+1)·C_H > 0,
```
where `C_H = (2π)^{-d} ∫_{h_m(x,ξ)≤1} dx dξ` (canonical Liouville volume). Strictly
lower-order terms involving powers of `log(1/t)` may occur and are irrelevant to the
leading-order comparison with `Z_ζ`.

**Proof.**
*Step 1 (Weyl leading term, comparison).* Choose a positive classical elliptic ΨDO `P` of
order `m` on `M` with the same principal symbol `h_m`. By Hörmander (1968), Theorem 4.4
applied to the positive order-1 elliptic `P^{1/m}` (classical complex-power reduction, ibid.
p. 215), `N_P(Λ) ~ C_H Λ^{d/m}`. By the remainder condition, `R := H − P ∈ Ψ^{m−1+ε}_{1,0}`
for every `ε > 0`. Elliptic estimates and Sobolev interpolation give, for each `0 < δ < 1`,
a constant `C_δ` such that `(1−δ)P − C_δ ≤ H ≤ (1+δ)P + C_δ` as quadratic forms. The
min–max principle gives `N_P((Λ−C_δ)/(1+δ)) ≤ N_H(Λ) ≤ N_P((Λ+C_δ)/(1−δ))`. Letting
`Λ → ∞` then `δ ↓ 0`: `N_H(Λ) ~ C_H Λ^{d/m}`.

*Step 2 (Karamata, with negative-spectrum shift).* Let `b` be large enough that `H + b ≥ 1`.
Then `N_{H+b}(Λ) = N_H(Λ − b) ~ C_H Λ^{d/m}`. The counting function is non-decreasing and
right-continuous. By BGT Theorem 1.7.1 (Karamata–Laplace–Stieltjes, ρ = d/m > 0),
`Z_{H+b}(t) ~ C_H Γ(d/m+1) t^{-d/m}`. Since `Z_H(t) = e^{−bt} Z_{H+b}(t)` and
`e^{−bt} → 1` as `t → 0⁺`: `Z_H(t) ~ Γ(d/m+1) C_H t^{-d/m}` — a pure power, no leading
log. ∎

**Riemann–von Mangoldt comparison (Link D).** Let `{γ_n}` denote the multiset of positive
imaginary parts `γ > 0` of all nontrivial zeros `ρ = β + iγ` of `ζ`, counted with analytic
multiplicity; no condition `β = 1/2` is imposed. By Titchmarsh–Heath-Brown (1986), Theorem
9.4 (unconditional), `N_ζ(T) ~ T log T / (2π)`, hence (BGT Thm 1.7.1)
`Z_ζ(t) ~ (1/2π) t⁻¹ log(1/t)`. A pure power `a_0 t^{-d/m}` cannot match a leading
`t⁻¹ log(1/t)` for any fixed `d/m > 0`, so no `H ∈ 𝒞_logpoly^{sub,ell}` has spectrum equal
to `{γ_n}` as a multiset.

**Non-elliptic contrast and necessity caveat.** The `H = (I−Δ_x)(I−Δ_y)` counterexample
(principal-symbol `|ξ_x|²|ξ_y|²` vanishes on the coordinate subspaces `{ξ_x=0}∪{ξ_y=0}`)
genuinely produces a leading `t⁻¹log(1/t)`, confirming that ellipticity is load-bearing.
Ellipticity guarantees `0 < C_H < ∞`; the non-elliptic example shows the universal
`𝒞_logpoly` claim fails without it. This does **not** assert that every non-elliptic operator
has a leading log (there exist non-elliptic operators with finite sublevel volume and a pure-
power leading term).

**What does NOT hold (OB-31).** Over the full finite-log-degree `𝒞_logpoly` — without
ellipticity, or with a top-order log (Lesch `CL^{m,k}` permits `h_{m,k}(log|ξ|)^k`) — the
leading term need **not** be a pure power. So `𝒞_logpoly` (as originally defined) is **not**
shown to be covered by Theorem D; only `𝒞_logpoly^{sub,ell}` is. The lemma
`LEADING-SINGULARITY-COVERS-SUBPRINCIPAL-LOGPOLY` advances PENDING → **INDEPENDENTLY-CHECKED**
(OB-33 GATE-A CONDITIONAL → integrated 2026-08-13, M1–M9).

---

## §2. The genuine escape class (from OB-16) and why the exact model fails

**What produces a leading `t^{-1}log(1/t)`.** By the Abelian/Karamata correspondence, a
leading heat singularity `Z_H(t) ~ c·t^{-1}log(1/t)` is equivalent to a counting law
`N_H(T) ~ c·T·log T`. This requires eigenvalues `λ_n ~ n/log n`, i.e. a symbol growing
like `|ξ|/log|ξ|` — a **log-weighted** class `S^{1,-1}` (elliptic w.r.t. the weight
`w(ξ)=⟨ξ⟩/log(e+⟨ξ⟩)`), **outside** `𝒞_ell` and outside finite-log-degree `𝒞_logpoly`,
but **inside** the ordinary Hörmander class `S¹_{1,0}` (OB-16 §2, §6). So `𝒞_logpoly` is
NOT the escape class; the log-weighted class is.

**The exact model `λ_n = 2πn/log(n+e)` is refuted (OB-16 §2.6).** On `S¹`/`ℓ²(ℕ)`
(NOT `L²(ℝ)`, where the multiplier has continuous spectrum and is not trace class), the
count differs from Riemann–von Mangoldt at the next scale:
```
N_{2π}^+(T) − N_ζ(T) = (T/2π)[log log(T/2π) + 1 + o(1)] ≍ T·log log T.
```
Equal discrete spectra (with multiplicity) force equal counting functions; the
`T log log T` discrepancy excludes the exact model as a Hilbert–Pólya candidate.

**What stays open (OB-16 §4).** A Lambert-`W`-corrected symbol `g(r)=2πr/W(r/e)` matches
even the two-term smooth law `(T/2π)(log(T/2π)−1)` exactly at the continuous-inverse
level (it does not reproduce the `O(log T)` remainder, spacings, multiplicities, or zero
locations). Whether an unconditional, zero-independent self-adjoint operator in this
broader log-weighted class has spectrum exactly `{γ_n}` is the open Hilbert–Pólya
frontier — a literature-status statement, not an impossibility theorem.

---

## §3. Status

| Step | Status |
|---|---|
| Earlier §1 c_{0,1}=(2π)^{-1} "escape via 𝒞_logpoly" | **REFUTED / WITHDRAWN** (OB-01, OB-16) |
| "Leading singularity of full finite-log-degree 𝒞_logpoly is a pure power" | **REFUTED (OB-31)** — needs ellipticity; non-elliptic `(I−Δ_x)(I−Δ_y)` on `𝕋⁴` has a leading log |
| Narrowed lemma: `𝒞_logpoly^{sub,ell}` (pos. elliptic principal symbol + strictly-lower-order log) ⇒ leading pure power `t^{-d/m}` | **INDEPENDENTLY-CHECKED** (§1, OB-33 GATE-A CONDITIONAL → integrated 2026-08-13; comparison/min-max + shifted Karamata; M1–M9) |
| Escape class = log-weighted `S^{1,-1}` (`|ξ|/log|ξ|`), outside 𝒞_ell/𝒞_logpoly, inside `S¹_{1,0}` | PROOF-DRAFT ✓ (OB-16 §2, §6; OB-31 confirmed) |
| Exact model `2πn/log(n+e)` as HP candidate | **REFUTED** — differs from N_ζ by ≍ T log log T (OB-16 §2.6; OB-31 numerics corrected 1.81→1.48) |
| Broader `W`-corrected `\|ξ\|/log\|ξ\|` class | OPEN / localized — matches two-term law; zero-independent spectral realization unknown (OB-16 §4) |
| Hilbert space for the model | `S¹`/`ℓ²(ℕ)`, NOT `L²(ℝ)` (continuous spectrum, not trace class) — OB-16 §1.1 |