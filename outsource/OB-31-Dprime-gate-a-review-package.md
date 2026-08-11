# Problem OB-31 — D' Gate-A package: independent review of the log-polyhomogeneous escape-route audit

**Type:** Gate-A independent mathematical review (whole-document inspection, scoped).

**What this is.** A request to **independently inspect Theorem D' (D-prime-logpoly)** and
issue a **Gate-A verdict**. D' is **not a barrier and not a positive theorem** — it is an
*escape-route audit* of Theorem D: it asks whether the log-polyhomogeneous class is the
escape from D's heat-trace obstruction, and reaches a **negative refinement** plus a precise
localization. Concretely D' establishes:
1. **The leading-singularity obstruction of Theorem D EXTENDS to finite-log-degree
   `𝒞_logpoly`** — such operators have a pure-power leading heat-trace term; logs appear
   only at subleading orders. So **`𝒞_logpoly` is NOT an escape** (this *narrows* D's escape
   frontier — a hardening of D, not a widening).
2. **The genuine escape class** is a log-*weighted* symbol class `S^{1,-1}` (`|ξ|/log|ξ|`-
   type), which gives `N_H(T) ~ c·T log T` and a genuine leading `t^{-1}log(1/t)`; it lies
   outside `𝒞_ell` and outside finite-log-degree `𝒞_logpoly`, but **inside** the ordinary
   Hörmander class `S¹_{1,0}`.
3. **The naive exact model `λ_n = 2πn/log(n+e)` is REFUTED** (its counting differs from the
   Riemann–von Mangoldt law by `≍ T log log T`).
4. Whether the broader (Lambert-`W`-corrected) log-weighted class contains a genuine,
   zero-independent Hilbert–Pólya operator is an **honest open frontier — a
   literature-status statement, NOT an impossibility theorem and NOT a claim about RH.**

The review targets: whether (1) is correctly proved, whether (2)'s symbol-class placement is
right, whether (3)'s discrepancy is correct, and whether (4) is stated with the right (non-
overclaiming) modality.

**Non-circularity (mandatory).** RH is not assumed and not used. `{γ_n}` appears only as the
target ordinate sequence whose *counting law* is compared; no zero location or reality is
used. The open-frontier statement (4) explicitly forbids a tautological `diag(γ_n)` (which
would read zero locations and has no explanatory content). Confirm no RH-import.

---

## All definitions (self-contained)

### Theorem D (the parent, for reference)
No positive classical **elliptic** ΨDO on a closed manifold (`𝒞_ell`) has spectrum `{γ_n}`,
because its heat trace `Z_H(t) = Tr(e^{-tH})` has a **pure-power** leading singularity
`a_0 t^{-d/m}` (Lesch 1999 Thm 3.7, `A=I`), while the Riemann side
`Z_ζ(t) := Σ_{γ>0} e^{-tγ} ∼ (1/2π) t^{-1} log(1/t)` carries a **leading log**. (Theorem D is
INDEPENDENTLY-CHECKED, Gate-A PASS OB-25.)

### The class `𝒞_logpoly` (finite log-degree)
`H ∈ 𝒞_logpoly` if it is a ΨDO of order `m>0` on a compact `d`-manifold whose symbol has a
**log-polyhomogeneous** expansion
`σ(H)(x,ξ) ∼ Σ_j (σ_{m-j}(x,ξ) + τ_{m-j}(x,ξ) log|ξ|)`, `σ_{m-j}, τ_{m-j}` homogeneous of
degree `m-j` (finitely many log powers per order — `CL^{m,k}`). Contains `𝒞_ell` (all
`τ_k=0`). Examples: `log H`, `H^z` (complex powers), Grubb–Seeley resolvent parametrix
contributions.

### The log-weighted class `S^{1,-1}` (`|ξ|/log|ξ|`-type)
`h_0(ξ) = ⟨ξ⟩/log(e+⟨ξ⟩)`, elliptic w.r.t. the weight `w(ξ)=⟨ξ⟩/log(e+⟨ξ⟩)`. From
`|∂_ξ^k h_0(ξ)| ≤ C_k ⟨ξ⟩^{1-k}/log(e+⟨ξ⟩) ≤ C_k⟨ξ⟩^{1-k}`, `h_0 ∈ S¹_{1,0}` (ordinary
Hörmander), a log-weighted `S^{1,-1}` class — **NOT** classical polyhomogeneous of any order
(∉ `𝒞_ell`) and **NOT** finite-log-degree (∉ `𝒞_logpoly`), but **not** "outside all standard
calculi" (that earlier phrasing was too strong — OB-16).

---

## The claims to inspect

**Claim A (𝒞_logpoly leading term is a pure power — the obstruction covers it).**
For `H ∈ 𝒞_logpoly` (finite log-degree), the **leading** heat-trace singularity is a pure
power `t^{-d/m}`; log terms appear only at **subleading** orders `t^k log(1/t)` (`k≥0`, from
`Wres(H^k)`). Explicit witness (on `S¹`): the Fourier multiplier `H_c e_n=(|n|+c log|n|)e_n`
has `Z_{H_c}(t) = 2/t − 2c log(1/t) + O(1)` — the log sits at order `t⁰`, NOT `t^{-1}`; the
leading term is `2/t`. **Consequence:** `𝒞_logpoly` cannot match the leading
`Z_ζ ∼ (1/2π) t^{-1}log(1/t)`, so it is **not** an escape from D — D's obstruction *extends*
to it. **Confirm** (a) the `S¹` witness computation, (b) that finite log-degree forces the
leading log to be absent, and (c) the correct citation scope: Lesch 1999 Thm 3.7 is about
`Tr(A e^{-tP})` with `P` **classical** (non-log); it does not *directly* give `Tr(e^{-tH})`
for log-`H`, so the argument is the direct symbol/Karamata computation, not a misapplication
of Lesch.

**Claim B (the escape class is `|ξ|/log|ξ|`-type, giving `T log T`).**
A counting law `N_H(Λ) ∼ C Λ log Λ` yields `Z_H(t) ∼ C t^{-1} log(1/t)` by Karamata; this
needs eigenvalues `λ_n ∼ n/(C log n)`, i.e. a symbol `~ |ξ|/log|ξ|`. **Confirm** the Karamata
Tauberian step and that this symbol class is `S¹_{1,0}` / log-weighted `S^{1,-1}` (Hörmander),
outside `𝒞_ell`/`𝒞_logpoly` but not "outside all calculi".

**Claim C (Hilbert space discipline — L20).** On `L²(ℝ)` the Fourier multiplier
`h_0(ξ)=|ξ|/log|ξ|` has **purely continuous** spectrum (essential range) and `e^{-tH}` is a
multiplication operator on a nonatomic space — **not trace class**, no discrete count. The
valid ΨDO model is the multiplier on the **closed manifold `S¹`** (eigenvalues
`a|n|/log(|n|+e)`, `n∈ℤ`) or a diagonal `ℓ²(ℕ)` model. **Confirm** the discrete-spectrum
analysis is done on `S¹`/`ℓ²`, never `L²(ℝ)`.

**Claim D (the exact model is REFUTED, not merely open).** With the leading constant
normalized (`a=2π` one-sided), the model `λ_n = 2πn/log(n+e)` has one-sided counting
`N^+(T)` with
```
N^+(T) − N_ζ(T) = (T/2π)[log log(T/2π) + 1 + o(1)] ≍ T log log T.
```
Equality of two discrete spectra (with multiplicity) forces equality of counting functions;
the `T log log T` discrepancy rules out the exact model. **Confirm** the discrepancy
asymptotic (script sanity: the gap grows and `gap/(T log log T)` stays bounded ≈ O(1),
approaching `1/2π·(log log+1)` — checked at `T=10³…10⁶`).

**Claim E (open frontier — correct modality).** A Lambert-`W`-corrected symbol
`g(r)=2πr/W(r/e)` (`W`=Lambert) has `g(r) ∼ 2πr/log r` and its continuous inverse reproduces
the **two-term** smooth law `x=(T/2π)(log(T/2π)−1)` exactly — but NOT the `O(log T)`
remainder, individual spacings, multiplicities, or zero locations. Whether an unconditional,
zero-independent self-adjoint operator in this broader class has spectrum exactly `{γ_n}` is
the **open Hilbert–Pólya frontier**. **Confirm** this is stated as a conjecture/frontier
(not a theorem), that matching a counting law is explicitly acknowledged as necessary-but-
far-from-sufficient (infinitely many spectra share an asymptotic; `{λ_n}` vs `{λ_n+1}`), and
that the tautological `diag(γ_n)` is explicitly excluded.

---

## Gate-A questions (the deliverable)

### Q1 — Non-circularity
Confirm no step uses RH, an RH-equivalent, or ζ-zero locations; only the RvM *counting law*
enters, and the open-frontier statement forbids reading zero locations.

### Q2 — Claim A is correct (the key positive content: 𝒞_logpoly is covered)
Confirm that finite-log-degree `𝒞_logpoly` has a pure-power leading heat-trace term (logs
only subleading), via the `S¹` witness and the general symbol argument, with the Lesch
citation scope correctly stated (Thm 3.7 is `Tr(A e^{-tP})`, `P` classical — not a direct
`Tr(e^{-tH})` for log-`H`). This is what makes D' a *hardening* of D, not a widening.

### Q3 — Symbol-class placement (Claim B/C, L20)
Confirm `|ξ|/log|ξ| ∈ S¹_{1,0}` (log-weighted `S^{1,-1}`), outside `𝒞_ell`/`𝒞_logpoly` but
NOT "outside all standard calculi"; and that the discrete-spectrum model is on `S¹`/`ℓ²(ℕ)`,
never `L²(ℝ)` (continuous spectrum, not trace class).

### Q4 — Claim D discrepancy (`T log log T`)
Confirm the exact model `2πn/log(n+e)` is refuted by an `≍ T log log T` counting discrepancy
against `N_ζ` (after leading-constant normalization), and that this correctly downgrades it
from "open" to "refuted beyond leading order".

### Q5 — Open-frontier modality (no overclaim)
Confirm Claim E is stated with the correct modality: a conjecture/open frontier, matching-
law-is-not-sufficient explicitly acknowledged, tautological `diag(γ_n)` excluded, no
impossibility theorem asserted, no RH claim. (This is the "does not overclaim" check.)

### Q6 — Citation scope (L17)
Confirm the citation scope corrections: Lesch 1999 Thm 3.7 (general classical elliptic ΨDO,
weighted trace) is load-bearing; BGV Thm 2.30 (Laplace-type only) and Gilkey **Lemma 1.8.2**
(differential only; NOT "Thm 1.8.1") are scope-limited and not load-bearing; Grubb–Seeley
1995 Thm 2.7 is the resolvent-expansion source.

### Q7 — Gate-A verdict + status
Given Claims A–E and Q1–Q6: is D' a correct, non-circular, honestly-scoped escape-route
audit? Its natural status is **ESCAPE-ROUTE-REFINED** (not a barrier, not INDEPENDENTLY-
CHECKED as a theorem). Confirm the two dependencies that would advance —
`LEADING-SINGULARITY-COVERS-LOGPOLY` (currently PENDING) — is correctly proved (Claim A/B),
so it can move PENDING → INDEPENDENTLY-CHECKED as a *lemma*, while the D' document as a whole
stays an audit whose open part (Claim E) remains a frontier. Or identify a specific gap.

---

## Numerical anchor (sanity only — not an input)

- Claim D (script-checked): with `λ_n=2πn/log(n+e)`, the one-sided count minus `N_ζ` grows,
  and `gap/((T/2π)·log log(T/2π))` stays ≈ O(1) (≈ 1.8 → 1.45 → 1.25 → 1.14 at
  `T=10³,10⁴,10⁵,10⁶`, decreasing toward the predicted `1 + 1/log log`), confirming a
  `≍ T log log T` discrepancy — the exact model is refuted.
- Claim A witness (on `S¹`): `H_c e_n=(|n|+c log|n|)e_n` ⇒ `Z_{H_c}(t)=2/t−2c log(1/t)+O(1)`,
  log at order `t⁰`, leading term `2/t` (pure power).
The Gate-A deliverable is the whole-document judgment (Claims A–E, Q1–Q7), not a re-run.

---

## Acceptance criteria (all outcomes decisive)

1. **GATE-A PASS:** Claims A–E confirmed, Q1–Q7 answered with no blocking gap; verdict
   "D' is a correct escape-route audit; `LEADING-SINGULARITY-COVERS-LOGPOLY` may advance to
   INDEPENDENTLY-CHECKED as a lemma; the document stays ESCAPE-ROUTE-REFINED with Claim E an
   open frontier". State any required textual conditions.
2. **GATE-A CONDITIONAL:** correct but a specific textual fix is required (e.g. sharpen the
   Karamata step, restate the modality of Claim E). Give the exact edit.
3. **GATE-A BLOCKED:** a genuine gap, circularity, RH-import, or overclaim (e.g. Claim E
   stated as more than a frontier) exists. Identify it, exhibit it, give the minimal repair.

An honest "the negative refinement (Claims A–D) is correct and hardens D; Claim E is a
correctly-hedged open frontier; publish as a short remark/appendix to Paper B, not a
standalone result" is a valid, first-class outcome.
