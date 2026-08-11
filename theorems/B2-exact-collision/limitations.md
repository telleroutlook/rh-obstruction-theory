# Limitations — Theorem B2

**Theorem ID:** B2-exact-collision  
**Status:** PROOF-DRAFT — rank step PROVED (proof.md §4.3–§4.4, self-contained Vandermonde);
integer-sign step RESOLVED (§4.5); OB-02 confirmed + OB-13 INDEPENDENT-CHECKER (2026-08-11).

---

## 1. Rank step is PROVED (not conjectural)

The rank condition (H-rank) is **proved** by the self-contained Chebyshev + lower-triangular
+ Vandermonde argument in proof.md §4.3 (Li-type) and §4.4 (moment-type) — no external
citation required, and confirmed by OB-02 external review. It is therefore no longer a
hypothesis-to-be-discharged; the earlier "conditional on rank" caveat is withdrawn.

## 2. Integer multiplicity requirement (H-real-mult) — RESOLVED

The integer-sign step is resolved (proof.md §4.5): `β = −C⁻¹d(T) ∈ ℚᵐ`, scaled by
`R = lcm(denominators)` to `n ∈ ℤᵐ`, with a multiplicity buffer `M = max_k|n_k|` making
all `M + n_k ≥ 0`. So signed/fractional multiplicities are not an obstruction; the
construction gives nonneg integer multiplicities. Independently reconstructed in exact
rational arithmetic by OB-13 (m=2 and m=3 instances, exact zero residual, mutation guard).

## 3. Counting law is O(1) perturbed

The constructed `𝒵_−` has `N_{𝒵_−}(T) = N_{𝒵_+}(T) + O(1)`. On the augmented class
`𝔛_sym^{(*),nr}` requiring the Riemann–von Mangoldt law with `O(log T)` error, this is
handled by the OB-07 counting-law lift (adjoin the unconditional inverse-counting
background `𝒟`; an `O(1)` change is `⊂ O(log T)`). So the counting-law refinement is
addressed by OB-07, not deferred. The bare finite construction still lives in the
`𝔛_sym` without the counting-law constraint.

## 4. Fixed test family only

Fixed finite `Φ`, fixed `m`. The infinite test hierarchy escapes (same as B1). This is a
scope statement, not a defect.

## 5. Not about ζ directly

Same escape routes as B1 apply unchanged: no Euler product, gamma factor, functional
equation, or coefficient arithmetic is assumed. `𝒵_+`/`𝒵_−` are constructed multisets,
not ζ's zeros.

## 6. Canonical-product realization not yet attempted

Converting the zero multiset `𝒵_−` to an order-one entire function `F_−` with exactly
those zeros, the correct Ξ-like symmetries, and identical `O_Φ` values is the B4 task
(not addressed in B2). B2 is a statement about zero *multisets* under a finite observation,
not about entire functions.

## 7. What remains for Gate A (independent mathematical review)

B2's remaining step to "established" is **independent inspection of the full analytic
chain** (statement + proof separation + normalization + witness), not any unproved
internal lemma. The finite core is already INDEPENDENT-CHECKER (OB-13). What is NOT yet
done: an independent referee confirming the §2–§6 assembly (quartet-decay lemma, rank
lemma, integer scaling, membership, exact-collision identity) as a coherent whole. Until
that closes, B2 stays PROOF-DRAFT — not because any step is conjectural, but because the
status of a proof is derived by an independent checker, never self-declared.
