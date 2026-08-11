# Proof — Theorem C (finite Euler factors ⇏ critical-line zeros)

**Status:** PROOF-DRAFT (Andersson Thm 5 dependency Gate-A CLEARED, source-verified in
`baseline/andersson-2408.15713/`; whole-theorem Gate-A review pending: OB-26)  
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
`Z = {z₁}` with `z₁ ∈ {0 < Re(z₁) < 1, Re(z₁) ≠ 1/2}` (one prescribed off-line zero,
simple). The theorem yields `ζ_χ` with exactly one prescribed zero at `z₁` in the strip.
Then the finite-factor modification (§3–§4) adjusts `χ` to be `P₀`-standard.

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
| Andersson prescribed-zero (§2) | INDEPENDENTLY-CHECKED ✓ — Thm 5 (thm5), Gate A CLEARED |
| R holomorphic, nonzero in strip (§3) | PROOF-DRAFT ✓ |
| P₀-standardness of χ̃ (§4) | PROOF-DRAFT ✓ |
| Scope: Helson class only | STATED ✓ |
| Novelty (standalone vs. section of A) | OPEN — see novelty.md |
| Davenport-Heilbronn separation (program §8.C.2) | STATED: DH lacks Euler product; Theorem C lacks functional equation; the two obstruction types are kept separate and NOT combined into a single example |
