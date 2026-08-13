# Statement — Theorem D' (D-prime-logpoly)

**Theorem ID:** D-prime-logpoly  
**Program ref:** EXT-1 (extension of Theorem D; audit of log-polyhomogeneous escape route)  
**Status:** ESCAPE-ROUTE-REFINED — **Gate-A BLOCKED (OB-31, 2026-08-12) for Claim A's
universal form.** Claim A ("finite-log-degree `𝒞_logpoly` always has a pure-power leading
heat trace, so it is covered by D / is not an escape") is **FALSE as stated**: the class as
defined omits **ellipticity**. Counterexample (OB-31 §3.2): `H=(I−Δ_x)(I−Δ_y)` on `𝕋⁴` is
positive, self-adjoint, classical (log-degree 0), non-elliptic, with `N_H(Λ)~π²Λ log Λ` and
`Z_H(t)~π²t⁻¹log(1/t)` — a **leading log**. The `S¹` witness is correct but does not prove
the universal claim. Survives (narrowed): `𝒞_logpoly^{sub,ell}` (positive **elliptic**
classical principal symbol + strictly-lower-order finite log) — see §0. Claims B/C/D-analytic/E
CONFIRMED (D's numerical anchors corrected). `LEADING-SINGULARITY-COVERS-SUBPRINCIPAL-LOGPOLY` advances PENDING → **INDEPENDENTLY-CHECKED** (OB-33 GATE-A CONDITIONAL → integrated 2026-08-13, M1–M9).

---

## §0. Reframing after OB-31 (Gate-A BLOCKED for Claim A) — READ FIRST

D' is an escape-route audit, not a barrier. OB-31 confirmed most of it but **BLOCKED Claim A's
universal form**:

- **Claim A is false as stated (missing ellipticity).** `𝒞_logpoly` as defined requires only
  "order-`m` ΨDO, finite log-degree symbol" — no ellipticity, positivity of the *principal*
  symbol, or compact-resolvent guarantee. Counterexample: `H=(I−Δ_x)(I−Δ_y)` on `𝕋⁴`
  (`−Δ≥0`), a positive self-adjoint classical 4th-order **differential** operator (log-degree
  0) that is **not** 4th-order elliptic (principal symbol `|ξ_x|²|ξ_y|²` vanishes on the
  coordinate subspaces `{ξ_x=0}∪{ξ_y=0}`). Its spectrum `(1+|p|²)(1+|q|²)` gives
  `N_H(Λ)=π²Λ log Λ+O(Λ)` and (Karamata) `Z_H(t)~π²t⁻¹log(1/t)` — a leading log,
  contradicting the predicted pure power `t^{-d/m}=t⁻¹`. So finite log-degree does **not**
  force a pure-power leading term, and `𝒞_logpoly` (as defined) is **not** shown to be covered
  by D. Ellipticity is a **sufficient** condition here (it guarantees `0 < C_H < ∞`); the
  non-elliptic example shows the universal claim fails without it, but does **not** assert
  that every non-elliptic operator has a leading log. Also refuted: "logs only at `t^k`, `k≥0`"
  (a `𝕋³` sub-principal-log example gives a subleading `t⁻¹log(1/t)`); and Lesch `CL^{m,k}`
  explicitly permits a *top-order* log.
- **Withdrawn:** the universal Claim A over the full finite-log-degree `𝒞_logpoly`, and the
  status "`LEADING-SINGULARITY-COVERS-LOGPOLY` may advance". Renamed
  `LEADING-SINGULARITY-COVERS-SUBPRINCIPAL-LOGPOLY`; was PENDING after OB-31; **advances
  to INDEPENDENTLY-CHECKED after OB-33 GATE-A CONDITIONAL (2026-08-13, M1–M9)**.
- **Survives (narrowed class `𝒞_logpoly^{sub,ell}`):** `H=H*≥−C`, closed manifold, compact
  resolvent, `σ(H)~h_m+Σ_{j≥1}Σ_{ℓ≤K}h_{m−j,ℓ}(log|ξ|)^ℓ` with `h_m` a **uniformly positive
  definite classical elliptic principal symbol** (log terms strictly below the principal
  order). Then the Weyl principal term is fixed by `h_m` alone, so the leading heat trace is a
  positive-coefficient pure power `t^{-d/m}` (Karamata); subleading logs may still occur (the
  earlier "only `t^k`, `k≥0`" is dropped). This is the honest lemma; it does not cover the full
  `𝒞_logpoly`.
- **Confirmed (unchanged):** Claim B (Karamata `N~CΛ log Λ ⇒ Z~Ct⁻¹log(1/t)`), Claim C
  (`S¹`/`ℓ²` not `L²(ℝ)`; `h_0∈S¹_{1,0}`), Claim D **analytic** result (exact `2πn/log(n+e)`
  refuted by `≍T log log T`), Claim E (Lambert-`W`, open-frontier modality). **Claim D's
  numerical table was wrong** (my `1.8→1.14` had a counting-script bug); the correct
  `gap/((T/2π)log log(T/2π))` is `1.81, 1.63, 1.54, 1.48` at `T=10³…10⁶` (re-verified) — the
  `T log log T` conclusion is unchanged.

---

## §1. Context and question

Theorem D (D-spectral-asymptotic) proves that no operator in the class 𝒞_ell (positive
elliptic pseudodifferential operators of any order on any compact smooth manifold) can
have spectrum equal to the Riemann zero ordinates `{γ_n}`. The obstruction is that
𝒞_ell operators have polyhomogeneous Seeley–DeWitt heat-trace expansions with no
`log(1/t)` terms, while `Z_ζ(t) ∼ (1/2π)·log(1/t)/t`.

Theorem D explicitly lists **log-polyhomogeneous operators** as an escape route (escape
item 3 of Theorem D, statement.md §Escape routes).

This document audits that escape route by asking: does the log-polyhomogeneous class
𝒞_logpoly (Schrohe 1992, Lesch 1995, Grubb–Seeley 1995) necessarily fail to reproduce
`Z_ζ(t) ∼ (1/2π)·log(1/t)/t`, or is it a live candidate?

---

## §2. The class 𝒞_logpoly

**Definition.** `H ∈ 𝒞_logpoly` if:
- `H` is a pseudodifferential operator of order `m > 0` on a compact smooth manifold `M`
  of dimension `d`;
- the symbol of `H` has a log-polyhomogeneous expansion:
  ```
  σ(H)(x,ξ) ~ Σ_j (σ_{m-j}(x,ξ) + τ_{m-j}(x,ξ)·log|ξ|)   as |ξ| → ∞,
  ```
  where `σ_{m-j}` is positively homogeneous of degree `m-j` and `τ_{m-j}` is
  positively homogeneous of degree `m-j`.

This class strictly contains 𝒞_ell (when all `τ_k = 0`).

**Key examples:**
- Powers `H^z` for complex `z` (Seeley's complex powers), expanded around non-integer `z`.
- The operator `log H` for `H ∈ 𝒞_ell`.
- Parametrix contributions involving log-symbols in the Grubb–Seeley resolvent calculus.

---

## §3. Heat-trace expansion — CORRECTED (external review OB-01, 2026-08-11)

**[CORRECTION]** The previous §3 stated that for `H ∈ 𝒞_logpoly`, the leading
heat-trace term is `c_{0,1}·t^{-d/m}·log(1/t)`. This is **incorrect as stated**.

The Grubb–Seeley / Lesch theorem (Lesch 1999, Theorem 3.7) gives an expansion for
the **weighted** heat trace `Tr(A·e^{-tP})` where `A` is log-polyhomogeneous and
`P` is a **classical** (non-log) elliptic generator. It does NOT directly give the
expansion of `Tr(e^{-tH})` when `H` itself is log-polyhomogeneous.

**What the external review established (OB-01 §6):**

For `H ∈ 𝒞_logpoly`, log terms in `Z_H(t)` appear at **subleading** orders, not
at the leading singularity. The explicit example: on `S¹`, the Fourier multiplier
```
H_c e_n = (|n| + c·log|n|) e_n
```
(log-polyhomogeneous order 1 with lower-order `c·log|ξ|` term) has:
```
Z_{H_c}(t) = 2/t − 2c·log(1/t) + O(1)   as t → 0⁺.
```
The log term appears at order `t⁰`, not `t^{-1}`. The leading singularity is still
`2/t` (a pure power).

**What produces `t^{-1}·log(1/t)` as a leading term:**

A counting law `N_H(Λ) ~ C·Λ·log Λ` yields `Z_H(t) ~ C·t^{-1}·log(1/t)` by Karamata.
This requires eigenvalues `λ_n ~ n/(C·log n)`, corresponding to a symbol growing like
`|ξ|/log|ξ|`. This is NOT in `𝒞_ell` nor in the finite-log-degree class `CL^{m,k}`.
It is a genuinely different (larger) escape class.

**Revised status of the escape route:**

| Claim | Status after correction |
|---|---|
| `𝒞_logpoly` can have `t^{-1}·log(1/t)` leading term | **FALSE** — leading term is always a pure power (Theorem 3.1 of OB-01 review) |
| `𝒞_logpoly` can have `t^k·log(1/t)` for `k ≥ 0` (subleading) | **TRUE** — Wres formula gives these |
| Escape from Theorem D: the escape class is LARGER than `𝒞_logpoly` | **TRUE** — requires `|ξ|/log|ξ|`-type symbols |
| `𝒞_logpoly` is still an escape from the **all-orders-no-log** version of Theorem D | **TRUE** (but that version of Theorem D was itself refuted) |

---

## §4. Escape-route verdict — REVISED (2026-08-11; refined by OB-16 external review)

**Revised verdict: `𝒞_logpoly` is NOT the correct escape class; the escape class is a
logarithmically-weighted symbol class, and the naive exact model is itself refuted.**

The escape class from Theorem D (corrected leading-singularity version) requires
operators with eigenvalue counting `N_H(T) ~ C·T·log T`, corresponding to symbols of
type `|ξ|/log|ξ|`.

**Corrections from OB-16 external review (2026-08-11):**

1. **Hilbert space must be `S¹` or `ℓ²(ℕ)`, not `L²(ℝ)`.** On `L²(ℝ)` a Fourier
   multiplier `h(ξ)=|ξ|/log|ξ|` has purely continuous spectrum (essential range), and
   `e^{-tH}` is a multiplication operator on a nonatomic space — **not trace class**, no
   discrete eigenvalue count. The valid ΨDO model is the multiplier on the **closed
   manifold `S¹`** (eigenvalues `a|n|/log(|n|+e)`, `n∈ℤ`); a diagonal `ℓ²(ℕ)` model works
   for counting.

2. **The symbol IS in a standard calculus — NOT "outside all standard calculi".** By
   `|∂_ξ^k h_0(ξ)| ≤ C_k⟨ξ⟩^{1-k}/log(e+⟨ξ⟩) ≤ C_k⟨ξ⟩^{1-k}`, `h_0 ∈ S¹_{1,0}`
   (ordinary Hörmander class), more precisely a logarithmically-weighted `S^{1,-1}`-type
   class, elliptic with respect to the weight `w(ξ)=⟨ξ⟩/log(e+⟨ξ⟩)`. It is NOT classical
   polyhomogeneous of any order (so `∉ 𝒞_ell`) and NOT finite-nonnegative-log-degree
   polyhomogeneous (so outside `𝒞_logpoly` under that convention) — but the earlier
   "outside all standard calculi" was too strong.

3. **The EXACT model `λ_n = 2πn/log(n+e)` is REFUTED, not merely open.** After
   normalizing the leading constant (`a=2π` one-sided, `a=4π` on `S¹`), its counting
   differs from `N_ζ` at the next scale:
   ```
   N_{2π}^+(T) − N_ζ(T) = (T/2π)[log log(T/2π) + 1 + o(1)] ≍ T·log log T.
   ```
   Equality of two discrete spectra (with multiplicity) forces equality of counting
   functions; the `T log log T` discrepancy rules out the exact model. So the naive
   `n/log(n+e)` sequence is NOT a Hilbert–Pólya candidate beyond leading order.

**What remains genuinely open (OB-16 §4).** A *subleadingly corrected* `|ξ|/log|ξ|`-type
symbol CAN match even the smooth two-term law: with `g(r)=2πr/W(r/e)` (`W` = Lambert),
`g(r) ~ 2πr/log r` and the continuous inverse reproduces
`x = (T/2π)(log(T/2π) − 1)` exactly (both the `T log T` and `T` terms). It does NOT
reproduce the `O(log T)` remainder, individual spacings, multiplicities, or zero
locations. Whether an unconditional, zero-independent self-adjoint operator in this
broader class has spectrum exactly `{γ_n}` is the open Hilbert–Pólya frontier — a
literature-status statement, not an impossibility theorem.

---

## §5. What this does NOT say

1. **Does not produce a Hilbert–Pólya operator:** The corrected escape class
   (`|ξ|/log|ξ|` symbols) is not known to contain any operator with spectrum `{γ_n}`.

2. **Does not refute Theorem D:** Theorem D (corrected) correctly excludes `𝒞_ell`
   and `𝒞_logpoly` from having a `t^{-1}·log(1/t)` leading heat-trace singularity.

3. **Does not assert any known class contains a Hilbert–Pólya operator.** The
   corrected escape class (`|ξ|/log|ξ|`-type) lies in `S¹_{1,0}` / a log-weighted
   `S^{1,-1}` class (NOT outside standard calculi — OB-16 correction); it is outside
   `𝒞_ell` and finite-log-degree `𝒞_logpoly`, but no operator in it is known to have
   spectrum `{γ_n}`.

---

## §6. New research question (opened by this audit — revised)

**Can a subleadingly-corrected symbol of type `|ξ|/log|ξ|` (elliptic w.r.t. the weight
`w(ξ)=⟨ξ⟩/log(e+⟨ξ⟩)`) produce a self-adjoint operator with spectrum `{γ_n}` in a
controlled Hilbert space, without reading zero locations?**

The naive exact model `λ_n = 2πn/log(n+e)` is **refuted** (OB-16: counting differs from
`N_ζ` by `≍ T log log T`). But a Lambert-`W`-corrected symbol `g(r)=2πr/W(r/e)` matches
both smooth terms `(T/2π)(log(T/2π) − 1)` exactly at the continuous-inverse level. The
open question is whether the broader corrected class contains a genuine, zero-independent
Hilbert–Pólya operator.

**This is recorded as a CONJECTURE / open frontier, not a theorem.** Matching the
counting law (even the two-term law) is necessary but far from sufficient: infinitely
many distinct spectra share a counting asymptotic (e.g. `{λ_n}` and `{λ_n+1}`). A
tautological `diag(γ_n)` violates the zero-independence requirement and has no
explanatory content.

---

## §7. Status summary — REVISED (OB-16 external review 2026-08-11)

| Component | Status |
|---|---|
| Log-polyhomogeneous heat-trace expansion (§3, Lesch 1999) | The theorem is about `Tr(A·e^{-tP})`, not `Tr(e^{-tH})`; citation scope corrected |
| `𝒞_logpoly` produces `t^{-1}·log(1/t)` leading term | **FALSE** — leading term is always a pure power (OB-01 review) |
| `𝒞_logpoly` produces subleading log terms | TRUE — but irrelevant to Theorem D's corrected claim |
| Hilbert space for the escape model | CORRECTED: `S¹`/`ℓ²(ℕ)`, NOT `L²(ℝ)` (continuous spectrum, not trace class) — OB-16 §1.1 |
| Symbol class of `|ξ|/log|ξ|` | CORRECTED: `∈ S¹_{1,0}` (Hörmander), log-weighted `S^{1,-1}`, elliptic w.r.t. `w=⟨ξ⟩/log⟨ξ⟩`; NOT "outside all calculi" — OB-16 §2/§6 |
| Escape model gives `N_H(T) ~ T log T` | CONFIRMED (leading order); heat trace `~ c t^{-1}log(1/t)` (OB-16 Claims A, B) |
| Outside `𝒞_ell` and finite-log-degree `𝒞_logpoly` | CONFIRMED (OB-16 Claim C, Steps 5–6) |
| Exact model `2πn/log(n+e)` as HP candidate | **REFUTED** — differs from `N_ζ` by `≍ T log log T` (OB-16 Claim D, §2.6–2.7) |
| Broader `W`-corrected `|ξ|/log|ξ|` class | OPEN / localized — matches two-term law; zero-independent spectral realization unknown (OB-16 §4) |
| Status of D-prime theorem | **ESCAPE-ROUTE-REFINED**: escape mechanism real at symbol-growth + leading-heat-singularity level; naive exact model refuted; genuine HP realization open |
