# Proof — Theorem C (finite Euler factors ⇏ critical-line zeros)

**Status:** PROOF-DRAFT (conditional on Andersson baseline verification)  
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

This is a finite product of rational functions in `p^{-s}`, hence a finite
exponential polynomial (Dirichlet-type) in `s`, meromorphic on all of `ℂ`.

The modified function is `ζ_χ̃(s) = ζ_χ(s) · R(s; P₀, χ)`.

---

## §2. Andersson's theorem (load-bearing baseline — PENDING VERIFICATION)

**Claim (Andersson 2024, arXiv:2408.15713):** For any prescribed finite set of
points `z₁, …, z_k` in the continuation domain of the Helson zeta class (with
`0 < Re(z_j) < 1`, `z_j ≠ 1`) and any multiplicities `m_j ≥ 1`, there exists
a Helson function `ζ_χ` (with `|χ(p)| = 1`) having zeros of the prescribed
multiplicities at `z₁, …, z_k`.

**Status:** This claim is the Mittag-Leffler / prescribed-zero theorem of Andersson
(arXiv:2408.15713, "Mittag-Leffler type theorems for Helson zeta-functions").
It is NOT yet verified by theorem number from the source (arXiv tarball not in
`baseline/`).  **This is an explicit PENDING Gate A item.**

Until verified, Theorem C is CONDITIONAL on this claim.

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

## §5. Gate A: Andersson baseline

The proof is BLOCKED on Gate A for the Andersson prescribed-zero theorem.
Action required:

1. Download arXiv:2408.15713 tarball into `baseline/`.
2. Identify the theorem number of the prescribed-zero result.
3. Verify the exact statement (especially: what continuation domain? what
   constraints on `χ`? what function class?).
4. Add to CLAIM_LEDGER.yaml as INDEPENDENTLY-CHECKED.
5. Update this proof's status to INDEPENDENTLY-CHECKED for the Andersson step.

Until Step 4–5 are complete, Theorem C remains CONDITIONAL.

---

## §6. Status

| Step | Status |
|---|---|
| Andersson prescribed-zero (§2) | PENDING Gate A verification |
| R holomorphic, nonzero in strip (§3) | PROOF-DRAFT ✓ |
| P₀-standardness of χ̃ (§4) | PROOF-DRAFT ✓ |
| Scope: Helson class only | STATED ✓ |
| Novelty (standalone vs. section of A) | OPEN — see novelty.md |
| Davenport-Heilbronn separation (program §8.C.2) | STATED: DH lacks Euler product; Theorem C lacks functional equation; the two obstruction types are kept separate and NOT combined into a single example |
