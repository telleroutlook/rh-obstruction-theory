# Two Corollary-Level No-Go Observations for Spectral and Euler-Product Approaches to RH

*Draft manuscript (Tier-2 note). Presents Theorem D and Theorem C as **attributed
corollaries / scope-extensions**, not standalone novelty, per their Gate-A reviews (OB-25,
OB-26). Sources: `theorems/{D-spectral-asymptotic, C-euler-tail}/`; authoritative status in
`docs/STATUS.md`.*

**Status of this draft:** short note (~6–8 pp). Both results are INDEPENDENTLY-CHECKED
(whole-theorem Gate-A review). Their reviews determined that neither is a standalone new
theorem: **D** is a scope-extension of Endres–Steiner [2010] and Watson–Valentinuzzi [2026];
**C** is a one-sided corollary of Andersson [2024, Thm 5]. This note is framed accordingly.
**It must not be read as a standalone barrier paper, and it does not fold in D'
(D-prime-logpoly), which is Gate-A BLOCKED** (see the closing remark).

---

## Abstract

We record two no-go observations, each an explicitly attributed corollary of published work,
for two families of spectral/arithmetic approaches to the Riemann Hypothesis (RH).

- **(D) A heat-trace leading-log exclusion for classical elliptic pseudodifferential
  operators.** No positive self-adjoint classical elliptic pseudodifferential operator of
  finite order on a closed manifold has spectrum equal to the multiset `Γ_ζ^+` of positive
  imaginary parts of the nontrivial zeros of `ζ`. This is a *scope-extension* of the
  quantum-graph result of Endres–Steiner and the elliptic-differential result of
  Watson–Valentinuzzi: the increment is the passage to the full classical elliptic ΨDO class
  and the leading-vs-subleading-log distinction.

- **(C) Finite Euler factors do not force critical-line zeros in the Helson class.** Fixing
  finitely many Euler factors of a Helson zeta function to the standard value does not force
  its strip zeros onto the critical line. This is a *one-sided corollary* of Andersson's
  prescribed-zero theorem [2024, Thm 5].

**Neither result proves, disproves, or approaches RH.** Both are no-go statements for a method
class, hold regardless of RH, and are stated here with explicit attribution to the prior work
of which they are corollaries.

---

## 1. Introduction and scope discipline

The two observations below share a structure with the finite-observable obstructions of the
companion paper [Paper A]: a method class sees a limited observation, and that observation
fails to determine the target predicate. What distinguishes the present note is honesty about
**novelty**: whole-theorem independent review (OB-25 for D, OB-26 for C) found that each
result, correct and RH-free as it is, is a *corollary* of published work rather than a new
theorem. We therefore present them as attributed corollaries. The hard boundary of Paper A
applies verbatim: **no RH progress is claimed.**

We also flag, prominently, what is **not** in this note. The log-polyhomogeneous escape-route
audit (D-prime) is Gate-A **BLOCKED**: its universal claim over the finite-log-degree class is
false (the class omits ellipticity; a non-elliptic counterexample has a leading log), and only
a narrowed sub-principal-elliptic lemma is pending re-review. It is therefore excluded here.

---

## 2. (D) Heat-trace leading-log exclusion for classical elliptic ΨDOs

### 2.1 Statement
Let `M` be a closed smooth manifold of dimension `d ≥ 1`, and let `𝒞_ell` be the class of
strictly positive, self-adjoint, classical (polyhomogeneous) elliptic pseudodifferential
operators of order `m > 0` on `L²(M)`. Let
```
Γ_ζ^+ := ⨆_{ρ: ζ(ρ)=0, 0<Re ρ<1, Im ρ>0} {Im ρ}^{m(ρ)}      (multiset, with multiplicity).
```
(Here `Im ρ ∈ ℝ` by definition; no condition is placed on `Re ρ`, and RH is not assumed.)

**Theorem D.** No `H ∈ 𝒞_ell` has `spec(H) = Γ_ζ^+`. Equivalently `P(H)=0` for all
`H ∈ 𝒞_ell`; the conclusion is unconditional.

### 2.2 Proof (two mutually reinforcing formulations)
Let `p = d/m`. Both arguments are unconditional (they use only the Riemann–von Mangoldt
*count*, no zero location).

**Weyl-mismatch.** For `H ∈ 𝒞_ell`, `N_H(T) ~ C_H T^{p}` (Hörmander [1968, Thm 4.4] applied to
the order-1 operator `H^{1/m}` via Seeley's complex powers [1967]). The Riemann–von Mangoldt
law is `N_ζ(T) = (T/2π)(log(T/2π) − 1) + O(log T)`. A pure power `C_H T^p` cannot match
`(1/2π)T log T`: for `p ≤ 1` the ratio `C_H T^p / ((1/2π)T log T) → 0`, for `p > 1` it
`→ ∞`; never `1`. Hence `spec(H) ≠ Γ_ζ^+`.

**Heat-trace (the same obstruction in Abel/Tauber form).** With `A = I`, Lesch's expansion
[1999, Thm 3.7, published eqs. (3.18)–(3.20); = preprint (3.9)/(3.10)] gives a **pure-power**
leading heat trace `Z_H(t) = a_0 t^{-p} + o(t^{-p})`, `a_0 = Γ(p)·Res_{s=p}ζ_H(s) > 0` — no
leading `log`, because the `j=0` exponent `−p < 0 ∉ ℤ_{≥0}` forces the degree-bound coefficient
to be constant, and `Γ` is regular at `p > 0` so `Γ(s)ζ_H(s)` has only a simple pole at `s=p`.
By contrast the Riemann side has a leading log:
```
Z_ζ(t) = Σ_{γ>0} e^{-tγ} = (1/2πt)(log(1/t) − γ_E − log 2π) + O(log(1/t)),
```
by Abel/Karamata from the RvM law (independently checked, symbolic + 110-digit). A pure power
`t^{-p}` cannot carry the leading `log(1/t)`; hence `spec(H) ≠ Γ_ζ^+`.

The heat trace is the Laplace–Stieltjes transform of the counting measure, so within `𝒞_ell`
the two formulations are the **same** leading-order fact; neither is stronger.

### 2.3 Ellipticity is load-bearing; subleading logs are permitted
Ellipticity is a genuine hypothesis: the non-elliptic `H_0 = 1 + D_x^2 + D_y^4` on `𝕋²` has
`Z_{H_0}(t) ~ (√π Γ(1/4)/2) t^{-3/4}` (exponent `3/4 ≠ d/m = 1/2`), so the pure-power
*exponent* uses ellipticity. Subleading `t^k log t` (`k ≥ 1`) can occur (from `Wres(H^k) ≠ 0`)
and are irrelevant: only the *leading* singularity enters the comparison.

### 2.4 Novelty: scope-extension, not standalone (attribution)
- **Endres–Steiner [2010, Thms 15.4–15.6]** obtain a Weyl-law no-go for the two Berry–Keating
  families `H_BK`, `H_BK²` on compact metric graphs — not closed smooth manifolds.
- **Watson–Valentinuzzi [2026, Thm 1.4, Prop 6.2]** state a closely related leading-log
  obstruction for elliptic **differential** operators on compact manifolds.
- **Theorem D's identifiable increment** is (i) the extension to the full classical elliptic
  **ΨDO** class (via Lesch's `Tr(A e^{-tP})` expansion), and (ii) the explicit
  leading-vs-subleading-log distinction. Accordingly D is a **scope-extension / corollary**,
  suitable as a proposition in this note, not an unprecedented standalone obstruction.

*(Citation scope, for the record: Lesch [1999, Thm 3.7] is the load-bearing general classical
ΨDO source; BGV [1992, Thm 2.30] (Laplace-type only) and Gilkey [Lemma 1.8.2] (differential
only) do not cover the general case and are not load-bearing.)*

### 2.5 Escape routes
D excludes only positive self-adjoint finite-order classical elliptic ΨDOs on closed
positive-dimensional manifolds. It does **not** exclude nonelliptic/hypoelliptic/anisotropic,
nonclassical/log-polyhomogeneous, noncompact/boundary/singular/graph, or abstract self-adjoint
models (any positive `λ_n → ∞` is realizable on `ℓ²`), nor a nonclassical functional-calculus
model engineered to give `N(T) ~ T log T`. It makes no assertion about RH.

---

## 3. (C) Finite Euler factors do not force critical-line zeros (Helson class)

### 3.1 Setting
For a completely multiplicative unimodular `χ: ℕ → 𝕋`, the Helson zeta function is
`ζ_χ(s) = Σ_n χ(n) n^{-s} = Π_p (1 − χ(p)p^{-s})^{-1}` (Helson [1969]; Seip [2020];
Bochkov–Romanov [2022]). Fix a cutoff `P_0`; call `χ` *`P_0`-standard* if `χ(p)=1` for all
`p ≤ P_0` (observation `O(ζ_χ) = (χ(p))_{p ≤ P_0}`, so `P_0`-standard means `O = (1,…,1)`).
Let `S = {0 < Re s < 1}`, `H_S` the Helson zetas meromorphic on `S`, and for `ζ_χ ∈ H_S`
define `P_S(ζ_χ) = 1` iff every zero `ρ ∈ S` of `ζ_χ` has `Re ρ = 1/2`.

### 3.2 Statement and proof
**Theorem C.** For every `P_0` and every `z_1` with `0 < Re z_1 < 1`, `Re z_1 ≠ 1/2`, there is
a completely multiplicative unimodular `χ̃` with `χ̃(p)=1` for `p ≤ P_0` (so `ζ_{χ̃}` is
`P_0`-standard) such that `ζ_{χ̃}` continues meromorphically to `ℂ` with a simple zero at
`z_1`. In particular `ζ_{χ̃} ∈ H_S` and `P_S(ζ_{χ̃}) = 0`.

*Proof.* By Andersson [2024, Thm 5] (with `U = ℂ` and the signed multiset `{z_1}`, multiplicity
`+1`), there is a completely multiplicative unimodular `χ` with `ζ_χ` meromorphic on `ℂ` and a
simple zero at `z_1` (unconditionally — Andersson's result is not RH-conditional). Replace the
first `π(P_0)` Euler factors by the standard ones via the finite ratio
```
R(s) = Π_{p ≤ P_0} (1 − χ(p)p^{-s}) / (1 − p^{-s}),   ζ_{χ̃} := ζ_χ · R.
```
Each factor's zeros (`1 − χ(p)p^{-s}=0`) and poles (`1 − p^{-s}=0`) satisfy `p^{-Re s}=1`, i.e.
`Re s = 0` (using `|χ(p)|=1`); so `R` is holomorphic and nowhere zero on the open strip `S`.
Hence `R(z_1) ≠ 0`, the zero at `z_1` survives in `ζ_{χ̃}`, and `χ̃` (`=1` on `p ≤ P_0`,
`=χ(p)` else) is completely multiplicative unimodular, so `ζ_{χ̃}` is a Helson zeta in `H_S`. ∎

**Consequence (one-sided non-forcing).** `O(ζ_χ) = (1,…,1)` does not imply `P_S(ζ_χ)=1`; any
rule depending only on `O` and declaring `P_S=1` at `(1,…,1)` is unsound on `H_S`. The same
argument with `R_a(s) = Π_{p≤P_0}(1−χ(p)p^{-s})/(1−a_p p^{-s})` (zero-free on `Re s > 0`)
installs any target Euler data `a ∈ 𝕋^{π(P_0)}`, so **no** `O`-only condition satisfiable by
some realizable observation is sufficient for `P_S=1`.

### 3.3 Novelty and scope (attribution)
C = Andersson [2024, Thm 5] + a standard finite Euler-factor ratio and its one-line modulus
argument. It is a **one-sided non-forcing corollary**, to be presented as a named remark, not a
standalone barrier. It applies to the **Helson class only**: it neither constructs nor claims
Selberg-class members, `ζ` itself, or any "Euler product + gamma factor + functional equation"
class (the finite ratio preserves no functional equation, and unimodular coefficients supply no
gamma factor). A same-observation `P_S = 1` companion is available unconditionally via
Andersson's Corollary 3 (an entire zero-free Helson zeta), but is not needed for the one-sided
claim.

---

## 4. Closing remark: what is deliberately excluded

- **D-prime (log-polyhomogeneous escape audit) is Gate-A BLOCKED** and is not in this note. Its
  universal claim over the finite-log-degree class is false (missing ellipticity); only a
  narrowed `𝒞_logpoly^{sub,ell}` lemma is pending re-review. Folding it in would repeat the
  overclaim the review removed.
- **Neither D nor C is presented as new.** Both are attributed corollaries. The value of this
  note is a precise, RH-free placement of two natural approaches' limitations, with explicit
  credit to Endres–Steiner, Watson–Valentinuzzi, and Andersson.
- **No RH progress is claimed anywhere.**

---

## References (to be completed)

- J. Andersson, *Mittag-Leffler type theorems for Helson zeta-functions*, arXiv:2408.15713v1
  (2024), Theorem 5, Corollary 3.
- N. Berline, E. Getzler, M. Vergne, *Heat Kernels and Dirac Operators*, Springer, 1992.
- I. Bochkov, R. Romanov, *[Helson zeta zero/pole prescription]*, J. Funct. Anal. 282 (2022).
- S. Endres, F. Steiner, *The Berry–Keating operator on … compact quantum graphs*,
  J. Phys. A 43 (2010), 095204.
- P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*,
  Lemma 1.8.2.
- H. Helson, *Compact groups and Dirichlet series*, Ark. Mat. 8 (1969), 139–143.
- L. Hörmander, *The spectral function of an elliptic operator*, Acta Math. 121 (1968).
- M. Lesch, *On the noncommutative residue for pseudodifferential operators with
  log-polyhomogeneous symbols*, Ann. Global Anal. Geom. 17 (1999), 151–187 (Thm 3.7).
- R. T. Seeley, *Complex powers of an elliptic operator*, Proc. Sympos. Pure Math. 10 (1967).
- K. Seip, *[Helson zeta functions]*, J. Anal. Math. 141 (2020).
- D. F. Watson, T. Valentinuzzi, *Spectral-Dimension Obstructions for Operators with
  Superlinear Counting Laws*, Bull. Sci. Math. 211 (2026), 103824.
