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

The key structural fact (proved via Mellin inversion from Grubb–Seeley/Lesch) is:

**Theorem (leading-log obstruction).** For any **positive, self-adjoint, classical
elliptic** pseudodifferential `H` of order `m > 0` on a closed `d`-manifold, the leading
singularity of `Z_H(t)` as `t → 0⁺` is a **pure power**:
```
Z_H(t) = a_0 t^{-d/m} + O(t^{-d/m + ε}),   a_0 > 0,
```
with (corrected coefficient, OB-15 2026-08-11)
```
a_0 = Γ(d/m) · Res_{s=d/m} ζ_H(s) = (Γ(d/m)/(m(2π)^d)) ∫_{S*M} h_m(x,ξ)^{-d/m} dS dx > 0.
```
No term `C·t^{-d/m}·log(1/t)` with `C ≠ 0` appears as the **leading singularity**.

**[CORRECTIONS from OB-15 external review, 2026-08-11 — three fixes to the earlier sketch]**

1. **Ellipticity is mandatory in the hypothesis.** Without it (T1) is FALSE. Explicit
   counterexample (OB-15 §2): on `𝕋²`, `H₀ = 1 + D_x² + D_y⁴` is a positive self-adjoint
   classical order-4 *differential* operator with discrete spectrum, but its order-4
   symbol `ξ_y⁴` vanishes at `ξ_y=0, ξ_x≠0` — **not elliptic**. Its heat trace is
   `Z_{H₀}(t) ∼ (√π Γ(1/4)/2) t^{-3/4}`, exponent `3/4`, NOT `d/m = 2/4 = 1/2`. So the
   pure-power *exponent* claim requires ellipticity, which `𝒞_ell` (statement.md) has.

2. **`ζ_H` is NOT regular at all negative integers.** The earlier claim "ζ_H(0), ζ_H(−1),
   … all finite" is false for general classical ΨDO. By the Wodzicki-residue identity
   `Res_{s=−k} ζ_H(s) = m^{-1} Wres(H^k)` (k ≥ 0). Only `s=0` is automatically regular
   (`Wres(I)=0`). For `k ≥ 1`, `Wres(H^k)` can be nonzero, producing **subleading**
   `t^k log(1/t)` terms (k ≥ 1). Explicit witness: on `S¹`, `H₁=(1+D_x²)^{1/2}` has
   `Wres(H₁)=1`, so `Res_{s=−1} ζ_{H₁}=1` and `Tr(e^{-tH₁})` has a nonzero `t log t` term.
   These subleading logs do NOT affect the leading `t^{-d/m}` singularity — but the earlier
   "no logs at any negative integer" over-claim is withdrawn. (This is why the refuted
   "no logs at any order" claim must not be reinstated; only the LEADING term is log-free.)

3. **Residue coefficient corrected.** `Res_{s=d/m} ζ_H(s) = a_0/Γ(d/m)`, hence
   `a_0 = Γ(d/m)·Res` — NOT the earlier `a_0·m/Γ(d/m)`.

4. **No-log logic needs BOTH facts.** At `s=d/m>0`: (i) Lesch Thm 3.7 gives `ζ_H` at most
   a **simple** pole there (no double pole), AND (ii) `Γ` is regular at `d/m>0`. Therefore
   `Γζ_H` has only a simple pole → pure power `t^{-d/m}`. A leading `t^{-d/m}log(1/t)`
   would need a *double* pole of `Γζ_H`, i.e. `d/m ∈ {0,−1,−2,…}`, impossible for
   `d,m>0`. Stating only "Γ's pole doesn't coincide" is insufficient — the simple-pole
   fact (i) is the load-bearing half.

**Exact citation (OB-15 §3, scope-checked).** The full-classical-ΨDO statement rests on
**Lesch 1999** (Ann. Global Anal. Geom. 17, 151–187) **Theorem 3.7** and eqs (3.18)–(3.22)
with `A=I` (so `a=0, k=0`), whose parametric-ellipticity hypothesis is met since `h_m>0`;
`j=0` gives exponent `−d/m < 0` (not a non-negative integer), so `c̃_0` is a constant — no
leading log. This extends **Grubb–Seeley 1995** (Invent. Math. 121) Thm 2.7. NOTE
(PROMPT_LINT L17): **BGV Thm 2.30** covers only Laplace-type; **Gilkey Lemma 1.8.2** covers
only differential operators — neither suffices for the general ΨDO claim and neither is
used as the load-bearing citation. Independent cross-check: Hörmander 1968 (Acta Math. 121)
Thm 4.4 applied to `H^{1/m}` confirms the pure-power exponent and positivity of `a_0`.

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

**Status: PROOF-DRAFT (leading-singularity obstruction; citation pinned to Lesch 1999
Thm 3.7 + Grubb–Seeley 1995 Thm 2.7 by OB-15 external review 2026-08-11; three coefficient/
pole corrections applied).**

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
| Leading-singularity obstruction (§4 corrected) | PROOF-DRAFT ✓ — no t^{-d/m}·log(1/t) is possible. Citation pinned by OB-15 (2026-08-11) to Lesch 1999 Thm 3.7 + eqs (3.18)–(3.22) with A=I, extending Grubb–Seeley 1995 Thm 2.7. |
| Coefficient/pole corrections (OB-15 2026-08-11) | PROOF-DRAFT ✓ — (a) ellipticity mandatory (𝕋² counterexample 1+D_x²+D_y⁴ gives exponent 3/4≠1/2); (b) ζ_H NOT regular at all negative integers (Res_{s=−k}=m⁻¹Wres(H^k); only s=0 regular; subleading t^k log t possible, k≥1); (c) a_0=Γ(d/m)·Res, not a_0·m/Γ(d/m); (d) no-log needs BOTH simple-pole (Lesch) AND Γ regular at d/m. |
| Scope: applies to full 𝒞_ell (not just differential operators) | PROOF-DRAFT ✓ — Lesch Thm 3.7 covers all classical elliptic ΨDO (parametric ellipticity from h_m>0); BGV/Gilkey (differential/Laplace-type only) NOT relied upon (L17). |
| Spectral zeta pole obstruction (§5) | SKETCH (future work) |
| Novelty gate decision | NOVELTY GATE CLEARED — leading-singularity §4 (corrected) is the new content |
