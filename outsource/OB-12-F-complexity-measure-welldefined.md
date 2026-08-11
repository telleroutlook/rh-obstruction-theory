# Problem OB-12 — F: is the Schur-certificate complexity measure κ well-defined and non-collapsing?

**Type:** linear algebra / convex optimization / proof-complexity (positive
semidefinite certificates, Schur complements, congruence)

**Non-circularity:** RH is not assumed and does not appear in any hypothesis. This is a
finite-dimensional linear-algebra question about a proof-complexity measure. The matrix
`M` below is an arbitrary real symmetric matrix; no property of ζ, no zero location, and
no spectral data of any L-function is used. (The intended application is a Weil-form
Galerkin matrix, but the question is purely about the certificate measure.)

---

## Background and the exact problem

Theorem F (repository theorem `F-schur-complexity`) claims a **lower bound** on a
"Schur-certificate complexity" `κ`. Two passages in its current proof draft appear to
contradict each other, and the contradiction traces to an **ambiguous definition of the
complexity measure**. This task is to pin down the definition and decide whether a
non-collapsing lower bound is possible, or whether the measure trivializes (making the
theorem vacuous as a complexity statement).

The two conflicting passages (paraphrased, self-contained):

- **Passage A (collapse):** "A rank-r certificate works **iff** `U^T M U − δI ≽ 0`,
  which is equivalent to `λ_min(M) ≥ δ` — a scalar statement independent of the basis
  `U` and of any block decomposition. Hence if `δ < λ_min(M)`, the full matrix itself is
  a certificate, and `κ = 1`."

- **Passage B (growth):** "For large a (a scaling parameter of M), the minimum
  eigenvector spreads across all N coordinates, so no rank-`r < N` Schur/pivot
  certificate can avoid the minimal direction; hence `κ = N`."

If Passage A's reading of "certificate" is correct, then `κ ∈ {1, +∞}` always (1 if
`λ_min(M) ≥ δ`, `+∞` otherwise), and Theorem F's "complexity grows" conclusion is
**vacuous**. Passage B intends `κ` to count something finer (pivot steps / block count
under a restricted rule). The task is to make this precise.

---

## All definitions (self-contained — everything is here)

Let `M ∈ ℝ^{N×N}` be symmetric, `δ > 0` a fixed real, and set `S := M − δ I_N`
(also symmetric). Denote by `λ_min(·)` the least eigenvalue.

We consider **restricted PSD certificates** for the assertion "`S ≽ 0`" (equivalently
`M ≽ δ I`). Three candidate certificate models are on the table; the task is to analyze
all three and determine which (if any) yields a non-trivial complexity measure.

### Model 1 — "any congruence + one PSD test" (the Passage-A reading)

A Model-1 certificate is: pick `U ∈ O(N)` (orthogonal), and assert `U^T S U ≽ 0`.
Cost = 1 (a single PSD assertion on the whole matrix).

Under Model 1, `S ≽ 0` is certifiable at cost 1 iff `λ_min(S) ≥ 0`, since congruence by
orthogonal U preserves eigenvalues. So the measure is `κ_1 ∈ {1, +∞}`.

### Model 2 — "Schur-complement elimination in a FIXED basis, counting pivot steps"

Fix the standard basis (no free `U`). A Model-2 certificate of rank r is a sequence of
r Schur-complement (block-pivot) steps:
- choose an ordered partition of `{1,…,N}` into blocks `I_1, …, I_r` (nonempty,
  disjoint, union = everything);
- require each pivot block `S_{I_1 I_1}` PD, form the Schur complement
  `S^{(1)} = S_{I_2∪…, I_2∪…} − S_{·,I_1} S_{I_1 I_1}^{-1} S_{I_1,·}`, and recurse;
- the certificate **succeeds** if every pivot block encountered is positive definite
  (this certifies `S ≻ 0` by the standard Schur/Haynsworth inertia additivity).
Cost = r = number of blocks. `κ_2(S) :=` minimum r over all block orderings that
succeed (or `+∞` if none succeeds, e.g. if `S` is not PD).

### Model 3 — "restricted: congruence allowed but block count bounded, residual rank r"

A Model-3 certificate of rank r: choose `U ∈ O(N)`, then apply a Model-2 certificate to
`U^T S U` **with at most r blocks**, where additionally each block has size ≤ some fixed
bound (or the "residual rank" — the size of the last Schur complement — is ≤ r). The
precise meaning of "residual rank r" is one of the things to pin down.

### The scaling family (for the growth question)

For the growth question, take a one-parameter family `S(a) = M(a) − δ I` where
`M(a) ∈ ℝ^{N×N}` is symmetric PD with `λ_min(M(a)) > δ` for all a in the range of
interest (so all three measures are finite for each fixed a), and where the unit
eigenvector `v(a)` of `λ_min(M(a))` becomes **delocalized** as `a → ∞`:
```
|⟨v(a), e_j⟩|² → 1/N   for every j = 1,…,N   as a → ∞.
```
(This delocalization is the property Passage B invokes. It is a hypothesis on the
family, to be used, not proved.)

---

## The claims to be verified

### Claim A: Model 1 collapses (Passage A is correct for Model 1)

**Claim A.** Under Model 1, for every symmetric S, `κ_1(S) = 1` if `λ_min(S) ≥ 0` and
`κ_1(S) = +∞` otherwise. In particular κ_1 cannot exhibit growth in a and Theorem F is
**vacuous under Model 1**.

**What to verify:** confirm that orthogonal congruence preserves the spectrum, so the
"cost-1 whole-matrix PSD assertion" succeeds iff `λ_min(S) ≥ 0`, independent of a.

### Claim B: Does Model 2 (fixed basis, pivot count) give a non-trivial κ_2?

**Claim B.** Determine `κ_2(S)` for PD `S`. Specifically:

1. Is it true that for any PD `S`, `κ_2(S) = 1`? (I.e., does the single block
   `I_1 = {1,…,N}` — testing `S ≻ 0` directly — always count as one Model-2 step,
   trivializing κ_2 as well?) If "testing `S_{I_1 I_1} ≻ 0`" for the full block is
   itself an allowed atomic step, then κ_2 ≡ 1 for all PD S, and Model 2 is also vacuous.

2. If instead an atomic pivot is restricted to blocks of size 1 (scalar pivots, i.e.
   Cholesky/LDL^T), then a Model-2 certificate is a full symmetric Gaussian elimination:
   it succeeds iff all N leading principal minors (in the chosen order) are positive,
   and the "cost" is N scalar pivots regardless of S. Then κ_2 ≡ N for all PD S — also
   not a function that "grows with a". Confirm or refute.

3. Conclusion: state whether Model 2, under either atomic-step convention, can produce a
   complexity measure that is **finite and varies with a** (i.e. genuinely between 1 and
   N depending on the matrix), or whether it collapses to a constant (1 or N).

### Claim C: Is there ANY certificate model for which a delocalized minimum eigenvector forces growing cost?

**Claim C.** This is the crux. Find a certificate model (Model 3 or a precise variant)
such that:
- (finiteness) for each fixed a with `λ_min(M(a)) > δ`, the cost `κ(S(a))` is finite;
- (non-collapse) `κ(S(a))` is NOT identically 1 and NOT identically N;
- (growth) under the delocalization hypothesis, `κ(S(a)) → ∞` (or `≥ f(a) → ∞`) as
  `a → ∞` while N stays fixed OR while the relevant dimension grows.

Determine whether such a model exists, and if so, state its precise atomic-step
definition and prove the growth bound. If NO such model exists among natural
Schur/congruence certificate systems (i.e. every such measure collapses to 1 or N, or
becomes basis-dependent in a way that violates the representation-invariance discipline
below), state that decisively — this would mean **Theorem F cannot be a genuine
complexity lower bound** and must be downgraded (see Acceptance criterion REFUTED).

**Representation-invariance constraint (mandatory).** Any proposed measure must be
invariant under orthogonal congruence `S ↦ U^T S U` (U ∈ O(N)), OR must explicitly
justify why a basis-dependent measure is meaningful. A measure that "grows" only because
it is pinned to one special basis (and can be reduced to 1 by choosing the eigenbasis of
M) is a **representation artifact**, not a complexity lower bound. This is the exact
failure mode the repository's methodology forbids: a scalar/basis quantity masquerading
as an invariant.

**What to verify for Claim C:**
1. If a valid non-collapsing invariant model exists: give its atomic step, prove
   finiteness for fixed a, and prove the growth bound from delocalization.
2. If not: prove that every orthogonally-invariant Schur/congruence measure of "cost to
   certify `M ≽ δI`" collapses to a spectral condition (hence to `κ ∈ {1, +∞}` or a
   constant), so no growth in a is possible. In this case identify what EXTRA restriction
   on the certificate system (e.g. "congruence forbidden; only fixed-basis size-≤b
   blocks allowed") would be needed to recover a non-trivial measure, and whether that
   restriction corresponds to any actually-published proof method.

---

## Proof skeleton to be closed

### Step 1 — Model 1 collapse (Claim A)
Confirm orthogonal-congruence spectral invariance ⟹ κ_1 ∈ {1, +∞}.
**Acceptance:** CONFIRMED (one paragraph) or a counterexample.

### Step 2 — Model 2 triviality analysis (Claim B)
Analyze κ_2 under (i) full-block atomic step and (ii) scalar-pivot atomic step. Decide
whether either yields a non-constant finite measure.
**Acceptance:** decisive statement of κ_2 under each convention.

### Step 3 — Existence/non-existence of a non-collapsing invariant measure (Claim C)
Either construct one and prove growth, or prove collapse for all invariant models.
**Acceptance:** CONFIRMED (with explicit model + growth proof), or REFUTED (with the
collapse proof), or PARTIAL (a candidate model whose growth is open, with the precise
remaining gap).

---

## Acceptance criteria

1. **CONFIRMED (Theorem F salvageable):** there is a precisely-defined, orthogonally
   invariant (or justifiably basis-fixed) certificate measure κ that is finite for each
   fixed a and provably grows as `a → ∞` under delocalization. Give the definition and
   the growth proof.

2. **REFUTED (Theorem F is not a complexity lower bound):** every natural
   Schur/congruence certificate measure for "`M ≽ δI`" collapses to a spectral condition
   (κ ∈ {1, +∞} or a dimension-only constant), so the "complexity grows with a"
   conclusion is vacuous. Give the collapse proof and state what the theorem CAN honestly
   claim instead (e.g. only a statement about `λ_min(M(a))` itself, which is a
   margin/eigenvalue statement, not a proof-complexity bound).

3. **PARTIAL / inconclusive + localization:** a candidate non-collapsing measure is
   identified but its growth under delocalization is not settled; state the precise
   remaining lemma. Or: the answer depends on the atomic-step convention; specify which
   convention gives which outcome.

All outcomes are decisive and acceptable. Do NOT force a "F is fine" conclusion — a
clean REFUTED (with a correct restatement of what F can claim) is a valuable result and
is explicitly allowed.

---

## Numerical anchor (sanity only — not an input)

Let `N = 2`, `δ = 1`, and
```
M(a) = R(a)^T diag(2, 3) R(a),   R(a) = rotation by angle θ(a),
```
so `λ_min(M(a)) = 2 > δ = 1` for all a, and the min eigenvector is
`v(a) = R(a)^T e_1 = (cos θ(a), −sin θ(a))`. Choosing `θ(a) → π/4` delocalizes v(a) to
`(1/√2, −1/√2)`, so `|⟨v, e_j⟩|² → 1/2 = 1/N`.

- Model 1: `κ_1 = 1` for every a (since `λ_min(M(a)) = 2 ≥ 1`), regardless of θ(a).
  This already illustrates the collapse: delocalization does NOT change κ_1.
- Eigenbasis choice `U = R(a)^T` diagonalizes `M(a) − I = R^T diag(1,2) R`, so in that
  basis it is `diag(1,2) ≻ 0`, certified with one 2×2 PD block — cost 1.

This 2×2 example is a sanity check on the collapse phenomenon only; it is not an input to
the general analysis. A correct solution must treat general N (and, for Claim C, the
`a → ∞` delocalization regime), not just this example.
