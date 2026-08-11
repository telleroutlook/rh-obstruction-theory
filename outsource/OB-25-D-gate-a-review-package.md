# Problem OB-25 — D Gate-A package: independent review of the spectral-asymptotic exclusion

**Type:** Gate-A independent mathematical review (whole-theorem inspection, scoped).

**What this is.** A request to **independently inspect Theorem D** — no positive elliptic
pseudodifferential operator on a closed manifold has spectrum equal to the Riemann zero
ordinates — as a coherent whole, and issue a **Gate-A verdict**: is it correct,
self-contained, non-circular, RH-free, with its citations covering the objects used and its
novelty honestly assessed? The Riemann-side heat coefficient (`Z_ζ` leading singularity
`(1/2π)log(1/t)/t`) is already independently certified (prior review OB-19, symbolic +
110-digit); the load-bearing operator-side citation (Lesch 1999 heat expansion) is
source-verified in-repo (arXiv dg-ga/9708010, deposited). This review targets the analytic
assembly and the scope/novelty judgment.

**Non-circularity (mandatory).** RH is not assumed and is not used. The Riemann side uses
ONLY the unconditional Riemann–von Mangoldt counting law `N(T)` (a count, no zero
location); no zero ordinate, Euler product, or functional equation enters the operator-side
argument. Confirm no step assumes RH or an RH-equivalent.

---

## All definitions (self-contained — everything is here)

### The operator class
`H ∈ 𝒞_ell` iff `H` is a positive, self-adjoint, classical (polyhomogeneous) elliptic
pseudodifferential operator of order `m > 0` on a closed (compact, boundaryless) smooth
`d`-manifold `M`, with discrete spectrum `0 < λ_1 ≤ λ_2 ≤ … → ∞`. Its counting function is
`N_H(T) = #{n : λ_n ≤ T}`; heat trace `Z_H(t) = Tr(e^{-tH}) = Σ_n e^{-tλ_n}`; spectral zeta
`ζ_H(s) = Σ_n λ_n^{-s}` (converges for `Re s > d/m`).

### Target predicate
`P(H) = 1` iff the spectrum of `H` (with multiplicity) equals `{γ_n : n ≥ 1}`, the positive
imaginary parts of the nontrivial zeros of ζ. (The `γ_n` are used only as a *counting*
target — their reality/RH is never assumed.)

### The two counting laws
- **Weyl (for `H ∈ 𝒞_ell`, REFEREED):** `N_H(T) ~ C_H T^{d/m}`, `C_H > 0` (Hörmander 1968
  Acta Math. 121; Seeley 1969; Ivrii 1980). A pure power.
- **Riemann–von Mangoldt (unconditional):** `N_ζ(T) = (T/2π)log(T/2π) − T/2π + O(log T)`.

### Allowed premises (source-verified / REFEREED)
- **Lesch 1999 heat expansion** (baseline/lesch-dg-ga-9708010/, verified in-repo): for a
  positive classical elliptic ΨDO `P` and `A ∈ CL^{a,k}`,
  `Tr(A e^{-tP}) ∼ Σ_j t^{(j−n−a)/m} c̃_j(log t) + Σ_j d̃_j t^j`, with `deg c̃_j ≤ k` if
  `(j−a−n)/m ∉ ℤ₊`, else `≤ k+1` (eq. (3.9), published Thm 3.7; extends Grubb–Seeley 1995
  Thm 2.7). Meromorphic `ζ_H` continuation, poles at `(a+n−j)/m` of order `≤ k+1`.
- **Z_ζ leading singularity** (OB-19, INDEPENDENT-CHECKER): from RvM by Abel/Stieltjes,
  `Z_ζ(t) = (1/2πt)(log(1/t) − γ_E − log2π) + O(log(1/t))`; leading `(1/2π)log(1/t)/t`.

---

## The claimed theorem (D)

No `H ∈ 𝒞_ell` has spectrum `{γ_n}`. Two independent arguments:
- **(D-Weyl)** If `spec(H) = {γ_n}` then `N_H = N_ζ`, i.e. `C_H T^{d/m} ~ (1/2π) T log T`;
  a pure power cannot match `T log T` (the log is not a power). Contradiction.
- **(D-heat, stronger)** With `A = I` (so `a=0, k=0`), Lesch's expansion gives
  `Z_H(t) = a_0 t^{-d/m} + o(t^{-d/m})`, a **pure-power leading singularity, no log**
  (`j=0` exponent `−d/m < 0 ∉ ℤ₊` ⟹ `c̃_0` constant). But `Z_ζ(t) ∼ (1/2π)log(1/t)/t`
  carries a `log(1/t)` at leading order. Incompatible ⟹ `spec(H) ≠ {γ_n}`.

---

## Links to inspect

**Link A (Weyl mismatch).** `N_H(T) ~ C_H T^{d/m}` (pure power) vs `N_ζ(T) ~ (1/2π)T log T`;
no `(d,m,C_H)` makes `C_H T^{d/m} = (1/2π)T log T` asymptotically. **Confirm** (elementary,
but confirm the log-vs-power incompatibility is stated correctly).

**Link B (heat-trace leading singularity — the load-bearing argument).** For `H ∈ 𝒞_ell`,
`A=I`: Lesch eq. (3.9) with `j=0`, exponent `−d/m<0 ∉ ℤ₊` ⟹ `deg c̃_0 ≤ 0` ⟹ leading term
`a_0 t^{-d/m}` is log-free; via Mellin, `a_0 = Γ(d/m)·Res_{s=d/m} ζ_H(s) > 0`. **Confirm**
the citation covers the object (positive classical elliptic ΨDO, `A=I`), the `j=0`
degree-bound gives no leading log, and the `a_0` coefficient/sign is right.

**Link C (no-log needs BOTH facts).** A leading `t^{-d/m}log(1/t)` would require a *double*
pole of `Γ(s)ζ_H(s)` at `s=d/m`; since (i) Lesch gives `ζ_H` at most a simple pole there
and (ii) `Γ` is regular at `d/m>0`, `Γζ_H` has only a simple pole ⟹ pure power. **Confirm
both halves are needed and both hold** (stating only "Γ's pole doesn't coincide" is
insufficient — the simple-pole fact is the load-bearing half).

**Link D (Z_ζ side, OB-19).** `Z_ζ(t) = (1/2πt)(log(1/t) − γ_E − log2π) + O(log(1/t))`,
leading `(1/2π)log(1/t)/t`. **Confirm** (already INDEPENDENT-CHECKER; just confirm it is the
correct comparison object and the leading term genuinely carries a log).

**Link E (incompatibility).** Pure power `t^{-d/m}` (or `a_0 t^{-d/m}`) vs
`(1/2π)t^{-1}log(1/t)`: even at `d/m = 1` the Riemann side has a `log(1/t)` factor the ΨDO
side cannot. **Confirm** the conclusion `spec(H) ≠ {γ_n}` follows.

---

## Gate-A questions (the deliverable)

### Q1 — Hidden gap / circularity / RH-import
Does any step assume RH or a ζ-zero location? (The operator side is pure spectral geometry;
the Riemann side uses only the RvM *count*.) Confirm or exhibit the leak.

### Q2 — Ellipticity is mandatory (correction check)
Confirm ellipticity is a genuine hypothesis, not decorative: the non-elliptic
`H₀ = 1 + D_x² + D_y⁴` on `𝕋²` (positive, self-adjoint, classical, discrete spectrum, but
symbol `ξ_y⁴` vanishes at `ξ_y=0`) has `Z_{H₀}(t) ∼ (√π Γ(1/4)/2) t^{-3/4}` — exponent
`3/4`, NOT `d/m = 1/2`. So (D-heat)'s pure-power *exponent* uses ellipticity. Confirm this
counterexample is correct and that `𝒞_ell` correctly requires ellipticity.

### Q3 — Subleading logs do not sink the argument (correction check)
Confirm the earlier "no logs at any order" claim is correctly WITHDRAWN: `ζ_H` need not be
regular at negative integers (`Res_{s=−k} ζ_H = m^{-1} Wres(H^k)`; witness
`(1+D_x²)^{1/2}` on `S¹` has `Wres = 1`, giving a nonzero `t log t` term), so subleading
`t^k log t` (`k≥1`) can occur — but these do NOT affect the *leading* `t^{-d/m}`
singularity, which is all D uses. Confirm the argument correctly relies only on the leading
term.

### Q4 — Citation scope
Confirm the load-bearing citation (Lesch 1999 heat expansion, source-verified in
baseline/lesch-dg-ga-9708010/) genuinely covers the **full classical elliptic ΨDO** class
with `A=I`, and that BGV Thm 2.30 (Laplace-type only) and Gilkey Lemma 1.8.2 (differential
only) are correctly relegated to scope-limited non-load-bearing references (PROMPT_LINT L17;
Gilkey is Lemma 1.8.2, not "Thm 1.8.1"). Confirm the Hörmander cross-check (order-1 Weyl
law for `H^{1/m}`) independently supports the pure-power exponent.

### Q5 — Novelty honesty (Paper B gate)
Theorem D's Weyl-mismatch (Link A) is close to a standard corollary and overlaps
Endres–Steiner 2010 (who proved it for compact quantum graphs). Confirm whether the
**heat-trace leading-log argument (Links B–E)** is genuinely a materially stronger, sharply
defined result — covering the full `𝒞_ell` class via a finer invariant (leading-singularity
*type*, not just leading-term *order*) — or whether it reduces to Endres–Steiner + standard
Weyl. State honestly whether D warrants a standalone note or is a corollary.

### Q6 — Gate-A verdict
Given Links A–E and Q1–Q5: does Theorem D (with the heat-trace argument as its primary
content) constitute a correct, self-contained, non-circular exclusion theorem — should its
mathematical status advance from PROOF-DRAFT toward INDEPENDENTLY-CHECKED? Or does a
specific gap block it?

---

## Numerical anchors (sanity only — already certified)

- Non-elliptic counterexample `H₀ = 1+D_x²+D_y⁴` on `𝕋²`: `Z_{H₀}(t) ∼ (√πΓ(1/4)/2)t^{-3/4}`
  (exponent 3/4 ≠ 1/2) — script-verified (ratio → 1 at `t=10⁻³,10⁻⁴`).
- `Z_ζ` leading coefficient `1/2π`, exact closed form `(1/2πt)(log(1/t)−γ_E−log2π)` —
  OB-19-certified (110-digit).
- Lesch eq. (3.9) degree bound `deg c̃_j ≤ k` (`(j−a−n)/m ∉ ℤ₊`) — source-verified in
  baseline/lesch-dg-ga-9708010/ (`A=I,j=0` ⟹ constant leading coefficient, no log).
The Gate-A deliverable is the whole-theorem judgment (Links A–E, Q1–Q6), not a re-run of
these.

---

## Acceptance criteria

1. **GATE-A PASS:** Links A–E confirmed, Q1–Q6 answered with no blocking gap; verdict
   "advance D toward INDEPENDENTLY-CHECKED", with an explicit statement of whether D is a
   standalone result or a corollary (Q5). State any required textual conditions.

2. **GATE-A CONDITIONAL:** the chain is correct but a specific textual fix is required
   (e.g. sharpen the ellipticity hypothesis, restate the novelty claim). Give the exact
   edit.

3. **GATE-A BLOCKED:** a genuine gap, circularity, RH-import, or citation-scope failure
   exists. Identify it, exhibit it, give the minimal repair.

All outcomes decisive. An honest "PASS for the heat-trace obstruction; the Weyl-mismatch
part is a corollary of Endres–Steiner and should be labeled as context, not new" is a valid
and useful result — the goal is a truthful judgment of what D newly establishes.
