# OE-01 Solution Verdict: NT-C Square Subcase — CONFIRMED

**Problem file:** `outsource/OE-01-NT-C-gaussian-zsygmondy-row3.md`  
**Outcome:** **CONFIRMED (square subcase)**  
**Theorem:** `theorems/L-row3-zsygmondy-square/`  
**Checker:** `theorems/L-row3-zsygmondy-square/checker/verify_L.py` — all PASS

---

## 1. Verdict summary

The square subcase of NT-C (OE-01 acceptance criterion 2) is **confirmed**: there are
zero Row-3 pairs (a, n) such that both A⁺ = a²+n² and A⁻ = (n−a)²+n² are
simultaneously perfect squares. The proof uses the proof skeleton from OE-01 Steps 1–2
(Pythagorean parametrization → elliptic curve reduction) and resolves Step 2 via a
complete 2-isogeny descent establishing rank 0.

The full NT-C claim (cube-factor case, OE-01 criterion 1) remains OPEN.

---

## 2. Proof outline

**Step 1.** Pythagorean parametrization converts the simultaneous-square condition to:
find s₁,s₂ | m² with S = s₁+s₂, P = Sm²/(S+2m) ∈ ℤ, and Δ = S²−4P = □.

**Step 2.** The discriminant condition reduces to rational points on the genus-1 curve:

    C : y² = x⁴ − 3x² + 1

using the rational base point (0,1) and the substitution U=(y+1)/x².

**Step 3.** Birational equivalence transforms C to the elliptic curve:

    E : Y² = X(X+4)(X−1)   [Weierstrass: Y² = X³+3X²−4X]

with full 2-torsion E(ℚ)_tors = {∞, (0,0), (1,0), (−4,0)}.

**Step 4.** 2-isogeny descent (φ: E → E' with kernel ⟨(0,0)⟩):
- E' : Y² = X³−6X²+25X
- |S^φ(E)| = 2: candidates {1,−1} survive; d=2 blocked in ℚ₂ (mod-8 check)
- |S^{φ̂}(E')| = 2: candidates {1,5} survive; d=−1,−5 blocked over ℝ
- Rank formula: 2^r = 4/4 = 1 ⟹ r = 0

**Step 5.** Pullback of 4 torsion points to C gives x ∈ {0, ∞, ±√(8/3), nonreal}.
Row-3 requires x = a/(2m) ∈ (0,1) ∩ ℚ; none qualify. □

---

## 3. Sha: not a gap

The proof does NOT require trivial Sha.  The combined 2-isogeny descent bound gives:

    dim_{F₂}(E(Q)/2E(Q)) ≤ dim S^φ + dim S^{φ̂} = 1 + 1 = 2

Since E(Q)[2] ≅ (Z/2Z)² (four 2-torsion points), dim_{F₂}(E(Q)/2E(Q)) = r + 2.
Therefore r + 2 ≤ 2, giving r = 0 unconditionally.  No Sha triviality is assumed.

This was confirmed by running `theorems/L-row3-zsygmondy-square/checker/verify_L.py`
(all five checks PASS: torsion points, pullback irrationality, numerical sweep n≤2000,
d=2 local obstruction mod 8, d=5 Selmer solution).

The status PROOF-DRAFT is retained pending an *independent human* check of the analytic
steps, not pending a CAS oracle.

---

## 4. Remaining open problem

The full NT-C (OE-01 criterion 1, cube factors s²t³ with t≥2) remains open.
The growing-S Evertse obstacle (OE-01 Step 3, DE-2) has not been circumvented.
OE-01 remains active for the full powerful case.
