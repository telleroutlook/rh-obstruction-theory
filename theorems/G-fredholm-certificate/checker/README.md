# Checker README — Theorem G (G-fredholm-certificate)

## Independent replay path

This directory will contain the independent verification of Theorem G's
computational claims.

### C-G-1: S(T) gap formula verification

Implement the formula:
```python
# theta_level(n): solve theta(T)/pi + 1 = n
# gamma_n: known zero ordinates (from LMFDB or odlyzko tables)
# S(gamma_n): (1/pi) * arg(zeta(1/2 + i*gamma_n))
# expected: gamma_n - d_n ~ S(gamma_n) / N'(gamma_n)
```

Requirements:
- Use only stdlib + mpmath for evaluation of theta and S(T).
- Read gamma_n from a local file (not from a zero-free construction).
- Output a comparison table for n = 1..30.
- Must be runnable offline.

Status: NOT YET.

### C-G-2: Hadamard uniqueness check (formal)

The Hadamard uniqueness lemma (G.1) is a classical theorem. A formal checker
is not required here; the claim is REFEREED. The check is that the lemma is
correctly applied (order ≤ 1 hypothesis satisfied by Ξ).

Verify:
- Ξ(z) = ξ(1/2 + iz) has order exactly 1 (standard: Ξ is of order 1 and genus 1).
- The product over γ_n is absolutely convergent (∑ 1/γ_n² < ∞; known from zero
  counting N(T) ~ T log T / 2π, so ∑ γ_n^{-2} ~ ∫ T^{-2} d(T log T/2π) < ∞).

Status: Argumentally clear; checker implementation NOT YET.

## Philosophy

The proof of G-info rests on REFEREED lemmas (Hadamard uniqueness, argument-principle
counting identity). The checker's role is to verify the S(T) gap formula numerically
(C-G-1) and confirm the explicit perturbed-zero exhibit when W-G-2 is written.
No finite certificate can validate the analytic theorem; the checker corroborates
and does not replace the analytic proof steps.
