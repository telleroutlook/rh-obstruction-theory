# checker/ — independent replay path for Theorem B2

## B2-CHK-0: Full finite-collision pipeline — CERTIFIED EXACT-RATIONAL REPLAY (deposit-ready)

**File:** `b2_certified_checker.py`
**Provenance:** OB-21 external referee (2026-08-11); independently written from the
definitions, source-verified and re-run in-repo.
**SHA-256:** `776eeab52d6012b8149250613abb7de098241c8f645b50de0515a9148b64dc83`
**Run:** `python3 b2_certified_checker.py` → prints `ALL_CERTIFIED_CHECKS_PASSED`.

Pure-stdlib (`fractions.Fraction` + integers) exact checker. **No floating point anywhere
in the certificate path** (no `float(`, no `numpy`/`scipy`/`mpmath`). It independently
reconstructs the entire B2 pipeline from the definitions and certifies:

1. **K1** — `O_j(𝒵)` computed by **traversing the multiset** per its definition
   (`Σ [φ_j(ρ)+φ_j(1−ρ)]`), asserting the imaginary part is exactly 0; **cross-checked**
   entry-by-entry against an **independent** Chebyshev-closed-form route
   `C_{jk}=4(1−T_j(x_k))`. Two independent routes agreeing = genuine cross-implementation.
2. **K2** — `det C ≠ 0` by exact Fraction Gaussian elimination; `β = −C⁻¹d` verified by
   `Cβ = −d` exactly.
3. **K3** — `R = lcm(denominators of β)`, `n = Rβ ∈ ℤᵐ`, `M = max_k|n_k|`, `M+n_k ≥ 0`.
4. **K4** — exact collision `Cn + Rd = 0`.
5. **K5** — `P(𝒵_+)=1`, `P(𝒵_−)=0`.
6. **K6** — two instances: anchor `m=2, t=(1,2), T=1` and self-chosen `m=3, t=(1,2,3), T=2`,
   both with exact zero collision residual.
7. **K7** — adversarial mutation guard: `n_1 ↦ n_1+1` makes the residual `= (8/5, 128/25)`
   = first column of `C` ≠ 0 (collision check is not vacuously true).
8. **K8** — `𝒵_+, 𝒵_−` closed (with multiplicity) under `ρ↦ρ̄` and `ρ↦1−ρ` (∈ `𝔛_sym`).
   Plus an anchor cross-check of every field against the request's stated values.

**Scope (what this certifies):** only the **finite algebraic identity** `Cn + Rd = 0` and
the surrounding pipeline (rank, integer scaling, membership, predicate separation) for the
constructed multisets. It asserts **nothing** about ζ zeros, RH, or any analytic function —
`ρ` is notation; `L(t)`, `Q` are explicit complex-rational multisets fixed by `t, T`. This
is the permanent computational replay path for B2; combined with the OB-20 Gate-A math
review, B2 is INDEPENDENTLY-CHECKED (math) + INDEPENDENT-CHECKER (computational).

The checker is pinned in the test suite (`tests/test_ledger.py`): it must run and emit
`ALL_CERTIFIED_CHECKS_PASSED`, and a guard rejects any float / numpy / scipy / mpmath in
the certified file.

---

## Original design notes (superseded by B2-CHK-0 above)

The finite-collision pipeline is now certified end-to-end by `b2_certified_checker.py`.
The earlier checklist (compute `J_{jk}` from scratch, `det J ≠ 0` exact, solve `α`,
verify `|O_j(𝒵_−)−O_j(𝒵_+)|=0`, membership, `P(𝒵_−)=0`) is fully realized by K1–K8.
No `discovery/` import; runnable offline; stdlib only.