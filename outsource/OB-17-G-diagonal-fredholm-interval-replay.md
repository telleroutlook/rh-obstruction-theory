# Problem OB-17 — G: independent interval-arithmetic replay of the diagonal Fredholm obstruction

**Type:** computational verification (certified interval arithmetic; independent
reconstruction of a finite spectral certificate)

**Non-circularity:** RH is not assumed and is never used. All quantities are computed
from the Riemann–Siegel theta function and elementary interval arithmetic. No zero
ordinate of ζ is read as an input; the comparison ordinate `γ_1 ≈ 14.1347` appears ONLY
as a published sanity constant in the final separation check, clearly labeled, and is not
used to build any object. The task validates a **finite** algebraic/analytic statement,
not the analytic limit theorem that motivates it.

**Why this task exists (computational-axis gate).** The repository's evidence ledger
requires, for a finite certificate, an *independent* certified replay (interval / exact
arithmetic, outward rounding), independent reconstruction from raw data, an
adversarial-mutation check, and cross-implementation agreement. Theorem G's diagonal
obstruction (`𝔐_d^{tr}` core) has been argued analytically (OB-08) but its finite
numerical content has not had an independent certified replay. This task requests one.

---

## All definitions (self-contained — everything is here)

### The Riemann–Siegel theta function and Gram-type levels

Define, for real `t > 0`,
```
θ(t) = Im log Γ(1/4 + i t/2) − (t/2) log π,
```
using the continuous branch with `θ(0) = 0`. `θ` is smooth and strictly increasing for
`t` beyond its single minimum (`θ'(t) > 0` for `t ≳ 6.29`; `θ''(t) > 0` for all `t > 0`).
The **archimedean levels** `d_n` (`n ≥ 1`) are the unique strictly positive solutions of
```
θ(d_n) = (n − 1) π.
```
(These are the Gram points shifted by one index: `d_n = g_{n−1}` in the standard Gram
notation `θ(g_k) = kπ`.) Numerically, `d_1 ≈ 17.8456`, `d_2 ≈ 23.1703`, `d_3 ≈ 27.6702`.
The `d_n` are transcendental in general, so all computations below must be done in
**certified interval arithmetic** (outward rounding), NOT floating point.

### The diagonal operator and its Fredholm determinant

Define the eigenvalues
```
κ_n = 1 / (1/4 + d_n²)   (n ≥ 1),
```
and the finite-rank diagonal operator `D_N = diag(κ_1, …, κ_N)` on the first `N`
coordinates. Its Fredholm determinant is the polynomial in `z`
```
det(I − z² D_N) = ∏_{n=1}^{N} (1 − z² κ_n).
```
(Corrected Fredholm formula: zeros at `z = ±κ_n^{−1/2} = ±√(1/4 + d_n²)`, NOT at `±d_n`
and NOT at `±κ_n^{1/2}`.)

### The three functions to be kept distinct

- `G_d(z) = ∏_{n≥1} (1 − z²/(1/4 + d_n²))` — the locally uniform limit of `det(I−z²D_N)`.
  Its zeros are `±√(1/4 + d_n²)`.
- `F_d(z) = ∏_{n≥1} (1 − z²/d_n²)` — zeros at `±d_n` (the shifted-normalization target).
- `Ξ̂(z) = ξ(1/2+iz)/ξ(1/2)` — the normalized Riemann xi; under RH its zeros are `±γ_n`
  (`γ_1 ≈ 14.1347`). RH is NOT assumed; `γ_1` is used only as a labeled sanity constant.

The obstruction (Theorem G, OB-08) is that `G_d ≠ Ξ̂` **unconditionally**, via two
independent gaps: (i) the spectral shift `d_n ↦ √(1/4+d_n²) > d_n`, and (ii) the
`S(T)`-gap `{d_n} ≠ {γ_n}`.

---

## The claims to be verified (all by certified interval arithmetic)

### V1 — Gram levels, certified enclosures

Compute rigorous interval enclosures of `d_1, …, d_5` from `θ(d_n) = (n−1)π`, each of
width `< 10^{−8}`, and verify they contain:
```
d_1 ∈ 17.84559954 ± 10^{-6},   d_2 ∈ 23.17028270 ± 10^{-6},
d_3 ∈ 27.67018222 ± 10^{-6},   d_4 ∈ 31.71797995 ± 10^{-6},
d_5 ∈ 35.46718430 ± 10^{-6}.
```
Method: enclose `θ(t)` via an interval evaluation of `Im log Γ` (e.g. Arb/`python-flint`,
or `mpmath` with certified error bounds), then interval-bisect on the monotone branch.
Report the enclosure widths.

### V2 — Eigenvalues and determinant zeros

From the `d_n` enclosures, compute certified enclosures of `κ_n = 1/(1/4+d_n²)` and of the
determinant zeros `√(1/4+d_n²)`. Verify:
```
κ_1 ∈ 0.0031375953 ± 10^{-8},   √(1/4+d_1²) ∈ 17.8526027 ± 10^{-5}.
```

### V3 — The three-way separation (the obstruction, certified)

Verify, with **non-overlapping** intervals, that for `n = 1, 2, 3`:
```
γ_n  <  d_n  <  √(1/4 + d_n²),
```
using the published sanity constants `γ_1 ≈ 14.1347`, `γ_2 ≈ 21.0220`, `γ_3 ≈ 25.0109`
(labeled: these are the only place a ζ-zero value appears, and only for the comparison —
they build nothing). Confirm the three enclosures are pairwise disjoint for each `n`.
This certifies that the determinant zeros `√(1/4+d_n²)` differ from both `d_n` and `γ_n` —
the finite core of the obstruction `G_d ≠ Ξ̂`.

### V4 — Determinant convergence tail bound

Verify the product `∏(1 − z²κ_n)` converges locally uniformly by a certified tail bound:
show `Σ_{n>N} κ_n < ε` for a chosen `N`. Since `d_n ∼ 2πn/log n`,
`κ_n = O((log n / n)²)`, so `Σ κ_n < ∞`. Give a certified `N` such that
`Σ_{n>N} κ_n < 10^{−3}` (use a rigorous tail majorant, e.g. an integral bound on
`(log x / x)²` beyond an explicit point where the `d_n ≥ c·n/log n` lower bound is
certified). Report `N` and the tail bound.

### V5 — Adversarial mutation guard

Perturb the construction and confirm the obstruction check responds:
(a) replace `κ_1` by `1/d_1²` (i.e. drop the `1/4` shift) → the corresponding zero becomes
    `d_1`, and V3's strict inequality `d_1 < √(1/4+d_1²)` must collapse to equality at that
    node (confirm the mutated zero equals `d_1` within enclosure);
(b) replace `d_1` by `γ_1 ≈ 14.1347` → the node moves below the true `d_1` (confirm the
    V3 ordering breaks). Both mutations must make the certified separation fail, showing
    the check is not vacuously true.

---

## Proof skeleton to be closed (verification steps)

### Step 1 — Certified θ evaluation and inversion (V1)
Implement an interval enclosure of `θ(t) = Im log Γ(1/4+it/2) − (t/2)log π`. Verify `θ` is
strictly increasing on `[10, 40]` (e.g. certified `θ'(t) > 0` there), then interval-bisect
`θ(d_n) = (n−1)π`. **Acceptance:** enclosures of width `< 10^{−8}` matching V1, or the
first `d_n` that disagrees with the stated value.

### Step 2 — Eigenvalues, zeros, separation (V2, V3)
Propagate enclosures through `κ_n` and `√(1/4+d_n²)`; check the three-way disjointness.
**Acceptance:** all separations certified disjoint, or the first `n` where they overlap.

### Step 3 — Tail bound (V4)
Give a certified `N` and majorant for `Σ_{n>N} κ_n`. **Acceptance:** explicit `N` with
`Σ_{n>N} κ_n < 10^{−3}` proven, or a statement that the majorant cannot be certified.

### Step 4 — Mutation guard (V5)
Run both mutations; confirm the separation check fails. **Acceptance:** both mutations
break V3.

---

## Acceptance criteria

1. **CONFIRMED:** V1–V5 all verified in an independent certified-interval implementation
   (report the library: `python-flint`/Arb, or `mpmath` with rigorous error control).
   Enclosure widths reported; the three-way separation is certified disjoint; the tail
   bound is explicit; both mutations break the check. This provides the
   INDEPENDENT-CHECKER computational evidence for Theorem G's diagonal obstruction —
   validating ONLY the finite separation, not the analytic limit `det → G_d` or anything
   about RH.

2. **DISCREPANCY:** a stated enclosure value does not reproduce; report the certified
   interval obtained and whether the obstruction (three-way separation) still holds with
   corrected values.

3. **INCONCLUSIVE:** if certified interval arithmetic cannot achieve the stated widths
   (e.g. `Im log Γ` enclosure too coarse), report the achievable precision and which
   step blocks.

All outcomes decisive. Floating-point-only confirmation is NOT acceptable — the `d_n` are
transcendental and the separation gaps (e.g. `d_1` vs `√(1/4+d_1²)`, a gap of `≈ 0.007`)
must be certified by outward-rounded intervals.

---

## Numerical anchor (sanity only — this IS the reconstruction target)

The single quickest eyeball check (float, for orientation only; the deliverable is the
certified version): `d_1 ≈ 17.8456`, so `1/4 + d_1² ≈ 318.706`, `√(318.706) ≈ 17.8523`,
`κ_1 ≈ 0.0031376`. Meanwhile `γ_1 ≈ 14.1347`. The ordering `14.1347 < 17.8456 < 17.8523`
(i.e. `γ_1 < d_1 < √(1/4+d_1²)`) is the finite core of the obstruction. The full V1–V5
certified replay is the actual target.
