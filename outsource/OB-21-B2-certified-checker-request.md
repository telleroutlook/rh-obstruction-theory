# Problem OB-21 — B2: request for an independently-written exact-rational certified checker

**Type:** computational verification — request for a **runnable, deposit-ready** checker
program (like the certified interval checker supplied for the G theorem).

**What this is.** A request for an **independently written** Python program (standard
library only; exact `fractions.Fraction`, no floating point in any certificate) that
reconstructs and certifies the full B2 finite-collision pipeline from the definitions
below, prints a single `ALL_CERTIFIED_CHECKS_PASSED` line on success, and is suitable for
deposit into the repository's `theorems/B2-exact-collision/checker/` directory as the
permanent independent replay path. Please also report the program's SHA-256 so it can be
pinned and re-run in-repo.

**Non-circularity (mandatory).** RH is not assumed; no ζ zero, Euler product, or functional
equation is used. All objects are constructed finite multisets of complex rationals. The
program validates only a **finite algebraic identity**, asserting nothing about analytic
functions or RH.

**Independence requirement.** The program must be written **from the definitions below**,
not adapted from any producer script. It must compute the observation `O_j` by traversing
the multiset per its definition (NOT by hard-coding the Chebyshev closed form), and then
**separately** cross-check against the Chebyshev closed form — the two routes must agree
entry-by-entry. This mirrors the independence standard met by the G-theorem checker.

---

## All definitions (self-contained — everything is here)

### Complex-rational arithmetic
Represent a complex rational as an ordered pair `(a, b)` of `fractions.Fraction`,
`z = a + bi`. Implement `+, −, ×`, reciprocal `1/z = (a−bi)/(a²+b²)`, integer powers.

### Test functions and observation
Li-type `φ_j(ρ) = 1 − (1 − 1/ρ)^j`, `j = 1,…,m`. For a finite multiset `𝒵` of nonzero
complex rationals avoiding `{0,1}`, with multiplicity:
```
O_j(𝒵) = Σ_{ρ ∈ 𝒵} [ φ_j(ρ) + φ_j(1−ρ) ]   (must be real; assert imaginary part = 0).
```

### The pipeline to reconstruct
Input: integer `m ≥ 1`, distinct positive rationals `t_1 < … < t_m`, positive rational `T`,
`σ_0 = 3/4`.
1. `L(t) = {1/2+it, 1/2−it}`; `Q = {3/4+iT, 3/4−iT, 1/4+iT, 1/4−iT}`.
2. `C_{jk} = O_j(L(t_k))`  (j,k = 1..m); `d_j = O_j(Q)`  (j = 1..m). All in ℚ.
3. Cross-check: `C_{jk} =? 4(1 − T_j(x_k))`, `x_k = (4t_k²−1)/(4t_k²+1)`, `T_j` via the
   Chebyshev recurrence `T_0=1, T_1=x, T_{j+1}=2xT_j−T_{j−1}`. Assert equality.
4. `det C` by exact fraction Gaussian elimination; assert `det C ≠ 0`.
5. `β = −C⁻¹ d ∈ ℚ^m` by exact elimination.
6. `R = lcm` of the denominators of `β_1,…,β_m` (positive integer); `n = Rβ ∈ ℤ^m`;
   assert each `n_k` has denominator 1. `M = max_k |n_k|`.
7. Multisets `𝒵_+ = ⊔_k M·L(t_k)`, `𝒵_− = (⊔_k (M+n_k)·L(t_k)) ⊔ R·Q`.

### Predicate
`P(𝒵) = 1` iff every atom has real part `1/2`, else `0`.

---

## Checks the program must certify (all exact rational)

### K1 — Observation is real and matches Chebyshev
For each `(m, t, T)` tested: `O_j` returns imaginary part exactly 0; the per-definition `C`
equals the Chebyshev-route `C` entry-by-entry.

### K2 — Nonsingularity and rational solve
`det C ≠ 0` (exact); `β = −C⁻¹d` recomputed and verified by `Cβ = −d` exactly.

### K3 — Integer scaling and nonneg multiplicity
`n = Rβ ∈ ℤ^m` (denominators 1); `M+n_k ≥ 0` for all `k`.

### K4 — Exact collision
`Σ_k n_k C_{jk} + R d_j = 0` for all `j` (i.e. `Cn + Rd = 0` exactly).

### K5 — Predicate separation
`P(𝒵_+) = 1` and `P(𝒵_−) = 0`.

### K6 — Two independent instances
Run `m=2, t=(1,2), T=1` AND a second self-chosen instance, e.g. `m=3, t=(1,2,3), T=2`.
Both must satisfy K1–K5 with exact zero collision residual. Report the full rational data
(C, d, det C, β, R, n, M) for both.

### K7 — Adversarial mutation guard (must FAIL the collision)
For the `m=2` instance: replace `n_1` by `n_1 + 1` and confirm the residual `Cn + Rd`
becomes nonzero (specifically equals the first column of `C`, `(8/5, 128/25)`). This proves
the collision check is not vacuously satisfied.

### K8 — Symmetry (membership) check
Verify `𝒵_+` and `𝒵_−` are closed (with multiplicity) under `ρ ↦ ρ̄` and `ρ ↦ 1−ρ`, so
both lie in `𝔛_sym`.

---

## Expected exact anchor values (m=2, t=(1,2), T=1) — for the reviewer to reproduce

```
C = [[8/5, 8/17], [128/25, 512/289]],   det C = 3072/7225,
d = [1216/425, 1763072/180625],
β = [−1426/1275, −854/375],
R = 6375,  n = [−7130, −14518],  M = 14518,  M+n = [7388, 0],
C n + R d = [0, 0]   (exact),
mutated (n_1+1): C n' + R d = [8/5, 128/25] ≠ 0.
```
(These are the reconstruction targets; the deliverable is the independently-written program
that reproduces them and passes K1–K8, plus its SHA-256.)

---

## Deliverable and acceptance

1. **CONFIRMED (deposit-ready):** a single stdlib-only Python file that (a) uses no float
   in any certificate path (assert-guarded), (b) computes `O_j` per-definition and
   cross-checks Chebyshev, (c) passes K1–K8 for both instances, (d) prints
   `ALL_CERTIFIED_CHECKS_PASSED`, (e) comes with its SHA-256. This file will be deposited at
   `theorems/B2-exact-collision/checker/` and pinned in the test suite (re-run on every
   `pytest`), moving B2's independent-replay path from a one-off reconstruction to a
   permanent, machine-re-verified checker.

2. **DISCREPANCY:** if any anchor value does not reproduce, report the exact computed value
   and whether the collision `Cn + Rd = 0` still holds with corrected values.

3. **DEGENERATE:** if `det C = 0` for the stated heights, report it (would indicate the
   rank lemma fails for those specific `t_k`).

All outcomes decisive; exact rational arithmetic only; no floating point in acceptance
checks. A non-certified floating-point cross-check may be included for orientation but must
not be imported into the certificate path (the deposit test will reject `import numpy`,
`import scipy`, `import mpmath`, or `float(` in the certified file).
