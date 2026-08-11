# Problem OB-10 — G: PSD Fredholm limit has all-real zeros

**Type:** operator theory / complex analysis (Fredholm determinants, Hurwitz theorem)

**Non-circularity:** RH is not assumed. The claim is a purely analytic/operator-theoretic
statement about locally uniform limits of Fredholm determinants of positive semidefinite
finite-rank operators.  No zeta function, Euler product, or zero ordinate appears as
an input.

---

## All definitions (self-contained — everything is here)

**Fredholm determinant for finite-rank PSD operators.** Let K_N be a finite-rank
positive semidefinite operator on a separable Hilbert space H, with nonzero eigenvalues
λ_1(K_N) ≥ λ_2(K_N) ≥ … ≥ λ_{r_N}(K_N) > 0 (counted with algebraic multiplicity,
r_N < ∞).  The Fredholm determinant is:
```
f_N(z) := det(I − z² K_N) = ∏_{j=1}^{r_N} (1 − z² λ_j(K_N)).
```
This is a polynomial in z² of degree r_N, normalized to f_N(0) = 1.

**Zeros of f_N.** Each zero of f_N satisfies `z² = λ_j(K_N)^{−1} > 0`, hence
`z = ±λ_j(K_N)^{−1/2} ∈ ℝ \ {0}`.  In particular:
- f_N has NO zeros in the open upper half-plane `{Im z > 0}`.
- f_N has NO zeros in the open lower half-plane `{Im z < 0}`.

**Locally uniform convergence.** Let (K_N) be a sequence of finite-rank PSD operators
and assume:
```
f_N(z) → f(z)   locally uniformly on ℂ,
```
where f is an entire function.  (Locally uniform convergence of polynomials to an
entire function is possible only if f is an entire function, by Weierstrass's theorem.)

**Notation.** Write `𝕌 = {z ∈ ℂ : Im z > 0}` (open upper half-plane) and
`𝕃 = {z ∈ ℂ : Im z < 0}` (open lower half-plane).

---

## The theorem to be verified

**Theorem (PSD Fredholm limit has all-real zeros).**
Under the conditions above, every zero of f is real.

*Proposed proof.*

**Step 1.** Each f_N is a polynomial with all zeros in ℝ.  In particular, f_N has no
zeros in 𝕌 and no zeros in 𝕃.

**Step 2.** The locally uniform convergence `f_N → f` on ℂ implies, in particular,
locally uniform convergence on 𝕌 and on 𝕃.

**Step 3 (Hurwitz's theorem).** Let D be any open disk with D ⊂ 𝕌.  Since f_N → f
locally uniformly on D, and each f_N has no zeros in D (by Step 1), Hurwitz's theorem
(see below) implies: f either has no zeros in D, or f ≡ 0 on D.

**Step 4.** f is not identically zero: f(0) = lim f_N(0) = 1 ≠ 0.

**Step 5.** Since f ≢ 0 (Step 4), by Hurwitz's theorem f has no zeros in any disk
D ⊂ 𝕌.  Since 𝕌 is covered by such disks, f has no zeros in 𝕌.  The same argument
applies to 𝕃.  Hence all zeros of f (if any) are in ℝ.  ∎

**Hurwitz's theorem (to be cited precisely).** Let D ⊂ ℂ be a connected open set,
let (g_N) be a sequence of functions holomorphic on D converging locally uniformly to
a holomorphic function g.  If each g_N has no zeros in D and g ≢ 0 on D, then g has
no zeros in D.

*Standard reference:* Conway, *Functions of One Complex Variable I*, 2nd ed., Theorem VII.2.5.
(Or: Ahlfors, *Complex Analysis*, 3rd ed., p. 176.)

---

## The claims to be verified

### Claim A: Hurwitz's theorem is correctly applied

**Claim A.** The application of Hurwitz's theorem in Steps 3–5 is valid as stated.

**What to verify for Claim A:**
1. Confirm that the locally uniform convergence `f_N → f` on ℂ implies locally uniform
   convergence on every open disk D ⊂ 𝕌.  (Trivially yes: a restriction of a locally
   uniform limit is locally uniform.)
2. Confirm that each f_N is holomorphic on D (trivially yes: polynomials are entire).
3. Confirm the exact version of Hurwitz's theorem that applies: the version requiring
   "g ≢ 0" versus the version requiring "g has isolated zeros" — state which form is
   being used and cite it by theorem number in a standard reference.
4. Confirm Step 5: 𝕌 is covered by open disks in 𝕌, and a zero-free function on every
   open disk in an open set is zero-free on the full open set.

### Claim B: f(0) = 1 (normalization)

**Claim B.** If f_N(0) = 1 for all N and f_N → f locally uniformly, then f(0) = 1.

**What to verify for Claim B:**
Simply: f(0) = lim_{N→∞} f_N(0) = 1 by continuity of evaluation at a fixed point under
locally uniform convergence. Confirm this one-line argument.

### Claim C: The conclusion is non-vacuous

**Claim C.** The class of limits f satisfying the conditions is non-empty and contains
non-trivial entire functions (i.e., not just f ≡ 1).

*Proposed example.* Take `K_N = diag(κ_1,…,κ_N)` with `κ_n = (1/4 + d_n²)^{-1}`
where d_n are the Gram points defined by θ(d_n) = (n−1)π (see OB-08 for definition).

Since Σ κ_n < ∞ (d_n ∼ 2πn/log n by Stirling), K_N converges in trace norm to
`K = diag(κ_n)`.  By the Fredholm determinant stability inequality (see OB-08 Theorem
6.1), `det(I − z²K_N) → G_d(z) = ∏_{n≥1}(1 − z²κ_n)` locally uniformly.

The function G_d is a non-trivial entire function (G_d ≢ 1, since κ_1 > 0 implies
G_d(κ_1^{-1/2}) = 0 ≠ 1).  By the theorem, G_d has all-real zeros.  Explicit
confirmation: the zeros of G_d are at `±κ_n^{-1/2} = ±√(1/4 + d_n²) ∈ ℝ`. ✓

**What to verify for Claim C:**
Confirm that the example K_N above satisfies all conditions of the theorem (PSD,
finite-rank, locally uniform convergence) and that the limit G_d has all-real zeros.

---

## Proof skeleton to be closed

### Step 1 — Zeros of f_N are real (trivial)

State and confirm: each factor `(1 − z²λ_j)` has zeros at `z = ±λ_j^{-1/2} ∈ ℝ`.

**Acceptance:** CONFIRMED (one sentence).

### Step 2 — Hurwitz application (Claim A)

State the precise version of Hurwitz's theorem being used, with theorem number and
reference.  Confirm Steps 3–5 of the proposed proof are valid.

**Acceptance:** CONFIRMED with exact citation (e.g., "Conway VII.2.5"), or PARTIAL
(identifying which step requires a stronger hypothesis).

### Step 3 — Normalization (Claim B)

Confirm f(0) = 1.

**Acceptance:** CONFIRMED.

### Step 4 — Non-vacuity (Claim C)

Confirm the diagonal example.

**Acceptance:** CONFIRMED.

---

## Acceptance criteria

1. **CONFIRMED:** All four steps verified; Hurwitz cited by exact theorem number;
   f has all-real zeros is established cleanly.

2. **PARTIAL:** some steps confirmed; one step has a gap (specify).  The minimum
   acceptable result: confirm Steps 1–2 with a precise Hurwitz citation.

3. **REFUTED:** a step fails; an explicit counterexample is given; if f can have
   non-real zeros despite the conditions, an explicit example is required.

All outcomes decisive.  "The theorem is well-known" is not CONFIRMED unless accompanied
by a specific theorem number in a standard reference.

---

## Numerical anchor (sanity only — not an input)

For N = 1, K_1 = diag(κ_1) with κ_1 = 1 (choose for simplicity):
```
f_1(z) = 1 − z².
```
Zeros: z = ±1 ∈ ℝ. ✓  No zeros in 𝕌 or 𝕃. ✓

For the sequence K_N = diag(1, 1/4, 1/9, …, 1/N²):
```
f_N(z) = ∏_{n=1}^N (1 − z²/n²).
```
Locally uniformly, `f_N → sin(πz)/(πz)`, which has zeros at z = ±1, ±2, … ∈ ℝ. ✓
