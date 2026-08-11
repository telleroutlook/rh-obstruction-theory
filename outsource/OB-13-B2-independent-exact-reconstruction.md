# Problem OB-13 — B2: independent exact-arithmetic reconstruction of the finite-observation collision

**Type:** computational verification (exact rational arithmetic; independent
reconstruction from raw parameters, not from producer summaries)

**Non-circularity:** RH is not assumed. All inputs are explicit rational numbers and
elementary test functions. No zeta zero, Euler product, or functional equation of ζ is
used. This task asks a reviewer to **independently recompute** a finite algebraic
identity from scratch (their own code, their own arithmetic) and either reproduce the
claimed exact collision or find a discrepancy.

**Why this task exists (computational-axis gate).** The repository's evidence ledger
requires, for a finite certificate, an *independent* exact/interval replay and
cross-implementation agreement — not a re-run of the producer's own script. The B2
theorem's finite collision has so far only been checked by the producer and by one
referee (OB-02). This task requests a genuinely independent reconstruction, in a
different computer-algebra environment, of the exact identity.

---

## All definitions (self-contained — everything is here)

### Test functions (Li-type)

For `j = 1, 2, …, m`, the Li-type test function is
```
φ_j(ρ) = 1 − (1 − 1/ρ)^j.
```

### On-line contribution matrix C

For a height `t > 0`, the on-line pair is `L(t) = {1/2 + it, 1/2 − it}`. The
observation of one copy of `L(t)` under test `φ_j`, using the symmetric-summation
convention
```
O_j(L(t)) = φ_j(1/2+it) + φ_j(1/2−it) + φ_j(1−(1/2+it)) + φ_j(1−(1/2−it)),
```
reduces (since `1 − (1/2+it) = 1/2 − it` and `1 − (1/2−it) = 1/2 + it`) to
```
O_j(L(t)) = 2[φ_j(1/2+it) + φ_j(1/2−it)] = 4 Re φ_j(1/2 + it).
```
A closed form (to be verified by the reviewer, not assumed): with
`x = x(t) := (4t² − 1)/(4t² + 1)` and `T_j` the degree-j Chebyshev polynomial of the
first kind,
```
O_j(L(t)) = 4(1 − T_j(x(t))).
```
Define the m×m matrix, for chosen distinct heights `t_1, …, t_m > 0`:
```
C_{jk} := O_j(L(t_k)) = 4(1 − T_j(x(t_k))),   j,k = 1,…,m.
```

### Off-line quartet contribution d(T)

The off-line symmetric quartet at abscissa `σ₀ = 3/4` and height `T > 0` is
`Q(3/4, T) = {3/4 + iT, 3/4 − iT, 1/4 + iT, 1/4 − iT}`. Its observation under `φ_j`
(the four points already form a full symmetric orbit) is
```
d_j(T) := O_j(Q(3/4,T)) = 4 Re[φ_j(3/4 + iT) + φ_j(1/4 + iT)].
```

### The collision identity

Given rational `t_1,…,t_m`, rational `T`, one computes:
1. `C ∈ ℚ^{m×m}` and `d(T) ∈ ℚ^m` (both rational, since `φ_j` are rational functions
   evaluated at points with rational real/imaginary parts, and `Re` of a rational
   complex number is rational).
2. `β := −C^{-1} d(T) ∈ ℚ^m` (requires `det C ≠ 0`).
3. `R :=` least common multiple of the denominators of `β_1, …, β_m` (a positive
   integer); `n := R·β ∈ ℤ^m`.
4. `M := max_k |n_k|` (nonneg-multiplicity buffer).

The two multisets are
```
𝒵_+ := ⊔_{k=1}^m  M · L(t_k),
𝒵_− := (⊔_{k=1}^m (M + n_k) · L(t_k)) ⊔ R · Q(3/4, T).
```
The claimed **exact collision** is: for every `j = 1,…,m`,
```
O_j(𝒵_−) − O_j(𝒵_+) = Σ_{k=1}^m n_k · C_{jk} + R · d_j(T) = 0.      (COLLISION)
```
Equivalently, in vector form, `C n + R d(T) = 0` in `ℚ^m`.

---

## The claim to be verified

**Claim (exact reconstruction).** Implement the pipeline above **independently** (your
own exact-rational code, not the repository's) and verify:

- **(V1)** For `m = 2`, `t_1 = 1`, `t_2 = 2`, `T = 1`, `σ₀ = 3/4`, Li tests `j = 1, 2`,
  the exact values are:
  ```
  x(1) = 3/5,   x(2) = 15/17,
  C = [[8/5,   8/17],
       [128/25, 512/289]],           det C = 3072/7225,
  d(1) = [1216/425,  1763072/180625],
  β = [−1426/1275,  −854/375],
  R = 6375,   n = [−7130, −14518],   M = 14518,
  C n + R d(1) = [0, 0]   (exactly).
  ```
  Reproduce every one of these rational numbers exactly, or report the first that
  differs.

- **(V2)** Multiplicity nonnegativity: confirm `M + n_1 = 7388 ≥ 0` and `M + n_2 = 0 ≥ 0`,
  so `𝒵_−` has valid nonnegative integer multiplicities.

- **(V3)** Predicate values: confirm `P(𝒵_+) = 1` (all atoms on `Re = 1/2`) and
  `P(𝒵_−) = 0` (`Q(3/4,T)` has atoms at `Re = 3/4 ≠ 1/2`).

- **(V4)** A second, independent instance to guard against a lucky coincidence: choose
  your own distinct rational heights and rational T (e.g. `m = 3`, `t = (1, 2, 3)`,
  `T = 2`), recompute `C, d, β, R, n, M`, and verify `C n + R d(T) = 0` exactly. Report
  the full rational data so a third party can re-check.

- **(V5)** Adversarial mutation (falsification guard): perturb one entry — e.g. replace
  `n_1` by `n_1 + 1` — and confirm the collision identity then FAILS (nonzero residual).
  This checks that the identity is not trivially satisfied by construction bugs.

---

## Proof skeleton to be closed (verification steps)

### Step 1 — Recompute C and d(T) from the definitions (V1)
Independently derive `O_j(L(t))` and `d_j(T)` — do NOT assume the Chebyshev closed form;
compute `4 Re φ_j(1/2 + it_k)` directly from `φ_j(ρ) = 1 − (1−1/ρ)^j` in exact rational
complex arithmetic, then separately check it equals `4(1 − T_j(x(t_k)))`. Report both and
confirm they agree.

**Acceptance:** the two computations of C agree exactly, and match the V1 table (or the
first discrepancy is reported).

### Step 2 — Solve and scale (V1, V2)
Compute `β = −C^{-1} d(T)` in exact rationals, form R and n, verify `C n + R d = 0`, and
check the nonnegativity buffer.

**Acceptance:** exact reproduction of β, R, n, M, and the zero residual; or first
discrepancy.

### Step 3 — Second instance + mutation (V4, V5)
Repeat for an independently chosen instance and run the adversarial mutation.

**Acceptance:** exact zero residual for the honest instance; nonzero residual for the
mutated one.

---

## Acceptance criteria

1. **CONFIRMED:** all of V1–V5 reproduced exactly in an independent exact-rational
   implementation; the m=2 table matches to the last digit; the second instance also
   gives an exact zero; the mutation gives a nonzero residual. Report the code
   environment used (language + exact-arithmetic library) so the check is itself
   reproducible.

2. **DISCREPANCY:** one or more of the V1 rational values does not reproduce; report the
   exact computed value, the definitional step where it diverges, and whether the
   collision identity `C n + R d = 0` still holds with the corrected values (i.e., is it
   a typo in the anchor, or a genuine error in the construction?).

3. **DEGENERATE:** if `det C = 0` for the stated heights (which would make β undefined),
   report it — this would indicate the Jacobian full-rank claim fails for these specific
   heights.

All outcomes are decisive. A CONFIRMED here provides the independent
cross-implementation agreement the evidence ledger requires for the B2 finite
certificate; it does NOT validate any analytic statement beyond the finite identity
replayed (per the repository rule that a finite certificate validates only the finite
statement).

---

## Numerical anchor (sanity only — this IS the object to reconstruct)

Unlike other problems, here the numerical content is the deliverable, not a side sanity
check. The single scalar sanity value a reviewer can eyeball first:
```
O_1(L(1)) = 4(1 − T_1(3/5)) = 4(1 − 3/5) = 8/5 = 1.6.
```
and
```
d_1(1) = 4 Re[φ_1(3/4+i) + φ_1(1/4+i)]
       = 4 Re[(1/(3/4+i)) + (1/(1/4+i))]      (since φ_1(ρ)=1−(1−1/ρ)=1/ρ)
       = 4[ (3/4)/((3/4)²+1) + (1/4)/((1/4)²+1) ]
       = 4[ (3/4)/(25/16) + (1/4)/(17/16) ]
       = 4[ 12/25 + 4/17 ] = 4·(204+100)/425 = 1216/425.
```
These two rationals (8/5 and 1216/425) are the quickest first-line sanity checks; the
full V1 table is the actual reconstruction target.
