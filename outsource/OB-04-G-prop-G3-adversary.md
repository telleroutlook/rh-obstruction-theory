# Problem OB-04 — Smooth adversary O_θ-indistinguishability (Theorem G, Prop. G.3)

**Type:** Analytic number theory. Requires knowledge of the Riemann-von Mangoldt
formula, the argument function S(T), and properties of the completed xi function.  
**Repo context:** This verifies Proposition G.3 in Theorem G (`theorems/G-fredholm-certificate/`)
of the RH Obstruction Theory repository. You do NOT need any other file from that repo.

---

## Self-contained setup

### The smooth zero-counting function and archimedean levels

The Riemann-von Mangoldt formula states:
```
N(T) = θ(T)/π + 1 + S(T),
```
where:
- `N(T) = #{ρ : Im(ρ) ∈ (0,T]}` is the zero-counting function of ζ in the upper
  critical strip;
- `θ(T) = Im(log Γ(1/4 + iT/2)) − (T/2) log π` is the smooth (zero-free) phase;
- `S(T) = (1/π) arg ζ(1/2 + iT)` is the argument function (fluctuation).

**Archimedean levels.** Define `d_n` as the unique solution to:
```
θ(d_n)/π + 1 = n,
```
i.e., the n-th value of T where the smooth part of N equals n. These satisfy
`d_n → ∞`, `d_n ~ γ_n` (the true Riemann zero ordinates), but with discrepancy
`γ_n − d_n = S(γ_n)/N'(γ_n) + O(1/γ_n)`, `N'(T) ~ log(T/2π)/(2π)`.

### The observation map O_θ

A method `P ∈ 𝔐_FC` (Fredholm certificate class) reads only the archimedean level
data. Its observation map is:
```
O_θ : {zero multisets} → ℝ^ℕ,   O_θ(𝒵) = (d_1, d_2, d_3, …),
```
where `(d_n)` is the sequence of archimedean levels computed from the gamma factor
alone (zero-free). **Key point:** `O_θ` does NOT depend on where the zeros of ζ
actually are; it is entirely determined by `θ(T)`, which is zero-free.

---

## The proposition to be verified

**Proposition G.3.** Define the two multisets:
```
𝒵_RH   := {γ_n : n ≥ 1}   (true Riemann zero ordinates, with multiplicity)
𝒵_smooth := {d_n : n ≥ 1}   (archimedean levels)
```
Then:
1. `O_θ(𝒵_RH) = O_θ(𝒵_smooth) = (d_n)_{n≥1}`.
2. `𝒵_RH ≠ 𝒵_smooth` as multisets.
3. The entire functions determined by these multisets are distinct:
   ```
   Ξ_smooth(z) := Ξ(0) · ∏_{n≥1} (1 − z²/d_n²)   ≠   Ξ(z) = Ξ(0) · ∏_{n≥1} (1 − z²/γ_n²).
   ```
4. Quantitative separation: there exists an explicit sequence of radii `R_k → ∞` such
   that `|Ξ_smooth(iR_k)| / |Ξ(iR_k)|` is bounded away from 1.

---

## The proof strategy to be verified

### Step 1 — O_θ outputs the same sequence for both

`O_θ` outputs `(d_n)` by definition, regardless of the input zero multiset (it
computes from `θ(T)` only). Therefore `O_θ(𝒵_RH) = (d_n) = O_θ(𝒵_smooth)`. ✓

**Please verify:** Is this the correct definition of O_θ for the Fredholm certificate
class? Is it standard in the literature that the archimedean levels `d_n` are
determined from the smooth part of the counting function, without reference to zero
locations?

### Step 2 — The two multisets differ

**Claim.** `{γ_n} ≠ {d_n}`.

*Evidence.* By the von Mangoldt formula, `γ_n − d_n = S(γ_n)/N'(γ_n) + O(1/γ_n)`.
The argument function `S(T)` is:
- Not identically zero (Backlund, 1914: `S(γ_{1000}) ≠ 0` explicitly);
- Has infinitely many sign changes (Tsang, 1986; and earlier results);
- Satisfies `|S(T)| = O(log T)` unconditionally (classical).

Therefore `γ_n ≠ d_n` for infinitely many `n`.

**Please verify:** Cite the precise statement that `S(T) ≠ 0` for some specific `T`,
and that `S(T)` has infinitely many sign changes. Source: Titchmarsh, *The Theory of
the Riemann Zeta-Function*, §9.3–§9.4; Backlund (1914) Acta Math. 36; Tsang (1986).

### Step 3 — Hadamard uniqueness implies Ξ_smooth ≠ Ξ

The Hadamard factorization theorem for entire functions of order 1 states: an entire
function of order at most 1 with prescribed zeros `{±z_n}` (counted with multiplicity)
and prescribed value `F(0) = C ≠ 0` is uniquely determined.

Since `{γ_n} ≠ {d_n}` and both `Ξ` and `Ξ_smooth` are entire of order 1 with
normalization `Ξ(0) = Ξ_smooth(0) = Ξ(0)`, Hadamard uniqueness gives `Ξ ≠ Ξ_smooth`. ✓

**Please verify:** (a) That `Ξ_smooth` is indeed entire of order 1. The condition
`Σ d_n^{-2} < ∞` is needed; this follows from `d_n ~ γ_n ~ n/(2π) log n` (von Mangoldt)
and `Σ γ_n^{-2} < ∞`. (b) That `Ξ_smooth(0) = Ξ(0)` (same normalization constant).

### Step 4 — Quantitative separation

At `z = iR`:
```
Ξ_smooth(iR) / Ξ(iR) = ∏_{n≥1} [(1 + R²/d_n²) / (1 + R²/γ_n²)].
```
For `n` with `γ_n ≠ d_n`, the factor `(1 + R²/d_n²)/(1 + R²/γ_n²) ≠ 1`.

Specifically: at `R = γ_n` for any `n` with `d_n < γ_n` (which occurs when `S(γ_n) < 0`):
```
factor_n = (1 + γ_n²/d_n²) / 2  > 1/2   (and ≠ 1 since d_n ≠ γ_n).
```

Since `|Ξ(iR)| → ∞` as `R → ∞` (standard; each factor `≥ 1`), we have:
```
|Ξ_smooth(iR) − Ξ(iR)| ≥ |Ξ(iR)| · |Ξ_smooth(iR)/Ξ(iR) − 1|.
```
The ratio `Ξ_smooth(iR)/Ξ(iR)` is a convergent infinite product of positive terms;
for `R` near a zero ordinate where `d_n ≠ γ_n`, the ratio deviates from 1 by a
definite amount.

**Open quantitative question for the reviewer.** Can you give an explicit lower bound
on `|Ξ_smooth(iR)/Ξ(iR) − 1|` in terms of the first `N` zeros where `γ_n ≠ d_n`?
Specifically: for `R = γ_1` (the first zero ordinate, `γ_1 ≈ 14.134`), and using the
known fact `S(γ_1) ≠ 0`, what is `|d_1 − γ_1|` and how large is the factor deviation?

**Note:** The reviewer may use zero tables and numerical values for the quantitative
bound (Step 4 is a discovery-tier check). Steps 1–3 are the analytic core and require
no numerical inputs.

---

## What this does and does not prove

This proposition says: a method that observes only archimedean levels `(d_n)` cannot
distinguish the true Riemann zero multiset `{γ_n}` from the smooth adversary `{d_n}`.
The two are O_θ-indistinguishable but produce distinct entire functions under Hadamard
factorization. This is an **information obstruction** for the Fredholm certificate class
`𝔐_FC`.

It does NOT claim: (a) that `𝒵_smooth` is meaningful beyond this obstruction argument;
(b) that S(T) = 0 almost everywhere; (c) any claim about RH. The argument is
obstruction-theoretic, not constructive toward RH.

---

## Acceptance criteria

1. Verify Step 2: precise citation for `S(T) ≠ 0` infinitely often and for the
   discrepancy formula `γ_n − d_n = S(γ_n)/N'(γ_n) + O(1/γ_n)`.
2. Verify Step 3: that `Ξ_smooth` is entire of order 1 with the right normalization.
3. Verify or improve Step 4: quantitative separation at a specific `R`.
4. If the proof of any step is incomplete as stated, identify the gap precisely.
5. Optional: can the statement be strengthened from `O_θ` to a larger observation class
   (e.g., the full von Mangoldt explicit formula)? What additional data would be needed?
