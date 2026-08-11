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
W(z) = z² ξ(1/2 − iz) / ξ'(1/2 − iz).
```

**Parity correction (OB-06 referee, 2026-08-11).** W is ODD, not even.
Proof: ξ satisfies `ξ(s) = ξ(1−s)`, so `X(z) := ξ(1/2−iz)` is even in z.
Differentiating the functional equation gives `ξ'(s) = −ξ'(1−s)`, so
`ξ'(1/2−iz)` is ODD in z.  Therefore `X(z)/X'(z) = ξ(1/2−iz)/ξ'(1/2−iz)`
is odd, and `W(z) = z² · (odd) = odd`.  In particular `W(−z) = −W(z)`.

**Zero/pole structure of W (OB-06 referee, 2026-08-11).**
- The zeros of ξ at `s = 1/2 − iγ` (of multiplicity m) become **simple zeros** of
  W at `z = γ`, regardless of m.  Near `z = γ`:
  `W(z) = −iγ²/m · (z−γ) + O((z−γ)²)`.
  There is no residue at γ; γ is a zero of W, not a pole.
- The **poles** of W come from zeros of `ξ'(1/2−iz)` that are not cancelled by zeros
  of `ξ(1/2−iz)`.  At `z = 0`: `ξ'(1/2) = 0` (functional equation), and the local
  behavior at 0 depends on the vanishing order of ξ' there.
- The earlier statement that "poles of W are at `γ_n`" was INCORRECT.

**Consequence for method class.** The E'-neg non-uniqueness construction and E'-pos
identification steps must be redesigned for the correct target function W (odd,
zeros at γ_n, poles at zeros of ξ').  The current E'-pos identification step
(which attempts to show even F_N → even W) is REFUTED: even F_N cannot converge
to the odd function W (OB-06).

Suzuki Cor. 6 (baseline, INDEPENDENTLY-CHECKED): RH follows if
`e^{φ(a,z)} W(a,θ;z) → z²ξ(1/2−iz)/ξ'(1/2−iz)` uniformly on compacts.
The target `z²ξ(1/2−iz)/ξ'(1/2−iz)` is meromorphic with the correct zero/pole
structure as above.

This theorem audits whether the E-neg non-uniqueness obstruction transfers to the
meromorphic target W.

---

## §2. Method class and observation

**Method class 𝔐_Suz.** A method `P ∈ 𝔐_Suz` constructs a sequence of meromorphic
functions `(F_n)` satisfying finite evidence `ℰ_N^{mer}`:
- meromorphic of order 1 (Nevanlinna characteristic T(r,F) = O(r));
- poles at the zeros of `ξ'(1/2−iz)` (not at γ_n — see §1 parity correction);
- **ODD**: `F_n(−z) = −F_n(z)` (matching W's true parity);
- normalization condition matching `W` at one non-pole, non-zero base point `w₀`;
- first `J_N` Taylor coefficients at `w₀` matching `W`.

**Target predicate.** `(F_n) → W` locally uniformly on `ℂ \ {poles of W}`.

**Status note.** The earlier §2 stated F_n should be even; this was WRONG (OB-06).
The method class must use ODD functions to match W's parity.  A sequence of even
functions cannot converge locally uniformly to W.

---

## §3. Meromorphic Hadamard uniqueness (the key lemma — CONFIRMED AFTER CORRECTION)

**Lemma E'.1 (meromorphic Hadamard uniqueness — corrected, OB-06).** Let `F`, `G` be
meromorphic functions with `T(r,F) = O(r)` and `T(r,G) = O(r)` (Nevanlinna order ≤ 1),
with:
- identical complete zero divisors: `ord_a F = ord_a G` for every `a ∈ ℂ`;
- `F/G` is an even function (in particular, F and G both even suffices);
- `F(w₀) = G(w₀) ≠ 0` at some non-pole point `w₀`.

Then `F = G`.

*Proof (OB-06 referee §3).* The quotient `H := F/G` is an entire function (all
poles and zeros cancel) with `T(r,H) = O(r)`.  Since H is a zero-free entire
function of Nevanlinna order ≤ 1, Hadamard's theorem (Conway, XI.3.4) gives
`H(z) = e^{az+b}`.  By evenness of H: `H(−z)/H(z) = e^{−2az} = 1` for all z,
hence `a = 0`.  The normalization `H(w₀) = 1` gives `e^b = 1`, so `H ≡ 1`. ☐

*Correct canonical product (OB-06 referee §3.3).* For paired symmetric zeros `±z_j`
with `Σ|z_j|^{-2} < ∞`, the correct convergent paired product is:
```
Z(z) = ∏_j (1 − z²/z_j²),
```
NOT `∏_j (1 − z²/z_j²) e^{z²/z_j²}` — the latter introduces a spurious exponential
factor `exp(z² Σ z_j^{-2})` of order 2.  The pairing identity `E_1(z/a)E_1(z/−a) =
(1−z/a)e^{z/a}·(1+z/a)e^{−z/a} = (1−z²/a²)` shows the exponential factors cancel.

*Status: CONFIRMED AFTER CORRECTION (OB-06 2026-08-11).*
The proof is valid via the H := F/G route.  The original proof using separate Weierstrass
products P, P', Q, Q' had an error in the canonical product formula; the H-ratio proof
avoids this.

**Consequence for E'.** The identification step in E'-pos requires:
the limit function G has the same COMPLETE zero divisor as W (not merely same pole
positions), is odd (matching W's parity, replacing "even" from the old statement),
and matches W at one point.  Then Lemma E'.1 (with "odd" replacing "even" — the
argument is identical: F/G even follows from both F, G odd) gives G = W.

---

## §4. Theorem E'-neg (non-uniqueness for meromorphic target, PROOF-DRAFT)

**Status note (OB-06 2026-08-11).** The E'-neg construction requires redesign:
the old construction perturbed "poles at γ_n" — but γ_n are ZEROS of W, not poles
(§1 correction).  A corrected construction must either:
(a) perturb the zeros of W at γ_n (i.e., perturb the zeros of ξ that appear as
    zeros of W), or
(b) work with a different (correctly defined) odd meromorphic target W̃.

The corrected E'-neg strategy is:

**Statement.** For any `ε > 0` and any `N`, there exists an odd meromorphic function
`F ≠ W` satisfying all conditions of `ℰ_N^{mer}` with:
```
sup_{z ∈ K, z not near a pole of W} |F(z) − W(z)| ≥ ε
```
for some compact K = K(N, ε).

*Proof strategy (corrected — PROOF-DRAFT).*

1. **Perturb tail zeros of W.** W has simple zeros at `γ_n` (zeros of ξ); the tail
   zeros `γ_n` for `n > k_N` are free.  Perturb: `μ_n^{(c₀)} = γ_n(1 + c₀/(n−k_N))`
   for `n > k_N`, keeping `γ_1, …, γ_{k_N}` fixed.  This gives a perturbed odd
   meromorphic function (with the same pole set as W, matching W at zero positions
   up to index k_N).

2. **IFT for matching.** Adjust `J_N` of the free tail zero positions to enforce
   Taylor coefficient matching at base point `w₀`.  The Jacobian is a Vandermonde
   matrix in `{1/(w₀ − γ_n)}_{n=k_N+1}^{k_N+J_N}`, nonsingular by distinctness.
   IFT gives a unique smooth branch of perturbed zero positions for `|c₀| < δ`.

3. **Separation.** For `c₀ ≠ 0`, the perturbed function differs from W at the
   (J_N+1)-th Taylor coefficient; Cauchy's estimate gives sup-norm separation on
   any disk of radius `R_0`.

*Residue note.* The perturbed function has the same poles as W (zeros of ξ'); the
residues at those poles change because the numerator ξ is perturbed.  The IFT
system uses Taylor data at `w₀`, not residues at poles.  Since W is odd, the
Taylor expansion at `w₀ ≠ 0` involves both even and odd coefficients.

**What remains open.** The IFT step for the odd meromorphic setting (step 2) needs
to be written out fully, analogous to E-neg §3 for the entire case.  The Vandermonde
structure is identical in principle; the execution is PROOF-DRAFT.

---

## §5. Theorem E'-pos (sufficient conditions, OPEN)

The E-pos sufficient conditions for the entire target use the Montel normal family theorem
(local uniform boundedness → precompact family). For the meromorphic target, the
analogue requires:
- **(H'-bound) / (LB*) (corrected, OB-06):** for each compact `L ⊂ Ω = ℂ\{poles of W}`,
  there exists an open `U_L` with `L ⊂ U_L ⊂ Ω` and constants `N_L, M_L` such that
  `F_n` is holomorphic on `U_L` and `|F_n| ≤ M_L` on `U_L` for all `n ≥ N_L`.
  (This is stronger than the earlier (H'-bound); the weaker form is vacuously satisfiable
  — see OB-06 referee §4.2.)
- **(H'-pole-sep):** Poles of `F_n` are eventually outside any compact disjoint from
  the poles of W; equivalently `U_L` in (LB*) is pole-free for all large n.
- **(H'-tail):** Tail zeros of `F_n` at `γ_n` for `n > k_N` converge, with the
  tail no-intrusion condition (T) (see E-compactness/proof.md §4).
- **(H'-norm):** Normalization at a non-pole, non-zero base point `w₀`.

Under these conditions, Montel (not Marty — OB-06 referee §4.4 confirms Montel suffices
on Ω) + diagonal subsequence argument gives a locally uniform limit G on Ω, which is
holomorphic on Ω.  The identification G = W then requires:
- G odd (locally uniform limit of odd functions);
- same complete zero divisor (zeros at γ_n — via H'-tail + tail no-intrusion);
- same poles (limit of functions with same pole set — via H'-pole-sep + argument
  principle or Hurwitz applied to 1/F_n);
- G(w₀) = W(w₀) — via H'-norm.

Then Lemma E'.1 (with "odd" in place of "even") gives G = W.

**Note on Marty vs Montel (OB-06 referee §4.5).** On Ω = ℂ\{poles of W}, with
(LB*) ensuring F_n is holomorphic and bounded on an open neighborhood of each compact,
**Montel's theorem for analytic functions suffices** — no Marty criterion needed.
Marty would be required only to obtain convergence in the spherical metric on a domain
that contains the poles as interior points; for convergence on Ω that is unnecessary.

**Status:** OPEN. The argument structure is complete; writing out all steps is open.

---

## §6. Application to Suzuki framework

Suzuki Cor. 6 (baseline, INDEPENDENTLY-CHECKED): RH follows if
`e^{φ(a,z)} W(a,θ;z) → z²ξ(1/2−iz)/ξ'(1/2−iz)` uniformly on compacts.

The E'-neg result (once written out) will say: finite evidence alone (first `k_N` zeros of
W, normalization, first `J_N` Taylor coefficients) does not uniquely determine the locally
uniform limit.  The E'-pos conditions identify what extra structure is needed.

**Missing ingredients for Suzuki convergence:**
- (H'-bound)/(LB*) not established for the Suzuki sequence `W(a,θ;z)`.
- (H'-tail) not established: tail zeros of W(a,θ;z) converge to γ_n as a → 0 — not
  yet proved.
- The correct parity structure (odd functions) must be verified for the Suzuki family.

These are the **precise missing ingredients** for the Suzuki track.

---

## §7. Status summary

| Component | Status |
|---|---|
| Meromorphic Hadamard uniqueness (Lemma E'.1) | CONFIRMED AFTER CORRECTION (OB-06 2026-08-11; F/G ratio route; correct paired product) |
| W parity | CORRECTION: W is ODD, not even (OB-06 2026-08-11) |
| W zero/pole structure | CORRECTION: γ_n are ZEROS of W (not poles); poles come from zeros of ξ' (OB-06 2026-08-11) |
| E'-neg construction (§4) | PROOF-DRAFT — redesigned: perturb zeros of W (not poles); IFT write-out open |
| Old E'-neg (perturbing "poles at γ_n") | REFUTED (γ_n are zeros, not poles of W) |
| Old E'-pos identification ("even F_N → even W") | REFUTED (W is odd; even functions cannot converge to W) |
| E'-pos sufficient conditions (§5) | OPEN — structure correct; Montel (not Marty) suffices on Ω |
| (LB*) replacing old (H'-bound) | CORRECTION: old form vacuously satisfiable; (LB*) is the correct assumption |
| Suzuki (H'-bound)/(H'-tail) | OPEN (missing ingredients) |
| Connection to Theorem E (same template) | ✓ explicit (corrected: zeros not poles) |
