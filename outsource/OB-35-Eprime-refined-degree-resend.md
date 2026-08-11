# Problem OB-35 — E' resend: the abstract odd-meromorphic jet lemma with REFINED leading degree

**Type:** Gate-A independent mathematical review (single abstract lemma, scoped).

**What this is.** A **resend** after OB-30 BLOCKED E' as a Suzuki-target theorem. Two of the
three OB-30 defects (the false `z^{2J+3}` degree; the withdrawn Suzuki-target claim) are now
resolved and the lemma is re-scoped to the honest survivor: an **abstract odd-meromorphic jet
non-identifiability lemma** over independent hypotheses (A1)–(A3), with the leading separation
degree **pinned to `d=3` via an exact criterion** (replacing the vague "some nonzero odd
degree"). It makes **no** claim about the real `ξ/ξ'` or Suzuki's entire family (those were the
OB-30 blocks and are respected, not re-asserted).

**Non-circularity (mandatory).** RH is not used. The `γ_n` (equivalently the abstract `a_n`)
are prescribed parameters of an abstract even function `A`; nothing uses their being ζ-zeros
or their reality. Confirm no RH-import.

---

## All definitions (self-contained)

Abstract odd meromorphic target `W(z) = z² A(z)/B(z)` with:
- **(A1)** `A` even, conventional order ≤ 1, simple zeros exactly `{±γ_n}`, `A(0)≠0`:
  `A(z)=A(0)∏_{n≥1}(1−a_n z²)`, `a_n=γ_n^{-2}`, `a_1>a_2>…>0`, `Σa_n<∞`.
- **(A2)** `B` odd (`B(z)=z·B̃(z)`, `B̃` even, `B̃(0)≠0`), conventional order ≤ 1, all zeros
  simple, **`Z(B)∩ℝ={0}`** (no nonzero real `B`-zero — a genuine abstract hypothesis).
- **(A3)** base point `w₀=iτ`, `τ∈ℝ\{0}`, `B(iτ)≠0`.
`A` and `B` are **independent** abstract functions (this is NOT the real `ξ,ξ'`, where
`B=iA'` forces real `B`-zeros by Rolle and violates (A2) — see the scope note).

Finite record `ℰ_N^{mer}`: `F` odd meromorphic, conventional order ≤ 1 (`T(r,·)≤C_ε
r^{1+ε}+C_{0,ε}`), poles exactly those of `W`, first `k` positive zeros `=γ_1,…,γ_k`,
normalization + first `J` Taylor coefficients matching `W` at `w₀`.

---

## The lemma to inspect

**Lemma (abstract jet non-identifiability, refined degree).** Under (A1)–(A3), fix `k≥0`,
`J≥1`. For all sufficiently small `c<0` there is an odd meromorphic `F^{(c)}≠W` satisfying
`ℰ_N^{mer}`, and
```
F^{(c)}(z) − W(z) = −(A(0)/B̃(0))·Δ₁(c)·z³ + O(z⁵),
```
where `Δ₁(c) = Σ_ℓ u_ℓ(c) + Σ_m b_m(c) − Σ_ℓ x_ℓ − Σ_m y_m` is the **net reciprocal-square-zero
shift**. Hence the leading degree is **`d = 3` iff `Δ₁(c) ≠ 0`**, and then
`sup_{|z|=R}|F^{(c)}−W| ≥ |A(0)/B̃(0)|·|Δ₁(c)|·R³` for `0<R<R_B:=dist(0,Z(B)\{0})` (Cauchy). If
`Δ₁(c)=0`, the degree is the next odd `r` with `Δ_r(c)≠0` (some such `r` exists since `F≠W`).

**Construction (OB-09 core, unchanged).** Freeze `γ_1..γ_k`; tail `μ_{k+J+m}(c)=γ_{k+J+m}
(1+c/(J+m))`; free `u_ℓ=μ_{k+ℓ}^{-2}`. Jet system `Ψ_j(u,c)=∂_t^j L(t₀;u,c)=0`, `j=0..J−1`
(`t=z²`, `t₀=w₀²`, `L=log[A_{u,c}/A]`), closes by IFT with the rational Wronskian–Vandermonde
Jacobian `det = (−t₀)^J(∏_{j<J}j!)∏_{p<q}(x_q−x_p)/∏_ℓ(1−x_ℓt₀)^J ≠ 0`. This matches the
**`w₀`-jet**, which is why it does NOT touch the origin power-sums `Δ_r`.

**Why `d=3` (the key correction of OB-30).** `L(0)=0` always, so `A_{u(c),c}(0)=A(0)`; the
first origin term is `A_{u,c}−A = A(0)L'(0)·z² + O(z⁴) = −A(0)Δ₁(c)z² + O(z⁴)`, and
`z²/B = z/B̃ ~ z/B̃(0)` near 0, giving the `z³` leading term. The `J`-jet match at `w₀≠0`
constrains the `w₀`-Taylor jet, **not** `Δ₁` — so the old `z^{2J+3}` was wrong.

**`d=3` for each fixed `J` at small `c` (script-verified, exact).** Solving the jet system
exactly (sympy; tail 2000–3000 terms) for `γ_n=n`, `k=1`, `w₀=i`:
`Δ₁'(0) = +0.033858 (J=1), −0.0014 (J=2), +4.3·10⁻⁵ (J=3), −1.2·10⁻⁶ (J=4)` — all nonzero
(J=1 reproduces OB-30's `0.03386`). So `Δ₁(0)=0`, `Δ₁'(0)≠0` ⇒ `∃c₀(J)>0` with `d=3` for
`0<|c|<c₀(J)`.

**Honest caveat (no uniform-in-`J`).** `|Δ₁'(0)|` falls ~10× per unit `J` and **alternates
sign**; the separation *constant* `|c₃|≈|A(0)/B̃(0)||Δ₁'(0)||c|` degrades rapidly in `J` (and
could vanish at a special `(J,c)`, pushing `d≥5`). The claim is **per-fixed-`J`, small `c`**;
neither degree nor constant is uniform in `J`.

---

## Links to inspect

**Link A (jet IFT core).** `Ψ_j` system, rational Wronskian–Vandermonde Jacobian ≠ 0 (distinct
`x_ℓ`, `w₀∉Z(A)`), IFT branch `u(c)`, `J`-jet match, membership `F^{(c)}∈ℰ_N^{mer}`, `F^{(c)}≠W`.
**Confirm** (this is the OB-09-confirmed core, given abstract (A1)–(A3)).

**Link B (the `z³` origin expansion + `Δ₁` criterion).** `L(0)=0` ⇒ `A_{u,c}(0)=A(0)`; leading
origin term `−(A(0)/B̃(0))Δ₁(c)z³`; `d=3 ⟺ Δ₁(c)≠0`; Cauchy bound at `d`. **Confirm** the
expansion and that the `w₀`-jet match leaves `Δ₁` free (so the degree is 3, not `2J+3`).

**Link C (`Δ₁'(0)≠0` per `J`, with degradation).** The exact `Δ₁'(0)` values (J=1..4), that
each is nonzero (so `d=3` per fixed `J`, small `c`), and that the magnitude degrades ~10×/J and
alternates sign (so no uniform-in-`J` degree/constant). **Confirm** the computation and the
honest non-uniformity.

**Link D (scope — abstract only).** `A,B` independent (A1)–(A3); **not** the real `ξ/ξ'`
(`B=iA'` ⇒ real `B`-zeros by Rolle ⇒ (A2) fails) and **not** Suzuki (entire approximants
incompatible with the meromorphic `W`, OB-30). **Confirm** the lemma is correctly *not* claimed
for the real target.

---

## Gate-A questions

### Q1 — Non-circularity
No RH / zero-location used (abstract `a_n`)? Confirm.

### Q2 — Refined degree correct
Confirm Link B: `d=3 ⟺ Δ₁(c)≠0`, with the exact `Δ₁` formula and the `z³` Cauchy bound; and
that the earlier `z^{2J+3}` is correctly retired (the jet match does not constrain `Δ₁`).

### Q3 — `Δ₁'(0)≠0` and the honest non-uniformity
Confirm the `Δ₁'(0)` values (J=1..4) are nonzero (⇒ `d=3` per fixed `J`, small `c`), and that
the ~10×/J degradation + sign alternation are correctly flagged as precluding a uniform-in-`J`
degree or constant. (An honest "d=3 per J, constant not uniform" is the intended claim.)

### Q4 — Scope (abstract, not Suzuki)
Confirm the lemma is scoped to abstract independent (A1)–(A3), and that the OB-30 blocks (real
`ξ/ξ'` fails (A2); Suzuki entire ⇒ no moving-pole convergence) are respected, not re-asserted.

### Q5 — Gate-A verdict
Given Links A–D and Q1–Q4: is the abstract lemma (with refined degree `d=3`, exact `Δ₁`
criterion, honest `J`-degradation) correct, non-circular, honestly scoped? May the E'-neg
abstract lemma advance PROOF-DRAFT → INDEPENDENTLY-CHECKED (as an abstract lemma, explicitly
not a Suzuki-target result)? Or identify a specific gap.

---

## Numerical anchor (sanity only — not an input)

- `Δ₁'(0)`: `+0.033858, −0.0014, +4.3·10⁻⁵, −1.2·10⁻⁶` for `J=1,2,3,4` (γ_n=n, k=1, w₀=i;
  jet system solved exactly, tail to 2000–3000 terms). Nonzero, shrinking ~10×/J, alternating.
- J=1 cross-check: `Δ₁'(0)=Σ_{n≥3}(n²−4)/(2n²(n²+1)(n−1))=0.0338580562…` (positive-term series,
  partial sum to 2·10⁶) — matches the OB-30 value.
The deliverable is the Links A–D / Q1–Q5 judgment.

---

## Acceptance criteria (all outcomes decisive)

1. **GATE-A PASS:** Links A–D confirmed, Q1–Q5 answered; verdict "advance the abstract E'-neg
   lemma to INDEPENDENTLY-CHECKED (abstract, refined degree `d=3` per fixed `J`), explicitly not
   a Suzuki-target result". State any textual conditions.
2. **GATE-A CONDITIONAL:** correct modulo a specific fix (e.g. sharpen the `Δ₁'(0)≠0` argument to
   a proof rather than J=1..4 computation, or the `c₀(J)` quantifier). Give the edit.
3. **GATE-A BLOCKED:** a genuine gap (e.g. `Δ₁'(0)` provably vanishes at some `J`, or the `z³`
   expansion is wrong). Identify and exhibit it.

An honest "the abstract jet lemma with degree `d=3` (per fixed `J`, small `c`) is correct; it
is not a Suzuki-target theorem and the constant is not uniform in `J`" is a valid, first-class
outcome.
