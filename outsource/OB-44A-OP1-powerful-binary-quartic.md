# Problem OB-44A — Powerful values of an explicit binary quartic on the Row-3 family

> **SEND STATUS: SUPERSEDED — do not send.** The sharper focused replacement is
> `OB-46-OP1A-simultaneous-gaussian-powerful.md`, which isolates the shifted
> Gaussian-powerful core and the exact `5`-adic branch.

**Type:** arithmetic / algebraic number theory (powerful values, squarefree values,
Gaussian integer factorization)

**Non-circularity.** This is a purely finite arithmetic problem. It does not assume
RH, an RH-equivalent criterion, a zero of `ζ`, an L-value, a fitted zero ordinate,
or any analytic zero-counting input. RH stays `[OUT]`.

This problem is the sharp number-theoretic core of OP1's odd-carrier route. A full
proof would show that every relevant orbit has a simple carrier prime. A partial
result, explicit counterexample, or precise proof strategy is also valuable.

---

## 1. All definitions

An integer `N ≥ 2` is **powerful** if every prime `p | N` satisfies `p² | N`;
equivalently, `N` can be written as `u² v³` with positive integers `u,v`.
For a prime `p`, `v_p(N)` denotes the exponent of `p` in the prime factorization
of `N`.

Fix integers `a,n` satisfying the following **Row-3 conditions**:

```
n is even and n≥4;
3 ∤ n;
a is odd and 1≤a<n;
gcd(a,n)=1.
```

Define

```
r = a² + n² − na,
N(a,n) = r² + n⁴
        = (a²+n²−na)² + n⁴.
```

Also define the Gaussian integer

```
z = r + n² i ∈ Z[i].
```

Three auxiliary Gaussian representations are useful. Put

```
w = a+n i,
w_- = w−n=(a−n)+n i.
```

Then

```
M = w w_- = (a²−n²−na) + n(2a−n)i,
z = conjugate(w) w_- = r+n² i,
g = gcd(Re M, Im M),
M' = M/g.
```

The following identities hold:

```
N(a,n) = |z|² = |M|²
        = |w|² |w_-|²
        = (a²+n²)((a−n)²+n²).
```

The gcd `g` lies in `{1,5}`; see §3 below.

---

## 2. The problem to be solved

> **Problem A.** Prove that for every Row-3 pair `(a,n)`, the integer
> `N(a,n)` is not powerful. Equivalently, prove that there exists a rational
> prime `p` with
> ```
> v_p(N(a,n)) = 1.
> ```

An equivalent Gaussian formulation is:

> Show that `z = r+n² i` is not a powerful Gaussian integer; i.e. some Gaussian
> prime divides `z` with multiplicity exactly one.

Because `gcd(r,n)=1`, the rational prime factors of `r²+n⁴` are either `2` or
`1 mod 4`. The Row-3 parity conditions exclude `2`, so every rational prime
divisor is `1 mod 4`.

---

## 3. What has already been checked or proved

The following facts are elementary and may be used freely:

1. If `ℓ | n`, then `r ≡ a² mod ℓ`; since `gcd(a,n)=1`, `ℓ ∤ r`. Hence
   `gcd(r,n)=1`.
2. Therefore `z=r+n²i` has coprime real and imaginary parts.
3. A sum of two coprime squares has no rational prime factor `3 mod 4`.
4. The displayed identity `N=|M|²` is a polynomial identity.
5. The rational factors
   ```
   A_+(a,n)=a²+n²,
   A_-(a,n)=(a−n)²+n²
   ```
   have gcd `1` or `5`. A common prime divisor `p` cannot divide `n`; then
   `p | n(2a−n)` forces `p | 2a−n`, so `n≡2a mod p` and
   `A_+≡5a² mod p`. Since `p∤a`, this gives `p=5`; the same congruence
   modulo `25` shows the common power is at most `5`.
6. The gcd `g=gcd(Re M,Im M)` is `1` or `5`. Indeed, a prime `ℓ|n` cannot
   divide `Re M` because `Re M≡a² mod ℓ`. If a prime `q∤n` divides both
   coordinates, then `q|(2a−n)`, so `n≡2a mod q` and
   `Re M≡−5a² mod q`; since `q∤a`, this forces `q=5`. The same congruence
   modulo `25` shows the power of `5` is at most one.

An exact scan of the finite box

```
4 ≤ n < 360, n even, 3∤n, 1 ≤ a < n, a odd, gcd(a,n)=1
```

contains `9856` Row-3 pairs. Exact factorization found:

```
0 powerful values N(a,n),
```

and `0` values with no simple prime factor. These searches are evidence only
and are not premises.

An external reply reported the same factorization and gcd reduction, a direct
scan with `0/75840` powerful values for `n<1000`, and `0` simultaneous
powerful-away-from-5 pairs among approximately `7.6 million` pairs for `n<10000`.
The larger external scan is not a premise. Local exact replays in
`checker/ob44a_factorization_scan.py` have confirmed the factorization,
`gcd∈{1,5}`, `0/75840` through `n<1000`, and `0/1898236` through `n<5000`;
each scan also has `0` simultaneous powerful-away-from-5 pairs.

Thus, in this finite box, the simple-carrier existence rate is

```
9856 / 9856 = 100%,
```
and the stronger deposited scan through `n<5000` shows that any counterexample
must have `n ≥ 5000` (under the restriction `1≤a<n`). These are only lower
bounds on the least possible counterexample; they are not premises.

### Known dead ends

Do not re-derive these stronger false claims:

1. The valuation pattern of every `p | N` is not uniform; split primes with
   high valuation can fluctuate.
2. The statement “`N` is squarefree” is stronger than needed and may be harder.
   Only one simple prime factor is required.
3. A generic squarefree-values theorem for arbitrary quartics need not apply
   directly; check primitivity, irreducibility, and local sieve hypotheses
   explicitly before invoking one.

### Structural obstacles a strategy must confront

The polynomial is not a generic irreducible binary quartic. Over `Q(i)` it is
a norm-type form, and for fixed `n` its roots in `a` lie in an abelian quadratic
extension. Consequently:

1. an irreducible-form squarefree-values theorem does not apply verbatim;
2. a Chebotarev-based equidistribution argument has very small Galois group to
   exploit;
3. the binary-parametric family is stronger than a one-variable powerful-values
   question.

For these reasons, a valid STRATEGY must say which obstacle it bypasses. It is
not sufficient to name a general squarefree sieve.

### Recommended Gaussian-integer strategy shape

The most promising route is not to treat `N` as an arbitrary quartic. Use

```
N=|w|²|w−n|²,       gcd(a²+n²,(a−n)²+n²)∈{1,5}.
```

Since prime divisors of the two rational factors are disjoint away from `5`,
the exact criterion is:

```
N is powerful
 ⟺ A_+ and A_- are both powerful away from 5
     and v_5(A_+)+v_5(A_-)≠1.
```

Thus the **hard case** is that both

```
a²+n²
(a−n)²+n²
```

are powerful away from `5`. Equivalently, work with the two coprime Gaussian
factors `w` and `w−n`; away from the split primes over `5`, both would have to
be Gaussian-powerful. This simultaneous-shift formulation is the recommended
target.

One may also use the primitive Gaussian integer `M'=M/g`, for which
`N=g²|M'|²`. Problem A is equivalent to showing that `M'` is not powerful in
`Z[i]`, but the two-factor `w,w−n` reduction is more structural.

If `M'` were powerful, since `Z[i]` is a UFD, one could write

```
M' = unit · κ² · λ³
```

for Gaussian integers `κ,λ`. A strategy should either:

1. prove a primitive-divisor theorem for one of the explicit sequences
   `w=a+ni` or `w−n=(a−n)+ni`, or identify the precise existing primitive-divisor
   tool that applies; or
2. prove that the horizontally shifted Gaussian integers `w` and `w−n` cannot
   both be powerful away from the primes over `5`; or
3. invoke a published squarefree/powerful-values theorem, but only after stating
   its exact hypotheses and verifying them for this form.

Route (3) must include theorem number and scope; a generic reference to the
squarefree-values literature is not an acceptable STRATEGY outcome.

Route (1) is listed first because a primitive prime divisor outside a fixed
finite set would handle both failure modes in the exact criterion: either one
factor has a non-5 simple prime, or the only simple prime is `5` and
`v_5(A_+)+v_5(A_-)=1`. Route (2) must also account for the latter `5`-adic
branch explicitly.

---

## 4. Acceptance criteria

Return exactly one of the following.

1. **CONFIRMED.** A proof that `N(a,n)` is never powerful on the full Row-3
   family.

2. **PARTIAL.** A proved non-powerful result for a genuine infinite subfamily,
   all but finitely many pairs, or a positive-density subfamily. State the
   exact subfamily and density convention.

3. **REFUTED.** An explicit Row-3 pair `(a,n)` for which `N(a,n)` is powerful.
   Give the exact factorization.

4. **STRATEGY.** A concrete proof plan, naming the intended tool:
   - squarefree/powerful-value sieve;
   - Gaussian integer factorization/descent;
   - parametrization of powerful values of binary quartics;
   - abc-type or determinant-method conditional route.

   The strategy must identify which sublemmas are standard, which are new, which
   structural obstacle above is bypassed, and the most likely failure point.

5. **INCONCLUSIVE.** A precise localization of why current technology does not
   apply, including the exact missing hypothesis.

---

## 5. Numerical anchor (sanity only, not a proof input)

Take `a=1`, `n=10`. Then

```
r = 1 + 100 − 10 = 91,
N = 91² + 10⁴
  = 8281 + 10000
  = 18281
  = 101 · 181.
```

Both prime factors occur with exponent `1`, so this anchor is non-powerful.
Also

```
M = (1−100−10) + 10(2−10)i = −109 − 80i,
|M|² = 109² + 80² = 18281.
```

The anchor was checked by exact integer arithmetic; it is not an input to a proof.

---

## Pre-send lint record

| PROMPT_LINT item | Result |
|---|---|
| L1–L4 | N/A: no entire function, order, zero/pole, or canonical-product claim. |
| L5 | PASS: no RH or zero-location input; “Row-3” is only a parity/coprimality family name. |
| L6 | PASS: full proof, partial infinite family, explicit counterexample, strategy, and inconclusive outcomes are all non-vacuous. |
| L7–L16 | PASS/N/A as applicable: no analytic-growth, zero-location, or representation-invariant claim is made. The norm-type structure and small Galois group are now explicitly listed as strategy obstacles rather than silently ignored. |
| L17 | PASS: no cited black box is assumed; a strategy may propose one but must state its exact scope. |
| L18 | PASS: exact integer anchor is labeled sanity only. |
| L19 | PASS: STRATEGY, PARTIAL, REFUTED, and INCONCLUSIVE are first-class. |
| L20–L24 | N/A. |
| Self-containment | PASS: `a`, `n`, `r`, `N`, powerful, Gaussian representations, outcomes, and anchor are defined in-file. |
| Privacy | PASS: no personal path, username, company, or internal host occurs. |
| Execution record (2026-08-17) | PASS: required sections present; even code-fence parity; external repository dependency grep empty; exact anchor and deposited `n<5000` scan PASS; `git diff --check` clean at final rerun. |
