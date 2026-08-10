# Statement — Theorem H (H-information-hierarchy)

**Theorem ID:** H-information-hierarchy  
**Program ref:** EXT-2a (unification of B1, B2, G under a common information-obstruction framework)  
**Status:** PROOF-DRAFT

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

Four natural layers, ordered by information content:

```
O_finite ⊂ O_theta ⊂ O_vM ⊂ O_oracle
```

| Layer | What it computes | Encodes S(T)? | Used in |
|---|---|---|---|
| `O_finite` | finite set {Li_k : k≤K} or {W(φ_j) : j≤K} | No | Theorems B1, B2 |
| `O_theta` | archimedean levels {d_n = θ_level(n) : n≤N} | No | Theorem G |
| `O_vM` | full von Mangoldt explicit formula data (Λ(n) for all n) | Partially (via explicit formula) | — |
| `O_oracle` | all zero ordinates {γ_n} | Yes, by definition | trivially resolves |

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
  The observation collision is the Jacobian rank theorem (B2 §4.3). **Status: PROOF-DRAFT (B2).**
- For `L = O_theta`: the adversary pair is the S(T)-perturbed multiset of Theorem G
  (Prop. G.3). The observation collision is the S(T) gap identity (Theorem G Lemma G.2).
  **Status: PROOF-DRAFT (G-info).**

**Common structure.** Both cases use:
1. **Hadamard uniqueness** (Lemma G.1 / Lemma E'.1): two distinct zero multisets give
   distinct entire functions of order 1.
2. **Vanishing-Jacobian / IFT argument**: finite evidence (Taylor coefficients or
   observable values) can be matched by the perturbed multiset, making the collision exact.
3. **Growth argument** (`|Ξ(Ri)| → ∞`): shows separation on compact sets despite
   the finite-evidence matching.

---

## §4. Boundary of the hierarchy

**Theorem H' (separation theorem, PROOF-DRAFT).** The layers are strictly separated:
`O_finite ⊊ O_theta` as information content, meaning:
- There exist pairs `(𝒵₊, 𝒵₋)` with `O_finite(𝒵₊) = O_finite(𝒵₋)` but
  `O_theta(𝒵₊) ≠ O_theta(𝒵₋)` — theta-level data breaks the B1/B2 collision.
- There exist pairs `(𝒵₊, 𝒵₋)` with `O_theta(𝒵₊) = O_theta(𝒵₋)` but
  `O_oracle(𝒵₊) ≠ O_oracle(𝒵₋)` — the S(T) gap is the theta/oracle separation.

*Proof of first separation.* Any two zero multisets with the same first K Li values
(B1 collision) but different `γ_n` ordinates will generally have different theta-levels
`d_n = θ_level(n)`. Explicit: the B2 adversary pair `Q(σ₀,T)` has zeros off the
critical line, whose `d_n` sequence differs from the Riemann `d_n` by a computable amount.
**Status: PROOF-DRAFT** (explicit computation needed).

*Proof of second separation.* Follows from Lemma G.2: any two multisets related by an
S(T) perturbation `γ_n → γ_n + ε_n` with `ε_n` bounded by `S(γ_n)/N'(γ_n)` have
the same `O_theta` image by construction. **Status: PROOF-DRAFT (Prop. G.3 open step).**

---

## §5. Open layer: O_vM

The question of whether `O_vM` (full von Mangoldt data) resolves S(T) is the G-hard
conjecture. Two sub-cases:

- **If G-hard is TRUE**: `O_vM` cannot recover `S(T)`, so `O_vM ⊊ O_oracle` in
  information content, and the hierarchy has four strict layers.
- **If G-hard is FALSE**: `O_vM` recovers `S(T)` (perhaps by a non-constructive
  argument), so `O_vM = O_oracle` in information content, and the hierarchy collapses
  to three effective layers.

In either case, the obstructions for `O_finite` and `O_theta` are unaffected.

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
| Observation lattice (§2) | PROOF-DRAFT (S(T) gap identity REFEREED) |
| Theorem H for O_finite | PROOF-DRAFT (inherits B2) |
| Theorem H for O_theta | PROOF-DRAFT (inherits G-info) |
| Theorem H' separation (§4) | PROOF-DRAFT (explicit computations open) |
| O_vM layer analysis (§5) | CONJECTURE (G-hard) |
