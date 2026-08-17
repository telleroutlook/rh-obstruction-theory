# OE-04 Review Record — NT-D Corrected Analysis

**Date:** 2026-08-17
**Status:** PARTIALLY VALID SETUP; STEP 5 CONTAINS KNOWN BARRIER
**NT-D status:** GAP-ONLY ROUTE REFUTED; ROW-3-SPECIFIC CORE REMAINS OPEN

## Update (2026-08-17): second geometric/Vojta submission — REJECTED

The second submission's symmetric quartic identity is correct, but it does not close
NT-D. Its square-case elliptic proof switches between non-isomorphic models and does
not supply a complete descent. For fixed cube factors, the system is a genus-one
intersection of quadrics, not a genus>1 curve; Darmon-Granville and Vojta are invoked
outside a source-verified scope.

Salvaged exact outcome: `4=2^2` and `8=2^3` are powerful away from 5 and have gap
`4~4`, so OE-04's gap-only route is refuted. This does not produce a Row-3 pair and
does not affect the core conjecture. Full audit:
`outsource/solutions/OE-04-geometric-feedback-review.md`.

---

## Submission summary

"Corrected Analysis and Proof Structure for Problem OE-04 (NT-D)":
1. Identifies and corrects the "square assumption fallacy" from a prior (wrong) attempt
2. Sets up the Gaussian ideal-theoretic framework (§1–4)
3. Claims a "Refined Proof Strategy" via Thue-Mahler / S-unit equations (§5)

---

## §1–3: Setup — VALID

The correction is genuine. The prior error was assuming A⁺ powerful ⟹ A⁺ a perfect
square. Powerful means every prime p|A⁺ has p²|A⁺; 8=2³ is powerful but not a square.
The Erdős–Szekeres decomposition A⁺ = 5^e · s² · t³ with t=1 is the square case (NT-C),
which is now proved (Theorem M). NT-D concerns the general powerful-away-from-5 case
and requires handling t≥1 cube factors — a genuinely harder problem.

The Gaussian setup with w⁺ = a+ni, w⁻ = (n−a)+ni, norms A⁺ and A⁻, and the gap
Δ = n(2a−n) is correct. The gcd constraint N(gcd(w⁺,w⁻)) ∈ {1,5} from Theorem C
is correct and useful.

---

## §4: Ideal-theoretic claim — CORRECT but gap in justification

**Claim:** For any Gaussian prime π ∤ (2+i) with π|w⁺, (π)² must divide w⁺.

**This is true, but for a reason not stated in the document.**

### The missing lemma

For a prime p≡1 mod 4 (which splits: p = π·π̄ in ℤ[i]), the "dangerous" case is the
(1,1) distribution: both π|w⁺ and π̄|w⁺ each to exponent 1. In that case v_p(A⁺) =
v_π(w⁺) + v_{π̄}(w⁺) = 2, satisfying the powerful condition — but π² does NOT divide
w⁺.

However, this case is excluded by gcd(a,n) = 1:

  If π|w⁺ AND π̄|w⁺, then π·π̄ = p | w⁺ = a+ni in ℤ[i],
  forcing p|a and p|n, i.e., p|gcd(a,n) = 1.  Contradiction.

Therefore exactly ONE of {π, π̄} divides w⁺. Its exponent equals v_p(A⁺), so the
powerful condition v_p(A⁺) ≥ 2 translates to π²|w⁺ or π̄²|w⁺. The claim holds. ✓

**The document should add this lemma explicitly.** Without it the claim appears to
confuse the condition on A⁺ (a rational norm) with a condition on w⁺ (a Gaussian integer).

### For p≡3 mod 4

p remains prime in ℤ[i], N(p)=p². If p|A⁺=N(w⁺) then p|w⁺ in ℤ[i], giving
v_p(A⁺) = 2·v_p(w⁺). The powerful condition v_p(A⁺)≥2 gives v_p(w⁺)≥1. Since p
is an associate of its own conjugate, the single-prime analysis is immediate.

---

## §5: Refined Proof Strategy — CONTAINS KNOWN BARRIER (same as OE-03)

**Claimed:** The S-unit equation ξ₊/ξ₋ = (w⁺/w⁻) has support restricted to
"primes dividing 5 and prime factors of n."

**This is false.** The support of ξ₊ consists of the Gaussian primes dividing w⁺,
i.e., the prime factors of A⁺ = a²+n² in ℤ[i]. By gcd(a,n) = 1:

  gcd(a²+n², n) = gcd(a², n) = 1

(since gcd(a,n)=1 implies gcd(a²,n)=1). Therefore A⁺'s prime factors never divide n.
The support of ξ₊ is ENTIRELY OUTSIDE S₀∪S(n) where S(n) = {rational primes dividing n}.

**Computational confirmation:** Among Row-3 pairs with n≤32, all 81 pairs have at least
one prime factor of A⁺ lying outside S₀∪S(n). Concrete examples:

  n=4,  a=1: A⁺=17 (prime),  S₀∪S(4)={2,5};  17 ∉ S
  n=8,  a=1: A⁺=65=5·13,    S₀∪S(8)={2,5};  13 ∉ S
  n=8,  a=3: A⁺=73 (prime),  S₀∪S(8)={2,5};  73 ∉ S

The Thue-Mahler approach would require bounding solutions to an S-unit equation
where S = S(A⁺,n) grows with (a,n). This is the **same barrier** identified for OE-03
(Attempt 1, 2026-08-17): effective S-unit bounds require |S| fixed, but the support
of ξ₊ depends on A⁺ and grows arbitrarily.

Baker's method also fails here for the same reason as in OE-03 Pivot 2:
|ξ₊/ξ₋ − 1| ≍ 1/n is polynomially small, not exponentially small in height.

---

## Overall verdict

| Section | Assessment |
|---|---|
| §1–3 Setup | VALID — genuine correction of the square fallacy; standard framework |
| §4 Ideal-theoretic claim | CORRECT but needs the gcd(a,n)=1 lemma to complete the proof |
| §5 Thue-Mahler strategy | CONTAINS KNOWN BARRIER — xi+ is NOT an S₀∪S(n)-unit |

**NT-D status: OPEN.** The setup in §1–4 is a useful starting framework for future
attempts, but Step 5 does not close the problem.

---

## What a genuine NT-D proof would need

The S-unit / Thue-Mahler route faces a fundamental obstacle: the prime support of
w⁺ grows with (a,n) in an uncontrolled way. Approaches that might bypass this:

1. **Geometry of numbers over ℤ[i]:** bound the size of w⁺ from the powerful condition
   without tracking individual prime factors
2. **Arithmetic geometry:** embed the powerful condition in a family of varieties and
   use Faltings / Chabauty
3. **Avoid S-unit equations entirely:** a structural argument (congruences, local
   obstructions at many primes simultaneously) might close t≥2 without Baker
4. **Uniform Thue-Mahler:** an effective result bounding solutions for FAMILIES of
   equations with growing S — currently unknown, beyond state of the art
