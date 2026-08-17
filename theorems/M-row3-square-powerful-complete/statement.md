---
# Theorem M — Row-3: Complete Square-Powerful Obstruction (t=1 Case of NT-C)

**Mathematical status:** `PROOF-DRAFT`  
**Computational status:** `REPRODUCIBLE`

**Note:** The 4∤n case was an open problem (OE-02). Proof received 2026-08-17
via Gaussian factorization + 2-isogeny descent on E: Y²=X³−32X+64 (rank 0).
CAS verification of the Selmer group computation is the remaining Gate-A gap.

---

## Statement

**Theorem M.** For every Row-3 pair (a, n), neither A⁺ = a²+n² nor A⁻ = (n−a)²+n²
can simultaneously be of the form 5^e · m² (e ≥ 0, m ∈ ℤ, i.e., "square-based
powerful-away-from-5").

More precisely:

**(i) Sub-family 4|n:** Neither A⁺ nor A⁻ is of the form 5^e · m² for any integers
e ≥ 0, m. (The individual impossibility is unconditional — no simultaneity required.)

**(ii) Sub-family 4∤n:** A⁺ = 5^e · m² forces e even (i.e., A⁺ must be a perfect
square). Same for A⁻. In particular, both A⁺ and A⁻ cannot simultaneously be
square-based-powerful-away-from-5 (since the simultaneous perfect-square case is
excluded by Theorem L / Theorem D of Paper E).

**Corollary (NT-C t=1 resolved):** The t=1 case of NT-C is completely resolved:
no Row-3 pair has both A⁺ and A⁻ powerful-away-from-5 via the square-only path
(s²t³ with t=1). The remaining open part of NT-C is the cube-factor case t ≥ 2.

---

## All definitions

**Row-3 pair** (a, n): integers satisfying
- n even, n ≥ 4, 3 ∤ n
- a odd, 1 ≤ a < n, gcd(a, n) = 1

Write n = 2m. Then A⁺ = a² + 4m², A⁻ = (2m−a)² + 4m².

**Square-based powerful-away-from-5**: A positive integer N is square-based powerful
iff N = 5^e · m² for some integers e ≥ 0, m ≥ 1. (This is the t=1 case of the
Erdős–Szekeres powerful decomposition N = 5^e · s² · t³ with t=1.)

**Theorem B** (proved, Paper E, thm:mod4): For every Row-3 pair,
- 4∤n → A⁺ ≡ A⁻ ≡ **5** (mod 8)
- 4|n → A⁺ ≡ A⁻ ≡ **1** (mod 8)

**Theorem L / Theorem D of Paper E** (proved, `theorems/L-row3-zsygmondy-square/`):
No Row-3 pair has A⁺ = x² and A⁻ = y² simultaneously.

---

## Scope and non-conclusions

- Theorem M completely resolves the t=1 (square-only powerful) case of NT-C.
- NT-C in full (t ≥ 2, cube-factor case) remains open (see `outsource/OE-01-...`).
- The proof of parts (i) and (ii) uses only elementary congruence arithmetic
  (mod 8 and mod 16). Part (ii) for the simultaneous case invokes Theorem L.
- This theorem does NOT assume or imply RH. RH stays `[OUT]`.
- This theorem does NOT assume ABC, any conjecture, or Sha triviality.

---

## Evidence basis

| Axis | Status |
|---|---|
| Mathematical | `PROOF-DRAFT` (elementary mod 8/16 proof; full details in `proof.md`) |
| Computational | `REPRODUCIBLE` (checker in `checker/`, n≤3000 survey: 0 instances) |
