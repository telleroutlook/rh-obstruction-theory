# Theorem E — Real-Rooted Approximants and the Missing Compactness Theorem

**Mathematical status:** PROOF-DRAFT  
**Computational status:** NONE  
**Theorem ID:** E-compactness  
**Program ref:** §10 (WP-E), §10.E.1–E.5  
**Paper target:** Paper C (primary, unconditional)

---

## Part I — Negative theorem (finite evidence ⇏ compact convergence)

### Setting

**Normalization (CCM entire-target, frozen for this theorem).**  
Following Connes–Consani–Moscovici (arXiv:2511.22755), the target is:

```
Ξ(z) = ξ(1/2 + iz)         (entire, even, all zeros real by RH)
```

with the CCM determinant identity:

```
det_reg(𝔇_{λ,N} − z) = −i · λ^{−iz} · ξ̂(z),
```

where `ξ̂` is the Fourier transform of `ξ` (entire, all zeros real = spectrum
of `𝔇_{λ,N}`).  The **open CCM step** is:
`suitably normalized det_reg → Ξ` as `N, λ → ∞`.

**This theorem works with the CCM entire target.**  The Suzuki meromorphic
target `z² ξ/ξ'` is kept separate (REFERENCE_BASELINE §5).

**Finite evidence record.**  An approximating entire function sequence `(F_N)_{N≥1}`
satisfies the **CCM finite evidence record** `ℰ_N` if:

1. `F_N` is an entire function of order one.
2. `F_N` is even: `F_N(−z) = F_N(z)`.
3. `F_N` is real on the real axis: `F_N(z̄) = F_N(z)̄`.
4. All zeros of `F_N` are **real** (real-rootedness).
5. The first `k_N → ∞` zeros of `F_N` (ordered by size) agree with
   the verified ordinates `γ₁ ≤ γ₂ ≤ …` of `ζ`.
6. A finite-dimensional determinant identity holds:
   `F_N(0) = ξ̂(0) · c_N` for a normalization constant `c_N > 0`.
7. Finitely many Taylor coefficients agree:
   `F_N^{(2j)}(0) = ξ̂^{(2j)}(0)` for `j = 0, 1, …, J_N`.

The record `ℰ_N` contains **no proved tail envelope**: the behavior of `F_N(z)`
for `|z|` large is uncontrolled.

**Convergence target:** locally uniform convergence
```
F_N(z) → Ξ(z)   as  N → ∞,   uniformly on every compact  K ⊂ ℂ.
```

---

### Theorem E-neg (finite evidence ⇏ compact convergence)

**Theorem E-neg.** There exists a sequence `(F_N)_{N≥1}` of entire functions,
each satisfying the CCM finite evidence record `ℰ_N` for every `N`, such that
`(F_N)` does **not** converge locally uniformly to `Ξ`.

More precisely: there exists `R > 0`, `ε > 0`, and a subsequence `(F_{N_j})`
such that

```
sup_{|z| ≤ R} |F_{N_j}(z) − Ξ(z)| ≥ ε   for all  j.
```

The counterexample sequence exposes a specific **invisible degree of freedom**:
the canonical-product tail (growth of the infinite-product factor beyond `z_{k_N}`).

---

### Construction of the counterexample sequence (proof sketch)

**Step 1: Hadamard factorization.**  Write
```
Ξ(z) = e^{A + Bz²} · Π_{n≥1} (1 − z²/γ_n²)
```
(using real zeros `±γ_n`, even function; `A, B` are explicit constants from
the rank and genus of `Ξ`).

For each `N`, define `F_N` by keeping the first `k_N` zeros in place and
inserting a **compensating tail** via a modified Hadamard factor:

```
F_N(z) = c_N · e^{A + B_N z²} · Π_{n=1}^{k_N} (1 − z²/γ_n²)
          · Π_{n=k_N+1}^{∞} (1 − z²/μ_{n,N}²),
```

where `μ_{n,N}` are **modified tail zeros** chosen so that:

- `|μ_{n,N} − γ_n| = δ_n > 0` for `n > k_N` (off-line perturbation);
- `Σ_{n>k_N} δ_n / γ_n^2 < ∞` (admissibility for order-one entire function);
- the normalization `c_N` and `B_N` are adjusted to enforce conditions 6–7.

**Step 2: Finite-record verification.**  
- Conditions 1–5: `F_N` is entire order-one, even, real on `ℝ_real`, and all
  zeros `±γ_1, …, ±γ_{k_N}, ±μ_{k_N+1,N}, …` are real (choose `μ_{n,N} ∈ ℝ`).
- Conditions 6–7: the normalization constants are adjusted accordingly (see §2).

**Step 3: Non-convergence.**  
Choose `δ_n = c / n` for `n > k_N` with `c > 0` fixed.  Then the tail product
```
Π_{n>k_N}(1 − z²/μ_{n,N}²) / (1 − z²/γ_n²)
```
does not converge to 1 uniformly on `|z| ≤ R` for any `R > γ_{k_N}`, because
the perturbation `Σ_n z²(γ_n^{-2} − μ_{n,N}^{-2})` accumulates for `|z| \sim γ_{k_N}`.

**Open item in this sketch:** making the non-convergence rigorous requires an
estimate showing that the accumulated tail perturbation does not vanish.  This
is a standard canonical-product convergence-rate argument (see e.g.
Levin, *Distribution of Zeros of Entire Functions*, Ch. II).  The details are
left for `proof.md §3` (to be completed with a quantitative version).

---

## Part II — Positive escape theorem (sufficient convergence package)

### Theorem E-pos (normal-family sufficiency)

**Theorem E-pos.** Let `(F_N)_{N≥1}` be a sequence of entire functions satisfying
the CCM finite evidence record `ℰ_N`, and additionally:

(H-norm) A base-point normalization: `F_N(z₀) → Ξ(z₀) ≠ 0` for some `z₀ ∈ ℂ`.

(H-bound) Local uniform boundedness: for every `R > 0`, there exists `M_R > 0`
with `sup_N sup_{|z| ≤ R} |F_N(z)| ≤ M_R`.

(H-tail) Summable tail control: there exist coefficients `a_{n,N} ∈ ℝ` such that
`Σ_n |a_{n,N} − γ_n^{-2}| < C` uniformly in `N`, and `F_N` has Hadamard
representation with zero sequence `(±r_{n,N})` satisfying
`Σ_n |r_{n,N}^{-2} − γ_n^{-2}| < C`.

(H-modulus) Effective convergence: there exists a computable `N(R, ε)` such that
`|F_N(z) − Ξ(z)| < ε` for `|z| ≤ R` and `N ≥ N(R, ε)`.

Then `F_N → Ξ` locally uniformly, and by Hurwitz's theorem the zeros of `F_N`
converge (with multiplicity) to the zeros of `Ξ`.

**Proof sketch.** (H-bound) gives a normal family (Montel).  Any subsequential
limit `G` satisfies conditions 1–4 by uniform convergence; (H-norm) forces `G ≠ 0`
and identifies `G = Ξ` uniquely (by (H-tail) + the identification-via-Taylor-jet
or Hadamard-product uniqueness).  Hurwitz then transfers real-zero location. ☐

---

## Part III — Application checklist

**For CCM truncations (`𝔇_{λ,N}`):**

| Condition | Status in CCM literature |
|---|---|
| (1) entire | PROVED (CCM det identity) |
| (2–3) even, real on ℝ | PROVED (symmetry of 𝔇) |
| (4) real-rootedness | PROVED (CCM Thm, real zeros = spectrum) |
| (5) first k_N zeros agree with ζ zeros | OPEN (numerical evidence; analytic proof missing) |
| (6) normalization at 0 | PARTIAL (λ^{−iz} phase is the obstacle) |
| (H-norm) F_N(z₀) → Ξ(z₀) | OPEN (the "suitably normalized" step) |
| (H-bound) local uniform bound M_R | OPEN (no tail envelope in CCM 2511.22755) |
| (H-tail) summable tail control | OPEN (the decisive missing estimate) |

**The theorem identifies (H-bound) and (H-tail) as the exact missing ingredients.**

**For Suzuki W(a, θ; z):**

The Suzuki target is `z² ξ/ξ'` (meromorphic).  The CCM entire-target theorem does
not apply directly.  The pole/residue version is needed (see limitations.md).

---

## Escape route

An `F_N` satisfying the full positive package (H-norm + H-bound + H-tail + H-modulus)
is NOT excluded by the negative theorem.  The escape condition is precisely the
addition of a proved tail envelope.  A bound of the form
```
Σ_{n > k_N} |r_{n,N}^{-2} − γ_n^{-2}| ≤ C(N) → 0   as  N → ∞
```
is sufficient; it converts the finite zero-agreement into a global one.

Methods that are NOT excluded:
1. Any proof supplying a certified `M_R` (e.g. via operator norm bounds on `𝔇_{λ,N}`).
2. Any proof of (H-tail) via spectral theory of `A_a` (Suzuki's `λ(a)` bounds).
3. Infinite-order methods (full Weil criterion, all Li tests, exact Hadamard product).
