# Statement — Theorem H (H-information-hierarchy)

**Theorem ID:** H-information-hierarchy  
**Program ref:** EXT-2a (unification of B1, B2, G under a common information-obstruction framework)  
**Status:** PROOF-DRAFT — **Gate-A BLOCKED (OB-32, 2026-08-12).** No RH input, but the
framework had definitional errors: (a) `O_oracle` was ordinates-only, so the same-Im witness
refuted the needed `O_finite ≼ O_oracle` — fixed by defining `O_oracle = 𝒵` (full multiset);
(b) under Theorem G's literal `O_theta` (a fixed 𝒵-independent sequence, hence *constant*),
`O_theta ≺ O_finite` — so the two are **comparable**, and the incomparability claim H'(i) is
**NOT established** (only `O_finite ⋠ O_theta` holds; the reverse needs a nonconstant
`O_theta` + an exact witness, both absent); (c) "lattice" → "refinement preorder". Inherited
B2/G obstructions remain established; H's own increment (incomparability H'(i)) does not. See
§2, §4.

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

## §2. The observation refinement preorder

**OB-32 correction (2026-08-12).** Two fixes forced by the Gate-A review, before any of the
diagram below is legitimate:
- **`O_oracle` must be the FULL zero multiset `𝒵` (all `(β,γ)` with multiplicity), NOT the
  ordinates `{γ_n}` alone.** An ordinates-only oracle does *not* refine `O_finite`: the
  same-imaginary-part quartet pair (`σ=3/4` vs `σ=9/10` at height `T`) has identical
  ordinates but different `Li_1` (§4), so under the ordinates-only definition
  `O_oracle` collides while `O_finite` separates — i.e. `O_finite ⋠ O_oracle`, refuting the
  very arrow the framework needs. With `O_oracle(𝒵)=𝒵` (full multiset), `O_finite ≼ O_oracle`
  and `O_theta ≼ O_oracle` hold (both are functions of `𝒵`).
- **This is a `refinement PREORDER`, not a lattice.** `≼` is reflexive and transitive but not
  antisymmetric on raw maps (`O(x)=x` and `O'(x)=(x,0)` mutually refine but differ); it
  becomes a partial order only on information-equivalence classes (fibers). No meet/join
  closure for the four maps is claimed. "Lattice" is withdrawn.

Under the corrected `O_oracle = 𝒵`:
```
        O_oracle = 𝒵         (the full zero multiset — finest)
        /    |    
   O_vM   O_finite     O_theta
     |
   (O_theta ≼ O_vM only under a nonconstant reading — see below)
```
Established relations: `O_finite ≼ O_oracle`, `O_theta ≼ O_oracle`, `O_vM ≼ O_oracle`.

| Map | What it computes | Sees Re ρ? | Sees Im-count? | Used in |
|---|---|---|---|---|
| `O_finite` | finite `{Li_k : k≤K}` (`K≥1`) | **Yes** (via 1/ρ) | No | B1, B2 |
| `O_theta` | Theorem-G archimedean levels `d_n=θ_level(n)` — a **fixed, 𝒵-independent** sequence | No | No | G |
| `O_vM` | full von Mangoldt data `Λ(n)` | — | — | — |
| `O_oracle` | the full multiset `𝒵` (all `(β,γ)`, with multiplicity) | Yes | Yes | trivially resolves |

**Status of the incomparability claim (OB-32 — HONEST DOWNGRADE).** The earlier "`O_finite`
and `O_theta` are incomparable" is **NOT established**:
- **Only one direction holds:** `O_finite ⋠ O_theta` (the same-Im pair separates under `Li_1`
  but not under `O_theta`), CONFIRMED for the `Li` branch with `K≥1` (§4, script-verified).
- **The other direction is FALSE under the literal `O_theta`.** Since Theorem G's
  `O_theta(𝒵)=d_n=θ_level(n)` is a **fixed sequence independent of 𝒵**, it is a *constant*
  map, so `O_theta ≼ O` for **every** map `O` — in particular `O_theta ≼ O_finite`. Combined
  with the first bullet, the literal reading gives `O_theta ≺ O_finite` (strictly coarser),
  **not incomparable**. ("Either reading gives incomparability" was a logic error, OB-32 §1.)
- To *recover* genuine incomparability one must (a) redefine `O_theta` as a nonconstant
  functional of `𝒵` (e.g. sampled counts `N_𝒵(d_m)` at fixed levels), and (b) supply an
  exact same-`O_finite`/different-`O_theta` witness — the current draft has neither (the
  "`ker DF`" sketch in §4 is only a first-order condition, not an exact collision).

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

**Theorem H' (BLOCKED as stated, OB-32 — one direction only).** The maps are not a total
chain, but the claimed **incomparability of `O_finite` and `O_theta` is NOT established**:

(i) **Incomparability — NOT established (OB-32).**
- **`O_finite ⋠ O_theta` — CONFIRMED (`Li` branch, `K≥1`).** Two symmetric quartets at the
  same height `T`, different real offset (`σ=3/4` vs `σ=9/10`), have identical imaginary-part
  data (identical `O_theta`) but `Li₁ = Σ1/ρ` differs (script-verified `0.019913…` vs
  `0.019855…`). So `O_theta` does not refine `O_finite`.
- **`O_theta ⋠ O_finite` — FALSE under the literal `O_theta`.** Theorem G's
  `O_theta(𝒵)=d_n=θ_level(n)` is a **fixed, 𝒵-independent** sequence, i.e. a *constant* map;
  a constant map refines every map, so `O_theta ≼ O_finite`. Combined with the first bullet
  this gives `O_theta ≺ O_finite` (strictly coarser) — the two are **comparable**, not
  incomparable. The purported reverse witness ("`v ∈ ker DF`") is only a first-order
  condition, not an exact `O_finite`-collision (OB-32 §4.4). So (i) is **unproven / false as
  stated**; genuine incomparability would need a *nonconstant* `O_theta` (e.g. sampled counts
  `N_𝒵(d_m)`) plus an exact same-`O_finite`/different-`O_theta` witness — neither is provided.

(ii) **Coarsenings of `O_oracle = 𝒵` (full multiset) — hold, inherited.**
- `O_finite ≺ O_oracle`: the B2 quartet pair has `O_finite(𝒵₊)=O_finite(𝒵₋)` (exact Li
  collision, B2 §4.3, Gate-A PASS OB-20) but `𝒵₊ ≠ 𝒵₋`. (Requires `O_oracle = 𝒵`; with the
  old ordinates-only oracle this arrow FAILED — the same-Im witness refutes it, OB-32 §4.2.)
- `O_theta ≺ O_oracle`: `O_theta` is constant (literal reading), so trivially a coarsening;
  under a nonconstant reading it would need G Lemma G.2 — deferred with that reading.

**Status: BLOCKED as stated (OB-32); PARTIAL repair for `K=1` (OB-32-repair).** Only
`O_finite ⋠ O_theta` and the two coarsenings (with `O_oracle=𝒵`) were established at review
time. **Repair progress:** with a **nonconstant** `O_theta` — the sampled-count map
`O_theta^{samp}(𝒵) := (N_𝒵(d_m))_{m≤M}`, `N_𝒵(u)=#{ρ∈𝒵 : |Im ρ| ≤ u}` at fixed θ-levels
`d_m` — the reverse direction is now established **for the `K=1` observation** by an *exact*
witness: the two symmetric quartets `Q(1/4, 2)` and `Q(1/3, T₂)` with `T₂ = 2.024521…`
(the positive root of `Li₁(1/3,T₂)=Li₁(1/4,2)=2144/4745`) have **equal `Li₁`** (exact, by
construction) but different heights, so any sampled level `d_m ∈ (2, T₂)` gives
`N_{𝒵₊}(d_m)=2 ≠ 0=N_{𝒵₋}(d_m)` — i.e. `O_finite^{(K=1)}` collides while `O_theta^{samp}`
separates. Combined with `O_finite ⋠ O_theta`, this gives genuine **incomparability of
`O_finite^{(K=1)}` and `O_theta^{samp}`**.

**What remains open.** (i) For the full `O_finite = (Li_1,…,Li_K)`, `K≥2`, an exact reverse
witness needs `K` matched coordinates with `>K` free tail parameters — i.e. the B1/B2 IFT
construction, **not** a closed-form 2-quartet pair; not delivered here. (ii) Under Theorem G's
**literal** `O_theta = d_n = θ_level(n)` (a constant map), incomparability is still false
(`O_theta ≺ O_finite`) — the repair requires adopting the nonconstant `O_theta^{samp}` as the
definition. So H'(i) holds for `(K=1, O_theta^{samp})` and is open for `K≥2`; a resend should
scope the claim to `O_theta^{samp}` and either restrict to `K=1` or supply the IFT witness.

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
| Observation structure (§2) | **BLOCKED as stated (OB-32)** — a refinement PREORDER (not a lattice); `O_oracle` must be the full multiset 𝒵; literal `O_theta` is constant ⇒ `O_theta ≺ O_finite` |
| Theorem H for O_finite | INDEPENDENTLY-CHECKED via inheritance (B2 Gate-A PASS OB-20 + INDEPENDENT-CHECKER OB-21) |
| Theorem H for O_theta | INDEPENDENTLY-CHECKED via inheritance (G-info Gate-A PASS OB-22 + INDEPENDENT-CHECKER OB-17) |
| Theorem H' incomparability (§4(i)) | **NOT ESTABLISHED (OB-32)** — only `O_finite ⋠ O_theta` holds; reverse is false under literal `O_theta`; needs nonconstant `O_theta` + exact witness |
| Theorem H' coarsening ≺ O_oracle=𝒵 (§4(ii)) | inherits exact B2/G collisions (firm, once `O_oracle=𝒵`) |
| O_vM layer analysis (§5) | CONJECTURE (G-hard) |
| H's own unification claim (partial-order framing) | PROOF-DRAFT — not independently reviewed |
