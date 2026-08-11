# Problem OB-18 — B1: independent exact-rational replay of the approximate-collision decay

**Type:** computational verification (exact rational arithmetic; independent
reconstruction of the finite observation-collision certificate)

**Non-circularity:** RH is not assumed. All inputs are explicit rationals and elementary
test functions. No ζ zero, Euler product, or functional equation is used. The task
replays a **finite** algebraic statement (a tolerance-collision at explicit parameters),
asserting nothing about any analytic function or RH.

**Why this task exists (computational-axis gate).** Theorem B1 (the unconditional
finite-observation *approximate*-collision, weaker than B2's exact collision) has no
independent certified replay of its quantitative decay. B2 reached INDEPENDENT-CHECKER
via OB-13; this task does the analogous independent reconstruction for B1's decay
certificate, so B1's computational axis can move NONE → INDEPENDENT-CHECKER.

---

## All definitions (self-contained — everything is here)

### Test functions (Li-type)

For `j = 1, 2, …, m`: `φ_j(ρ) = 1 − (1 − 1/ρ)^j`. Note `φ_1(ρ) = 1/ρ`,
`φ_2(ρ) = 2/ρ − 1/ρ²`.

### Global observation map (symmetric Σ' convention)

For a finite multiset `𝒵` of nonzero complex numbers avoiding `{0,1}`, with
multiplicity,
```
O_j(𝒵) = Σ_{ρ ∈ 𝒵} [φ_j(ρ) + φ_j(1−ρ)].
```
Additive under multiset union. Reality: since `φ_j` has real coefficients,
`φ_j(z̄) = φ_j(z)‾`.

### The B1 construction (approximate collision)

Fix a reference on-line multiset `𝒵_+` with `P(𝒵_+) = 1` (all atoms on `Re = 1/2`).
Form
```
𝒵_−(T) = 𝒵_+ ⊔ Q(σ_0, T),   Q(σ_0, T) = {σ_0+iT, σ_0−iT, 1−σ_0+iT, 1−σ_0−iT},
```
with `σ_0 ∈ (1/2, 1)` (take `σ_0 = 3/4`) and `T > 0`. Then `P(𝒵_−) = 0` (off-line
atoms at `Re = 3/4 ≠ 1/2`), and by additivity
```
O_j(𝒵_−(T)) − O_j(𝒵_+) = δ_j(T) := O_j(Q(σ_0, T)) = 4 Re[φ_j(σ_0+iT) + φ_j(1−σ_0+iT)].
```
(The quartet is reflection-symmetric, so `Σ'` over it equals twice the ordinary sum,
which combines into `4 Re[·]` over the two upper-half points — hence the factor 4.)

**B1 claim:** for any fixed finite Li family `Φ = (φ_1,…,φ_m)` and any tolerances
`ε_j > 0`, there is `T` with `|δ_j(T)| < ε_j` for all `j` simultaneously. I.e. the
off-line `𝒵_−(T)` collides with the on-line `𝒵_+` to within any prescribed tolerance,
under the finite observation `O_Φ` — so a fixed finite window cannot certify the
predicate `P`.

### The decay rate (to be verified exactly)

For `φ_1(ρ) = 1/ρ`: `δ_1(T) = 4 Re[1/(σ_0+iT) + 1/(1−σ_0+iT)]`. As `T → ∞`,
```
δ_1(T) = 4[σ_0/(σ_0²+T²) + (1−σ_0)/((1−σ_0)²+T²)] = 4/T² + O(T^{-4}),
```
so `δ_1(T)·T² → 4` (independent of `σ_0`, since `σ_0 + (1−σ_0) = 1` and the leading term
is `4(σ_0+(1−σ_0))/T² = 4/T²`). More generally `δ_j(T) = O_j(T^{-2})`.

---

## The claims to be verified (exact rational arithmetic)

### V1 — Exact quartet contributions at T = 1, σ_0 = 3/4

Compute `δ_1(1)` and `δ_2(1)` in exact rationals from `φ_j`, and verify:
```
δ_1(1) = 1216/425,
δ_2(1) = 1763072/180625.
```
(Compute `Re φ_j(3/4+i)` and `Re φ_j(1/4+i)` exactly via `ρ = a+ib`,
`1/ρ = (a−ib)/(a²+b²)`, etc.; then `δ_j(1) = 4(Re φ_j(3/4+i) + Re φ_j(1/4+i))`.)

### V2 — Monotone decay to below tolerance

For `σ_0 = 3/4`, `m = 2`, tolerance `ε = 10^{−3}`: find the least positive integer `T*`
with `|δ_1(T*)| < ε` and `|δ_2(T*)| < ε` simultaneously, computing each `δ_j(T)` in exact
rationals. Report `T*` and the exact rational values `δ_1(T*), δ_2(T*)`. (Sanity: the
float table gives `δ_1(100) ≈ 4.0·10^{−4}`, `δ_2(100) ≈ 1.6·10^{−3}`, so `T* ≈ 130`;
confirm the exact threshold.)

### V3 — Leading decay constant

Verify `δ_1(T)·T² → 4` by computing the exact rational `δ_1(T)·T²` at `T = 100, 1000,
10000` and confirming convergence to 4:
```
δ_1(100)·100² = 3.9998…,   δ_1(1000)·1000² = 3.99999…,   δ_1(10000)·10000² = 4.0000…
```
Give the exact rationals and confirm the limit is 4 (independent of `σ_0`: repeat for
`σ_0 = 2/3` and confirm the same limit 4).

### V4 — Predicate separation and membership

Confirm `P(𝒵_+) = 1` (all atoms on `Re = 1/2`), `P(𝒵_−(T)) = 0` (quartet at
`Re = 3/4`), and that `𝒵_−(T)` is symmetric under `ρ ↦ ρ̄` and `ρ ↦ 1−ρ` (the quartet is
closed under both), hence lies in the ambient class `𝔛_sym`.

### V5 — Adversarial mutation guard

(a) Replace the quartet abscissa `σ_0 = 3/4` by `σ_0 = 1/2` (on-line): then `δ_j(T)`
    still `→ 0`, BUT `P(𝒵_−) = 1` — the predicate no longer separates, so the "collision"
    is trivial. Confirm the predicate flips (this shows the off-line requirement is
    load-bearing).
(b) Replace `φ_1` by the constant test `φ ≡ 1`: then `δ(T) = 4·(number of quartet
    upper-half points) = 8 ≠ 0` for all `T` — no decay. Confirm `δ` does not tend to 0,
    showing the decay depends on `φ_j` vanishing at infinity (Li tests do; constants
    don't).

---

## Proof skeleton to be closed (verification steps)

### Step 1 — Exact δ_j(T) from φ_j (V1, V4)
Implement exact rational-complex arithmetic; compute `δ_j(T)` directly from
`φ_j(ρ)=1−(1−1/ρ)^j`. **Acceptance:** V1 table reproduced exactly, or first discrepancy.

### Step 2 — Threshold and decay (V2, V3)
Scan `T` for the tolerance threshold; compute `δ_1(T)·T²` at the three scales.
**Acceptance:** exact `T*` and the certified limit 4 (for two values of `σ_0`).

### Step 3 — Mutation guard (V5)
Run both mutations. **Acceptance:** (a) predicate flips to `P=1`; (b) `δ` stays `= 8`.

---

## Acceptance criteria

1. **CONFIRMED:** V1–V5 verified in an independent exact-rational implementation (report
   language + exact-arithmetic library). This provides INDEPENDENT-CHECKER computational
   evidence for B1's approximate-collision decay — validating ONLY the finite tolerance
   statement, not any analytic limit or RH.

2. **DISCREPANCY:** a V1/V2/V3 value does not reproduce; report the exact computed value
   and whether the decay `δ_j(T) → 0` still holds.

3. **INCONCLUSIVE:** if some step needs a convention not fixed here (e.g. a different
   Σ' normalization), state which and give the value under each reading.

All outcomes decisive; exact rationals only (no floats in acceptance checks).

---

## Numerical anchor (sanity only — this IS the reconstruction target)

Quickest first check: `φ_1(ρ)=1/ρ`, so
`δ_1(1) = 4[Re(1/(3/4+i)) + Re(1/(1/4+i))] = 4[(3/4)/(9/16+1) + (1/4)/(1/16+1)] =
4[12/25 + 4/17] = 4·(204+100)/425 = 1216/425 ≈ 2.861`. And `δ_1(100)·100² ≈ 3.9998 → 4`.
These (`1216/425` and the decay constant `4`) are the quickest sanity anchors; the full
V1–V5 exact replay is the target.
