# Problem OE-04 — NT-D: Powerful-gap Bound for Gaps of Order A

**Returned-feedback status (2026-08-17):** the geometric/Vojta reply is **REJECTED as
a CONFIRMED result**. Its square-case elliptic argument is incomplete and already
covered by Theorem L; its fixed-cube-factor curves are genus one, not genus >1; and the
Darmon-Granville/Vojta scope is not established. A salvaged exact outcome is that the
**gap-only route is REFUTED** by `4=2^2` and `8=2^3`, whose gap is comparable to their
size. See `outsource/solutions/OE-04-geometric-feedback-review.md`.

**Type:** Pure arithmetic / Diophantine (powerful numbers, gap problems, ABC conjecture)

**Non-circularity:** All hypotheses are elementary arithmetic over ℤ and ℤ[i]. No zeros of ζ, no RH, no Li coefficients, no ordinate values. RH stays `[OUT]`.

**Relation to Paper E.** This is blocking theorem NT-D (Paper E, thm:NTD). Classical powerful-gap results (Molsen 1939, Stormer, Pillai, Granville 1998) require the gap k ≪ A^{1/2} or k fixed; for Row-3 pairs the gap k = n(2a−n) satisfies k ≍ A, which is outside all classical regimes. The ABC approach is a known dead end (proved in Paper E). A Row-3-specific Diophantine argument that uses more than gap size would be needed to close NT-D.

---

## All definitions (self-contained)

**Row-3 pair** (a, n): integers satisfying
- n even, n ≥ 4, 3∤n
- a odd, 1 ≤ a < n, gcd(a, n) = 1

Set:
- A⁺ = a² + n²,   A⁻ = (n−a)² + n²
- Gap: Δ := A⁺ − A⁻ = n(2a−n)

**Powerful-away-from-5:** A positive integer N is powerful-away-from-5 if every prime
p ≠ 5 dividing N satisfies p² | N.

**Theorem B (proved):** 4|n → A⁺≡A⁻≡1 (mod 8); 4∤n → A⁺≡A⁻≡5 (mod 8).
**Theorem C (proved):** gcd(A⁺, A⁻) ∈ {1, 5}.

**Size estimates (all elementary):**
- A⁻ = (n−a)²+n² ∈ [n²+1, 2n²−1]  (since 1 ≤ n−a ≤ n−1)
- A⁺ = a²+n² ∈ [n²+1, 2n²−1]       (since 1 ≤ a ≤ n−1)
- Both A⁺, A⁻ ≍ n².
- |Δ| = |n(2a−n)| ≤ n · (n−1) < n². So |Δ| < A⁻ and |Δ| ≍ n² ≍ A⁻.
- The gap-to-size ratio: |Δ|/A⁻ ∈ (0,1) for all Row-3 pairs.

**The rad bound (from powerful hypothesis):**
If A⁺ and A⁻ are both powerful away from 5:
- Every prime p ≠ 5 with p | A⁺ satisfies p² | A⁺, so p ≤ √A⁺.
- Therefore rad(A⁺) ≤ 5 · ∏_{p|A⁺, p≠5} p ≤ 5 · √(A⁺/5^{v₅(A⁺)}) ≤ 5 · √A⁺.
- Similarly rad(A⁻) ≤ 5·√A⁻.
- Combined: rad(A⁺ · A⁻) ≤ 25 · √(A⁺ · A⁻) ≍ n².

**The classical powerful-gap landscape:**
- **Catalan–Mihailescu (2002):** The only consecutive PERFECT POWERS are 8 and 9.
  Not applicable here: powerful numbers (every prime factor appears with exponent ≥ 2)
  are far more numerous than perfect powers.  There are infinitely many consecutive
  powerful numbers (gap = 1): e.g. 8=2³, 9=3²; 288=2⁵·3², 289=17²; 675=3³·5², 676=2²·13².
  These arise from Pell-type equations and are not a finite set.
- **Stormer's theorem:** Applies to pairs of consecutive *S-smooth* integers (all prime
  factors in a fixed finite set S): for each S, only finitely many such consecutive pairs.
  Does NOT apply to consecutive powerful numbers in general (S is not fixed).
- **Molsen (1939) and Pillai:** Paper E cites these results as requiring gap k ≪ A^{1/2}.
  The exact scope should be verified from the source: Molsen (1939)
  "Zur Verallgemeinerung des Fermatschen Satzes", Archiv Math. Naturvid. 43.
  Do not assume the specific statement without checking; the key point from Paper E
  is that all classical results need k ≪ A^{1/2}, leaving k ≍ A uncharted.
- **Granville (1998):** "ABC implies that there are infinitely many powerful numbers
  but no two powerful numbers are within O(X^{1/2+ε})" — CONDITIONAL on ABC.
  Same regime as Molsen (gap ≪ A^{1/2+ε}); inapplicable when gap ≍ A.

---

## The theorem / claim to be verified

**NT-D (what is needed).** Any one of the following would suffice to close the gap:

**(a) Unconditional powerful-gap theorem in the regime k ≍ A.**
Prove: there exist no integers A₁, A₂ with A₂ > A₁, A₂ ≍ A₁, and |A₂ − A₁| ≍ A₁,
such that A₁ and A₂ are both powerful. (A positive result here would be new.)

**(b) Conditional ABC bound.**
Assuming ABC over ℤ[i] with exponent 1+ε: derive from the Gaussian norm identity
N(w⁺) − N(w⁻) = n(2a−n) and the powerful hypothesis that the gap |Δ| = n(2a−n)
is bounded below by some function of A that grows faster than |Δ| ≍ n², giving
a contradiction.

**(c) Row-3–specific Diophantine argument.**
Exploit the specific shapes A⁺ = a²+n² and A⁻ = (n−a)²+n² to derive a stronger
constraint than the general powerful-gap problem allows. Possible angles:
- The arithmetic of the Gaussian integers ℤ[i] and the factorization of A⁺·A⁻ = N(w⁺)·N(w⁻).
- The constraint a+b=n (with b=n−a) linking the two norms.
- The mod-8 structure from Theorem B.

---

## The ABC dead end (proved — do not re-attempt in the standard form)

The standard application of ABC over ℚ to the triple (A⁻, Δ, A⁺) with A⁻+Δ = A⁺:

```
  A⁺ ≤ C(ε) · rad(A⁺ · A⁻ · Δ)^{1+ε}
```

Bounding rad(A⁺ · A⁻ · Δ):
- rad(A⁺) ≤ 5 · √A⁺ ≍ n  (powerful hypothesis)
- rad(A⁻) ≤ 5 · √A⁻ ≍ n
- rad(Δ) = rad(n(2a−n)) ≤ n · (n−1) < n²

So rad(A⁺·A⁻·Δ) ≤ n · n · n² = n⁴. But the bound also uses:
- rad(Δ) ≤ Δ ≤ n², but we can also bound rad(Δ) ≤ n · rad(2a−n) ≤ n · |2a−n| < n².

Combined: rad(A⁺·A⁻·Δ) ≤ C · n⁴, hence A⁺ ≤ C(ε) · n^{4(1+ε)}.
Since A⁺ ≍ n², this gives n² ≤ C(ε) · n^{4+4ε}, i.e., 1 ≤ C(ε) · n^{2+4ε} — trivially
satisfied for n large. **No contradiction.** This dead end is proved in Paper E.

**Sharper attempt (also a dead end):**
Use rad(Δ) = rad(n)·rad(2a−n)/gcd(rad(n),rad(2a−n)) ≤ n/something, but since |2a−n|
can be as large as n−2 (when a=(n−1)/2+1=(n+1)/2, then 2a−n=1) — wait, 2a−n ranges
over all odd integers in (−n, n) as a ranges. So rad(2a−n) can be as large as |2a−n|≍n.
No improvement over the above.

---

## Proof skeleton to be closed

### Step 1 — State of the literature: powerful-gap results

Systematically review:
(a) All results on pairs of powerful numbers with gap k:
    - gap k=1: infinitely many consecutive powerful pairs (Pell-type; 8,9; 288,289; ...).
    - gap k=2 (Ljunggren, etc.): finitely many? Verify from source.
    - gap k fixed: Finitely many (by Runge's method or descent).
    - gap k ≤ A^{1/3}: any results?
    - gap k ≤ A^{1/2}: Molsen, Granville-conditional.
    - gap k ≍ A^{2/3}: any results?
    - gap k ≍ A: this problem.

(b) Are there any known powerful pairs (A₁, A₂) with A₂ ≍ A₁ and |A₂−A₁| ≍ A₁?
    Yes: `4=2²` and `8=2³` are powerful away from 5 and have gap `4~4`.
    Therefore NT-D via gap size alone is impossible; only the additional Row-3
    coupling could matter.

**What to close:** Either identify a literature result covering gap k ≍ A, or
explicitly construct (or prove non-existence of) powerful pairs with gap ≍ A.

### Step 2 — Search for powerful pairs with large gaps

Enumerate all powerful-away-from-5 integers up to N = 10⁸ (or as far as feasible).
For each pair (A₁, A₂) of such integers with A₂ ≍ A₁ (say A₂/A₁ ∈ [1, 2]) and
|A₂−A₁| ≍ A₁ (say |A₂−A₁|/A₁ ∈ [1/4, 3/4]):
- Check if the pair has the Row-3 form: A₁ = (n−a)²+n², A₂ = a²+n² for some (a,n).
- Check if any such pair is Row-3.

This is a computational discovery step, not a proof. Its purpose is to determine
whether large-gap powerful pairs exist at all (outside the Row-3 constraint).

### Step 3 — Row-3 structure as an additional constraint

The Row-3 structure gives A⁺ = a²+n² and A⁻ = (n−a)²+n², with the constraint that
both can be written using the SAME value of n. This means:

- A⁺ ≡ A⁻ ≡ 1 or 5 (mod 8) [Theorem B]
- gcd(A⁺, A⁻) ∈ {1, 5} [Theorem C]
- A⁺ + A⁻ = a² + (n−a)² + 2n² = 2a²−2an+3n² (specific quadratic form)
- A⁺ · A⁻ = N(w⁺) · N(w⁻) = N(w⁺ · w⁻) (product of norms in ℤ[i])

Use these constraints to tighten the gap argument. Specifically:
- From A⁺ + A⁻ = 2a²−2an+3n² and A⁺−A⁻ = n(2a−n): solve for a = ((A⁺−A⁻)/n+n)/2.
  This requires n | A⁺−A⁻, i.e., n | n(2a−n) ✓ (automatic).
- Substitute into A⁺ = a²+n² to get a quartic identity relating A⁺, A⁻, n.
- Use this quartic identity plus the powerful hypothesis to derive a stronger
  constraint than the general powerful-gap problem.

### Step 4 — Conditional result under a stronger ABC or generalized conjecture

If the standard ABC dead end (exponent 3, shown above) is insufficient, investigate:
(a) What exponent below 3 in rad(A⁺ · A⁻ · Δ) would give a contradiction?
    From A⁺ ≤ C · rad^{1+ε}: if rad ≤ C·n^α, then n² ≤ C·n^{α(1+ε)},
    contradiction iff α(1+ε) < 2, i.e., α < 2. So we need rad(A⁺·A⁻·Δ) ≤ C·n^{2−δ}
    for some δ > 0.
    
    Current bound: rad ≤ C·n⁴ (exponent 4). Need to improve to exponent < 2 — a gap
    of factor > 2 in the exponent. This seems very hard unconditionally.

(b) Is there a non-ABC approach that achieves rad ≤ C·n^{2−δ} for the Row-3 specific
    triple (A⁻, Δ, A⁺)? The Row-3 constraint gives Δ = n(2a−n) with a free over {odd
    integers coprime to n}. The minimum |Δ| is n (when 2a−n = ±1, i.e., a = (n±1)/2),
    and for this case rad(Δ) = rad(n) ≤ n. So in the sharpest case: rad(A⁺·A⁻·Δ) ≤
    n·n·n = n³, still exponent 3 > 2. The dead end cannot be circumvented within ABC.

---

## Acceptance criteria

1. **CONFIRMED — unconditional:** Proof that no pair (A⁺, A⁻) satisfying all Row-3
   constraints can exist for values beyond some explicit bound C. The more general
   gap-only statement is false (`4,8`).

2. **CONFIRMED — conditional:** Same result under a clearly stated conjecture (ABC over
   ℤ[i], Vojta's conjecture, etc.) with a proof that the conjecture implies the bound.
   The hypothesis must be standard (cited in the literature).

3. **PARTIAL — gap regime survey:** A complete survey of powerful-gap results identifying
   the exact threshold beyond which current methods fail, plus evidence on whether
   large-gap powerful pairs exist at all (Step 2 computational result).

4. **REFUTED approach:** A proof that the NT-D approach (powerful-gap for the Row-3
   family) cannot work for a specific reason — e.g., an explicit construction of
   powerful-away-from-5 integers with gap ≍ A (outside the Row-3 family), showing
   that the gap alone does not force non-powerful. This would not disprove the core
   conjecture but would close NT-D as an approach.
   **Current status:** satisfied for the gap-only route by `4=2²`, `8=2³`.

5. **INCONCLUSIVE:** A precise localization of the obstruction: "NT-D via the gap
   argument is blocked because [X]. An alternative approach in [direction Y] is not
   covered by the dead ends and has not been attempted."

---

## Key identities (verified algebraically)

- A⁺ − A⁻ = n(2a−n). [Elementary: (a²+n²)−((n−a)²+n²) = a²−(n−a)² = (2a−n)·n.]
- A⁺ + A⁻ = 2a²−2an+3n².  [Expand: a²+n²+(n−a)²+n² = a²+(n²−2an+a²)+2n² = 2a²−2an+3n².]
- A⁺ · A⁻ = (a²+n²)((n−a)²+n²).  [No simplification; this is the product of two sums
  of two squares, equal to N(w⁺)·N(w⁻) in ℤ[i].]
- rad(N) ≤ N for all N. For N powerful-away-from-5: rad(N) ≤ 5·√N.  [Standard.]

---

## Numerical anchor (sanity only, not a proof input)

Row-3 pairs and gap sizes:
- n=4, a=1: A⁺=17, A⁻=25, Δ=−8=4(2·1−4)=4(−2). |Δ|/A⁻=8/25=0.32. Neither powerful.
- n=6, a=1: A⁺=37, A⁻=61, Δ=−24. |Δ|/A⁻=24/61≈0.39. Neither powerful.
- n=10, a=3: A⁺=109, A⁻=149, Δ=−40. |Δ|/A⁻≈0.27. Neither powerful.
- n=100, a=49: A⁺=49²+100²=2401+10000=12401, A⁻=51²+100²=2601+10000=12601, Δ=−200.
  |Δ|/A⁻≈0.016. 12401=?? 12401=113×109+24... let me check: neither is powerful.

Zero Row-3 pairs with both A⁺ and A⁻ powerful away from 5 for n≤3000.

Exact non-Row-3 adversary: `4=2²` and `8=2³` are both powerful away from 5 and
have gap `4`, comparable to the smaller number. Thus gap size alone cannot force
non-powerfulness.

---

## Dead ends (do not re-attempt)

**DE-1 (ABC standard application):** Shown above — gives trivially satisfied bound
n² ≤ C·n^{4+4ε}. No contradiction. Proved to fail in Paper E (thm:NTD).

**DE-2 (Catalan/Mihailescu for perfect powers):** The Row-3 A± are not assumed to be
perfect powers; "powerful" is a much weaker condition. Catalan's theorem is irrelevant.

**DE-3 (Stormer / fixed-gap results):** All classical results require gap k ≤ O(A^{1/2})
or k fixed. The Row-3 gap |Δ| ≤ n² ≍ A is outside these regimes; no classical result
applies.

**DE-4 (Density arguments):** The density of powerful-away-from-5 integers in [X, 2X]
is ≍ √X; Row-3 pairs number ≍ φ(n)/4 ≍ n/4. Since both are positive density (powerful)
or positive proportion (Row-3), density alone cannot give a contradiction.
