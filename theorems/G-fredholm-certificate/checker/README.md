# Checker README — Theorem G (G-fredholm-certificate)

## Independent replay path

### C-G-0: Diagonal Fredholm obstruction — CERTIFIED INTERVAL REPLAY (INDEPENDENT-CHECKER)

**File:** `diagonal_fredholm_interval_replay.py`  
**Provenance:** OB-17 external referee (2026-08-11); source-verified and re-run in-repo.  
**SHA-256:** `e197f2bb091a3ea805815b3d1fbe4e5d07209891ee27f946e10fcba6c8f4058b`  
**Run:** `python3 diagonal_fredholm_interval_replay.py` → prints `ALL_CERTIFIED_CHECKS_PASSED`.

Pure-stdlib (`fractions.Fraction` + integers) certified-interval checker. **No
floating-point value enters any certificate**; transcendentals (`π`, `log`, `arctan`,
`log Γ`) are enclosed by convergent rational series with explicit remainder bounds
(Machin `π`; `atanh`-series `log`; Binet/Stirling `log Γ` with proved complex remainder
`|R_8| < 4.68e-22`). It independently:
- bisects the first five Gram-type levels `d_n` (solving `θ(d_n)=(n−1)π` on the certified
  monotone branch `[10,40]`), each to interval width `< 6.83e-12 < 10^{-8}`;
- propagates to `κ_n = 1/(1/4+d_n²)` and determinant zeros `λ_n = √(1/4+d_n²)`;
- certifies the three-way strict separation `γ_n < d_n < λ_n` (n=1,2,3), using ONLY
  Odlyzko's printed first-three ζ ordinates with their stated `±3e-9` accuracy as the
  external comparison input — no `γ_n` enters the construction of `d_n, κ_n, λ_n`, or the
  tail bound;
- runs two adversarial mutations (drop the `1/4` shift → zero collapses to `d_1`; replace
  `d_1` by `γ_1` → left separation fails), both correctly rejected;
- certifies the tail `Σ_{n>2048} κ_n ∈ [0.000932724311548, 0.000932724311549] < 10^{-3}`,
  hence local-uniform convergence `det(I−z²D_N) → G_d`.

**Scope (what this certifies):** the finite three-way separation `γ_n < d_n < √(1/4+d_n²)`
and the diagonal-product convergence — i.e. the finite core of `G_d ≠ Ξ̂` (via a direct
value comparison `G_d(γ_1) ≠ 0 = Ξ̂(γ_1)`, NOT an invalid transitivity of `≠`). It does
NOT certify RH, any zero-table re-verification, OB-08's other analytic content, or any
thermodynamic/continuum limit.

### C-G-1: S(T) gap formula verification

Implement the formula:
```python
# theta_level(n): solve theta(T)/pi + 1 = n
# gamma_n: known zero ordinates (from LMFDB or odlyzko tables)
# S(gamma_n): (1/pi) * arg(zeta(1/2 + i*gamma_n))
# expected: gamma_n - d_n ~ S(gamma_n) / A'(gamma_n),  A'(t) = theta'(t)/pi
```

Requirements:
- Use only stdlib + mpmath for evaluation of theta and S(T).
- Read gamma_n from a local file (not from a zero-free construction).
- Output a comparison table for n = 1..30.
- Must be runnable offline.

Status: NOT YET (C-G-0 above already certifies the d_n side to 1e-8 without needing S(T)).

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
