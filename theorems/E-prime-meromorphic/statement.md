# Statement — Theorem E' (E-prime-meromorphic)

**Theorem ID:** E-prime-meromorphic  
**Program ref:** EXT-3 (extension of Theorem E to Suzuki meromorphic target)  
**Status:** PROOF-DRAFT — **Gate-A BLOCKED (OB-30, 2026-08-12)** for the Suzuki-target
claim. Three independent errors (see §0): (i) the E'-neg separation degree `z^{2J+3}` is
**wrong** (a `J=1` counterexample gives leading `z³`); (ii) assumption (A2) `Z(B)∩ℝ={0}` is
**false** for the actual `B=iA'=iξ'(1/2−iz)` (Rolle between real `A`-zeros forces real
`B`-zeros); (iii) Suzuki's `W(a,θ;z)` is **entire** (Thm 1.5), incompatible with the
moving-pole (PL⁺) approximation. Survives only as an **abstract odd-meromorphic lemma** with
a corrected "some nonzero Taylor coefficient" separation (not a fixed degree). See §0.

---

## §0. Reframing after OB-30 (Gate-A BLOCKED) — READ FIRST

The submitted E' claimed a Suzuki-target (`W=z²ξ/ξ'`) non-identifiability + sufficiency
pair. OB-30 **BLOCKED** it. Three genuine errors, each fatal on its own:

- **(1) E'-neg separation degree is wrong.** Matching the `J`-jet at `w₀ = iτ ≠ 0` makes
  `L(t) = O((t−t₀)^J)` at `t₀ = w₀²`; it does **NOT** force the first `J` log-power-sums
  `Δ_1,…,Δ_J` at `t=0` to vanish. So the leading discrepancy of `F^{(c)}−W` at the origin is
  generically `z³` (odd, `=z^{2·1+1}` for `J=1`), **not** `z^{2J+3}`. Explicit counterexample
  (OB-30 §2.2): `A(z)=sin πz/(πz)=∏(1−z²/n²)`, `B(z)=sinh z`, `w₀=i`, `k=J=1` satisfy
  (A1)–(A3), yet `F^{(c)}(z)−W(z) = −Δ₁(c)z³+O(z⁵)` with `Δ₁'(0) = Σ_{n≥3}
  (n²−4)/(2n²(n²+1)(n−1)) > 0`. The `z^{2J+3}` Cauchy bound is therefore unproven; the honest
  statement is only "**some** nonzero Taylor coefficient of order ≥ 3 exists", giving a
  Cauchy bound at that (unspecified) degree.
- **(2) (A2) is false for the actual target.** `A(z)=ξ(1/2−iz)` gives `B(z)=ξ'(1/2−iz)=iA'(z)`.
  By Hardy there are infinitely many real zeros of `A`; Rolle gives a real zero of `A'`, hence
  of `B`, between consecutive ones — so `Z(B)∩ℝ ≠ {0}`. Thus (A1)–(A3) **cannot** hold for the
  real `ξ/ξ'`; they describe an *abstract* pair of independent functions only. And (A1)'s "all
  `A`-zeros simple and real" for the actual `A` **is** RH + simplicity.
- **(3) Suzuki approximants are entire; moving poles are incompatible.** Suzuki Thm 1.5:
  `W(a,θ;z)` is **entire**; `e^{φ(a,z)}W(a,θ;z)` stays entire for holomorphic finite `φ`. A
  sequence of entire functions cannot converge locally uniformly, on compacts encircling a
  target pole, to the meromorphic `W` (contour integral `∮(z−p)^{m−1}·entire = 0` passes to
  the limit, contradicting a pole). So (PL⁺) is **not** a "still-open Suzuki property" — it is
  *incompatible* with Suzuki's entire family under the stated normalization.

**Withdrawn:** the Suzuki-target E'-neg/E'-pos claims; the `z^{2J+3}` degree; the "(LB)/(ZT_ℂ)/
(PL⁺)/(UG) are OPEN Suzuki ingredients" framing (PL⁺ is incompatible, not open). Also: the
Suzuki citation is **Corollary 1.6**, not "Cor 6".

**What survives (as an abstract lemma, PARTIAL):** over an abstract odd meromorphic target
`W = z²A/B` with `A,B` *independent* order-≤1 functions satisfying (A1)–(A3) as **abstract
hypotheses** (not the real `ξ/ξ'`), the `w₀`-jet IFT / Cauchy–Vandermonde Jacobian gives a
record-respecting `F^{(c)}≠W` (Link A/B core, CONFIRMED given the abstract hypotheses), with a
**nonzero-Taylor-coefficient** separation (degree not fixed). The meromorphic uniqueness Lemma
E'.1 is correct. Neither specializes to the real Suzuki target. Do not read this as a Suzuki
companion.

---

## §1. Context

Theorem E (E-compactness) proves a non-uniqueness result (E-neg) and a sufficient
conditions theorem (E-pos) for the **CCM normalization**: the entire function
`Ξ(z) = ξ(1/2 + iz)`.

The **Suzuki normalization** targets a different object: the meromorphic function
```
W(z) = z² ξ(1/2 − iz) / ξ'(1/2 − iz).
```

**Parity correction (OB-06 referee, 2026-08-11).** W is ODD, not even.
Proof: ξ satisfies `ξ(s) = ξ(1−s)`, so `X(z) := ξ(1/2−iz)` is even in z.
Differentiating the functional equation gives `ξ'(s) = −ξ'(1−s)`, so
`ξ'(1/2−iz)` is ODD in z.  Therefore `X(z)/X'(z) = ξ(1/2−iz)/ξ'(1/2−iz)`
is odd, and `W(z) = z² · (odd) = odd`.  In particular `W(−z) = −W(z)`.

**Zero/pole structure of W (OB-06 referee, 2026-08-11).**
- The zeros of ξ at `s = 1/2 − iγ` (of multiplicity m) become **simple zeros** of
  W at `z = γ`, regardless of m.  Near `z = γ`:
  `W(z) = −iγ²/m · (z−γ) + O((z−γ)²)`.
  There is no residue at γ; γ is a zero of W, not a pole.
- The **poles** of W come from zeros of `ξ'(1/2−iz)` that are not cancelled by zeros
  of `ξ(1/2−iz)`.  At `z = 0`: `ξ'(1/2) = 0` (functional equation), and the local
  behavior at 0 depends on the vanishing order of ξ' there.
- The earlier statement that "poles of W are at `γ_n`" was INCORRECT.

**Consequence for method class.** The E'-neg non-uniqueness construction and E'-pos
identification steps must be redesigned for the correct target function W (odd,
zeros at γ_n, poles at zeros of ξ').  The current E'-pos identification step
(which attempts to show even F_N → even W) is REFUTED: even F_N cannot converge
to the odd function W (OB-06).

Suzuki Cor. 1.6 (baseline, INDEPENDENTLY-CHECKED): RH follows if
`e^{φ(a,z)} W(a,θ;z) → z²ξ(1/2−iz)/ξ'(1/2−iz)` uniformly on compacts.
The target `z²ξ(1/2−iz)/ξ'(1/2−iz)` is meromorphic with the correct zero/pole
structure as above.

This theorem audits whether the E-neg non-uniqueness obstruction transfers to the
meromorphic target W.

---

## §2. Method class and observation

**Method class 𝔐_Suz.** A method `P ∈ 𝔐_Suz` constructs a sequence of meromorphic
functions `(F_n)` satisfying finite evidence `ℰ_N^{mer}`:
- meromorphic of **(conventional/Nevanlinna) order ≤ 1** — i.e. for every `ε>0`,
  `T(r,F) ≤ C_ε r^{1+ε} + C_{0,ε}`. **NOT** the linear/finite-type bound `T(r,F)=O(r)`:
  the target `W = z²ξ/ξ'` has poles at the zeros of `ξ'(1/2−iz)`, whose counting density is
  `~(r/2π)log r`, so `N(r,∞) ≍ (1/2π) r log r` and hence `T(r,W) ≍ r log r` — order 1 but
  **maximal type**, exactly as `Ξ` has order 1 but infinite exponential type. A linear
  `O(r)` characteristic would exclude `W` itself and make the class vacuous
  (L1/L14 discipline; the analogue of OB-14's E fix, re-scanned into E' by OB-30);
- poles at the zeros of `ξ'(1/2−iz)` (not at γ_n — see §1 parity correction);
- **ODD**: `F_n(−z) = −F_n(z)` (matching W's true parity);
- normalization condition matching `W` at one non-pole, non-zero base point `w₀`;
- first `J_N` Taylor coefficients at `w₀` matching `W`.

**Target predicate.** `(F_n) → W` locally uniformly on `ℂ \ {poles of W}`.

**Status note.** The earlier §2 stated F_n should be even; this was WRONG (OB-06).
The method class must use ODD functions to match W's parity.  A sequence of even
functions cannot converge locally uniformly to W.

---

## §3. Meromorphic Hadamard uniqueness (the key lemma — CONFIRMED AFTER CORRECTION)

**Lemma E'.1 (meromorphic Hadamard uniqueness — corrected, OB-06).** Let `F`, `G` be
meromorphic functions of **conventional order ≤ 1** (for every `ε>0`,
`T(r,·) ≤ C_ε r^{1+ε}+C_{0,ε}`; this includes the maximal-type case `T ≍ r log r`, i.e. `W`),
with:
- identical complete zero divisors: `ord_a F = ord_a G` for every `a ∈ ℂ`;
- `F/G` is an even function (in particular, F and G both even suffices);
- `F(w₀) = G(w₀) ≠ 0` at some non-pole point `w₀`.

Then `F = G`.

*Proof (OB-06 referee §3).* The quotient `H := F/G` is an entire function (all
poles and zeros cancel) of **conventional order ≤ 1** (`T(r,H) ≤ T(r,F)+T(r,1/G)+O(1) ≤
2C_ε r^{1+ε}+O(1)`, First Main Theorem).  A zero-free entire function of order ≤ 1 is
`H(z) = e^{az+b}` (Hadamard, Conway XI.3.4: genus ≤ 1, no zeros ⟹ the product is empty and
the exponential polynomial has degree ≤ 1).  By evenness of H: `H(−z)/H(z) = e^{−2az} = 1`
for all z, hence `a = 0`.  The normalization `H(w₀) = 1` gives `e^b = 1`, so `H ≡ 1`. ☐

*Correct canonical product (OB-06 referee §3.3).* For paired symmetric zeros `±z_j`
with `Σ|z_j|^{-2} < ∞`, the correct convergent paired product is:
```
Z(z) = ∏_j (1 − z²/z_j²),
```
NOT `∏_j (1 − z²/z_j²) e^{z²/z_j²}` — the latter introduces a spurious exponential
factor `exp(z² Σ z_j^{-2})` of order 2.  The pairing identity `E_1(z/a)E_1(z/−a) =
(1−z/a)e^{z/a}·(1+z/a)e^{−z/a} = (1−z²/a²)` shows the exponential factors cancel.

*Status: CONFIRMED AFTER CORRECTION (OB-06 2026-08-11).*
The proof is valid via the H := F/G route.  The original proof using separate Weierstrass
products P, P', Q, Q' had an error in the canonical product formula; the H-ratio proof
avoids this.

**Consequence for E'.** The identification step in E'-pos requires:
the limit function G has the same COMPLETE zero divisor as W (not merely same pole
positions), is odd (matching W's parity, replacing "even" from the old statement),
and matches W at one point.  Then Lemma E'.1 (with "odd" replacing "even" — the
argument is identical: F/G even follows from both F, G odd) gives G = W.

---

## §4. Theorem E'-neg (non-uniqueness for meromorphic target, CONFIRMED AFTER CORRECTION)

**Status (OB-09 referee 2026-08-11).** The construction is CONFIRMED after correction.
The original power-sum matching system Φ_r was REFUTED (it controls the expansion at
z=0, not the Taylor jet at a nonzero base point w₀); the corrected construction uses
a **direct w₀-jet system** with an explicit rational Wronskian–Vandermonde Jacobian
(referee §7). See proof.md §3 for the full argument.

**Statement.** Fix k ≥ 1, J ≥ 1, and a base point `w₀ = iτ` (`τ ∈ ℝ\{0}`, `B(iτ) ≠ 0`).
Under method-class assumptions (A1)–(A3) (see proof.md §3), for all sufficiently small
`c < 0` there exists an odd meromorphic function `F^{(c)} ≠ W` satisfying all conditions
of `ℰ_N^{mer}`, with quantitative separation:
```
sup_{|z| = R} |F^{(c)}(z) − W(z)| ≥ |A(0)/B̃(0) · Δ_{J+1}(c)/(J+1)| · R^{2J+3}
```
for `0 < R < R_B := dist(0, Z(B)\{0})`, and `Δ_{J+1}(c) ≠ 0`.

**Key corrections (OB-09):**
1. Frozen first-k terms belong in the matching system (the power-sum system omitted them).
2. Tail perturbation denominator is `J+m`, not `m`.
3. Matching is at nonzero `w₀`, via jet functionals `Ψ_j(u,c) = ∂_t^j L(t₀;u,c)`,
   NOT via power sums.
4. Leading separation degree is `2J+3` (odd), consistent with F−W being odd — NOT `2J+2`.
5. Non-collision assumption `Z(B)∩ℝ={0}` (A2) is mandatory to prevent pole/zero
   cancellation.
6. The claim `|W(iR)|→∞` is FALSE in general and is not used; separation is via Cauchy
   estimate.

**Jacobian (OB-09 §7).** `det D_u Ψ(u⁰,0) = (−t₀)^J (∏_{j<J} j!) ∏_{p<q}(x_q−x_p) /
∏_ℓ(1−x_ℓ t₀)^J ≠ 0` — a rational Wronskian–Vandermonde determinant, nonzero by
distinctness of `x_ℓ = γ_{k+ℓ}^{-2}`.

**Status: PROOF-DRAFT ✓ CONFIRMED AFTER CORRECTION (OB-09 2026-08-11).**

---

## §5. Theorem E'-pos (sufficient conditions — CORRECTED, OB-11 2026-08-11)

**Status (OB-11 referee).** The E'-pos claim as originally stated (hypotheses (LB*),
(H'-pole-sep), (H'-tail), (H'-norm) ⟹ G = W) is **REFUTED**: those hypotheses are
insufficient. Two independent gaps, each with an explicit counterexample:

1. **Growth gap.** The complete zero/pole divisor plus one-point normalization only
   forces `G = W·H` for a zero-free even entire `H` with `H(w₀) = 1`; they do NOT force
   `H ≡ 1`. Counterexample: `F_n ≡ W·exp(z²−w₀²)` (constant sequence) satisfies (P),
   (LB), (ZT), (PL), (N) but converges to `W·e^{z²−w₀²} ≠ W`. Here `T(r,H) ≍ r²`, so
   the limit is NOT Nevanlinna order ≤ 1 — the order must be an independent hypothesis.

2. **Pole-cancellation gap.** The original (PL) (pole matching "on compact K ⊂ Ω") is
   vacuous at the target poles `p ∈ 𝒫 ⊄ Ω`, and (ZT) only controls zeros *in Ω*.
   Counterexample: a rational-multiplier family `F_n = W·H·Q_n` whose factors put a
   double zero at `±p` (killing W's simple pole there) while moving the pole to `±p_n`;
   it satisfies every stated hypothesis but its limit `W·H` has p removed from its polar
   divisor. This gap is independent of the growth gap (the rational multipliers `Q_n` are
   `O(1)`-degree, so they keep the same conventional order as `W`, `T(r,F_n) ≍ r log r`
   uniformly — well within any `r^{1+ε}` envelope).

**Corrected hypotheses (OB-11 §5).** Replace (H'-bound)/(H'-tail) etc. by:

- **(P) Parity.** Each `F_n` odd.
- **(LB) Local boundedness on Ω.** For every compact `L ⊂ Ω` there is an open `U_L`
  with `L ⊂ U_L ⋐ Ω` and `n_L, M_L` such that `F_n` is holomorphic and `|F_n| ≤ M_L`
  on `U_L` for `n ≥ n_L`. (Montel on Ω; Marty not needed.)
- **(ZT_ℂ) Full-plane tail no-intrusion.** For every `R > 0` there are `K, n₀` such that
  for `n ≥ n₀`, EVERY zero of `F_n` in `{|z| ≤ R}` — including any at points of `𝒫` —
  lies in `{0, ±z_{n,1}, …, ±z_{n,K}}`. (Strengthens (ZT.2) from "zeros in Ω" to
  "zeros in ℂ"; this closes the pole-cancellation gap.)
- **(PL⁺) Local pole matching without cancellation.** For each `p ∈ 𝒫` there is
  `ρ_p > 0` with `D̄(p,ρ_p)` free of other W-zeros/poles, such that for large n, `F_n`
  has exactly one simple pole `p_n → p` in the disk and **no zeros** there.
- **(N) Normalization** at a non-pole, non-zero `w₀` with `F_n(w₀) → W(w₀) ≠ 0`.
- **(UG) Uniform conventional-order bound.** For every `ε>0` there are constants
  `C_ε, C_{0,ε}, r_ε` **independent of n** with `T(r, F_n) ≤ C_ε r^{1+ε} + C_{0,ε}` for all
  n, `r ≥ r_ε`. (Closes the growth gap — a per-n bound with n-dependent constant does NOT
  transfer to the limit.) **The exponent must be `r^{1+ε}`, NOT linear `Cr+C₀`**: the target
  `W` has `T(r,W) ≍ r log r` (poles = zeros of `ξ'`, density `~(r/2π)log r`), so a uniform
  *linear* bound would exclude `W` itself and make the hypothesis vacuous — the meromorphic
  analogue of the L1/L14 finite-type error OB-14 fixed for the entire target `Ξ`.

**Corrected Theorem E'-pos.** Under (P), (LB), (ZT.1), (ZT_ℂ), (PL⁺), (N), (UG): there
is a subsequence `F_{n_j} → W` locally uniformly on Ω; if every subsequence has a
further subsequence converging to W, the full sequence does. (Full proof: OB-11 §6 —
Montel + diagonal extraction; zero identification via Hurwitz + (ZT_ℂ); genuine simple
pole at each `p` via a contour/residue argument on `1/F_{n_j}` using (PL⁺); order
transfer via Ahlfors–Shimizu characteristic + (UG); then Lemma E'.1 gives `G = W`.)

**Montel vs Marty (OB-11 §1.3, confirmed).** On Ω, (LB) gives holomorphy + local uniform
boundedness on an open neighborhood of each compact, so **Montel suffices** (Conway
VII.2.9); Marty's spherical-derivative criterion is not needed.

**Status:** the corrected theorem is PROOF-DRAFT (OB-11 §6 gives a line-by-line proof).
The Suzuki application still requires verifying (LB), (ZT_ℂ), (PL⁺), (UG) for the
specific Suzuki family — these are the concrete missing ingredients (§6).

---

## §6. Application to Suzuki framework

Suzuki Cor. 1.6 (baseline, INDEPENDENTLY-CHECKED): RH follows if
`e^{φ(a,z)} W(a,θ;z) → z²ξ(1/2−iz)/ξ'(1/2−iz)` uniformly on compacts.

The E'-neg result (once written out) will say: finite evidence alone (first `k_N` zeros of
W, normalization, first `J_N` Taylor coefficients) does not uniquely determine the locally
uniform limit.  The E'-pos conditions identify what extra structure is needed.

**Missing ingredients for Suzuki convergence:**
- (LB) not established for the Suzuki sequence `W(a,θ;z)`.
- (ZT_ℂ) full-plane tail no-intrusion not established.
- (PL⁺) local pole matching without cancellation not established.
- (UG) uniform Nevanlinna characteristic bound (constant independent of the truncation
  index) not established — the growth-control ingredient identified by OB-11.
- The correct parity structure (odd functions) must be verified for the Suzuki family.

These are the **precise missing ingredients** for the Suzuki track (OB-11-corrected list).

---

## §7. Status summary

| Component | Status |
|---|---|
| Meromorphic Hadamard uniqueness (Lemma E'.1) | CONFIRMED AFTER CORRECTION (OB-06 2026-08-11; F/G ratio route; correct paired product) |
| W parity | CORRECTION: W is ODD, not even (OB-06 2026-08-11) |
| W zero/pole structure | CORRECTION: γ_n are ZEROS of W (not poles); poles come from zeros of ξ' (OB-06 2026-08-11) |
| E'-neg construction (§4) | PROOF-DRAFT ✓ CONFIRMED AFTER CORRECTION (OB-09 2026-08-11; direct w₀-jet system, Wronskian–Vandermonde Jacobian) |
| Old E'-neg (perturbing "poles at γ_n") | REFUTED (γ_n are zeros, not poles of W) |
| E'-neg power-sum system Φ_r | REFUTED (OB-09): controls z=0 expansion, not w₀-jet |
| E'-neg separation degree | CORRECTED to z^{2J+3} (odd), not z^{2J+2} (OB-09 §5.1) |
| Old E'-pos identification ("even F_N → even W") | REFUTED (W is odd; even functions cannot converge to W) |
| E'-pos as first stated ((LB*)+(H'-pole-sep)+(H'-tail)+(H'-norm) ⟹ G=W) | REFUTED (OB-11 2026-08-11): two counterexamples — growth gap (F_n=W·e^{z²−w₀²}) and pole-cancellation gap |
| E'-pos CORRECTED (§5: adds (ZT_ℂ), (PL⁺), (UG)) | PROOF-DRAFT ✓ (OB-11 §6 line-by-line proof; Montel not Marty) |
| E'-pos growth control (UG) | REQUIRED: per-n order bound with n-dependent constant does NOT transfer to limit (OB-11 §2) |
| E'-pos pole non-cancellation (ZT_ℂ + PL⁺) | REQUIRED: old (PL)/(ZT) allow a zero to cancel a target pole (OB-11 §4) |
| Suzuki missing ingredients | OPEN: (LB), (ZT_ℂ), (PL⁺), (UG), odd parity — for the Suzuki family |
| Connection to Theorem E (same template) | ✓ explicit (corrected: zeros not poles) |
