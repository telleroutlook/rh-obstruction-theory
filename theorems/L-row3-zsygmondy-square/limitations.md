# Limitations of Theorem L

## What is proved
Theorem L proves: for every Row-3 pair (a,n), it is impossible that BOTH
A⁺ = a²+n² AND A⁻ = (n−a)²+n² are simultaneously **perfect squares**.

## What is NOT proved (primary limitation)

### L1 — NT-C full case (cube factors) is OPEN
The full NT-C claim requires: at least one of A⁺, A⁻ is NOT powerful-away-from-5
(every prime p≠5 dividing it appears to ≥2nd power). Powerful numbers include
s²t³ with cube factor t≥2. Theorem L only handles t=1 (square case).

The cube-factor case: A⁺ = 5^{e}·s²·t³ (t>1) requires the Gaussian S-unit analysis
of OE-01 Step 3, which remains blocked by growing-S Evertse obstacle. NT-C full
proof requires new tools (see OE-01).

### L2 — Sha: not a gap in the rank proof

The proof does NOT require trivial Sha. The rank-0 conclusion follows from the
dimension bound alone (no Sha assumption needed):

- dim_{F₂}(E(Q)/2E(Q)) = r + t₂  where r = rank and t₂ = dim_{F₂} E(Q)[2] = 2
  (since E(Q)[2] = {O,(0,0),(1,0),(−4,0)} ≅ (Z/2Z)²).
- The combined 2-isogeny descent gives: dim E(Q)/2E(Q) ≤ dim S^φ + dim S^{φ̂} = 1+1 = 2.
- Therefore r+2 ≤ 2, giving r ≤ 0, i.e., r = 0. □

No Sha triviality is assumed. The former note about a Sha gap was incorrect.

### L3 — Square subcase does not cover the full NT-C symmetry
NT-C states: at least one of w⁺ = a+ni or w⁻ = (a−n)+ni has a Gaussian prime
𝔭 ∤ 5n to exactly first power. Theorem L rules out the case where v_p(A⁺) is odd
AND A⁺ is a perfect square. It does not rule out A⁺ = 5^e·m² with e odd (5 to an
odd power times a square), because such A⁺ is powerful-away-from-5 (5 contributes
the only odd prime factor).

**However:** since gcd(A⁺, A⁻) ∈ {1,5} (Theorem C), and 5^e·m² has 5|A⁺, the
5-contribution to gcd is bounded. The case e odd is handled separately via the
5-adic analysis of Theorem C. Theorem L handles the sub-case where the 5-part
is a perfect square (e even, or 5∤A⁺).

### L4 — Not a proof of NT-C for the full Row-3 powerful problem
NT-C implies: for every Row-3 pair (a,n) with n>C, both A⁺ and A⁻ cannot
simultaneously be powerful-away-from-5. Theorem L proves the weaker statement
(no simultaneous perfect squares, ever). The "ever" vs "for n>C" distinction is
immaterial here since Theorem L holds for ALL n, not just large n.

## Summary table

| Claim | Status |
|---|---|
| No simultaneous perfect squares (Theorem L) | PROOF-DRAFT (complete; pending independent check) |
| NT-C square subcase (no simultaneous A±=x²) | Equivalent to Theorem L above |
| NT-C full case (no simultaneous powerful A±) | OPEN — cube factor case unresolved |
| NT-C implies OP1-A | Not implied; OP1-A is a different (stronger) simultaneous condition |
