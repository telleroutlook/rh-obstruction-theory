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

The Weyl law `N_H(T) ~ C_H T^{d/m}` is a classical theorem. The load-bearing route (used
by Theorem D, closed manifold, no boundary):

- **Order-one scalar elliptic ΨDO on a closed manifold:** Hörmander (1968) *Acta Math.*
  121, **Theorem 4.4** (local spectral function; integrate the diagonal for
  `N_A(λ) ~ C λ^d`).
- **Reduction of `H` (order `m`) to order one:** `H^{1/m}` is a classical order-one
  elliptic ΨDO by Seeley's complex-power calculus — **Seeley (1967)**, *Complex powers of
  an elliptic operator*, Proc. Sympos. Pure Math. **10**, AMS, pp. 288–307 — and
  `N_{H^{1/m}}(λ) = N_H(λ^m)`, so `N_H(T) ~ C_H T^{d/m}`.

(Boundary-value / two-term refinements exist but are **not** used by D, which lives on a
closed manifold; no unspecified "Ivrii 1980" entry is relied upon.)

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

## §4. Heat-trace reformulation — quantitative (PROOF-DRAFT; Z_ζ side INDEPENDENT-CHECKER)

**Setup.** For a sequence `(γ_n)` with `N(T) = #{γ_n ≤ T} = (T/2π)log(T/2π) − T/2π +
O(log T)` (Riemann–von Mangoldt, unconditional — a count only, no zero location), define
the zeta heat sum:
```
Z_ζ(t) := Σ_{n≥1} e^{−t γ_n},   t > 0.
```

**Lemma (log singularity of Z_ζ — exact closed form, OB-19-confirmed).** As `t → 0⁺`:
```
Z_ζ(t) = (1/(2π t)) ( log(1/t) − γ_E − log(2π) ) + O(log(1/t)),
```
so the leading singularity is `(1/2π) · log(1/t)/t`, coefficient **exactly 1/2π**.

*Proof (OB-19 external review, 2026-08-11).* Stieltjes/Abel: `Z_ζ(t) = t ∫_0^∞ e^{−tu}N(u)du`
(boundary term vanishes since `N(u)=O(u log u)`). Write `N = N_main + E`,
`N_main(u) = (u/2π)(log u − log2π − 1)`. Two exact Laplace identities (substitute `v=tu`):
```
t ∫_0^∞ e^{−tu} u du = 1/t,
t ∫_0^∞ e^{−tu} u log u du = (1/t)(1 − γ_E − log t)   [since Γ'(2) = 1 − γ_E].
```
(**Correction:** the earlier draft wrote `∫_0^∞ e^{−v} v log v dv = −γ_E − 1`; the correct
value is `Γ'(2) = 1 − γ_E ≈ 0.42278433510`.) Combining gives the **exact** main-term
identity, valid for every `t > 0`:
```
t ∫_0^∞ e^{−tu} N_main(u) du = (1/(2π t))( log(1/t) − γ_E − log(2π) ).
```
The remainder `t ∫ e^{−tu} E(u) du = O(log(1/t)) = o(1/t)` (see remainder note below), so
it does not affect the leading `t^{-1}log(1/t)` term. ☐

**Remainder-constant caveat (OB-19 V4 discrepancy).** The *qualitative* remainder
`O(log(1/t))` follows from `E(u) = O(log u)`. But an **explicit numerical** constant
`C` in `|t∫e^{−tu}E(u)du| ≤ C log(1/t)` does NOT follow from the bare `O(log T)` in RvM
(that symbol carries no numerical constant). Given an explicit global bound
`|E(u)| ≤ A log(u+2)`, OB-19 proves `C = 2A` for `0 < t ≤ e^{−2}`. A numerical `A`
requires an added premise — e.g. Trudgian (2014, arXiv:1208.5846) explicit `S(T)`/counting
bounds — which is a *stronger* input than the `O(log T)` used here. This does not affect
the leading coefficient `1/2π` (which is exact), only a quantitative remainder certificate.

*Status: leading singularity + coefficient INDEPENDENT-CHECKER (OB-19: symbolic V1 +
110-digit replay at t=10⁻³,10⁻⁶,10⁻⁹; exact ratio `(L−a)/L`, `a=γ_E+log2π`; validates only
the Riemann-side finite/asymptotic identity, not the operator side or RH).*

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
   classical order-4 *differential* operator with discrete spectrum, but its **order-four
   principal symbol** `ξ_y⁴` (the full symbol is `1 + ξ_x² + ξ_y⁴`) vanishes on the nonzero
   covector `(ξ_x, 0)` — **not elliptic**. Its heat trace is
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

**Exact citation (OB-15 §3, scope-checked; SOURCE-VERIFIED in-repo 2026-08-11).** The
full-classical-ΨDO statement rests on **Lesch 1999** (Ann. Global Anal. Geom. 17, 151–187)
**Theorem 3.7**, i.e. the heat expansion `Tr(A e^{-tP}) ∼ Σ_j t^{(j−n−a)/m} c̃_j(log t) +
Σ_j d̃_j t^j` with `deg c̃_j ≤ k` if `(j−a−n)/m ∉ ℤ₊` (else `≤ k+1`). Verified against the
arXiv source dg-ga/9708010 v4 (deposited in `baseline/lesch-dg-ga-9708010/`, see
PROVENANCE.md): the expansion is **published eq. (3.18)** (= preprint eq. `(3.9)`, label
`G1-3.9`), the degree bound is **published (3.19)**, and the Mellin/pole statement is
**published (3.20)** (= preprint `(3.10)`); all are consequences of **Theorem 3.7**
(= preprint Theorem `S1-3.5`). Cite **Theorem 3.7 + (3.18)/(3.19)/(3.20)** (the
version-independent anchor is the theorem number; in the *published* text a bare "(3.9)"
denotes a different equation — a preprint-vs-published renumbering, see PROVENANCE.md).
With `A=I` (so `a=0, k=0`) and `j=0`, the exponent
`−d/m < 0` is not a non-negative integer, so `c̃_0` is a constant — **no leading log**,
exactly as needed. The proof follows **Grubb–Seeley 1995** (Invent. Math. 121) Thm 2.7
(cited within Lesch's proof). NOTE
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

This is a **refinement** of the leading-term Weyl mismatch (§1) — not a logically stronger
exclusion within `𝒞_ell`, but a sharper description of the *same* spectral-asymptotic
obstruction (see the note below), and the argument is now correctly scoped:
- It applies to the **full** `𝒞_ell` class (all positive classical elliptic pseudodifferential
  operators on compact manifolds).
- It uses only the leading singularity (which is robustly a pure power by the Mellin argument)
  and does NOT require the false all-orders no-log claim.
- Logarithms at subleading orders (e.g., `t·log t` as in the counterexample above) do not
  affect the argument, since `Z_ζ`'s `log(1/t)/t` is the **leading** singularity.

**Two mutually reinforcing formulations, not two independent obstructions (OB-25 Q5).**
The heat trace is the Laplace–Stieltjes transform of the counting measure,
`Z(t) = ∫ e^{-tT} dN(T)`, so by Abel/Tauber theory for regularly varying `N` the
Weyl-counting leading term (`T^{d/m}` vs `(2π)^{-1}T log T`) and the heat-trace leading
singularity (`t^{-d/m}` vs `(2π)^{-1}t^{-1}log(1/t)`) are **the same** leading-order fact
in two languages. Within `𝒞_ell` the heat-trace formulation does **not** exclude any
operator the Weyl formulation misses; its value is a cleaner "leading-singularity *type*"
statement and the explicit separation of the impossible **leading** log from permissible
**subleading** logs. So D should be read as one obstruction with two formulations, not a
weaker + a stronger theorem.

**Comparison with prior art (Endres–Steiner; Watson–Valentinuzzi).** The `𝒞_ell` scope
here (all positive classical elliptic ΨDOs on a closed manifold, any order/dimension) is
broader than Endres–Steiner (2010), who obtain a Weyl-law no-go only for the two
Berry–Keating families `H_BK`, `H_BK²` on compact metric graphs (Thms 15.4–15.6) — graphs
are not closed smooth manifolds. Watson–Valentinuzzi (2026) state a closely related
leading-log obstruction for elliptic **differential** operators on compact manifolds. D's
identifiable increment is (a) extending from differential to the full classical elliptic
**ΨDO** class via Lesch's `Tr(Ae^{-tP})` expansion, and (b) the leading-vs-subleading log
distinction. Accordingly D is positioned as a **scope-extension / corollary**, not an
unprecedented standalone obstruction (see novelty.md).

**Status: PROOF-DRAFT (leading-singularity obstruction; citation SOURCE-VERIFIED in-repo
to Lesch 1999 Theorem 3.7 + heat expansion (3.18)/(3.19)/(3.20) [published] = preprint
`(3.9)`/`(3.10)`, baseline/lesch-dg-ga-9708010/; three coefficient/pole corrections applied
per OB-15; citation/positioning corrected per OB-25).**

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
| Weyl leading-term mismatch (§1) | PROOF-DRAFT (standard corollary; close to Endres–Steiner 2010, and to Watson–Valentinuzzi 2026 for differential operators) |
| Extensions: sums, graphs, polynomials, perturbations (§3) | PROOF-DRAFT |
| Heat-trace Z_ζ log-singularity lemma (§4) | PROOF-DRAFT ✓ + **INDEPENDENT-CHECKER** (OB-19 2026-08-11): exact closed form (1/2πt)(log(1/t)−γ_E−log2π), leading coeff exactly 1/2π; symbolic V1 + 110-digit replay. Fixed constant Γ'(2)=1−γ_E (earlier draft had −γ_E−1). V4 numerical remainder C=2A is conditional on an explicit \|E(u)\|≤A log(u+2) (e.g. Trudgian 2014), NOT derivable from bare O(log T). |
| All-orders no-log for 𝒞_ell (§4 previous claim) | **REFUTED** by external review (OB-01, 2026-08-11): counterexample He_n=(|n|+a/|n|)e_n on S¹ has t·log(1/t) term. Gilkey Thm 1.8.1 citation WRONG (should be Lemma 1.8.2, covers differential operators only). BGV Thm 2.30 covers Laplace-type only. |
| Leading-singularity obstruction (§4 corrected) | PROOF-DRAFT ✓ — no t^{-d/m}·log(1/t) is possible. Citation SOURCE-VERIFIED in-repo (2026-08-11; OB-25-checked) to Lesch 1999 **Theorem 3.7 + published (3.18)/(3.19)/(3.20)** (= preprint (3.9)/(3.10); baseline/lesch-dg-ga-9708010/, exact content match), extending Grubb–Seeley 1995 Thm 2.7. |
| Coefficient/pole corrections (OB-15 2026-08-11) | PROOF-DRAFT ✓ — (a) ellipticity mandatory (𝕋² counterexample 1+D_x²+D_y⁴ gives exponent 3/4≠1/2); (b) ζ_H NOT regular at all negative integers (Res_{s=−k}=m⁻¹Wres(H^k); only s=0 regular; subleading t^k log t possible, k≥1); (c) a_0=Γ(d/m)·Res, not a_0·m/Γ(d/m); (d) no-log needs BOTH simple-pole (Lesch) AND Γ regular at d/m. |
| Scope: applies to full 𝒞_ell (not just differential operators) | PROOF-DRAFT ✓ — Lesch Thm 3.7 covers all classical elliptic ΨDO (parametric ellipticity from h_m>0); BGV/Gilkey (differential/Laplace-type only) NOT relied upon (L17). |
| Spectral zeta pole obstruction (§5) | SKETCH (future work) |
| Positioning (OB-25 Q5) | SCOPE-EXTENSION / COROLLARY — the ΨDO-class extension + leading-vs-subleading-log distinction is the identifiable increment over Endres–Steiner (graphs) and Watson–Valentinuzzi (differential operators); NOT marketed as standalone novelty. |
