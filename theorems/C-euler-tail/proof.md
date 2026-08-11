# Proof — Theorem C (finite Euler factors ⇏ critical-line zeros)

**Status:** INDEPENDENTLY-CHECKED (Gate-A PASS, OB-26 2026-08-11, after mod1–mod6; scope:
one-sided non-forcing corollary of Andersson Theorem 5)  
**Analytic / finite separation:** purely analytic; no finite certificate.

---

## §1. Notation

Recall the setting of statement.md.  For a prime `p` and `s ∈ ℂ` with `Re(s) > 1`:

```
L_p(s, χ) := (1 − χ(p) p^{-s})^{-1}   (single Euler factor).
```

For the modification factor:

```
R(s; P₀, χ) := Π_{p ≤ P₀} L_p(s, 1) / L_p(s, χ)
             = Π_{p ≤ P₀} (1 − χ(p) p^{-s}) / (1 − p^{-s}).
```

This is a **ratio of two finite Euler products** (a finite product of rational
functions in `p^{-s}`), meromorphic on all of `ℂ`. It is **not** a Dirichlet
polynomial: the denominator factors `(1 − p^{-s})` are inverted, so `R` has poles
(at the zeros of the denominator). Its zeros and poles are located in §3.

The modified function is `ζ_χ̃(s) = ζ_χ(s) · R(s; P₀, χ)`.

---

## §2. Andersson's theorem (load-bearing baseline — GATE A CLEARED)

**Theorem (Andersson 2024, arXiv:2408.15713, Theorem 5):** Let `U` be an open connected
set containing `{Re(s) > 1}`, and let `Z` be any signed multiset in `U ∩ {Re(s) < 1}`
without limit points on `U ∪ (1+iℝ)`.  Then there exists a completely multiplicative
unimodular function `χ` such that the Helson zeta-function `ζ_χ(s)` has meromorphic
continuation from `{Re(s) > 1}` to `U`, with prescribed poles and zeros (with given
multiplicities) from `Z`, and `U` is its maximal domain of meromorphicity.

**Verification:** Theorem number confirmed as **Theorem 5** (LaTeX label `thm5`) in the
source file `Andersson_Mittag-Leffler_paper.tex` (tarball in
`baseline/andersson-2408.15713/`). Statement transcribed and verified against source.
Gate A status: **CLEARED**.

**How used in Theorem C:** Take `U = ℂ` (or any connected domain containing `{Re(s) > 1}`),
and the **signed multiset** `𝒵` with `m_𝒵(z₁) = +1` (the `+` sign denoting a zero, multiplicity
1) and `m_𝒵 = 0` elsewhere, where `z₁ ∈ {0 < Re(z₁) < 1, Re(z₁) ≠ 1/2}`. The single point
has no limit point in `ℂ`, so Theorem 5's hypotheses hold; it yields a completely
multiplicative unimodular `χ` with `ζ_χ` meromorphic on `ℂ` and a simple zero at `z₁`.
Then the finite-factor modification (§3–§4) adjusts `χ` to be `P₀`-standard while preserving
this zero (§3).

**Note on scope:** Andersson's theorem is for the **entire** open half-plane `{Re(s) < 1}`
(unconditionally), not just the critical strip. For Theorem C we only need one prescribed
zero in the open critical strip, which is covered.

---

## §3. Finite-factor modification (zero preservation)

**Goal:** Given `ζ_χ` with zero at `z₁ ∉ {Re(s) = 1/2}`, show `ζ_χ̃ = ζ_χ · R`
also has a zero near `z₁`.

**Dirichlet polynomial zero-free region for `R`.**

`R(s; P₀, χ) = Π_{p ≤ P₀} (1 − χ(p) p^{-s}) / (1 − p^{-s})`.

Each factor `(1 − χ(p) p^{-s}) / (1 − p^{-s})` has:
- zeros at: `s = 2πi k / \log p` (zeros of the denominator `1 − p^{-s} = 0`,
  i.e. `p^{-s} = 1`).  These are at `Re(s) = 0`.
- poles at: `s = (2πi k + \log χ(p)) / \log p` (zeros of numerator).  Since
  `|χ(p)| = 1`, `\log χ(p)` is purely imaginary: poles are at `Re(s) = 0`.

So all zeros and poles of `R` lie on the line `Re(s) = 0`.  In the strip
`0 < Re(s) < 1`, `R(s)` is holomorphic and nowhere zero.

**Conclusion:** For any `z₁ ∈ {0 < Re(z_1) < 1}`, we have `R(z₁) ≠ 0`.
Therefore the zero `z₁` of `ζ_χ` is preserved in `ζ_χ̃ = ζ_χ · R`.  ☐

**Note on poles of `R` for the denominator zeros.**  The factors `(1 − p^{-s})^{-1}`
have poles at `Re(s) = 0`, i.e., on the boundary of the critical strip but
outside `{0 < Re(s) < 1}`.  So `R` is holomorphic in the open strip.  ✓

---

## §4. Verification of `P₀`-standardness

By construction, `χ̃(p) = 1` for `p ≤ P₀`:
```
ζ_χ̃(s) = ζ_χ(s) · R(s; P₀, χ)
         = [Π_{p > P₀} L_p(s, χ)] · [Π_{p ≤ P₀} L_p(s, χ)] · R(s; P₀, χ)
         = [Π_{p > P₀} L_p(s, χ)] · [Π_{p ≤ P₀} L_p(s, 1)]
         = ζ_χ̃(s)
```
with `χ̃(p) = 1` for `p ≤ P₀` and `χ̃(p) = χ(p)` for `p > P₀`. ✓

The identity `ζ_χ · R = ζ_{χ̃}` first holds on `Re(s) > 1` (absolute convergence of both
Euler products); since `ζ_χ` is meromorphic on `ℂ` (Theorem 5) and `R` is meromorphic on
`ℂ`, the product `ζ_χ · R` is the meromorphic continuation of `ζ_{χ̃}`, and the identity
extends to `ℂ` by uniqueness of analytic continuation. (This is why the formal Euler product
is not treated as a full-plane identity directly — only the continued functions are.)

---

## §4.5. All-fiber strengthening and optional `P_S = 1` companion (OB-26 Q3)

**All observation fibers (broad consequence).** Fix any target Euler data
`a = (a_p)_{p ≤ P₀} ∈ 𝕋^{π(P₀)}`. Replace `R` by
```
R_a(s) := Π_{p ≤ P₀} L_p(s, a_p) / L_p(s, χ) = Π_{p ≤ P₀} (1 − χ(p) p^{-s}) / (1 − a_p p^{-s}).
```
Each factor's numerator vanishes only where `χ(p)p^{-s} = 1` and denominator only where
`a_p p^{-s} = 1`; since `|χ(p)| = |a_p| = 1`, taking absolute values forces `p^{-Re(s)} = 1`,
i.e. `Re(s) = 0`. So `R_a` is holomorphic and zero-free on `Re(s) > 0` (a fortiori on `S`),
and `ζ_{χ_a} := ζ_χ · R_a` installs the Euler data `χ_a(p) = a_p` for `p ≤ P₀` while keeping
the simple zero at `z₁`. Hence for **every** realizable observation `a` there is a Helson
`ζ_{χ_a} ∈ H_S` with `O(ζ_{χ_a}) = a` and `P_S(ζ_{χ_a}) = 0`. Consequently no `O`-only
condition satisfiable by at least one realizable `a` can be a *sufficient* criterion for
`P_S = 1` (the vacuous always-false criterion is excluded). This is the honest broad form.

**Optional same-fiber `P_S = 1` companion (not required for the non-forcing claim).** If a
two-sided information obstruction is wanted (same observation, both `P_S = 0` and `P_S = 1`
present), Andersson's **Corollary 3** (`\label{cor3}`, source line 196: "there exists an
entire zero-free Helson zeta function") supplies, unconditionally, a Helson `ζ_0` with **no**
zeros in `ℂ`; then `ζ_0 · R_a ∈ H_S` has observation `a`, is zero-free on `S`, so
`P_S = 1`. This uses Corollary 3 (source-verified) — still no RH and no Riemann ζ. It is
recorded as an option; Theorem C's stated one-sided non-forcing result does not need it.

---

## §5. Gate A: Andersson baseline — CLEARED

Gate A for the Andersson dependency is now cleared:

1. ✅ Tarball downloaded into `baseline/andersson-2408.15713/`.
2. ✅ Theorem number: **Theorem 5** (LaTeX label `thm5`).
3. ✅ Exact statement verified: prescribed zeros and poles as a signed multiset in
   any open connected set `U ⊃ {Re(s)>1}`, without limit points on `U ∪ (1+iℝ)`.
4. ✅ Added to CLAIM_LEDGER.yaml as `ANDERSSON-HELSON-PRESCRIBED-ZERO`,
   `mathematical: INDEPENDENTLY-CHECKED`, `usable_as_premise: true`.
5. ✅ Theorem C is now **PROOF-DRAFT** (no longer CONDITIONAL).

---

## §6. Status

| Step | Status |
|---|---|
| Andersson prescribed-zero (§2) | INDEPENDENTLY-CHECKED ✓ — Thm 5 (thm5), signed multiset m(z₁)=+1 |
| R holomorphic, nonzero in strip (§3) | INDEPENDENTLY-CHECKED ✓ (OB-26 Link C) |
| P₀-standardness of χ̃ + analytic-continuation identity (§4) | INDEPENDENTLY-CHECKED ✓ (OB-26 Link B, D) |
| All-fiber R_a + optional Cor 3 companion (§4.5) | PROOF-DRAFT ✓ (OB-26 Q3; same modulus argument) |
| Target predicate P_S on strip S | DEFINED (OB-26 mod1) |
| Novelty: corollary of Andersson Thm 5 | DECIDED (OB-26 Q5 = option a) — see novelty.md |
| Scope: Helson class only; Selberg/ζ NOT claimed | STATED (OB-26 mod6) — see limitations.md |
| Davenport-Heilbronn separation (program §8.C.2) | STATED: kept logically separate, NOT combined with C |
