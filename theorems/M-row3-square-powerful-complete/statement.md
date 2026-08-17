---
# Theorem M — Row-3: Complete Square-Powerful Obstruction (t=1 Case of NT-C)

**Mathematical status:** `PROOF-DRAFT`  
**Computational status:** `INDEPENDENT-CHECKER` for the elliptic rank/torsion and birational-map replays (PARI/GP 2.17.4 + exact polynomial checker; finite surveys remain sanity evidence)

**Note:** The 4∤n case was an open problem (OE-02). The corrected 2026-08-17
route is a direct pair of rational 5-conics reducing to E: Y²=X³−32X+64 (rank 0).
The rank/torsion computation has been independently replayed by PARI/GP.
Gate A remains open for independent review of the corrected direct 5-conic
reduction and explicit birational map, not for the finite CAS rank computation.

---

## Statement

**Theorem M.** For every Row-3 pair (a, n), A⁺ = a²+n² and A⁻ = (n−a)²+n²
cannot both be of the form 5^e · m² (e ≥ 0, m ∈ ℤ, i.e., "square-based
powerful-away-from-5").

More precisely:

**(i) Sub-family 4|n:** If either of A⁺ or A⁻ is of the form 5^e·m², then its
exponent `e` is even. Thus an individual odd-`e` representation is impossible;
the remaining simultaneous perfect-square case is excluded by Theorem L.

**(ii) Sub-family 4∤n:** If either of A⁺ or A⁻ is of the form 5^e·m², then its
exponent `e` is odd. Thus an individual even-`e` representation is impossible;
the remaining simultaneous `(5S²,5T²)` case is excluded by the direct
5-conic-to-elliptic reduction.

**Corollary (NT-C t=1 resolved):** The t=1 case of NT-C is completely resolved:
no Row-3 pair has both A⁺ and A⁻ powerful-away-from-5 via the square-only path
(s²t³ with t=1). The remaining open part of NT-C is the cube-factor case t ≥ 2.

---

## All definitions

**Row-3 pair** (a, n): integers satisfying
- n even, n ≥ 4, 3 ∤ n
- a odd, 1 ≤ a < n, gcd(a, n) = 1

Write n = 2m. Then A⁺ = a² + 4m², A⁻ = (2m−a)² + 4m².

**Square-based powerful-away-from-5**: A positive integer N is square-based powerful
iff N = 5^e · m² for some integers e ≥ 0, m ≥ 1. (This is the t=1 case of the
Erdős–Szekeres powerful decomposition N = 5^e · s² · t³ with t=1.)

**Theorem B** (proved, Paper E, thm:mod4): For every Row-3 pair,
- 4∤n → A⁺ ≡ A⁻ ≡ **5** (mod 8)
- 4|n → A⁺ ≡ A⁻ ≡ **1** (mod 8)

**Theorem L / Theorem D of Paper E** (proved, `theorems/L-row3-zsygmondy-square/`):
No Row-3 pair has A⁺ = x² and A⁻ = y² simultaneously.

---

## Scope and non-conclusions

- Theorem M completely resolves the t=1 (square-only powerful) case of NT-C.
- NT-C in full (t ≥ 2, cube-factor case) remains open (see `outsource/OE-01-...`).
- Parts (i) and (ii) use elementary congruence arithmetic to force the parity of
  `e`. The remaining simultaneous square case in (i) invokes Theorem L; the
  remaining simultaneous `(5S²,5T²)` case in (ii) invokes the OE-02 descent.
- The theorem makes no claim that individual square representations are impossible.
  For example, the Row-3 pair `(a,n)=(15,8)` has `A⁺=17²`; this illustrates why
  the individual even-`e` case cannot be excluded in the `4|n` branch.
- This theorem does NOT assume or imply RH. RH stays `[OUT]`.
- This theorem does NOT assume ABC, any conjecture, or Sha triviality.

---

## Evidence basis

| Axis | Status |
|---|---|
| Mathematical | `PROOF-DRAFT` (elementary congruences plus direct 5-conic reduction; awaiting independent Gate-A review) |
| Computational | `INDEPENDENT-CHECKER` for rank/torsion (PARI/GP replay); `REPRODUCIBLE` finite surveys only |
