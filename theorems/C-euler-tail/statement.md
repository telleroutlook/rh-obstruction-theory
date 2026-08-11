# Theorem C — Finite Euler Factors Do Not Force Critical-Line Zeros

**Mathematical status:** INDEPENDENTLY-CHECKED (Gate-A: OB-26 2026-08-11 — Links A–D +
RH-non-circularity CONFIRMED; CONDITIONAL→PASS after mod1–mod6. Scope: **one-sided
non-forcing corollary of Andersson Theorem 5**, NOT standalone novelty — see novelty.md)  
**Computational status:** NONE (analytic existence result; no finite certificate)  
**Paper target:** Paper A — named corollary / remark ("Finite-Euler-factor non-forcing corollary to Andersson, Theorem 5")
**Theorem ID:** C-euler-tail  
**Program ref:** §8 (WP-C), §8.C.1–C.4

---

## Setting

**Helson zeta functions.**  For a completely multiplicative function `χ: ℕ → 𝕋`
(`𝕋` the unit circle, so `|χ(p)| = 1` for all primes `p`) define the Dirichlet series
`ζ_χ(s) = Σ_{n≥1} χ(n) n^{-s} = Π_p (1 − χ(p) p^{-s})^{-1}` (absolutely convergent, Euler
product, for `Re(s) > 1`). This is the **Helson class** (Helson 1969; Seip 2020;
Bochkov–Romanov 2022; Andersson 2024 §1). Individual members may or may not continue past
`Re(s) = 1`.

**Finite prime cutoff.**  Fix `P₀ > 0`.  Say `χ` is **`P₀`-standard** if
`χ(p) = 1` for all primes `p ≤ P₀` (agrees with the Riemann ζ on the first
`π(P₀)` Euler factors). The **observation map** is `O(ζ_χ) = (χ(p))_{p ≤ P₀} ∈ 𝕋^{π(P₀)}`;
`P₀`-standard means `O = (1,…,1)`.

**Target predicate (OB-26 mod1 — defined on the open strip, no undefined "nontrivial").**
Let `S = {s ∈ ℂ : 0 < Re(s) < 1}` and let `H_S` be the Helson zeta functions admitting
meromorphic continuation to `S`. For `ζ_χ ∈ H_S`,
```
P_S(ζ_χ) = 1  ⟺  every zero ρ ∈ S of ζ_χ satisfies Re(ρ) = 1/2.
```
(This avoids an undefined "nontrivial zero" notion — the Helson class carries no gamma
factor or canonical trivial-zero set — and pins the predicate to a fixed region `S` rather
than a per-object continuation domain. The construction below produces members continued to
all of `ℂ`, hence in `H_S`.)

---

## Theorem C (finite Euler factors ⇏ critical-line zeros)

**Theorem C (finite Euler factors ⇏ critical-line zeros).** For every finite prime cutoff
`P₀` and every `z₁` with `0 < Re(z₁) < 1`, `Re(z₁) ≠ 1/2`, there exists a completely
multiplicative unimodular `χ̃ : ℕ → 𝕋` with `χ̃(p) = 1` for all `p ≤ P₀` (so `ζ_{χ̃}` is
`P₀`-standard), such that `ζ_{χ̃}` admits meromorphic continuation to `ℂ` and has a **simple
zero at `z₁`**. In particular `ζ_{χ̃} ∈ H_S` and `P_S(ζ_{χ̃}) = 0`.

**Consequence (one-sided non-forcing).** For the Helson class `H_S`, the observation
`O(ζ_χ) = (1,…,1)` does **not** imply `P_S(ζ_χ) = 1`. Hence any rule depending only on `O`
and declaring `P_S = 1` at the standard observation `(1,…,1)` is unsound on `H_S`. **No
`P_S = 1` companion is needed for this one-sided non-forcing claim.**

**Consequence (all-fiber strengthening — OB-26 Q3).** The same argument with the modified
ratio `R_a(s) = Π_{p≤P₀}(1 − χ(p)p^{-s})/(1 − a_p p^{-s})` (which is holomorphic and zero-free
on `Re(s) > 0` by the identical modulus argument, and installs the target Euler data
`a = (a_p)_{p≤P₀} ∈ 𝕋^{π(P₀)}`) produces, for **every** observation value `a`, a Helson
`ζ ∈ H_S` with `O(ζ) = a` and `P_S(ζ) = 0`. Therefore **no** `O`-only condition that is
satisfiable by at least one realizable observation can be a *sufficient* criterion for
`P_S = 1`. (This is the honest form of the broad "no finite-Euler-factor criterion forces
critical-line zeros" statement; the vacuous always-false criterion is excluded.)

**Method.**  The proof reduces to Andersson's prescribed-zero theorem
(arXiv:2408.15713v1, Theorem 5), plus a finite-Euler-factor modification argument. No RH,
no Riemann ζ, no functional equation is used.

---

## Proof strategy (PROOF-DRAFT)

**Step 1 (Andersson's theorem).** By Andersson (2024), for any prescribed finite
set of desired zeros `z₁, …, z_k ∈ {0 < Re(s) < 1} \ {1/2}` in the continuation
region, there exists a Helson zeta function `ζ_χ` (with `|χ(p)| = 1`) that has
zeros at `z₁, …, z_k`.

**Step 2 (Finite-factor modification).** Given such `ζ_χ`, define
`ζ_χ̃ := ζ_χ · R(s)` with the finite-factor **ratio of Euler factors**
```
R(s) := Π_{p ≤ P₀} (1 − χ(p) p^{-s}) / (1 − p^{-s})       (χ̃(p) = 1 for p ≤ P₀),
```
which replaces the first `π(P₀)` Euler factors of `ζ_χ` by the standard ones
`(1 − p^{-s})^{-1}` (see proof.md §1 for the telescoping; verify by cancelling
`ζ_χ`'s own `p ≤ P₀` factors). Note the orientation: `R = Π L_p(s,1)/L_p(s,χ) =
Π (1 − χ(p)p^{-s})/(1 − p^{-s})` — the numerator carries `χ(p)`. `R` is a **ratio
of two finite Euler products**, meromorphic on `ℂ`; it is NOT a Dirichlet
polynomial (the denominator `(1 − p^{-s})` is inverted), so no "degree `≤ P₀^{1/2}`"
statement applies.

**Step 3 (Zero preservation — no cancellation possible).** Every factor of `R` has
its zeros (from `1 − χ(p)p^{-s} = 0`) and poles (from `1 − p^{-s} = 0`) on the line
`Re(s) = 0`, since `|χ(p)| = 1` forces `p^{-s} = χ(p)` or `p^{-s} = 1` to have
`Re(s) = 0` (see proof.md §3). Hence **`R` is holomorphic and nowhere zero on the
entire open strip `0 < Re(s) < 1`**. Therefore, for the prescribed `z_j` in the open
strip, `R(z_j) ≠ 0` **automatically** — there is no "critical issue" and no need to
push `Im(z_j)` large. The zero `z_j` of `ζ_χ` is preserved exactly in `ζ_χ̃`.

**Step 4 (P₀-standardness).** By construction, `χ̃(p) = 1` for `p ≤ P₀`, so
`ζ_χ̃` is `P₀`-standard, and it retains the prescribed off-line zero(s) `z_j`
(Step 3, unconditionally in the open strip). Moreover `ζ_χ̃` is itself a Helson
zeta function (its coefficient `χ̃` is completely multiplicative and unimodular:
`χ̃(p) = 1` for `p ≤ P₀`, `= χ(p)` for `p > P₀`), so `P(ζ_χ̃)` is well-defined and
equals `0`.

---

## Open items

| Item | Status |
|---|---|
| Andersson Thm verified by theorem number | CLEARED — Theorem 5 (label `thm5`), source-verified in `baseline/andersson-2408.15713/` |
| Finite-Euler-factor zero preservation (Step 3) | INDEPENDENTLY-CHECKED (OB-26 Link C) — `R` holomorphic and zero-free on the whole open strip |
| Target predicate | DEFINED as `P_S` on `S={0<Re<1}` (OB-26 mod1) |
| Broad consequence | one-sided + `R_a` all-fiber (OB-26 Q3); optional Cor-3 `P_S=1` companion |
| Scope: Helson class only | STATED — Selberg/ζ NOT claimed (OB-26 mod6); see limitations.md |
| Novelty | corollary of Andersson Thm 5 (OB-26 Q5 = option a) — see novelty.md |

---

## Escape route

The theorem applies to the Helson class.  It does NOT apply to:

1. **Selberg class:** functional equation + Euler product with additional axioms
   not present in the Helson class.
2. **ζ itself:** the exact Euler factors of ζ, the gamma factor, and the
   functional equation jointly constrain the zero set in ways the Helson class
   does not replicate.
3. **Combined axioms:** a method using both Euler product for `p ≤ P₀` AND
   the functional equation AND gamma factor may still force critical-line zeros
   in a larger class.

The escape route is: any proof using the full Selberg-class axioms (or ζ-specific
structure) is not limited by Theorem C.
