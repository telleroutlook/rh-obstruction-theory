# Statement — Theorem D' (D-prime-logpoly)

**Theorem ID:** D-prime-logpoly  
**Program ref:** EXT-1 (extension of Theorem D; audit of log-polyhomogeneous escape route)  
**Status:** ESCAPE-ROUTE-REVISED (2026-08-11; see §3–§4: 𝒞_logpoly is not the correct escape class)

---

## §1. Context and question

Theorem D (D-spectral-asymptotic) proves that no operator in the class 𝒞_ell (positive
elliptic pseudodifferential operators of any order on any compact smooth manifold) can
have spectrum equal to the Riemann zero ordinates `{γ_n}`. The obstruction is that
𝒞_ell operators have polyhomogeneous Seeley–DeWitt heat-trace expansions with no
`log(1/t)` terms, while `Z_ζ(t) ∼ (1/2π)·log(1/t)/t`.

Theorem D explicitly lists **log-polyhomogeneous operators** as an escape route (escape
item 3 of Theorem D, statement.md §Escape routes).

This document audits that escape route by asking: does the log-polyhomogeneous class
𝒞_logpoly (Schrohe 1992, Lesch 1995, Grubb–Seeley 1995) necessarily fail to reproduce
`Z_ζ(t) ∼ (1/2π)·log(1/t)/t`, or is it a live candidate?

---

## §2. The class 𝒞_logpoly

**Definition.** `H ∈ 𝒞_logpoly` if:
- `H` is a pseudodifferential operator of order `m > 0` on a compact smooth manifold `M`
  of dimension `d`;
- the symbol of `H` has a log-polyhomogeneous expansion:
  ```
  σ(H)(x,ξ) ~ Σ_j (σ_{m-j}(x,ξ) + τ_{m-j}(x,ξ)·log|ξ|)   as |ξ| → ∞,
  ```
  where `σ_{m-j}` is positively homogeneous of degree `m-j` and `τ_{m-j}` is
  positively homogeneous of degree `m-j`.

This class strictly contains 𝒞_ell (when all `τ_k = 0`).

**Key examples:**
- Powers `H^z` for complex `z` (Seeley's complex powers), expanded around non-integer `z`.
- The operator `log H` for `H ∈ 𝒞_ell`.
- Parametrix contributions involving log-symbols in the Grubb–Seeley resolvent calculus.

---

## §3. Heat-trace expansion — CORRECTED (external review OB-01, 2026-08-11)

**[CORRECTION]** The previous §3 stated that for `H ∈ 𝒞_logpoly`, the leading
heat-trace term is `c_{0,1}·t^{-d/m}·log(1/t)`. This is **incorrect as stated**.

The Grubb–Seeley / Lesch theorem (Lesch 1999, Theorem 3.7) gives an expansion for
the **weighted** heat trace `Tr(A·e^{-tP})` where `A` is log-polyhomogeneous and
`P` is a **classical** (non-log) elliptic generator. It does NOT directly give the
expansion of `Tr(e^{-tH})` when `H` itself is log-polyhomogeneous.

**What the external review established (OB-01 §6):**

For `H ∈ 𝒞_logpoly`, log terms in `Z_H(t)` appear at **subleading** orders, not
at the leading singularity. The explicit example: on `S¹`, the Fourier multiplier
```
H_c e_n = (|n| + c·log|n|) e_n
```
(log-polyhomogeneous order 1 with lower-order `c·log|ξ|` term) has:
```
Z_{H_c}(t) = 2/t − 2c·log(1/t) + O(1)   as t → 0⁺.
```
The log term appears at order `t⁰`, not `t^{-1}`. The leading singularity is still
`2/t` (a pure power).

**What produces `t^{-1}·log(1/t)` as a leading term:**

A counting law `N_H(Λ) ~ C·Λ·log Λ` yields `Z_H(t) ~ C·t^{-1}·log(1/t)` by Karamata.
This requires eigenvalues `λ_n ~ n/(C·log n)`, corresponding to a symbol growing like
`|ξ|/log|ξ|`. This is NOT in `𝒞_ell` nor in the finite-log-degree class `CL^{m,k}`.
It is a genuinely different (larger) escape class.

**Revised status of the escape route:**

| Claim | Status after correction |
|---|---|
| `𝒞_logpoly` can have `t^{-1}·log(1/t)` leading term | **FALSE** — leading term is always a pure power (Theorem 3.1 of OB-01 review) |
| `𝒞_logpoly` can have `t^k·log(1/t)` for `k ≥ 0` (subleading) | **TRUE** — Wres formula gives these |
| Escape from Theorem D: the escape class is LARGER than `𝒞_logpoly` | **TRUE** — requires `|ξ|/log|ξ|`-type symbols |
| `𝒞_logpoly` is still an escape from the **all-orders-no-log** version of Theorem D | **TRUE** (but that version of Theorem D was itself refuted) |

---

## §4. Escape-route verdict — REVISED (2026-08-11)

**Revised verdict: `𝒞_logpoly` is NOT the correct escape class.**

The escape class from Theorem D (corrected leading-singularity version) requires
operators with eigenvalue counting `N_H(T) ~ C·T·log T`, which corresponds to
symbols of type `|ξ|/log|ξ|`. This is outside `𝒞_logpoly` (which has finite-degree
log-symbol expansions and retains pure-power leading singularities).

**The genuine escape route** from the corrected Theorem D is:
operators whose symbol grows like `|ξ|/log|ξ|` (or any symbol giving `T log T`
eigenvalue counting). This class has no standard name in the pseudodifferential
literature and is not covered by any of Schrohe, Lesch, or Grubb–Seeley.

**What `𝒞_logpoly` escapes:**
The **previously stated (and now refuted) all-orders-no-log** version of Theorem D.
Since that version of Theorem D is false (explicit counterexample exists), the escape
route through `𝒞_logpoly` addresses a false claim.

**What `𝒞_logpoly` does NOT escape:**
The **corrected leading-singularity** version of Theorem D (Corollary 3.2 of OB-01
review): no classical elliptic pseudodifferential operator (including `𝒞_logpoly`)
can have `t^{-d/m}·log(1/t)` as its leading heat-trace singularity.

---

## §5. What this does NOT say

1. **Does not produce a Hilbert–Pólya operator:** The corrected escape class
   (`|ξ|/log|ξ|` symbols) is not known to contain any operator with spectrum `{γ_n}`.

2. **Does not refute Theorem D:** Theorem D (corrected) correctly excludes `𝒞_ell`
   and `𝒞_logpoly` from having a `t^{-1}·log(1/t)` leading heat-trace singularity.

3. **Does not assert any known class contains a Hilbert–Pólya operator.** The
   corrected escape class (`|ξ|/log|ξ|`-type) is outside standard calculi.

---

## §6. New research question (opened by this audit — revised)

**Can a symbol of type `|ξ|/log|ξ|` (or equivalent) produce a compact operator
with spectrum `{γ_n}` in a controlled Hilbert space?**

This is an open question. The `|ξ|/log|ξ|` growth is not elliptic in the classical
sense, and constructing a self-adjoint operator with `T log T` counting from first
principles (without reading zero locations) is a genuine open problem.

**This is recorded as a CONJECTURE and future research direction, not a theorem.**

---

## §7. Status summary — REVISED

| Component | Status |
|---|---|
| Log-polyhomogeneous heat-trace expansion (§3, Lesch 1999) | The theorem is about `Tr(A·e^{-tP})`, not `Tr(e^{-tH})`; citation scope corrected |
| `𝒞_logpoly` produces `t^{-1}·log(1/t)` leading term | **FALSE** — refuted by OB-01 review |
| `𝒞_logpoly` produces subleading log terms | TRUE — but irrelevant to Theorem D's corrected claim |
| Escape route from corrected Theorem D | Requires `|ξ|/log|ξ|`-type symbols; outside standard calculi |
| Status of D-prime theorem | **ESCAPE-ROUTE-REVISED**: `𝒞_logpoly` is not the right escape class; the correct escape class is larger and unnamed |
| Weyl law for the correct escape class | OPEN — not yet analyzed |
