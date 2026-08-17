# Theorem L — NT-C Square Subcase: No Simultaneous Perfect Squares in the Row-3 Family

**Mathematical status:** `PROOF-DRAFT`  
**Computational status:** `REPRODUCIBLE`

---

## Statement

**Theorem L.** There are no Row-3 pairs (a, n) such that both A⁺ = a²+n² and
A⁻ = (n−a)²+n² are perfect squares.

**Corollary (NT-C square subcase).** NT-C holds unconditionally for the square
subcase: for every Row-3 pair (a, n), at least one of A⁺, A⁻ is NOT a perfect square
(and hence not powerful-away-from-5 via a perfect-square path).

---

## All definitions

**Row-3 pair** (a, n): integers satisfying
- n even, n ≥ 4, 3 ∤ n
- a odd, 1 ≤ a < n, gcd(a, n) = 1

Write n = 2m. Then A⁺ = a² + 4m², A⁻ = (2m−a)² + 4m².

**Prerequisite (Theorem C of Paper E, proved):** gcd(A⁺, A⁻) ∈ {1, 5}.

---

## Scope and non-conclusions

- This proves NT-C only for the *square* subcase: A⁺ = x², A⁻ = y² (perfect squares).
- NT-C in full requires the powerful-away-from-5 case including non-trivial cube factors
  (s²t³ with t > 1); that case remains open (see `limitations.md`).
- This theorem does NOT imply or assume RH. RH stays `[OUT]`.

---

## Evidence basis

| Axis | Status |
|---|---|
| Mathematical | `PROOF-DRAFT` (proof by 2-isogeny descent; full details in `proof.md`) |
| Computational | `REPRODUCIBLE` (checker in `checker/`, runs in under 30 s, zero failures up to n=2000) |
