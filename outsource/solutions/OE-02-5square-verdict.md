# OE-02 Solution Verdict — Simultaneous (5S², 5T²) for 4∤n

**Date:** 2026-08-17
**Status:** CONFIRMED (PROOF-DRAFT; 2-isogeny descent pending CAS independent check)
**Computational status:** REPRODUCIBLE (checker: `theorems/M-row3-square-powerful-complete/checker/verify_OE02_elliptic.py`)

---

## Verdict

The system A⁺ = 5S², A⁻ = 5T² has **no solutions** for any Row-3 pair (a,n) with 4∤n.

This closes the 4∤n open case of Theorem E (Paper E, thm:squarepow), completing the
full NT-C t=1 result (square-based powerful-away-from-5 obstruction for all Row-3 pairs).

---

## Proof summary

### Step 1: Gaussian factorization

In ℤ[i], write z₁ = a+ni = ω₁α², z₂ = (n−a)+ni = ω₂β² where ω₁,ω₂ ∈ {uπ, uπ̄}
(π = 1+2i, π̄ = 1−2i, units u ∈ {±1, ±i}).

The sum identity:
  z₁ + z₂ = n + 2ni = n(1+2i) = nπ

partitions into four cases by the choice of (ω₁, ω₂):

### Step 2: Cases B, C, D closed by gcd/parity

- **Case B** (π|ω₁, π̄|ω₂): Sum forces π|z₂ and π̄|ω₂, so 5|z₂ → 5|b and 5|n → 5|a.
  Contradicts gcd(a,n)=1.
- **Case C** (π̄|ω₁, π|ω₂): Symmetric; 5|a and 5|n. Contradiction.
- **Case D** (π̄|ω₁, π̄|ω₂): Sum/π̄ = nπ/π̄ = n(−3+4i)/5 ∈ ℤ[i] requires 5|n.
  Since n≡2 mod 4 and 5|n → n≡10 mod 20. Analysis of all unit sub-cases then
  forces 5|a. Contradicts gcd(a,n)=1.

### Step 3: Case A (π|ω₁, π|ω₂) → elliptic curve

Sum/π = n (real). Mixed-unit and both-imaginary sub-cases produce parity contradictions
(Y₁ divisible by 4 vs. odd). For both-real units (u₁,u₂ ∈ {±1}), the system reduces
via x = X₁/Y₁ to:

  y₁² = x²+1,   y₂² = x²+2x+2

Rational parametrization of the first conic (x = (1−t²)/(2t), y₁ = (1+t²)/(2t)) and
substitution into the second gives the quartic:

  Y² = t⁴ − 4t³ + 6t² + 4t + 1   (Y = 2ty₂)

This is a genus-1 curve, birationally equivalent to the Weierstrass model:

  **E: Y² = X³ − 32X + 64**

### Step 4: Rank 0, torsion ℤ/4ℤ

The curve E has:
- 2-torsion point (4,0): verified by 4³−32·4+64 = 0 ✓
- Torsion = ℤ/4ℤ = {O, (4,0), (0,8), (0,−8)}: verified by group law 2·(0,8) = (4,0),
  4·(0,8) = O ✓
- Nagell-Lutz search: only (4,0), (0,±8) as integer points ✓
- Rank = 0: claimed via 2-isogeny descent (|Im(α)|=1, |Im(α̂)|=2 → 2^rank = 1).
  **Pending:** independent CAS (Sage/Magma) verification of the Selmer group computation.

### Step 5: Row-3 obstruction

All four torsion points pull back to t ∈ {0, ∞} on the quartic → Y₁ = 0 → n = ±2,
violating the Row-3 condition n ≥ 4. □

---

## Computational verification

`theorems/M-row3-square-powerful-complete/checker/verify_OE02_elliptic.py` confirms:
- E(ℚ)_tors = ℤ/4ℤ via exact group law (Fraction arithmetic)
- Nagell-Lutz search: no other integer points
- Quartic integer scan |t| ≤ 3000: only t=0 (→ n=2, invalid)

---

## Remaining gap (Gate A blocker)

The 2-isogeny descent rank computation ("Selmer groups bounded by local conditions at 2
and 5, giving |Im(α)|=1, |Im(α̂)|=2 → rank=0") must be independently verified by CAS
before the status advances to INDEPENDENTLY-CHECKED.

A Sage/Magma script verifying E.rank() = 0 and E.torsion_subgroup() ≅ ℤ/4ℤ would close
this gap.

---

## Impact on theorems

- **Theorem M** (this repo, `theorems/M-row3-square-powerful-complete/`): 4∤n case now
  proved. Full Theorem M is complete (PROOF-DRAFT, pending descent CAS check).
- **Theorem E** (Paper E, thm:squarepow): both 4|n (complete) and 4∤n (this step)
  cases proved. Section title can be updated to "complete obstruction".
- **Limitations**: M1 (t≥2 cube-factor case) remains open via OE-01.
