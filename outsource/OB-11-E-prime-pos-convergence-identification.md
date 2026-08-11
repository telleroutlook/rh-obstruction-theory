# Problem OB-11 — E'-pos: convergence and identification for the odd meromorphic target

**Type:** complex analysis (normal families, Montel's theorem, meromorphic
identification of a locally uniform limit)

**Non-circularity:** RH is not assumed and zero locations of ζ are not used as
inputs. The sequence {γ_n} below is an abstract sequence of positive reals with a
growth condition. No Euler product, functional equation of ζ, or spectral property
of ζ is assumed. The question is a pure convergence/identification statement about
sequences of odd meromorphic functions.

---

## All definitions (self-contained — everything is here)

### The abstract target W

Fix data as follows (this is the corrected structure established in prior review
OB-06/OB-09, restated here in full so nothing external is needed):

- A: an even entire function, Nevanlinna characteristic `T(r,A) = O(r)`, with simple
  zeros exactly at `{±γ_n : n ≥ 1}`, `0 < γ_1 < γ_2 < …`, `γ_n → ∞`, `Σ γ_n^{-2} < ∞`,
  and `A(0) ≠ 0`. Concretely `A(z) = A(0) ∏_{n≥1}(1 − z²/γ_n²)`.
- B: an odd entire function, `T(r,B) = O(r)`, all zeros simple, with
  `Z(B) ∩ ℝ = {0}` (so 0 is a simple zero of B and no other zero of B is real; write
  `B(z) = z·B̃(z)`, B̃ even, B̃(0) ≠ 0).

Define the **odd meromorphic target**
```
W(z) = z² A(z) / B(z).
```
Facts (provable from the above, may be used freely):
- W is odd: `W(−z) = −W(z)`.
- W has simple zeros exactly at `{±γ_n}` (since `B(±γ_n) ≠ 0`, by `Z(B)∩ℝ={0}`) and
  a simple zero at 0.
- W has poles exactly at `Z(B) \ {0}` (all off the real axis), with the pole set
  `𝒫 := Z(B)\{0}` closed and discrete.
- Set `Ω := ℂ \ 𝒫`. W is holomorphic on Ω.

### Nevanlinna order convention (to avoid the earlier "exponential type" error)

"Nevanlinna order ≤ 1" for a meromorphic function F means `T(r,F) = O(r)`, where
`T(r,F) = m(r,F) + N(r,F)` is the Nevanlinna characteristic. This is NOT the same as
"finite exponential type" `|F(z)| = O(e^{C|z|})`; the latter is strictly stronger and
is NOT assumed anywhere.

### The method sequence and its hypotheses

Let `(F_n)_{n≥1}` be a sequence of odd meromorphic functions. Assume:

- **(P) Parity.** Each `F_n` is odd: `F_n(−z) = −F_n(z)`.

- **(LB) Local boundedness on Ω.** For every compact `L ⊂ Ω`, there exist an open set
  `U_L` and constants `n_L, M_L` with
  ```
  L ⊂ U_L ⊂ Ω,   U_L relatively compact in Ω,
  ```
  such that for all `n ≥ n_L`, `F_n` is holomorphic on `U_L` and
  `sup_{z ∈ U_L} |F_n(z)| ≤ M_L`.
  (In particular, for large n the poles of `F_n` stay outside `U_L`.)

- **(ZT) Zero-divisor convergence with tail no-intrusion.** The zeros of `F_n` in Ω
  converge to those of W in the following precise sense:
  1. (finite match) for each fixed k, `F_n` has, for all large n, exactly one simple
     zero `z_{n,k} → γ_k` and one at `−z_{n,k} → −γ_k`, and a simple zero at 0;
  2. (tail no-intrusion) for every `R > 0` there exist `K, n_0` such that for all
     `n ≥ n_0`, every zero `ζ` of `F_n` with `|ζ| ≤ R` is one of `{0, ±z_{n,1}, …,
     ±z_{n,K}}` (i.e. no extra or "wandering" zero enters the disk `|z| ≤ R`).

- **(PL) Pole-set stability.** For every compact `L ⊂ Ω` there is `n_L` such that for
  all `n ≥ n_L`, `F_n` has no poles in `L`, and on any compact `K ⊂ Ω` the poles of
  `F_n` that lie in a fixed neighborhood of `𝒫 ∩ K` converge to `𝒫 ∩ K` with matching
  multiplicity (each pole of W in K is the limit of exactly the poles of `F_n`, counted
  with multiplicity; no pole of `F_n` accumulates at a non-pole of W in Ω).

- **(N) Normalization.** There is a base point `w₀ ∈ Ω`, `w₀ ≠ 0`, `w₀` not a zero of
  W, with `F_n(w₀) → W(w₀)` and `W(w₀) ≠ 0`.

### The uniqueness lemma (already established — may be used as a black box)

**Lemma E'.1 (meromorphic Hadamard uniqueness; proved in prior review OB-06, restated).**
Let `F, G` be meromorphic with `T(r,F)=O(r)`, `T(r,G)=O(r)`, identical complete zero
divisors (`ord_a F = ord_a G` for every `a ∈ ℂ`, poles counted as negative order),
`F/G` even, and `F(w₀) = G(w₀) ≠ 0` for some non-pole `w₀`. Then `F ≡ G`.
(Proof: H = F/G is a zero-free entire function of Nevanlinna order ≤ 1, hence
`H = e^{az+b}`; evenness forces a = 0; normalization forces `e^b = 1`.) ∎

---

## The theorem / claim to be verified

**Theorem E'-pos (claim).** Under (P), (LB), (ZT), (PL), (N), there is a subsequence
`(F_{n_j})` and a function `G` meromorphic on Ω such that `F_{n_j} → G` locally
uniformly on Ω, and moreover `G` extends to a meromorphic function on ℂ equal to W:
```
F_{n_j} → W   locally uniformly on Ω.
```
If in addition the full sequence's every subsequence has a further subsequence with
the same limit W, then `F_n → W` locally uniformly on Ω (no subsequence needed).

---

## Proof skeleton to be closed

### Step 1 — Montel on Ω (normal family, no Marty)

Using (LB): for each compact `L ⊂ Ω`, the tail `{F_n : n ≥ n_L}` is a family of
holomorphic functions on the open neighborhood `U_L`, uniformly bounded there. By
Montel's theorem for holomorphic functions (locally uniformly bounded ⟹ normal), some
subsequence converges uniformly on compacts of `U_L`, hence on `L`.

**What to close for Step 1:** Confirm that Montel's theorem for **holomorphic** functions
suffices on Ω — i.e., that Marty's spherical-derivative criterion is NOT needed here
because (LB) supplies holomorphy + uniform boundedness on an open neighborhood of each
compact of Ω. Cite Montel by theorem number in a standard reference.

### Step 2 — A single global subsequence via diagonalization

Take an exhaustion `L_1 ⊂ L_2 ⊂ …` of Ω by compacts with `⋃ L_j = Ω` and each
`L_j ⊂ int(L_{j+1})` (possible since Ω is open; e.g.
`L_j = {|z| ≤ j, dist(z, 𝒫) ≥ 1/j}`, using 𝒫 closed discrete). Apply Step 1 on each
`L_j`, extract nested subsequences, and diagonalize to obtain a single subsequence
`(F_{n_j})` converging locally uniformly on all of Ω to a holomorphic `G` on Ω.

**What to close for Step 2:** Confirm each `L_j` above is compact in Ω (uses 𝒫 closed
discrete), that `⋃ L_j = Ω`, and that the diagonal subsequence converges locally
uniformly on every compact of Ω (each compact lies in some `L_j`).

### Step 3 — Identify the zeros and poles of the limit G

- **Zeros:** By Hurwitz's theorem applied on Ω, together with (ZT)'s tail no-intrusion,
  the zeros of G in Ω are exactly `{0, ±γ_n}` with the correct (simple) multiplicity,
  and no others. (Tail no-intrusion is what prevents G from acquiring a spurious zero
  as a limit of wandering zeros.)
- **Poles:** G is a priori holomorphic on Ω (a locally uniform limit of functions
  holomorphic on neighborhoods of each compact of Ω is holomorphic on Ω). To recover W's
  poles, consider the reciprocals `1/F_{n_j}` near each pole `p ∈ 𝒫`: apply (PL) and
  Hurwitz to `1/F_{n_j}` to show `G` extends meromorphically across `p` with a pole of
  the same order as W.

**What to close for Step 3:**
(a) State the exact form of Hurwitz's theorem used (zeros of a locally uniform limit),
    with a theorem-number citation.
(b) Show tail no-intrusion (ZT.2) rules out extra zeros of G in every disk `|z| ≤ R`.
(c) Justify the meromorphic extension of G across each `p ∈ 𝒫` via the reciprocal
    `1/F_{n_j}` and (PL) (or give an alternative rigorous argument). The result should
    be: G, extended, is meromorphic on ℂ with the complete zero/pole divisor of W.

### Step 4 — Identify G = W and pass to the full sequence

- G (extended) is odd (locally uniform limit of odd functions is odd).
- G has `T(r,G) = O(r)`: justify that the extended limit inherits Nevanlinna order ≤ 1
  (e.g. from the divisor being that of W plus the normalization; or via a growth
  argument). **This is a step to verify, not assume.**
- G and W have identical complete zero/pole divisors (Step 3), G/W is even (both odd),
  and `G(w₀) = lim F_{n_j}(w₀) = W(w₀) ≠ 0` by (N). By Lemma E'.1, `G ≡ W`.
- If every subsequence of `(F_n)` has a further subsequence converging to W, then the
  full sequence converges to W locally uniformly on Ω (standard subsequence principle).

**What to close for Step 4:** (a) Justify `T(r,G) = O(r)` for the extended limit
rigorously (this is the only nontrivial growth step). (b) Confirm the subsequence
principle gives full-sequence convergence.

---

## Acceptance criteria

1. **CONFIRMED:** all four steps are rigorous; Montel (Step 1) and Hurwitz (Step 3)
   cited by theorem number; the growth step (Step 4a) is justified; `G ≡ W` follows.

2. **PARTIAL:** the convergence (Steps 1–2) and zero identification (Step 3a–b) are
   confirmed, but the pole extension (Step 3c) or the growth step (Step 4a) has a gap;
   describe the gap and the minimal extra hypothesis that closes it.

3. **REFUTED:** one of the steps fails as stated; give an explicit counterexample
   (e.g. a sequence satisfying (P),(LB),(ZT),(PL),(N) whose limit is not W), and state
   the minimal additional hypothesis needed to repair it.

4. **INCONCLUSIVE + partial localization:** if the argument cannot be decided from the
   stated hypotheses, state precisely which hypothesis is too weak and what must be
   added (e.g. a uniform-order bound `T(r,F_n) ≤ Cr` with C independent of n).

An honest "the hypotheses as written are insufficient for Step 4a, and here is the
minimal uniform-order hypothesis that fixes it" is a valid and useful result — do not
force a CONFIRMED/REFUTED dichotomy.

---

## Numerical anchor (sanity only — not an input)

A concrete odd meromorphic instance illustrating the setup (NOT the ζ case): take
`γ_n = n`, so `A(z) = ∏_{n≥1}(1 − z²/n²) = sin(πz)/(πz)`, and `B(z) = z·cos(2πz)`
(odd, `Z(B) ∩ ℝ = {0}` fails here because cos(2πz) has real zeros — so this B is only
a shape illustration, NOT a valid instance).

A valid toy instance: `A(z) = sin(πz)/(πz)` (even, entire, simple zeros at `{±n : n≥1}`,
A(0)=1≠0), `B(z) = z·cosh(z)` (odd; cosh(z) has zeros only at `±(k+1/2)πi`, all off ℝ,
and cosh(0)=1≠0, so `Z(B)∩ℝ = {0}` as required). Then
```
W(z) = z²·[sin(πz)/(πz)] / [z·cosh z] = sin(πz)/(π cosh z),
```
which is odd, with simple zeros at `{±n : n ≥ 1} ∪ {0}` and poles at
`±(k+1/2)πi ∈ Ω`. Sanity: `W(1/2) = sin(π/2)/(π cosh(1/2)) = 1/(π·1.1276…) ≈ 0.2823`,
finite and nonzero at `w₀ = 1/2`. This is only a sanity illustration of the definitions;
it is not an input to any step.
