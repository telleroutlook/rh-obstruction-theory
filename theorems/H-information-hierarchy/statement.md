# Statement — Theorem H (H-information-hierarchy)

**Theorem ID:** H-information-hierarchy  
**Program ref:** EXT-2a (unification of B1, B2, G under a common information-obstruction framework)  
**Status:** PROOF-DRAFT (OB-27 self-audit 2026-08-11: the observation structure is a
PARTIAL order — `O_finite` and `O_theta` are incomparable — NOT the earlier strict linear
chain; inherited B2/G obstructions are Gate-A established, H's own partial-order/H′ increment
is PROOF-DRAFT)

---

## §1. Abstract framework

**Definition (observation map).** An *observation map* is a function
`O : 𝔛_sym → S` where `𝔛_sym` is the class of admissible zero multisets (symmetric
under conjugation and `ρ↦1−ρ`) and `S` is a set of observable records.

**Definition (information obstruction).** A method `P` operates via observation `O`
if its input is only `O(𝒵)` (not `𝒵` itself). An *information obstruction* for `(P, O)`
is a pair `(𝒵₊, 𝒵₋) ∈ 𝔛_sym²` such that:
1. `O(𝒵₊) = O(𝒵₋)` (observation collision — exact);
2. `T(𝒵₊) ≠ T(𝒵₋)` (the target predicate distinguishes them);
3. Neither `𝒵₊` nor `𝒵₋` involves an RH-equivalent hypothesis.

---

## §2. The observation lattice

Four natural observation maps, **partially** ordered by information content (refinement):

Four natural observation maps. They are **NOT a single total chain** — `O_finite` and
`O_theta` are *incomparable* (each sees coordinates the other cannot; see the correction
note below and proof.md §4). The correct structure is a **partial order** in which both are
coarsenings of `O_oracle`:

```
        O_oracle          (all zero ordinates γ_n — finest)
        /   |   \
   O_vM   O_theta   … 
     |       
   O_finite            with  O_finite ⋈ O_theta  (incomparable)
```

i.e. `O_finite ≼ O_oracle`, `O_theta ≼ O_oracle`, `O_vM ≼ O_oracle`, and `O_theta ≼ O_vM`
(von Mangoldt data determines the archimedean/smooth count), but **`O_finite` and `O_theta`
are incomparable** — neither refines the other.

| Layer | What it computes | Sees Re ρ (off-line)? | Sees Im-count / S(T)? | Used in |
|---|---|---|---|---|
| `O_finite` | finite set {Li_k : k≤K} or {W(φ_j) : j≤K} | **Yes** (via 1/ρ) | No | Theorems B1, B2 |
| `O_theta` | archimedean levels {d_n = θ_level(n) : n≤N} | **No** | No (fixed zero-free levels) | Theorem G |
| `O_vM` | full von Mangoldt explicit formula data (Λ(n) for all n) | Yes | Partially (via explicit formula) | — |
| `O_oracle` | all zero ordinates {γ_n} | Yes | Yes, by definition | trivially resolves |

**Correction note (OB-27 self-audit, 2026-08-11 — supersedes the earlier "total chain"
claim).** An earlier draft wrote `O_finite ⊂ O_theta ⊂ O_vM ⊂ O_oracle` as a strict total
chain. That is **false**: `O_finite` and `O_theta` are incomparable. Two ways to see it,
both script-verified:
- `O_theta` in the sense of Theorem G is the **fixed, zero-free** sequence `d_n = θ_level(n)`
  (Riemann–Siegel θ; independent of the zero multiset 𝒵), so as a map on multisets it is
  *constant* — it separates **no** pair, hence cannot dominate `O_finite`.
- Even reading `O_theta` charitably as an Im-part/unfolded-count functional of 𝒵, it is
  blind to real parts: a same-imaginary-multiset pair (e.g. the quartet at `σ=3/4` vs
  `σ=9/10`, both with Im-multiset `{±T,±T}`) has identical `O_theta` image but **different**
  `O_finite` (Li₁ = Σ1/ρ separates: `0.019913…` vs `0.019855…`). Conversely an S(T)-type
  perturbation moves ordinates (changing `O_finite`) while preserving the θ-levels. So
  neither map refines the other. H's genuine content is therefore the **two separate
  obstructions** (O_finite via B2, O_theta via G) placed in a partial order under
  `O_oracle`, **not** a strict linear hierarchy.

**Convention note (OB-23, cross-theorem).** H uses the `O_finite` layer only through the
*structural* B1/B2 facts (the quartet construction and the Jacobian-rank collision), never
through a raw numeric observation anchor. B1 and B2 use different Σ′ normalizations (B1
R-atom `Σ'_ρ φ_j(ρ)`; B2 R-symm `Σ_ρ[φ_j(ρ)+φ_j(1−ρ)]`, ×2 larger — see their statement.md
convention notes and PROMPT_LINT L21). H's information-lattice conclusions are
convention-independent (they concern which *coordinates* a layer can/can't see, not their
scale), so the divergence does not affect any H claim; H must not cite a δ/C/d value in
either convention as if it were canonical.

**Key fact (REFEREED, Titchmarsh §9.4).** The gap between `O_theta` and `O_oracle` is
precisely the arithmetic fluctuation:
```
γ_n − d_n ~ S(γ_n) / N'(γ_n),    S(T) = (1/π) arg ζ(1/2 + iT).
```
The gap between `O_vM` and `O_oracle` is whether the explicit formula for `S(T)` in
terms of `{Λ(n)}` can be summed to recover individual `γ_n` exactly — this is the
G-hard question (CONJECTURE, not proved).

---

## §3. Theorem H (unified information obstruction, PROOF-DRAFT)

**Theorem H.** For each observation layer `L ∈ {O_finite, O_theta}`, there exists an
explicit information obstruction pair `(𝒵_L^+, 𝒵_L^-)` such that:
1. `L(𝒵_L^+) = L(𝒵_L^-)` (exact observation collision);
2. `𝒵_L^+` and `𝒵_L^-` differ as entire functions (by Hadamard uniqueness);
3. The construction is explicit and does not involve RH as a hypothesis.

**Explicitly:**
- For `L = O_finite`: the adversary pair is the B2 quartet construction `Q(σ₀,T)`.
  The observation collision is the Jacobian rank theorem (B2 §4.3).
  **Status: inherits B2 = INDEPENDENTLY-CHECKED (Gate-A PASS OB-20) + INDEPENDENT-CHECKER (OB-21).**
- For `L = O_theta`: the adversary pair is the S(T)-perturbed multiset of Theorem G
  (Prop. G.3*, Items 2–4 proved unconditionally, OB-04 2026-08-11). The observation
  collision is the S(T) gap identity (Theorem G Lemma G.2).
  **Status: inherits G-info = INDEPENDENTLY-CHECKED (Gate-A PASS OB-22) + INDEPENDENT-CHECKER (OB-17); G-hard remains CONJECTURE, not used here.**

(H's own contribution — the *unified partial-order* framing and the §4 incomparability
computations — remains PROOF-DRAFT; what is inherited from B2 and G is now established, but
H's cross-layer separation theorem H′ is not independently reviewed.)

**Common structure.** Both cases use:
1. **Hadamard uniqueness** (Lemma G.1 / Lemma E'.1): two distinct zero multisets give
   distinct entire functions of order 1.
2. **Vanishing-Jacobian / IFT argument**: finite evidence (Taylor coefficients or
   observable values) can be matched by the perturbed multiset, making the collision exact.
3. **Growth argument** (`|Ξ(Ri)| → ∞`): shows separation on compact sets despite
   the finite-evidence matching.

---

## §4. Boundary of the hierarchy

**Theorem H' (incomparability + coarsening, PROOF-DRAFT; corrected OB-27).** The maps are
**not** a strict total chain. Precisely:

(i) **`O_finite` and `O_theta` are incomparable.**
- There exist pairs `(𝒵₊, 𝒵₋)` with `O_theta(𝒵₊) = O_theta(𝒵₋)` but
  `O_finite(𝒵₊) ≠ O_finite(𝒵₋)`: take two symmetric quartets at the same height `T` but
  different real offset (`σ=3/4` vs `σ=9/10`); identical imaginary-part data (so identical
  `O_theta`), but `Li₁ = Σ1/ρ` differs (script-verified `0.019913…` vs `0.019855…`). Thus
  `O_theta` does **not** refine `O_finite`.
- Conversely there exist pairs with `O_finite(𝒵₊) = O_finite(𝒵₋)` but
  `O_theta(𝒵₊) ≠ O_theta(𝒵₋)` (an S(T)-type ordinate move preserving the first K Li values
  while changing the unfolded count). Thus `O_finite` does not refine `O_theta`.

(ii) **Both are strict coarsenings of `O_oracle`.**
- `O_finite ≺ O_oracle`: the B2 quartet pair has `O_finite(𝒵₊) = O_finite(𝒵₋)` (exact Li
  collision, B2 §4.3) but `O_oracle(𝒵₊) ≠ O_oracle(𝒵₋)` (different ordinates).
- `O_theta ≺ O_oracle`: by Lemma G.2, an S(T) perturbation `γ_n → γ_n + ε_n` with `ε_n`
  bounded by `S(γ_n)/A'(γ_n)` (`A'(t)=θ'(t)/π`) preserves `O_theta` but changes `O_oracle`.

**Status: PROOF-DRAFT.** Part (ii) inherits the exact B2 (Gate-A PASS OB-20) and G (Gate-A
PASS OB-22) collisions and is on firm ground; part (i)'s two witness computations are
explicit but not yet independently checked. The earlier "`O_finite ⊊ O_theta` strict linear
separation" claim was **withdrawn** (OB-27): it is false — the two maps are incomparable.

---

## §5. Open layer: O_vM

The question of whether `O_vM` (full von Mangoldt data) resolves S(T) is the G-hard
conjecture. Two sub-cases (affecting the `O_vM`–`O_oracle` relation only):

- **If G-hard is TRUE**: `O_vM` cannot recover `S(T)`, so `O_vM ≺ O_oracle` strictly
  (`O_vM` is a proper coarsening).
- **If G-hard is FALSE**: `O_vM` recovers `S(T)`, so `O_vM ≡ O_oracle` in information
  content (that branch of the partial order collapses).

In either case, the obstructions for `O_finite` (B2) and `O_theta` (G) are unaffected, and
their mutual incomparability (Theorem H′(i)) is independent of the G-hard question.

---

## §6. Acceptance tests (program §14)

| Check | Status |
|---|---|
| Class (B1/B2 and G instantiated) | PASS — explicit from B2 and G |
| Non-vacuity | PASS — B2 quartet is the O_finite witness; kappa_toeplitz is the O_theta witness |
| Target (distinguishes adversary pairs) | PASS — Hadamard uniqueness |
| Observation (collision exact) | PROOF-DRAFT (inherits from B2 + G) |
| Invariant (survives equivalences) | PASS — observation layer is basis-independent |
| No-RH | PASS — same as B2 and G |
| Escape | PASS — O_oracle layer is explicit escape; O_vM is a conditional escape |
| Scope | PASS — four named layers; resource bounds from B2/G |

---

## §7. Status

| Component | Status |
|---|---|
| Abstract framework (§1) | DEFINITION |
| Observation lattice (§2) | PROOF-DRAFT — PARTIAL order (corrected OB-27; not a total chain); S(T) gap identity REFEREED |
| Theorem H for O_finite | INDEPENDENTLY-CHECKED via inheritance (B2 Gate-A PASS OB-20 + INDEPENDENT-CHECKER OB-21) |
| Theorem H for O_theta | INDEPENDENTLY-CHECKED via inheritance (G-info Gate-A PASS OB-22 + INDEPENDENT-CHECKER OB-17) |
| Theorem H' incomparability (§4(i)) | PROOF-DRAFT — witness computations explicit, not independently checked |
| Theorem H' coarsening ≺ O_oracle (§4(ii)) | inherits exact B2/G collisions (firm) |
| O_vM layer analysis (§5) | CONJECTURE (G-hard) |
| H's own unification claim (partial-order framing) | PROOF-DRAFT — not independently reviewed |
