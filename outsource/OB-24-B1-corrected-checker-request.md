# Problem OB-24 — B1: corrected R-atom certified checker (supersedes OB-18's doubled convention)

**Type:** computational verification — request for a **runnable, deposit-ready** exact-rational
checker of B1's finite-inequality decay certificate, in **B1's own R-atom Σ′ convention**.

**Why this exists.** OB-18 supplied a B1 decay checker, but OB-23 (B1 Gate-A review) found
it used **B2's doubled (R-symm) Σ′ convention**, not B1's. B1 defines
`O_j(𝒵) = Σ'_{ρ∈𝒵} φ_j(ρ)` — the sum of `φ_j` over the atoms once (`Σ'` is the
convergence regularization, not a doubling). Under this correct convention the anchors are
`δ_1(1) = 608/425` (not 1216/425), `T* = 90` (not 127), and decay `δ_j(T)·T² → 2j²` (not
4j²). This task requests an independently-written checker in the R-atom convention, to
restore B1's computational axis to INDEPENDENT-CHECKER and support its Gate-A advance.

**Non-circularity (mandatory).** RH is not assumed; no ζ zero, Euler product, or functional
equation is used. All objects are explicitly constructed finite complex-rational multisets.
The program validates only a finite algebraic decay statement, asserting nothing about
analytic functions or RH.

**Independence requirement.** Written from the definitions below, stdlib only
(`fractions.Fraction` + integers), no floating point in any certificate path (no `float(`,
no `numpy`/`scipy`/`mpmath`). Compute `O_j` by traversing the quartet per B1's R-atom
definition; separately cross-check the Li closed form. Report the program's SHA-256.

---

## All definitions (self-contained — everything is here)

### Complex-rational arithmetic
`z = a + bi`, `a,b ∈ Fraction`; implement `+, −, ×`, `1/z = (a−bi)/(a²+b²)`, integer powers.

### Test functions (Li-type, W1)
`φ_j(ρ) = 1 − (1 − 1/ρ)^j`, `j = 1,…,m`. (For the moment family `φ_j(ρ)=ρ^{−k_j}` the same
R-atom rule applies; this task uses Li.)

### B1 observation — R-ATOM convention (the corrected one)
For a finite multiset `𝒵` of nonzero complex rationals avoiding `{0,1}`, with multiplicity:
```
O_j(𝒵) = Σ'_{ρ ∈ 𝒵} φ_j(ρ)      (sum of φ_j over the atoms, each counted once).
```
`Σ'` denotes the convergence regularization (pairing `ρ` with `1−ρ` to define the
conditionally convergent sum), NOT a doubling. **Do NOT add a separate `φ_j(1−ρ)` term** —
that is B2's R-symm convention and gives values a factor of 2 too large.

### Off-line quartet
`Q(σ_0, T) = {σ_0+iT, 1−σ_0+iT, σ_0−iT, 1−σ_0−iT}` (`σ_0 = 3/4`, `T > 0`), four atoms.
Its contribution:
```
δ_j(T) = O_j(Q(σ_0,T)) = φ_j(σ_0+iT) + φ_j(1−σ_0+iT) + φ_j(σ_0−iT) + φ_j(1−σ_0−iT).
```
For real-coefficient `φ_j`, `δ_j(T) = 2 Re[φ_j(σ_0+iT) + φ_j(1−σ_0+iT)]` (conjugate pairs).

---

## Checks the program must certify (all exact rational)

### K1 — Observation real, per-definition == Li closed form
`δ_j(T)` has imaginary part exactly 0 (assert); the per-definition four-atom traversal
equals the closed form `2 Re[φ_j(σ_0+iT)+φ_j(1−σ_0+iT)]`, entry by entry.

### K2 — Anchor value (m=1, σ_0=3/4, T=1)
`δ_1(1) = 608/425` exactly. (Sanity: `φ_1(ρ)=1/ρ`, so
`δ_1(1) = 2[(3/4)/((3/4)²+1) + (1/4)/((1/4)²+1)] = 2[12/25 + 4/17] = 608/425`.)

### K3 — Leading decay constant
`δ_j(T)·T² → 2j²` as `T → ∞`. Verify the exact rationals `δ_1(T)·T²` and `δ_2(T)·T²` at
`T = 100, 1000, 10000` converge to `2` and `8` respectively.

### K4 — Joint integer threshold (m=2, ε = 10⁻³)
The least positive integer `T*` with `|δ_1(T*)| < 10⁻³` and `|δ_2(T*)| < 10⁻³` is
`T* = 90`. Verify by exact integer comparison: at `T=89` the `j=2` value exceeds `10⁻³`
(`δ_2(89) ≈ 1.0099·10⁻³`), at `T=90` both are below (`δ_2(90) ≈ 9.876·10⁻⁴`); `δ_j`
decreasing in `T`. Report the exact rational `δ_1(90), δ_2(90), δ_2(89)`.

### K5 — Predicate + membership + mutation guards
`P(𝒵_+)=1` (on-line), `P(𝒵_−)=0` (quartet at `Re=3/4`); `𝒵_± ∈ 𝔛_sym` (closed under
`ρ↦ρ̄`, `ρ↦1−ρ`, with multiplicity). Mutation guards: (a) `σ_0 = 1/2` flips the predicate
to `P(𝒵_−)=1` (off-line requirement load-bearing); (b) constant test `φ ≡ 1` gives
`δ ≡ 4 ↛ 0` (four atoms × value 1; decay needs `φ_j` vanishing at ∞) — note under R-atom
this is `4`, not `8`.

### K6 — Convention guard (the point of this task)
Assert explicitly that the R-atom `δ_1(1) = 608/425`, and that the R-symm value
`Σ_ρ[φ_1(ρ)+φ_1(1−ρ)] = 1216/425` is exactly twice it — documenting the factor-2
divergence so a future reader cannot silently reintroduce the wrong convention.

---

## Deliverable and acceptance

1. **CONFIRMED (deposit-ready):** a single stdlib-only file that (a) uses no float in any
   certificate path, (b) computes `O_j` per B1's R-atom definition and cross-checks the Li
   closed form, (c) passes K1–K6, (d) prints `ALL_CERTIFIED_CHECKS_PASSED`, (e) reports its
   SHA-256. It will be deposited at `theorems/B1-finite-inequality/checker/` and pinned in
   the test suite, restoring B1's computational axis to INDEPENDENT-CHECKER under the
   correct convention.

2. **DISCREPANCY:** if any anchor (608/425, T*=90, 2j²) does not reproduce, report the exact
   computed value and which definitional step diverges.

All outcomes decisive; exact rational arithmetic only; the deposit test rejects
`import numpy/scipy/mpmath` or `float(` in the certified file.

---

## Numerical anchor (sanity only — this IS the reconstruction target)

R-atom, `σ_0=3/4`: `δ_1(1) = 2[12/25 + 4/17] = 608/425 ≈ 1.4306`; `δ_1(T)·T² → 2`;
`T* = 90` for `m=2, ε=10⁻³`. (Contrast B2's R-symm `1216/425`, `T*=127`, `4j²` — a factor
2 larger; that convention is correct for B2 but wrong for B1. See PROMPT_LINT L21.)
