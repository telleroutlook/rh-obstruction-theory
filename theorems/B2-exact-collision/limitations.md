# Limitations — Theorem B2

**Theorem ID:** B2-exact-collision  
**Status:** CONDITIONAL on rank analysis (proof.md §4)

---

## 1. Conditional on the rank conjecture

Theorem B2 is not a proved result until proof.md §4.2–§4.5 is resolved.  The
rank condition (H-rank) is explicitly a hypothesis in the theorem statement.  Any
citation must include this conditionality.

## 2. Integer multiplicity requirement (H-real-mult)

If the solution `α` to `J α = −δ^{off}(T)` requires signed (negative) or
noninteger (fractional) components with no available scaling workaround, then B2
is retracted and B1 remains the best result.  The program explicitly forbids
marketing B2 in that case (program §7.B.4).

## 3. Counting law is O(1) perturbed

The constructed `𝒵_−` has `N_{𝒵_-}(T) = N_{𝒵_+}(T) + O(1)`.  If the
ambient class requires a strict `O(log T)` error, the theorem applies only to
the class **without** that constraint.  Fixing it requires the balancing
construction of §7 (deferred).

## 4. Fixed test family only

Same as B1: fixed finite `Φ`, fixed `m`.  The infinite test hierarchy escapes.

## 5. Not about ζ directly

Same escape routes as B1 apply unchanged.

## 6. Canonical-product realization not yet attempted

Converting the zero multiset `𝒵_−` to an order-one entire function `F_−` with
exactly those zeros, the correct Ξ-like symmetries, and identical `O_Φ` values
is the B4 task (not addressed in B2).

## 7. Vandermonde rank claim is CONJECTURE tier

The algebraic-independence argument in proof.md §4.4 is not proved.  Until
a formal proof exists, the rank step is labeled CONJECTURE in `dependencies.yaml`
and B2 cannot advance past PROOF-DRAFT (conditional).
