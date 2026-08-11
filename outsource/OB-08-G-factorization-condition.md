# Problem OB-08 — G: Factorization Condition (2.7) for 𝔐_FC

**Type:** pure analysis / operator theory (Fredholm determinants, spectral theory,
definition verification)  
**Non-circularity:** RH is not assumed, and RH does not appear in any hypothesis.
The question is whether a structural property of the method class 𝔐_FC (defined below)
holds — specifically whether every admissible output of every P ∈ 𝔐_FC factors through
the observation map O_θ.

---

## All definitions (self-contained — everything is here)

**The observation map O_θ.** Define the Riemann–Siegel theta function:
```
θ(t) = Im(log Γ(1/4 + it/2)) − t·log(π)/2,
```
which is a smooth, strictly increasing function for large t. The archimedean level
sequence (d_n)_{n≥1} is defined by:
```
θ(d_n) = (n − 1) π    (so A(d_n) = n,  A(t) := θ(t)/π + 1).
```
Explicitly, d_n is the n-th solution to θ(t) = (n−1)π; these are the Gram points
shifted by one index (d_n = g_{n-1} in the standard Gram-point notation, where
g_k is defined by θ(g_k) = kπ).

Numerical values: d_1 = g_0 ≈ 17.846, d_2 = g_1 ≈ 23.170, d_3 = g_2 ≈ 27.670.
(Note: d_1 ≈ 17.846, NOT γ_1 ≈ 14.134.)

The observation map is:
```
O_θ : {zero multisets} → ℝ^ℕ,   O_θ(𝒵) := (d_n)_{n≥1}.
```
The key property: O_θ is CONSTANT on all multisets — it returns the same sequence
regardless of the input 𝒵. The observation is computed from the theta function alone,
not from the zero locations of 𝒵.

**Method class 𝔐_FC.** A construction procedure P belongs to 𝔐_FC if it:
1. Takes as input only: the archimedean levels {d_n : n ≤ N}, arithmetic data
   (primes, local factors, weights) that are zero-free (no zero ordinates of any
   L-function), and no parameter fitted against known Riemann zeros or spectral
   samples of ζ.
2. Constructs a finite-rank self-adjoint positive semidefinite operator K_N on a
   Hilbert space H.
3. Claims that det(I − z² K_N) → Ξ(z) locally uniformly as N → ∞.

**The kappa_toeplitz construction (canonical example of 𝔐_FC).**
The sibling repository `absolute-arithmetic-spectral-verification` defines:
```
κ_n^{smooth} = 1 / (1/4 + d_n²),    n = 1, 2, 3, …
K_N = D_κ + α C_Toeplitz,
```
where D_κ = diag(κ_1, …, κ_N) and C_Toeplitz is a Bochner–Toeplitz correction with
α chosen to enforce positivity. The eigenvalues of K_N approximate {κ_n^{smooth}}.

The Fredholm determinant of I − z² K_N is:
```
det(I − z² K_N) = ∏_{n=1}^{N} (1 − z²/λ_n(K_N)),
```
where λ_n(K_N) are the eigenvalues of K_N. The goal is λ_n(K_N) ≈ κ_n^{smooth}
= 1/(1/4 + d_n²), so that (in the limit):
```
∏_n (1 − z² · (1/4 + d_n²)) "→" ∏_n (1 − z²/γ_n²) = Ξ(z)/Ξ(0)?
```
(The eigenvalue convergence λ_n(K_N) → 1/(1/4 + d_n²) as N → ∞ would give
det(I − z² K_N) → ∏_n (1 − z²/(1/4 + d_n²)), which converges to
F_d(z) = C · ∏_n (1 − z²/d_n²) only if the 1/4 is absorbed — see the main
obstruction below.)

**Factorization condition (2.7).** The program (spec/PROGRAM.md §7.B.2, item 2.7) states:
```
Every admissible output of every P ∈ 𝔐_FC factors through O_θ.
```
More precisely: the map P : (arithmetic data) → K_N must factor as
```
P = (construction from d_n) ∘ O_θ,
```
meaning that K_N is determined solely by the sequence (d_n) and zero-free arithmetic
data, and two inputs giving the same (d_n) sequence must give the same K_N (up to
unitary equivalence).

**The information obstruction (Theorem G).** Proposition G.3* (proof.md §4)
proves unconditionally (see OB-04 referee report, 2026-08-11):
- (Item 2) The multisets {d_n} and {γ_n} differ in infinitely many entries.
  (Proof: if symmetric difference were finite, S_1(T) = Ω(T), contradicting
  Littlewood's bound S_1(T) = O(log T).)
- (Item 3) F_d(z) := C · ∏(1 − z²/d_n²) ≠ F_γ(z) := C · ∏(1 − z²/γ_n²).
- (Item 4) |F_d(iR) / F_γ(iR)| ~ C/R → 0 as R → ∞.

The conclusion of Theorem G is: any P ∈ 𝔐_FC (IF factorization condition 2.7 holds)
produces K_N with det(I − z² K_N) → F_d (not Ξ = F_γ), so det ≠ Ξ. The claim is
that O_θ does not see the S(T) gap needed to transition from d_n to γ_n.

---

## The claims to be verified

### Claim A: Factorization condition (2.7) holds for kappa_toeplitz

**Claim A.** The kappa_toeplitz construction (the canonical example of 𝔐_FC) satisfies
the factorization condition (2.7): K_N is determined solely by (d_1, …, d_N) and
zero-free arithmetic data; two inputs giving the same (d_n) sequence produce the same K_N.

**Argument.** The definition
```
κ_n^{smooth} = 1 / (1/4 + d_n²)
```
shows that K_N depends only on (d_1, …, d_N) (plus the zero-free Bochner–Toeplitz
correction, which also depends only on d_n). Therefore K_N is a function of (d_n) alone.
Any other zero multiset 𝒵 with the same O_θ output (d_n) — which is trivially every
𝒵, since O_θ is constant — would give the same K_N. ✓

**What to verify for Claim A:**
1. Confirm the Bochner–Toeplitz correction C_Toeplitz is indeed a function of (d_n)
   only, not of (γ_n) or other zero locations. (The correction is defined to enforce
   positive semidefiniteness of K_N; if it depends on zero locations, condition (2.7)
   fails.)
2. The alpha parameter in K_N = D_κ + α C_Toeplitz: how is α chosen? If α depends on
   ζ or zero ordinates, condition (2.7) may fail.
3. Confirm condition (2.7) is a property of ALL P ∈ 𝔐_FC, not just kappa_toeplitz —
   i.e., it is part of the DEFINITION of 𝔐_FC (in which case it holds by assumption),
   or it is a THEOREM about 𝔐_FC (in which case it needs proof).

### Claim B: Is (2.7) definitional or a theorem?

**Question.** In the program definition of 𝔐_FC (§1 of statement.md above), condition
(2.7) is stated as a required property:
> "constructs K_N using ONLY: the archimedean levels {d_n}, arithmetic data that are
> zero-free, and no parameter fitted against known zeros."

This is a membership condition. Is the factorization condition (2.7) therefore:
- **(B-definitional)** Already implied by the membership conditions of 𝔐_FC as stated
  (conditions 1–3 in statement.md §1): any P satisfying those conditions automatically
  factors through O_θ; OR
- **(B-theorem)** A non-trivial additional claim that requires proof: there could be a
  construction satisfying conditions 1–3 but whose K_N does not factor through O_θ.

**What to verify for Claim B:**
Determine which case holds. Specifically:
1. Can a construction P satisfy conditions 1–3 of 𝔐_FC but have K_N NOT determined
   by (d_n)? (For example: K_N depends on a complicated function of the archimedean
   data that is equivalent to reading zero ordinates through a back door.)
2. Does the program's condition "zero-free input" (condition 1 of 𝔐_FC) plus
   "no fitting against known zeros" already force (2.7)?

### Claim C: The obstruction conclusion under (2.7)

**Claim C.** Assuming factorization condition (2.7) holds for all P ∈ 𝔐_FC,
the information obstruction (Theorem G) concludes: if the locally uniform limit
of det(I − z² K_N) exists, it is NOT equal to Ξ(z).

**The precise obstruction argument.** The kappa_toeplitz construction has
eigenvalues κ_n = 1/(1/4 + d_n²). The Fredholm determinant is therefore:
```
det(I − z² K_N) = ∏_{n=1}^{N} (1 − z² κ_n) = ∏_{n=1}^{N} (1 − z²/(1/4 + d_n²)).
```
As N → ∞ (assuming the product converges), the limit would be:
```
F̃_d(z) := C̃ · ∏_{n≥1} (1 − z²/(1/4 + d_n²)),
```
which has zeros at z = ±√(1/4 + d_n²) ≈ ±d_n (for large n). This function has:
- zeros at ±√(1/4 + d_n²), NOT at ±γ_n;
- even for small n: √(1/4 + d_1²) ≈ √318.73 ≈ 17.853 ≠ γ_1 ≈ 14.134.

Meanwhile Ξ(z) has zeros at ±γ_n. By the Hadamard canonical product structure,
F̃_d ≠ Ξ whenever {√(1/4 + d_n²)} ≠ {γ_n} as multisets. This fails unconditionally
because d_n ≠ γ_n for infinitely many n (Prop. G.3* Item 2) and √(1/4 + d_n²) > d_n.

**What to verify for Claim C:**
1. Does the infinite product ∏(1 − z²/(1/4 + d_n²)) converge locally uniformly?
   This requires Σ_n 1/(1/4 + d_n²) < ∞. Since d_n ∼ 2πn/log n, this sum
   converges (compare with Σ (log n/n)² < ∞). Confirm.
2. The N=1 sanity check (numerical anchor below) confirms F̃_d ≠ Ξ explicitly.
3. Is the obstruction purely about zeros (d_n vs γ_n), or also about the 1/4 shift?
   Both: even if d_n = γ_n for all n, the zeros of F̃_d would be at
   √(1/4 + γ_n²) ≠ γ_n. This is a SEPARATE obstruction from the d_n ≠ γ_n gap.

### Claim D: Non-vacuity — kappa_toeplitz is in 𝔐_FC

**Claim D.** The kappa_toeplitz construction is a valid example of 𝔐_FC:
it satisfies all three membership conditions (zero-free input, positive semidefinite K_N,
Fredholm-determinant goal).

**What to verify for Claim D:**
1. Positive semidefiniteness of K_N = D_κ + α C_Toeplitz: the Bochner–Toeplitz
   correction enforces this; what is the precise positive-semidefiniteness proof?
   (Reference: sibling repo proof/m3/bochner_positivity.py — but state the ANALYTIC
   argument, not just a numerical check.)
2. The Fredholm determinant is well-defined for trace-class operators K_N (since K_N
   is finite-rank, det is a polynomial in z², so convergence is trivial for fixed N).
3. The N → ∞ limit: what convergence mode is claimed? (The program says "locally
   uniform"; is this achieved for any known choice of α in the Toeplitz correction?)

---

## Proof skeleton to be closed

### Step 1 — Resolve Claim B: is (2.7) definitional or a theorem?

Read the membership conditions of 𝔐_FC as stated in statement.md §1 and
spec/PROGRAM.md §9.G. Determine whether condition (2.7) is already implied
by those conditions, or needs an additional hypothesis.

**Acceptance for Step 1:** a clear determination: DEFINITIONAL or THEOREM, with
the specific passage from the definition that establishes or fails to establish (2.7).

### Step 2 — Resolve Claim A: kappa_toeplitz satisfies (2.7)

Confirm (or refute) that the Bochner–Toeplitz correction and α-parameter depend only
on (d_n) and zero-free arithmetic data.

**Acceptance for Step 2:** CONFIRMED (with the argument for each component) or
REFUTED (with the specific component that uses zero ordinates or ζ-data).

### Step 3 — Resolve Claim C: precise form of the obstruction

Write out the exact form of the Fredholm determinant limit for kappa_toeplitz, and
confirm (or refute) that it cannot equal Ξ because d_n ≠ γ_n.

**Acceptance for Step 3:** a precise statement of what the limit IS (if it exists),
and why it ≠ Ξ (citing Prop. G.3* Items 2–4 from OB-04 review).

### Step 4 — Resolve Claim D: non-vacuity

Confirm or refute that kappa_toeplitz ∈ 𝔐_FC by checking all three membership conditions.

---

## Acceptance criteria

1. **CONFIRMED**: Claims A–D are all verified; the obstruction is stated cleanly;
   condition (2.7) is either definitional (trivially satisfied) or proved for kappa_toeplitz.

2. **PARTIAL**: some claims confirmed; at least one gap identified with a precise fix.
   The minimum acceptable result: determine whether (2.7) is definitional (Step 1).

3. **BLOCKING-GAP**: if (2.7) is a non-trivial theorem and fails for kappa_toeplitz,
   the non-vacuity of 𝔐_FC may be at risk; state what modification to the class
   definition would restore both non-vacuity and (2.7).

4. **NORMALIZATION-ISSUE**: if Claim C reveals that the limit of det(I − z² K_N) is
   NOT F_d but a different function (due to the 1/4 offset), give the correct form
   of the limit and explain whether the obstruction (det ≠ Ξ) still holds.

All outcomes must be decisive with precise arguments, not informal estimates.

---

## Numerical anchor (sanity only — not an input)

For N = 1, K_1 = diag(κ_1) = diag(1/(1/4 + d_1²)):
```
d_1 ≈ 17.846,   κ_1 = 1/(0.25 + 17.846²) = 1/(0.25 + 318.48) = 1/318.73 ≈ 0.003138.
```
det(I − z² K_1) = 1 − z² · κ_1 = 1 − z²/318.73.
This has zeros at z = ±√318.73 ≈ ±17.854 (not at γ_1 ≈ 14.134).
For Ξ: first factor is (1 − z²/γ_1²) = (1 − z²/199.77), zero at z ≈ ±14.134.
Clearly det(I − z² K_1) ≠ (Ξ normalization) even for N=1, because 1/κ_1 = 318.73
is NOT γ_1² ≈ 199.77. This confirms the normalization gap: d_1² + 1/4 ≠ γ_1².
