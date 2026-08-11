# Problem OB-14 — E-pos (CCM entire target): is a uniform Nevanlinna bound necessary and sufficient for order transfer?

**Type:** complex analysis (Nevanlinna theory, normal families, order of entire functions)

**Non-circularity:** RH is not assumed; zero locations of ζ are not used as inputs. The
target `Ξ` below is treated only as a fixed even entire function of conventional order 1
with a prescribed (possibly complex, unconditional) zero divisor. No Euler product,
functional equation of ζ, or reality of the zeros is assumed. The question is a pure
statement about locally uniform limits of entire functions.

---

## All definitions (self-contained — everything is here)

### Conventional order (NOT exponential type)

For an entire function `f`, let `M_f(r) = max_{|z|=r} |f(z)|`. The **conventional order**
is
```
ρ(f) := limsup_{r→∞} [ log log M_f(r) / log r ].
```
The **Nevanlinna characteristic** is `T(r,f) = m(r,f) + N(r,f)` (with `N ≡ 0` for entire
`f`, `m(r,f) = (1/2π)∫_0^{2π} log⁺|f(re^{iθ})| dθ`); for entire `f`,
`T(r,f) ≤ log⁺ M_f(r) ≤ 3 T(2r, f)` (standard). "Conventional order ≤ 1" is
`ρ(f) ≤ 1`, equivalently `log M_f(r) = O(r^{1+ε})` for every `ε > 0`.

**Warning (this is a documented past error).** "Order ≤ 1" is NOT the same as "finite
exponential type" `|f(z)| = O(e^{C|z|})`. The latter is strictly stronger. The Riemann
`Ξ` has conventional order 1 but is NOT of finite exponential type
(`log|Ξ(iy)| ∼ (y/2)log(y/2)`). This problem uses conventional order throughout.

### The target Ξ

`Ξ` is a fixed entire function with:
- `Ξ` even: `Ξ(−z) = Ξ(z)`;
- conventional order `ρ(Ξ) = 1`;
- `Ξ(0) ≠ 0`;
- complete zero divisor `{±ω_n : n ≥ 1}`, `ω_n ∈ ℂ` (NOT assumed real),
  `Σ |ω_n|^{-2} < ∞`, so `Ξ(z) = Ξ(0) ∏_{n≥1}(1 − z²/ω_n²)` (locally uniformly
  convergent, genus-1 paired product — no exponential factor).

### The sequence and the hypotheses under scrutiny

Let `(F_N)_{N≥1}` be entire functions. Consider:

- **(E-even)** each `F_N` even;
- **(H-norm)** `F_N(z_0) → Ξ(z_0)` at a fixed `z_0` with `Ξ(z_0) ≠ 0`;
- **(H-bound)** for every `R > 0` there is `M_R` (independent of N) with
  `sup_{|z| ≤ R} |F_N(z)| ≤ M_R` for all N (local uniform boundedness);
- **(H-tail)** the zeros of `F_N` converge to those of `Ξ` with the tail no-intrusion
  condition: for every `R > 0` there are `M, N_0` such that for `N ≥ N_0`, every zero of
  `F_N` in `{|z| ≤ R}` is one of the finitely many that converge to a zero of `Ξ` in that
  disk (no wandering zero enters);
- **(H-order)** there are constants `C, C_0, r_0` **independent of N** with
  `T(r, F_N) ≤ C·r + C_0` for all N and all `r ≥ r_0`.

---

## The claims to be verified

### Claim A: (H-bound) alone does NOT force the limit to have order ≤ 1

**Claim A.** There is a sequence `(F_N)` satisfying (E-even), (H-norm), (H-bound),
(H-tail) whose locally uniform limit `G` exists, has the same complete zero divisor as
`Ξ`, satisfies `G(z_0) = Ξ(z_0)`, but `G ≠ Ξ` and `ρ(G) = 2`.

**Witness (to be verified).** The constant sequence
```
F_N(z) := Ξ(z) · exp(z² − z_0²)   for all N.
```
Verify:
1. Each `F_N` is even (product of even `Ξ` and even `exp(z²−z_0²)`).
2. `F_N(z_0) = Ξ(z_0)·e^0 = Ξ(z_0)` — (H-norm) holds trivially (constant sequence).
3. (H-bound): on `|z| ≤ R`, `|F_N(z)| ≤ M_R(Ξ)·e^{R²}` uniformly in N.
4. (H-tail): `exp(z²−z_0²)` is zero-free, so `F_N` has exactly the zeros of `Ξ`, for
   every N — tail no-intrusion is immediate.
5. The limit `G = Ξ·e^{z²−z_0²}` has the same zero divisor as `Ξ`, `G(z_0)=Ξ(z_0)`,
   but `G ≠ Ξ` (they differ by `e^{z²−z_0²} ≢ 1`).
6. `ρ(G) = 2`: since `Ξ` has order 1 and `e^{z²}` has order 2, the product has order 2.
   (Verify: `log M_G(r) ≥ r² − O(r log r)`, so `ρ(G) = 2`.)

Hence (H-bound) + divisor + normalization are insufficient to identify `G = Ξ`. This is
the growth-transfer gap (the entire-target analogue of the OB-11 finding for the
meromorphic target).

### Claim B: (H-order) IS sufficient (with the other hypotheses) to force G = Ξ

**Claim B.** Under (E-even), (H-norm), (H-tail), and (H-order): every locally uniform
subsequential limit `G` of `(F_N)` equals `Ξ`.

**Proof skeleton to close:**
1. **(H-order) → normal family + order transfer.** (H-order) gives local uniform
   boundedness (via `T(r,F_N) ≤ Cr+C_0` and the standard `log⁺M_f(r) ≤ 3T(2r,f)`), so
   Montel yields a subsequence `F_{N_j} → G` locally uniformly, `G` entire. Moreover the
   Nevanlinna characteristic is lower-semicontinuous under locally uniform convergence:
   `T(r,G) ≤ liminf_j T(r,F_{N_j}) ≤ Cr + C_0`, so `ρ(G) ≤ 1`.
2. **Divisor of G.** (H-tail) + Hurwitz ⟹ `G` has the complete zero divisor `{±ω_n}` of
   `Ξ` (tail no-intrusion excludes spurious zeros).
3. **Ratio is a unit of order ≤ 1.** `H := G/Ξ` is entire (same zeros cancel) and
   zero-free; `T(r,H) ≤ T(r,G) + T(r,1/Ξ) + O(1) = O(r)`, so `ρ(H) ≤ 1`. By Hadamard,
   `H = e^{az+b}`.
4. **Parity + normalization.** `G` even (limit of even functions) and `Ξ` even ⟹ `H`
   even ⟹ `a = 0`. `H(z_0) = G(z_0)/Ξ(z_0) = 1` ⟹ `e^b = 1`. Hence `H ≡ 1`, `G = Ξ`.

**What to close for Claim B:**
(a) Confirm the lower-semicontinuity `T(r,G) ≤ liminf T(r,F_{N_j})` under locally uniform
    convergence (cite by theorem number — e.g. via the Ahlfors–Shimizu characteristic, or
    the argument that `m(r,·)` is l.s.c. under uniform convergence on `|z|=r`).
(b) Confirm step 3's `T(r,1/Ξ) = T(r,Ξ) + O(1)` (first main theorem) and the resulting
    `ρ(H) ≤ 1`.
(c) Confirm the Hadamard step for a zero-free entire function of order ≤ 1 gives exactly
    `e^{az+b}` (linear exponent), citing the theorem number.

### Claim C: is (H-order) also NECESSARY, or can a weaker per-N bound suffice?

**Claim C.** Determine whether a **per-N** order bound — "each `F_N` has `ρ(F_N) ≤ 1`,
i.e. `T(r,F_N) = O(r)` with a constant that may depend on N" — together with (E-even),
(H-norm), (H-bound), (H-tail), suffices to force `G = Ξ`.

**What to verify for Claim C:**
Either (i) prove that the per-N bound suffices (unlikely — give the argument), or
(ii) exhibit a counterexample: a sequence where each `F_N` has order ≤ 1 (n-dependent
constant), all other hypotheses hold, but `G` has order 2 (or `G ≠ Ξ`). A candidate:
`F_N(z) = Ξ(z)·exp((z²−z_0²)·φ(N))` where `φ(N) → 1` slowly while each `F_N` still has
order... — note this has order 2 for each N, so it does NOT witness a per-N *order-≤1*
family. The real question: can a family with `ρ(F_N) ≤ 1` for each N (n-dependent
constant) converge to an order-2 limit? Decide this. (Hint: relate to whether
`sup_N T(r,F_N)/r < ∞` can fail while each `T(r,F_N)/r` is individually bounded.)

---

## Acceptance criteria

1. **CONFIRMED:** Claim A witness verified (all 6 points); Claim B proof closed with
   theorem-number citations for (a)–(c); Claim C decided (per-N bound suffices, or a
   counterexample given). Conclusion: state precisely whether (H-order) is
   **necessary and sufficient**, sufficient-but-not-necessary, etc.

2. **PARTIAL:** Claim A confirmed and Claim B closed, but Claim C left with a precise
   remaining sub-question.

3. **REFUTED:** if Claim B's skeleton has a gap (e.g. l.s.c. of `T` fails as stated),
   give the counterexample and the minimal repair.

4. **INCONCLUSIVE + localization:** if some step cannot be decided from the stated
   hypotheses, name the missing ingredient.

An honest "(H-order) is sufficient; necessity holds in the following precise sense and
fails in this other sense" is a valid, first-class outcome.

---

## Numerical anchor (sanity only — not an input)

For the Claim A witness with a surrogate `Ξ_surr(z) = cos(z)` (even, order 1, real zeros
`±(k+1/2)π` — used ONLY to sanity-check the growth arithmetic, not as the real Ξ):
`H(z) = exp(z² − z_0²)`, `z_0 = 0.7`. Then `H(z_0) = 1`; `H(1.3) = e^{1.69−0.49} =
e^{1.2} ≈ 3.320`; `H(2.0) = e^{4−0.49} = e^{3.51} ≈ 33.45`. Conventional order of `H`:
`log M_H(r) = r²`, so `log log M_H(r)/log r = log(r²)/log r = 2` for all `r > 1` — order
exactly 2. (Verified by script: the ratio is 2.0000 at `r = 10, …, 10^{10}`.) This
confirms the witness has order 2 while being locally uniformly bounded and sharing the
divisor of the order-1 target — the L14 growth-transfer gap.
