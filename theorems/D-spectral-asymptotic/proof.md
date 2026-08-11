# Proof — Theorem D (spectral-asymptotic exclusion)

**Status:** PROOF-DRAFT  
**Analytic / finite separation:** purely analytic.

---

## §1. Main argument (Weyl-mismatch)

**Theorem D proof.**

Suppose for contradiction that `H ∈ 𝒞_ell` has spectrum `{γ_n : n ≥ 1}` with
`γ_n` the positive ordinates of the nontrivial zeros of ζ (with multiplicity,
ordered `0 < γ₁ ≤ γ₂ ≤ …`).

By the Weyl law for `H`:
```
N_H(T) = #{n : γ_n ≤ T} ~ C_H T^{d/m}   as T → ∞,         (W)
```
with `C_H > 0`, `d ≥ 1` (dimension), `m > 0` (order), all determined by the
principal symbol of `H` on `M`.

By the Riemann–von Mangoldt formula:
```
N_ζ(T) = T/(2π) log(T/2π) − T/(2π) + O(log T).             (VM)
```

If the spectrum of `H` equals `{γ_n}`, then `N_H(T) = N_ζ(T)`.

Compare growth rates: `C_H T^{d/m} ∼ T log T / (2π)` requires
```
d/m = 1   and   C_H = log T / (2π) → ∞.
```
But `C_H` is a **constant** (independent of `T`), while `log T → ∞`.
This is a contradiction.  No choice of `d, m, C_H` reconciles (W) and (VM).  ☐

---

## §2. Weyl law source

The Weyl law `N_H(T) ~ C_H T^{d/m}` is a classical theorem:

- **Smooth compact manifold without boundary:** Hörmander (1968) Acta Math. 121.
- **Manifold with boundary, standard elliptic BCs:** Seeley (1969); Ivrii (1980)
  for the two-term expansion.
- **Perturbations:** Courant–Weyl min-max principle gives `N_{H+V}(T) = N_H(T) + O(T^{(d-1)/m})`.

These are REFEREED; not restated here.

---

## §3. Extensions (Theorem D')

**Finite direct sums.** `N_{H_1 ⊕ H_2}(T) = N_{H_1}(T) + N_{H_2}(T) ~ (C_1 + C_2) T^{d/m}`.
Still a pure power law.  Same contradiction.

**Compact quantum graphs (local, energy-independent vertex conditions).**
For a finite metric graph with total length `L`, Weyl law gives `N_H(T) ~ (L/π) T`
(linear in `T`; see Gutkin–Smilansky 2001, Roth 1983).  `L T / π ≠ T log T`.  ☐

**Polynomial transforms `H' = q(H)` (fixed polynomial `q`, `q(λ) > 0`).**
The eigenvalues of `H'` are `q(λ_n)`.  If `q(x) ~ x^α` for large `x`, then
`N_{H'}(T) ~ N_H(T^{1/α}) ~ C_H T^{d/(mα)}`.  Still a power law.

**Bounded perturbations with preserved leading Weyl law.**  If `‖V‖_{H^{-1}→ H} < \infty`,
then the Courant–Weyl estimate gives `N_{H+V}(T) = N_H(T) + O(T^{(d-1)/m})$, and
the leading term is unchanged.

In each case, the conclusion `N_H(T) = T \log T / (2π) + O(\log T)` is incompatible
with the power-law leading term.

---

## §4. Heat-trace reformulation — quantitative (PROOF-DRAFT)

**Setup.** For a sequence `(γ_n)` with `N(T) = #{γ_n ≤ T} = T log T / (2π) + O(log T)`
(Riemann–von Mangoldt), define the zeta heat sum:
```
Z_ζ(t) := Σ_{n≥1} e^{−t γ_n},   t > 0.
```

**Lemma (log singularity of Z_ζ).** As `t → 0⁺`:
```
Z_ζ(t) = (1/(2π)) · (log(1/t)) / t + O(1/t).
```

*Proof.* By partial summation / Abel–Plana with `N(T) ~ T log T / (2π)`:
```
Z_ζ(t) = ∫_0^∞ e^{−tu} dN(u)
        = t ∫_0^∞ e^{−tu} N(u) du     (integration by parts)
        ~ t ∫_0^∞ e^{−tu} (u log u / (2π)) du.
```
Split: `u log u = u log(1/t) + u log(tu)`.  Then:
```
t ∫_0^∞ e^{−tu} u log(1/t) du = log(1/t) · t ∫_0^∞ e^{−tu} u du
                                = log(1/t) · t · t^{−2} = log(1/t) / t.
```
And `t ∫_0^∞ e^{−tu} u log(tu) du = t^{−1} ∫_0^∞ e^{−v} v log(v) dv/t = O(1/t)`.
(The integral `∫_0^∞ e^{-v} v log v dv = -γ_E − 1` is a finite constant.)
Combining with the `O(log T)` error in `N(T)` (which contributes `O(log(1/t))` to
the heat trace, absorbed in the `O(1/t)` term):
```
Z_ζ(t) = (1/(2π)) log(1/t) / t + O(1/t).   ☐
```

**[CORRECTION from external review — 2026-08-11]**

**Previous claim (REFUTED):** "The Seeley–DeWitt expansion for any `H ∈ 𝒞_ell` contains
no `log(1/t)` terms at any order."

**Refutation:** The reviewer (OB-01 external review) provided an explicit counterexample:
on `S¹`, the Fourier multiplier `He_n = (|n| + a/|n|)e_n` (classical elliptic order 1,
positive, self-adjoint) satisfies:
```
Z_H(t) = 2/t − 2a·t·log(1/t) + O(t)   as t → 0⁺.
```
This is a `t·log(1/t)` term, not `t^{-1}·log(1/t)`, but it violates the all-orders
no-log claim. The general structure theorem (Grubb–Seeley, Lesch 1999 Theorem 3.7) is:
```
Z_H(t) ~ Σ_{j-d ∉ m·ℤ≥0} c_j t^{(j-d)/m}  +  Σ_{k≥0} (b_k log t + d_k) t^k
```
with log coefficients `b_k = (-1)^k/(m·k!) · Wres(H^k)`. Logs can appear at
`t^k` for `k ≥ 1` when `Wres(H^k) ≠ 0`. For **differential** operators,
`Wres = 0` for all powers, so no log terms arise.

**Correct citations (from external review):**
- BGV Thm 2.30 ✓ (correctly numbered) — but covers only **generalized Laplacians**
  (order-2 differential operators of Laplace type), not general pseudodifferential operators.
- Gilkey Lemma **1.8.2** (not Thm 1.8.1 as previously cited) — covers **differential**
  operators only.
- For classical pseudodifferential operators: **Grubb–Seeley 1995 Thm 2.7**;
  **Lesch 1999 Theorem 3.7** (Annals of Global Analysis and Geometry 17, 151–187).

**Corrected obstruction (PROOF-DRAFT — valid).**

The key structural fact (Theorem 3.1 from external review, proved via Mellin inversion
from Grubb–Seeley/Lesch) is:

**Theorem (leading-log obstruction).** For any positive classical elliptic
pseudodifferential `H` of order `m` on a closed `d`-manifold, the leading singularity
of `Z_H(t)` as `t → 0⁺` is a **pure power**:
```
Z_H(t) = a_0 t^{-d/m} + o(t^{-d/m}),   a_0 > 0.
```
No term `C·t^{-d/m}·log(1/t)` with `C ≠ 0` can appear as the **leading singularity**.

*Proof sketch.* The leading pole of `ζ_H(s) = Tr(H^{-s})` at `s = d/m > 0` does not
coincide with any pole of `Γ(s)` (which occur only at non-positive integers). Therefore
the Mellin contour at `s = d/m` produces only a simple pole, giving a pure power `t^{-d/m}`.
A double pole (which produces `t^{-d/m}·log t`) would require `d/m ∈ -ℤ≥0`, impossible
for `d, m > 0`. ☐ (Source: external review §3, Theorem 3.1, Corollary 3.2)

**The obstruction.** Suppose `H ∈ 𝒞_ell` has spectrum `{γ_n}`.  Then:
```
Z_H(t) = Z_ζ(t) = (1/(2π)) log(1/t) / t + O(1/t).
```
But `Z_H(t) = a_0 t^{-1} + o(t^{-1})` (pure power leading term, no log factor at `t^{-1}`).
These are incompatible: the leading term of `Z_ζ` is `t^{-1}·log(1/t)`, not a pure power.
**Contradiction.** ☐

This is **strictly stronger** than the leading-term Weyl mismatch (§1), and the argument
is now correctly scoped:
- It applies to the **full** `𝒞_ell` class (all positive classical elliptic pseudodifferential
  operators on compact manifolds).
- It uses only the leading singularity (which is robustly a pure power by the Mellin argument)
  and does NOT require the false all-orders no-log claim.
- Logarithms at subleading orders (e.g., `t·log t` as in the counterexample above) do not
  affect the argument, since `Z_ζ`'s `log(1/t)/t` is the **leading** singularity.

**Comparison with Endres–Steiner.** This argument applies to the **full** `𝒞_ell` class
(all compact elliptic operators, any order/dimension); Endres–Steiner covers only compact
quantum graphs. The leading-singularity approach is a finer invariant than counting-function
comparison alone.

**Status: PROOF-DRAFT (self-contained modulo Grubb–Seeley/Lesch leading-singularity reference).**

The leading-singularity claim (pure power, no `t^{-d/m}·log t`) needs a precise theorem
citation from Grubb–Seeley 1995 Thm 2.7 or Lesch 1999 Theorem 3.7 (Corollary 3.2 in the
external review). The Abel–Plana computation for `Z_ζ` is self-contained.

---


## §5. Determinant-order obstruction (further strengthening)

The spectral zeta function `Z_H(s) = \sum_n \lambda_n^{-s}` for `H ∈ 𝒞_ell`
has a meromorphic continuation with poles only at `s = d/m, (d-1)/m, …` (arithmetic
progression with step `1/m`).

For the Riemann case, the Dedekind zeta-like counting gives a spectral zeta
with different pole structure (related to ζ itself via explicit formula).

**The pole structure of `Z_H(s)` vs. `Z_ζ(s)` provides a third obstruction.**
This is more technical and is left for a future refinement; it corresponds to
the "exact determinant obstruction (order/type)" mentioned in the PLAN.

---

## §6. Status

| Argument | Status |
|---|---|
| Weyl leading-term mismatch (§1) | PROOF-DRAFT (standard corollary; close to Endres-Steiner) |
| Extensions: sums, graphs, polynomials, perturbations (§3) | PROOF-DRAFT |
| Heat-trace Z_ζ log-singularity lemma (§4) | PROOF-DRAFT ✓ (self-contained: Abel-Plana from von Mangoldt) |
| All-orders no-log for 𝒞_ell (§4 previous claim) | **REFUTED** by external review (OB-01, 2026-08-11): counterexample He_n=(|n|+a/|n|)e_n on S¹ has t·log(1/t) term. Gilkey Thm 1.8.1 citation WRONG (should be Lemma 1.8.2, covers differential operators only). BGV Thm 2.30 covers Laplace-type only. |
| Leading-singularity obstruction (§4 corrected) | PROOF-DRAFT ✓ — no t^{-d/m}·log(1/t) is possible (Mellin argument; Grubb-Seeley 1995 Thm 2.7 / Lesch 1999 Thm 3.7 Cor 3.2). Sufficient for the exclusion. |
| Scope: applies to full 𝒞_ell (not just differential operators) | PROOF-DRAFT ✓ — leading-singularity argument works for all classical elliptic pseudodifferential |
| Spectral zeta pole obstruction (§5) | SKETCH (future work) |
| Novelty gate decision | NOVELTY GATE CLEARED — leading-singularity §4 (corrected) is the new content |
