# Paper C — Outline
# Real-Rooted Approximants and the Missing Compactness Theorem in Spectral Approaches to RH

**Working title:** Real-Rooted Approximants and the Missing Compactness Theorem in
Spectral Approaches to the Riemann Hypothesis  
**Target:** ~20 pages; research paper  
**Theorem files:** `theorems/E-compactness/`  
**Status:** PROOF-DRAFT complete (E-neg + E-pos both self-contained); ready for review

---

## Abstract (draft)

We study the gap between finite matching evidence and locally uniform convergence
in spectral approaches to the Riemann Hypothesis — specifically in the CCM framework
(Connes–Consani–Moscovici 2025) where RH follows if suitably normalized spectral
determinants converge to the Riemann Ξ function.

**Theorem E-neg (non-uniqueness / information obstruction):** A finite evidence record
ℰ_N (first k_N zero pairs, normalization, first J_N Taylor coefficients of an entire
function) does not uniquely determine the locally uniform limit. We construct explicit
pairs of entire functions satisfying ℰ_N that are ε-separated on any disk |z| ≤ R₀.
The separation is quantified: using the Hadamard product growth |Ξ(Ri)| → ∞ and a
Vandermonde-type implicit function theorem for the Taylor matching step.

**Theorem E-pos (sufficient conditions for convergence and real-rooted limit):** A
sequence (Fₙ) satisfying ℰ_N together with four additional hypotheses — (H-norm)
pointwise normalization, (H-bound) local uniform boundedness, (H-tail) tail zero
control, (H-modulus) modulus matching — converges locally uniformly to Ξ, and every
limit point has only real zeros. The proof uses the Montel normal family theorem,
Vitali's convergence theorem, and Hurwitz's theorem.

**Application to CCM:** The CCM framework satisfies (H-norm) and the finite matching
conditions ℰ_N. The missing ingredients for convergence are (H-bound) and (H-tail)
— the precise estimates needed to rule out the non-uniqueness case.

---

## §1. Introduction and context

**The CCM spectral approach.** Connes–Consani–Moscovici (arXiv:2511.22755) construct
a sequence of spectral triples whose regularized determinants satisfy
det_reg(𝔇 − z) = −i λ^{−iz} ξ̂(z), where ξ̂ is entire with all zeros real and equal
to the spectrum. As N, λ → ∞, these are conjectured to converge to the Riemann Ξ
function after suitable normalization; RH would follow via Hurwitz's theorem.

**The normalization issue.** The λ^{−iz} phase preserves zeros but is not bounded
on compact sets as λ → ∞ — it is the "normalization trap" for the convergence track.
The CCM open step ("suitably normalized") is load-bearing.

**What this paper does and does not claim.**
- Does NOT assert that CCM fails.
- Does NOT assert that RH is false.
- DOES give the precise list of conditions that separate "finite evidence" from
  "convergence to Ξ."
- DOES provide a counterexample sequence showing finite evidence alone is insufficient.

---

## §2. Setup

- **CCM normalization:** the entire function Ξ(z) = ξ(1/2 + iz); all zeros real.
  Distinct from the Suzuki meromorphic target z²ξ/ξ' (poles at zeros). These
  normalizations must never be conflated.
- **Finite evidence record ℰ_N:** entire order 1, even, real on ℝ, real zeros,
  first k_N zeros match Riemann, normalization F(0) = Ξ(0), first J_N Taylor coefficients.
- **Normal family package (E-pos):** (H-bound), (H-tail), (H-modulus), (H-norm).

---

## §3. Theorem E-neg

**Statement.** For any ε > 0 and any N, there exists an entire function F ≠ Ξ
satisfying all conditions of ℰ_N with sup_{|z| ≤ R₀} |F(z) − Ξ(z)| ≥ ε for
some R₀ = R₀(N, ε).

**Proof strategy.**
1. Construct F = F^{(c₀)}: perturb tail zeros μₙ = γₙ(1 + c₀/(n−k_N)) for n > k_N.
2. Match first J_N Taylor coefficients via a Vandermonde Jacobian (IFT argument,
   same structure as B2 §4.3; Jacobian is a generalized Vandermonde in μₙ⁻²).
3. Quantify: |F(Ri)/Ξ(Ri)| = product ratio bounded away from 1 at R = γ_{k_N+1}.
4. Conclude via |Ξ(Ri)| → ∞: proved from Hadamard product directly
   (∏ₙ(1 + R²/γₙ²) ≥ 2^N where N ∼ R log R / 2π).

**Key point.** The construction is self-contained — no external Stirling/functional
equation reference needed. The Hadamard product growth is elementary.

---

## §4. Theorem E-pos

**Statement.** If (Fₙ) satisfies ℰ_N and (H-norm) + (H-bound) + (H-tail) + (H-modulus),
then Fₙ → Ξ locally uniformly, and every accumulation point of zeros of Fₙ is a zero
of Ξ (all real). In particular: if Ξ has only real zeros, this gives real-rootedness
of the limit.

**Proof.** Montel (H-bound → normal family) + Vitali (H-norm pins the limit) +
Hurwitz (H-tail transfers real zeros). Hadamard uniqueness: order-1 entire function
with same zeros as Ξ and same value at one point is equal to Ξ.

---

## §5. Application to CCM

The CCM spectral triple sequence satisfies:
- ✓ ℰ_N conditions (by construction of the determinant identity).
- ✓ (H-norm) via the det_reg identity at z = 0 (after normalization).
- ✗ **(H-bound) — OPEN:** locally uniform bound on |det_reg| not established.
- ✗ **(H-tail) — OPEN:** tail zero control (convergence of high zeros to ζ zeros).

These are the precise missing ingredients. The paper does not claim they hold or fail;
it identifies them as the exact gap between the finite evidence and convergence.

---

## §6. Escape routes

1. **Non-CCM frameworks:** other spectral approaches (Suzuki meromorphic target, etc.)
   are not covered. The E-pos/E-neg theorems apply to the CCM entire-Ξ normalization only.
2. **Additional structure:** if CCM determinants satisfy (H-bound) and (H-tail) by
   some other argument, convergence follows from E-pos.
3. **Weaker conclusion:** the non-uniqueness (E-neg) applies to the class of all entire
   functions satisfying ℰ_N; it does not rule out convergence for the specific CCM sequence.

---

## §7. Novelty statement

The combination of (i) an explicit quantitative counterexample sequence (E-neg) and
(ii) a sufficient conditions package (E-pos) for the CCM convergence question appears
to be new. Prior work (e.g., Burnol 2001, Lagarias 2002) identifies conditions for
de Bruijn-Newman type results; the CCM framework is more recent (2025) and the present
analysis is specific to its entire-target normalization. The self-contained Hadamard
growth argument for |Ξ(Ri)| → ∞ may also be of independent interest.

---

## §8. Submission target

- **Venue (provisional):** Mathematische Annalen / Journal für die reine und angewandte
  Mathematik (full paper)
- **Length:** ~20 pages
- **Dependencies for submission:** independent review of E-neg Vandermonde IFT step;
  independent check that E-pos (Montel/Hurwitz) proof is complete.
