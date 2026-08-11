# checker/ — independent replay path for Theorem B1

## B1-CHK-0: R-atom finite-inequality decay — CERTIFIED EXACT-RATIONAL REPLAY (deposit-ready)

**File:** `b1_ratom_certified_checker.py`
**Provenance:** OB-24 external referee (2026-08-11); independently written from the
definitions, source-verified and re-run in-repo. Supersedes the OB-18 checker, which used
B2's doubled (R-symm) convention.
**SHA-256:** `199c7dad90d689950f03048aed236a24b096c95578f6ade3b73ed2b447fe4bc8`
**Run:** `python3 b1_ratom_certified_checker.py` → prints `ALL_CERTIFIED_CHECKS_PASSED`.
(Refuses `python -O`: certificate assertions require normal mode.)

Pure-stdlib (`fractions.Fraction` + integers) exact checker in **B1's own R-atom Σ′
convention** (`O_j(𝒵) = Σ'_ρ φ_j(ρ)`, atoms once — NOT B2's doubled `Σ_ρ[φ_j(ρ)+φ_j(1−ρ)]`).
No floating point in the certificate path (internal guard rejects `float(`, `numpy`,
`scipy`, `mpmath`). It computes `O_j` by traversing the four quartet atoms, cross-checks an
independently coded conjugate-pair closed form, and certifies:

- **K1** — `δ_j(T)` real (imag part exactly 0), traversal == conjugate-pair form, over
  `j∈{1,2}`, `T∈{1,2,89,90,100,1000,10000}`.
- **K2** — `δ_1(1) = 608/425` (R-atom; contrast B2's R-symm `1216/425`).
- **K3** — exact polynomial identities `δ_1(T)=32(y+3)/((y+9)(y+1))`,
  `δ_2(T)=128(y³+9y²+31y−9)/((y+9)²(y+1)²)` (`y=16T²`); leading-coefficient certificate
  `T²δ_j(T) → 2j²` (proved from degrees/leading coeffs, NOT from samples — the three
  sample heights are regression anchors only).
- **K4** — least joint integer threshold `T* = 90` for `ε=10⁻³` (`δ_2(89) > 10⁻³ > δ_2(90)`),
  by exact exhaustive integer search `1≤T≤90` plus strict monotonicity on **positive
  integers** `T≥1` (NOT all real T>0 — see caveat).
- **K5** — under the explicit minimal definitions in the module docstring
  (`𝔛_sym` = finite multisets invariant under `ρ↦ρ̄`, `ρ↦1−ρ`; `P=1` iff all atoms on
  `Re=1/2`; `𝒵_+=Q(1/2,1)`, `𝒵_−=Q(3/4,1)`): membership + predicate + mutation guards
  (`σ_0=1/2` flips `P` to 1; constant test gives `δ≡4` in R-atom, not 8).
- **K6** — convention guard: R-symm sum `= 1216/425 = 2 × 608/425` (documents the ×2).

**Monotonicity caveat (OB-24 correction).** `δ_2(T)` is NOT monotone over all real `T>0`
(counterexample: `δ_2(1/10) = −190275200/44102881 < δ_2(1/4) = 256/25`, despite `1/10<1/4`).
The load-bearing monotonicity holds only on **positive integers** `T≥1`, which is all K4
uses; the checker exhaustively searches `1≤T≤90` rather than relying on monotonicity alone.

**Scope.** Certifies only the finite decay statement in B1's R-atom convention; asserts
nothing about analytic functions or RH. Pinned in the test suite (runs + emits pass flag +
no-float guard). This restores B1's computational axis to INDEPENDENT-CHECKER under the
correct convention (the OB-18 checker was in the wrong convention).