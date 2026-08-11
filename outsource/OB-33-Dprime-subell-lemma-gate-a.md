# Problem OB-33 — D' resend: the narrowed 𝒞_logpoly^{sub,ell} leading-singularity lemma

**Type:** Gate-A independent mathematical review (single lemma, scoped).

**What this is.** A **resend** after OB-31 BLOCKED the universal Claim A of D'
(D-prime-logpoly). OB-31 established that the leading-heat-trace obstruction does **not** cover
the full finite-log-degree class `𝒞_logpoly` (the class omits ellipticity; the non-elliptic
`H=(I−Δ_x)(I−Δ_y)` on `𝕋⁴` has a leading `t⁻¹log(1/t)`), and gave an explicit **narrowed**
class + proof route. This package asks the reviewer to verify **only that narrowed lemma**,
which is the honest survivor. No universal `𝒞_logpoly` claim is made.

**Non-circularity (mandatory).** RH is not assumed or used. The only zeta-side input is the
unconditional Riemann–von Mangoldt counting law (a count, no zero location). The lemma is a
statement in spectral geometry; `{γ_n}` appears only as the comparison sequence whose counting
asymptotic (`~(1/2π)T log T`) the pure-power `t^{-d/m}` cannot match. Confirm no RH-import.

---

## All definitions (self-contained)

### The narrowed class `𝒞_logpoly^{sub,ell}`
`H ∈ 𝒞_logpoly^{sub,ell}` iff:
- `M` is a **closed** (compact, boundaryless) smooth `d`-manifold, `d ≥ 1`;
- `H = H* ≥ −C` is self-adjoint with **compact resolvent** (discrete spectrum
  `λ_1 ≤ λ_2 ≤ … → ∞`);
- `H` is a ΨDO of order `m > 0` whose symbol has the **sub-principal-log** expansion
  ```
  σ(H)(x,ξ) ~ h_m(x,ξ) + Σ_{j≥1} Σ_{ℓ=0}^{K} h_{m−j,ℓ}(x,ξ) (log|ξ|)^ℓ   (|ξ|→∞),
  ```
  where `h_m` is a **uniformly positive-definite classical elliptic principal symbol**
  (homogeneous of degree `m`, `h_m(x,ξ) ≥ c|ξ|^m` for `|ξ|≥1`, `c>0`), and **all log terms sit
  at strictly lower order `j ≥ 1`** (finite log-degree `K`).

Heat trace `Z_H(t) = Tr(e^{-tH}) = Σ_n e^{-tλ_n}`; counting `N_H(Λ) = #{n : λ_n ≤ Λ}`.

### Allowed premises (source-verified / REFEREED — to be confirmed by the reviewer)
- **Hörmander (1968), *The spectral function of an elliptic operator*, Acta Math. 121,
  Theorem 1.1 / §4:** for a positive self-adjoint order-1 classical elliptic ΨDO `A` on a
  closed manifold, `N_A(λ) = C_A λ^d + O(λ^{d-1})`, `C_A = (2π)^{-d} vol{h_1(x,ξ)≤1}`.
- **Seeley (1967), Proc. Sympos. Pure Math. 10, pp. 288–307:** `H^{1/m}` is a classical order-1
  elliptic ΨDO, and `N_{H^{1/m}}(λ) = N_H(λ^m)`.
- **Karamata Tauberian / Laplace–Stieltjes (Bingham–Goldie–Teugels 1987, Theorem 1.7.1):** if
  `N(Λ) ~ C Λ^ρ` (`ρ>0`, regularly varying), then `∫ e^{-tλ}dN(λ) ~ C Γ(ρ+1) t^{-ρ}` as
  `t→0⁺`.

---

## The lemma to inspect

**Lemma (`𝒞_logpoly^{sub,ell}` leading term is a pure power).** For `H ∈ 𝒞_logpoly^{sub,ell}`,
```
N_H(Λ) ~ C_H Λ^{d/m},   C_H = (2π)^{-d} vol{(x,ξ) : h_m(x,ξ) ≤ 1} > 0,
Z_H(t) = a_0 t^{-d/m} + o(t^{-d/m}),   a_0 = Γ(d/m+1) C_H > 0.
```
In particular the leading heat-trace singularity is a **positive-coefficient pure power**, with
**no** leading `t^{-d/m}log(1/t)`. (Subleading `t^k log(1/t)` terms may occur and are
irrelevant here.) Consequently no `H ∈ 𝒞_logpoly^{sub,ell}` has spectrum `{γ_n}` (whose heat
sum has a leading `(1/2π)t⁻¹log(1/t)`): the narrowed class is covered by Theorem D.

**Proof.**
1. `H^{1/m}` is order-1 classical elliptic (Seeley 1967) with principal symbol `h_m^{1/m}`; the
   sub-principal log terms of `H` (order `≤ m−1`, times `(log|ξ|)^ℓ = o(|ξ|^{ε})`) are
   `o(|ξ|^m)`, so they do **not** enter the principal symbol of `H^{1/m}` and shift only
   lower-order symbol terms.
2. Hörmander 1968 Thm 1.1 gives `N_{H^{1/m}}(λ) = C λ^d + O(λ^{d−1})` with
   `C = (2π)^{-d}vol{h_m^{1/m}≤1} = (2π)^{-d}vol{h_m≤1} = C_H`. Via `N_H(Λ)=N_{H^{1/m}}(Λ^{1/m})`,
   `N_H(Λ) = C_H Λ^{d/m} + O(Λ^{(d−1)/m})`.
3. Karamata (BGT Thm 1.7.1) on the regularly-varying `N_H` (index `d/m`) gives
   `Z_H(t) = Γ(d/m+1)C_H t^{-d/m} + o(t^{-d/m})`. ∎

**Ellipticity is load-bearing (counterexample — confirm).** Drop ellipticity: on `𝕋⁴`,
`H=(I−Δ_x)(I−Δ_y)` (`−Δ≥0`) is positive, self-adjoint, classical (log-degree 0), compact
resolvent, but its 4th-order principal symbol `|ξ_x|²|ξ_y|²` **vanishes off the axes**
(not elliptic). Its spectrum `(1+|p|²)(1+|q|²)` gives `N_H(Λ)=π²Λ log Λ+O(Λ)` and (Karamata)
`Z_H(t)~π²t⁻¹log(1/t)` — a **leading log**, `d/m=1` but not a pure power. So the positivity of
`vol{h_m≤1}` (finite iff `h_m` elliptic) is exactly what the lemma needs; without it the
principal-symbol volume is infinite and the Weyl asymptotic degrades to `Λ log Λ`.

---

## Links to inspect

**Link A (principal symbol controls the Weyl term).** Confirm the sub-principal log terms
(`order ≤ m−1`, log-weighted) are `o(|ξ|^m)` and hence do not affect `h_m^{1/m}` (the principal
symbol of `H^{1/m}`) nor `C_H = (2π)^{-d}vol{h_m≤1}`. **Confirm** the `H^{1/m}` reduction
(Seeley 1967) and that Hörmander 1968 Thm 1.1 gives `N_H(Λ)=C_H Λ^{d/m}+O(Λ^{(d−1)/m})`.

**Link B (Karamata to the heat trace).** Confirm `N_H(Λ)~C_H Λ^{d/m}` regularly varying ⇒
`Z_H(t)~Γ(d/m+1)C_H t^{-d/m}` (BGT Thm 1.7.1), a pure power, no leading log.

**Link C (ellipticity is necessary).** Confirm the `𝕋⁴` non-elliptic counterexample:
`N_H(Λ)=π²Λ log Λ+O(Λ)`, `Z_H(t)~π²t⁻¹log(1/t)` — so the lemma genuinely requires ellipticity,
and the universal `𝒞_logpoly` claim (without it) is false (this is the OB-31 block, now
respected).

**Link D (comparison with `Z_ζ`).** `Z_ζ(t) = Σ_{γ>0}e^{-tγ} ~ (1/2π)t⁻¹log(1/t)` (RvM +
Abel/Karamata, unconditional). A pure power `a_0 t^{-d/m}` cannot equal it at leading order for
any `(d,m)` (the log is not a power). **Confirm** the exclusion `spec(H) ≠ {γ_n}` for
`H ∈ 𝒞_logpoly^{sub,ell}`.

---

## Gate-A questions

### Q1 — Non-circularity
No RH / RH-equivalent / zero-location used (only the RvM count)? Confirm or exhibit the leak.

### Q2 — The narrowed lemma is correct
Confirm Links A–B: principal-symbol-only Weyl term (sub-principal logs `o(|ξ|^m)`), `H^{1/m}`
reduction, Hörmander constant, Karamata step. Confirm `a_0=Γ(d/m+1)C_H>0`.

### Q3 — Ellipticity load-bearing / block respected
Confirm the `𝕋⁴` counterexample (Link C) and that the lemma is stated **only** for the narrowed
`𝒞_logpoly^{sub,ell}` — i.e. the OB-31 block of the universal `𝒞_logpoly` claim is respected,
not re-asserted.

### Q4 — Citation scope (L17)
Confirm the three premises by author/year/number: Hörmander 1968 Acta 121 Thm 1.1; Seeley 1967
PSPM 10; BGT 1987 Thm 1.7.1. Flag any used beyond scope.

### Q5 — Gate-A verdict
Given Links A–D and Q1–Q4: is the narrowed lemma a correct, non-circular, honestly-scoped
result? May `LEADING-SINGULARITY-COVERS-SUBPRINCIPAL-LOGPOLY` advance PENDING → INDEPENDENTLY-
CHECKED (as a lemma), with D' as a whole staying ESCAPE-ROUTE-REFINED (Claim E open frontier)?

---

## Numerical anchor (sanity only — not an input)

Diagonal `ℓ²` model `λ_n = n^{m/d} + c·n^{(m-1)/d}log n` (elliptic principal + sub-principal
log, `d/m=1`): `t·Z(t)` per-halving-of-`t` increments **shrink** geometrically
(`+0.039, +0.036, +0.032, +0.027, +0.023, +0.019, +0.015`), i.e. `t·Z(t) → const` (≈1) — a
pure power `t⁻¹`, NOT a growing `log(1/t)` (script-verified). Contrast the non-elliptic `𝕋⁴`
model, which genuinely grows like `log(1/t)`. The deliverable is the Links A–D / Q1–Q5
judgment, not this sanity check.

---

## Acceptance criteria (all outcomes decisive)

1. **GATE-A PASS:** Links A–D confirmed, Q1–Q5 answered; verdict "advance the narrowed lemma to
   INDEPENDENTLY-CHECKED; D' stays ESCAPE-ROUTE-REFINED with Claim E open". State any textual
   conditions.
2. **GATE-A CONDITIONAL:** correct modulo a specific fix (e.g. sharpen the `o(|ξ|^m)` argument,
   or the exact BGT hypotheses). Give the edit.
3. **GATE-A BLOCKED:** a genuine gap (e.g. sub-principal logs *do* affect the Weyl term in some
   configuration, or the `H^{1/m}` reduction fails under log-symbols). Identify and exhibit it.

An honest "the narrowed lemma is correct and covers `𝒞_logpoly^{sub,ell}`; the full
`𝒞_logpoly` remains outside (OB-31); D' stays an escape-route audit with an open frontier" is a
valid, first-class outcome.
