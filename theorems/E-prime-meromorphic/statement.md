# Statement — Theorem E' (E-prime-meromorphic)

**Theorem ID:** E-prime-meromorphic  
**Program ref:** EXT-3 (extension of Theorem E to Suzuki meromorphic target)  
**Status:** PROOF-DRAFT (E'-neg PROOF-DRAFT; E'-pos open; meromorphic Hadamard lemma needed)

---

## §1. Context

Theorem E (E-compactness) proves a non-uniqueness result (E-neg) and a sufficient
conditions theorem (E-pos) for the **CCM normalization**: the entire function
`Ξ(z) = ξ(1/2 + iz)`.

The **Suzuki normalization** targets a different object: the meromorphic function
```
W(z) = z² ξ(1/2 − iz) / ξ'(1/2 − iz),
```
which has simple poles at the Riemann zero ordinates `{γ_n}` (if they are simple zeros
of ξ) and is entire away from these poles. Suzuki Cor. 6 states: RH follows if a
certain sequence of holomorphic functions converges to W uniformly on compacts.

This theorem audits whether the E-neg non-uniqueness obstruction transfers to the
meromorphic target W.

---

## §2. Method class and observation

**Method class 𝔐_Suz.** A method `P ∈ 𝔐_Suz` constructs a sequence of meromorphic
functions `(F_n)` satisfying finite evidence `ℰ_N^{mer}`:
- meromorphic of order 1;
- poles contained in the upper half-plane with imaginary parts approximating `{γ_n}`;
- real on `ℝ`;
- normalization condition matching `W` at one point;
- first `J_N` Taylor coefficients at a non-pole point matching `W`.

**Target predicate.** `(F_n) → W` locally uniformly on `ℂ \ {poles}`.

---

## §3. Meromorphic Hadamard uniqueness (the key lemma — PROOF-DRAFT)

**Lemma E'.1 (meromorphic Hadamard uniqueness).** Let `F`, `G` be meromorphic functions
of order 1, with the same multiset of poles `{p_k}` (with multiplicities) and the same
multiset of zeros `{z_j}` (with multiplicities), and with `F(w₀) = G(w₀) ≠ 0` at some
non-pole point `w₀`. Then `F = G`.

*Proof sketch.* Write `F = P/Q` and `G = P'/Q'` where `P, P'` are entire (numerators,
zeros of F and G) and `Q, Q'` are entire (denominators, poles of F and G). Same poles
means `Q = Q'` up to a constant; same zeros means `P = P'` up to a constant. The
normalization `F(w₀) = G(w₀)` pins the ratio. ☐

*Status: PROOF-DRAFT.* The Weierstrass/Mittag-Leffler product for meromorphic functions
of order 1 is classical (Titchmarsh 'Theory of Functions' §8.7); the uniqueness
statement above is a direct consequence. Needs a precise citation by theorem number.

**Consequence for E'.** If two sequences `(F_n)` and `(G_n)` in `𝔐_Suz` converge
locally uniformly to limits `F∞`, `G∞` and both limits have the same poles, zeros, and
value at `w₀`, then `F∞ = G∞` — the limit is unique if the pole/zero data is fixed.

The non-uniqueness (E'-neg) arises when the **finite evidence** `ℰ_N^{mer}` does NOT
fix the pole positions precisely — i.e. the pole locations of `F_n` match `{γ_n}` only
approximately, not exactly.

---

## §4. Theorem E'-neg (non-uniqueness for meromorphic target, PROOF-DRAFT)

**Statement.** For any `ε > 0` and any `N`, there exists a meromorphic function `F ≠ W`
satisfying all conditions of `ℰ_N^{mer}` with:
```
sup_{|z| ≤ R₀, z not near a pole} |F(z) − W(z)| ≥ ε
```
for some `R₀ = R₀(N, ε)`.

*Proof strategy (same template as E-neg §3).*
1. Perturb tail poles: `p_n^{(c₀)} = γ_n + c₀/(n − k_N)` for `n > k_N`.
2. Match first `J_N` Taylor coefficients at a base point (off the poles) via
   a meromorphic Vandermonde/implicit-function argument (same Jacobian structure
   as E-neg §3, but for the partial-fraction coefficients of the meromorphic function).
3. Quantify separation: the perturbed and unperturbed meromorphic functions differ
   on a disk by an amount controlled by `|W(Ri)|` growth — the same Hadamard product
   growth argument as E-neg, but for the numerator `ξ` of `W`.
4. Conclude via `|W(Ri)| → ∞` as `R → ∞` (same Hadamard product lower bound
   `∏_n(1 + R²/γ_n²) ≥ 2^N` with `N ∼ R log R / (2π)`).

*Meromorphic IFT Jacobian (explicit — PROOF-DRAFT).*

Write `W` and the perturbed function `F^{(c₀)}` in partial-fraction form near a
base point `w₀` not equal to any pole:

```
W(z)          = Σ_{n≥1} R_n / (z − γ_n) + Σ_{n≥1} R_n / (z + γ_n) + E(z)
F^{(c₀)}(z)  = Σ_{n≥1} R_n^{(c₀)} / (z − p_n^{(c₀)}) + … + E^{(c₀)}(z)
```
where `E, E^{(c₀)}` are the entire parts (Weierstrass product for numerators `ξ, ξ^{(c₀)}`),
`R_n` is the residue of `W` at `γ_n`, and `p_n^{(c₀)} = γ_n + c₀/(n − k_N)` for `n > k_N`.

**Residue formula.** Since `W(z) = z²ξ(1/2−iz)/ξ'(1/2−iz)` has a simple pole at
`γ_n` (assuming simple zeros of ξ):
```
R_n = lim_{z→γ_n} (z − γ_n) W(z) = γ_n² · ξ(1/2 − iγ_n) / ξ''(1/2 − iγ_n) · (−i)
    = −i γ_n² / (−i ξ''(1/2−iγ_n)/ξ(1/2−iγ_n)).   (ξ simple zero)
```
This is a real nonzero constant for each `n` (by the simplicity assumption and the
functional equation).

**Matching the first `J_N` Taylor coefficients of the meromorphic function.**  
The Taylor coefficients of `W` at `w₀` are determined by the partial-fraction
expansion. The `j`-th coefficient is:
```
c_j := (1/j!) W^{(j)}(w₀) = Σ_n R_n · (−1)^j j! / (w₀ − γ_n)^{j+1} + [entire part contrib.]
```
For the perturbed function `F^{(c₀)}`, the same expansion holds with `p_n^{(c₀)}` in
place of `γ_n` and `R_n^{(c₀)}` in place of `R_n` for `n > k_N`.

**The IFT system.** Adjust the `J_N` tail pole positions `p_{k_N+1}^{(c₀)}, …, p_{k_N+J_N}^{(c₀)}`
(or equivalently, their residues `R_n^{(c₀)}`) to enforce Taylor coefficient matching:

```
c_j(F^{(c₀)}) = c_j(W)    for  j = 0, 1, …, J_N − 1.
```

The Jacobian of `(c_0, …, c_{J_N-1})` with respect to the perturbed pole positions
`(p_{k_N+1}, …, p_{k_N+J_N})` at the unperturbed values `p_n = γ_n` is:

```
∂c_j / ∂p_n = ∂/∂p_n [ R_n / (w₀ − p_n)^{j+1} ]
             = (j+1) R_n / (w₀ − γ_n)^{j+2}       (leading term from n-th pole)
```

The `J_N × J_N` Jacobian matrix has entries:
```
M_{jn} = (j+1) R_n / (w₀ − γ_n)^{j+2},   j = 0, …, J_N−1,  n = k_N+1, …, k_N+J_N.
```
Factor out: `M = D_j · [R_n / (w₀ − γ_n)^{j+2}]` where `D_j = diag(j+1)` is invertible.
Set `a_n = 1 / (w₀ − γ_n)` (distinct, nonzero for `w₀ ∉ {γ_n}`). Then:
```
[R_n / (w₀ − γ_n)^{j+2}] = diag(R_n) · [a_n^{j+2}].
```
The matrix `[a_n^{j+2}]_{j=0,…,J_N-1; n=k_N+1,…,k_N+J_N}` is a Vandermonde matrix in
`(a_n)` with an overall factor `a_n^2`:
```
[a_n^{j+2}] = [a_n^j] · diag(a_n^2)
```
and `[a_n^j]_{j=0,…,J_N-1}` is exactly the standard Vandermonde in `a_n = 1/(w₀−γ_n)`.

**Nonsingularity.** Since `γ_{k_N+1}, …, γ_{k_N+J_N}` are distinct, the values
`a_n = 1/(w₀ − γ_n)` are distinct (and nonzero for `w₀` not a pole). Therefore the
Vandermonde matrix is nonsingular, and `det M = det(D_j) · ∏R_n · ∏a_n^2 · ∏_{k<l}(a_l−a_k) ≠ 0`.

The IFT applies for small `c₀`: a unique smooth branch of pole positions `p_n^{(c₀)}`
satisfies the `J_N` matching conditions. The perturbed function `F^{(c₀)}` then satisfies
all conditions of `ℰ_N^{mer}` and differs from `W` in its tail poles. ✓

**Status: PROOF-DRAFT (self-contained Vandermonde argument; residue formula needs
simplicity-of-zeros assumption; that assumption is explicit in the method class `𝔐_Suz`).**

---

## §5. Theorem E'-pos (sufficient conditions, OPEN)

The E-pos sufficient conditions for the entire target use the Montel normal family theorem
(local uniform boundedness → precompact family). For the meromorphic target, the
analogue requires:
- **(H'-bound):** Local uniform bound on `|F_n(z)|` away from poles.
- **(H'-pole-sep):** Poles of `F_n` stay separated from the domain of interest.
- **(H'-tail):** Tail poles of `F_n` converge to `γ_n` for large `n`.
- **(H'-norm):** Normalization at a non-pole base point.

Under these conditions, Montel + Vitali + the meromorphic Hadamard uniqueness lemma
(E'.1) would give convergence to `W`.

**Status:** OPEN. The argument structure is clear; the meromorphic Montel theorem
(normal families of meromorphic functions) is classical (Marty's theorem), but the
application to this specific setting needs to be written out.

---

## §6. Application to Suzuki framework

Suzuki Cor. 6 (baseline, INDEPENDENTLY-CHECKED): RH follows if
`e^{φ(a,z)} W(a,θ;z) → z²ξ(1/2−iz)/ξ'(1/2−iz)` uniformly on compacts.

The E'-neg result says: finite evidence alone (first `k_N` poles, normalization,
first `J_N` Taylor coefficients) does not uniquely determine the locally uniform limit.
The E'-pos conditions identify what extra structure is needed.

**Missing ingredients for Suzuki convergence:** same structure as E-pos for CCM:
- (H'-bound) not established for the Suzuki sequence.
- (H'-tail) not established: tail poles of `W(a,θ;z)` convergence to `γ_n` as `a → 0`
  not yet proved.

These are the **precise missing ingredients** for the Suzuki track, analogous to
(H-bound)/(H-tail) for the CCM track.

---

## §7. Status summary

| Component | Status |
|---|---|
| Meromorphic Hadamard uniqueness (Lemma E'.1) | PROOF-DRAFT (classical; citation by thm number open) |
| E'-neg construction (§4) | PROOF-DRAFT (meromorphic IFT Jacobian: explicit Vandermonde in pole reciprocals; simplicity assumed) |
| E'-pos sufficient conditions (§5) | OPEN (structure clear; Marty/meromorphic Montel) |
| Suzuki (H'-bound)/(H'-tail) | OPEN (missing ingredients, not shown here) |
| Connection to Theorem E (same template) | ✓ explicit |
