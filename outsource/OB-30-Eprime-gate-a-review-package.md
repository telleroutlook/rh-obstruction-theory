# Problem OB-30 — E' Gate-A package: independent review of the meromorphic (Suzuki-target) compactness theorem

**Type:** Gate-A independent mathematical review (whole-theorem inspection, scoped).

**What this is.** A request to **independently inspect Theorem E' (E-prime-meromorphic)** —
the Suzuki-meromorphic-target companion of Theorem E — and issue a **Gate-A verdict**. E' has
two parts: **E'-neg** (per-fixed-`(k,J)` non-identifiability: the finite record does not pin
down the odd meromorphic target `W`; its construction is CONFIRMED-after-correction by prior
review OB-09) and **E'-pos** (a corrected sufficiency package naming the exact extra
hypotheses that force convergence; corrected after OB-11 refuted the first version). The
review targets the analytic assembly, the parity/zero-pole structure of `W`, the
normalization discipline, non-circularity, and the honesty of the "missing ingredients".

**This theorem has already survived three targeted referee rounds** (OB-06 parity/structure,
OB-09 E'-neg construction, OB-11 E'-pos), each of which REFUTED an earlier version and
supplied a correction now integrated. This package asks for a **whole-chain** verdict, not a
re-run of those rounds.

**Non-circularity (mandatory).** RH is not assumed and not used. The `γ_n` (zeros of `ξ`,
equivalently zeros of `W`) appear only as prescribed real numbers the construction pins zeros
to; their being the true ζ-ordinates, and their reality (RH), is **never** used. Confirm no
step assumes RH, an RH-equivalent, or ζ-zero location as a hypothesis.

---

## All definitions (self-contained)

### The target `W` and the normalization discipline (READ FIRST)
```
W(z) = z² · ξ(1/2 − iz) / ξ'(1/2 − iz)        (Suzuki meromorphic target).
```
Write `W(z) = z² A(z)/B(z)` with `A(z)=ξ(1/2−iz)`, `B(z)=ξ'(1/2−iz)` (up to normalization).
**Three facts, all from the functional equation `ξ(s)=ξ(1−s)` (verify by hand/script):**
- `A(z)=ξ(1/2−iz)` is **even**; differentiating the FE gives `ξ'(s)=−ξ'(1−s)`, so
  `B(z)=ξ'(1/2−iz)` is **odd**; hence `W = z²·(even)/(odd)` is **ODD**: `W(−z)=−W(z)`.
- The `γ_n` (zeros of `ξ` on the critical line's image) are **simple zeros of `W`**
  (`W(z) = −iγ²/m·(z−γ)+O((z−γ)²)` for a mult-`m` `ξ`-zero) — **NOT poles**.
- The **poles** of `W` are the zeros of `ξ'(1/2−iz)` not cancelled by zeros of `ξ(1/2−iz)`.

**Order note (load-bearing — pre-send fix OB-30).** `W` has **conventional order 1 but
maximal type**: its poles (zeros of `ξ'`) have counting density `~(r/2π)log r`, so
`N(r,∞) ≍ (1/2π) r log r` and `T(r,W) ≍ r log r` — **NOT `O(r)`**. This exactly parallels
`Ξ` (order 1, infinite exponential type). Every order hypothesis below is therefore the
**conventional-order envelope** `T(r,·) ≤ C_ε r^{1+ε}+C_{0,ε}`; a *linear* `O(r)` / `Cr+C₀`
bound would exclude `W` itself and make the class vacuous — the meromorphic analogue of the
L1/L14 finite-type error that prior review OB-14 fixed for the entire target `Ξ`.
(script-checked: `N(r,∞)/r` grows `0.65 → 1.01 → 1.38` at `r=10³,10⁴,10⁵`, unbounded.)

(All three corrected in OB-06; an earlier draft had `W` even with poles at `γ_n` — wrong.)

**Normalization discipline (REFERENCE_BASELINE §5 — never conflate).** `W` (Suzuki,
**meromorphic**, `z²ξ/ξ'`) is a *different* normalization from the CCM **entire** target
`Ξ(z)=ξ(1/2+iz)` (Theorem E) and from `ξ̂` (Fourier transform of `ξ`). Suzuki Corollary 6
(baseline, INDEPENDENTLY-CHECKED): RH follows if `e^{φ(a,z)}W(a,θ;z) → W` uniformly on
compacts. E' studies whether finite evidence pins that limit. **Confirm the package never
conflates `W`, `Ξ`, `ξ̂`.**

### Method class `𝔐_Suz` and the finite record `ℰ_N^{mer}`
A method constructs meromorphic `F` with: **conventional order ≤ 1** (`∀ε>0`,
`T(r,F) ≤ C_ε r^{1+ε}+C_{0,ε}` — **NOT** the linear `T(r,F)=O(r)`: see the order note below);
**odd** (`F(−z)=−F(z)`,
matching `W`); poles at the zeros of `ξ'(1/2−iz)`; the first `k` positive zeros equal to
`γ_1,…,γ_k`; a base-point normalization at a non-pole non-zero `w₀`; and the first `J` Taylor
coefficients at `w₀` matching `W`. No tail envelope is imposed.

### Abstract structure assumptions (E'-neg)
- **(A1)** `A` even, order ≤ 1, simple zeros exactly `{±γ_n}`, `A(0)≠0`,
  `A(z)=A(0)∏(1−a_n z²)`, `a_n=γ_n^{-2}`, `a_1>a_2>…>0`, `Σa_n<∞`.
- **(A2)** `B` odd, order ≤ 1, all zeros simple, `Z(B)∩ℝ={0}` (no real zero of `B` collides
  with a real `±γ_n` — **mandatory** non-collision, else pole/zero cancellation, OB-09).
- **(A3)** base point `w₀=iτ`, `τ∈ℝ\{0}`, `B(iτ)≠0`.

---

## Part I — Theorem E'-neg (finite record does not identify `W`)

**Statement (per-fixed-`(k,J)` non-identifiability).** Fix `k≥1`, `J≥1`, `w₀=iτ`. Under
(A1)–(A3), for all sufficiently small `c<0` there is an **odd meromorphic** `F^{(c)}≠W`
satisfying `ℰ_N^{mer}`, with
```
sup_{|z|=R} |F^{(c)}(z) − W(z)| ≥ |A(0)/B̃(0) · Δ_{J+1}(c)/(J+1)| · R^{2J+3}
```
for `0 < R < R_B := dist(0, Z(B)\{0})`, and `Δ_{J+1}(c) ≠ 0`. (This is per-fixed-`(k,J)`
non-identifiability — the finite record leaves an uncontrolled tail degree of freedom — the
meromorphic analogue of E-neg; NOT a claim that a specific sequence fails to converge.)

**Construction (fixed `(k,J)`; §3, CONFIRMED-after-correction by OB-09).**
- Freeze `γ_1,…,γ_k`. Tail `n=k+J+m` (`m≥1`): `μ_{k+J+m}(c)=γ_{k+J+m}(1+c/(J+m))`, so
  `b_m(c)=γ_{k+J+m}^{-2}(1+c/(J+m))^{-2}` (**denominator `J+m`, not `m`** — OB-09). The `J`
  positions `u_ℓ=μ_{k+ℓ}^{-2}` are free.
- `A_{u,c}(z)=A(0)∏_{n≤k}(1−a_n z²)∏_{ℓ≤J}(1−u_ℓ z²)∏_{m≥1}(1−b_m(c)z²)`,
  `F^{(c)}(z)=z²A_{u(c),c}(z)/B(z)`.
- **Direct `w₀`-jet system (not power sums).** With `t=z²`, `t₀=w₀²=−τ²`,
  `L(t;u,c)=log[A_{u,c}/A]=Σ_ℓ log((1−u_ℓ t)/(1−x_ℓ t))+Σ_m log((1−b_m(c)t)/(1−y_m t))`
  (`x_ℓ=a_{k+ℓ}`, `y_m=a_{k+J+m}`), matching functionals `Ψ_j(u,c)=∂_t^j L(t₀;u,c)`,
  `j=0,…,J−1`. At `(u^0,0)=((x_1,…,x_J),0)`, `Ψ=0`; since `∂_{u_ℓ}L=−t/(1−u_ℓ t)`, the
  Jacobian is a **rational Wronskian–Vandermonde**:
  `det D_uΨ(u^0,0)=(−t₀)^J(∏_{j<J}j!)∏_{p<q}(x_q−x_p)/∏_ℓ(1−x_ℓ t₀)^J ≠ 0`. IFT ⇒ `C¹`
  branch `u(c)`, giving `A_{u(c),c}−A=O((z−w₀)^J)` and thus the `J`-jet match at `w₀`.
- **Separation (odd leading degree).** `F^{(c)}−W = −(A(0)/B̃(0))·Δ_{J+1}(c)/(J+1)·z^{2J+3}
  + O(z^{2J+5})` — degree **`2J+3` (odd)**, consistent with `F−W` odd (NOT `2J+2`; OB-09
  §5.1). `Δ_{J+1}(c)≠0` for small `c≠0` (nondegeneracy via one-signed `q(y_m)`). Cauchy's
  estimate on `0<R<R_B` gives the bound. **No `|W(iR)|→∞`** (that claim was REFUTED, OB-09):
  separation is purely the Cauchy coefficient estimate.

**Refuted earlier versions (confirm they are correctly retired).** (i) The old E'-neg that
perturbed "poles at `γ_n`" — wrong, `γ_n` are zeros. (ii) The power-sum matching system
`Φ_r` — matches the `z=0` expansion, not the `w₀`-jet. (iii) Even-degree `2J+2` separation —
contradicts `F−W` odd.

---

## Part II — Theorem E'-pos (corrected sufficiency package)

**The first version was REFUTED (OB-11) — confirm the two gaps and that the fix closes them.**
Under the original (LB*)/(H'-pole-sep)/(H'-tail)/(H'-norm), two independent counterexamples:
- **Growth gap:** `F_n ≡ W·e^{z²−w₀²}` (constant sequence) meets every original hypothesis
  but converges to `W·e^{z²−w₀²}≠W`; `T(r,e^{z²−w₀²})≍r²`, so the limit is order 2 — the
  divisor + one-point normalization only give `G=W·H` (`H` zero-free even, `H(w₀)=1`), NOT
  `H≡1`. Order must be an independent hypothesis.
- **Pole-cancellation gap:** a rational-multiplier family puts a double zero at a target pole
  `±p` (killing `W`'s simple pole) while relocating the pole to `±p_n`; meets every original
  hypothesis (rational `O(1)`-degree multipliers keep `T(r,F_n) ≍ r log r`, same order as `W`) but its limit drops `p` from the polar divisor.

**Corrected hypotheses.** (P) each `F_n` odd; (LB) local boundedness on the holomorphy
domain `Ω`; (ZT.1)+(**ZT_ℂ**) full-plane tail no-intrusion (every zero in `{|z|≤R}`,
*including at the poles* `𝒫`, is a matched zero — closes pole-cancellation); (**PL⁺**) each
`p∈𝒫` has a disk with exactly one simple pole `p_n→p` and no zeros; (N) normalization at
`w₀`; (**UG**) uniform conventional-order bound `∀ε>0, T(r,F_n)≤C_ε r^{1+ε}+C_{0,ε}`, constants independent of `n` (`r^{1+ε}` NOT linear — else it excludes `W`; closes the growth
gap).

**Corrected proof (OB-11 §6).** (LB)+**Montel** (Conway VII.2.9 — **not Marty**; (LB) gives
local uniform boundedness on a neighborhood of each compact) ⇒ subsequence `F_{n_j}→G`
locally uniformly on `Ω`, odd, `G(w₀)=W(w₀)≠0`. Hurwitz+(ZT.1)+(ZT_ℂ) ⇒ `G` has `W`'s zeros
in `Ω`. A contour/residue argument on `1/F_{n_j}` around each `p∈𝒫` (using (PL⁺)) ⇒ `G` has
a genuine simple pole at `p`. Ahlfors–Shimizu + (UG) ⇒ `T(r,G) ≤ C_ε r^{1+ε}+C_{0,ε}` (conventional order ≤ 1). Then `G,W` share the
complete divisor, `G/W` is even, `G(w₀)=W(w₀)≠0`, so **Lemma E'.1** ⇒ `G≡W`; subsequence
principle upgrades to full convergence.

**Lemma E'.1 (meromorphic Hadamard uniqueness, CONFIRMED OB-06).** If `F,G` meromorphic,
conventional order ≤ 1 (`T(r,·)≤C_ε r^{1+ε}+C_{0,ε}`, incl. the maximal-type `W`), identical complete zero divisors, `F/G` even, `F(w₀)=G(w₀)≠0`, then `F=G`.
Proof: `H:=F/G` is entire, zero-free, order ≤ 1, so `H=e^{az+b}` (Conway XI.3.4); evenness ⇒
`a=0`; normalization ⇒ `e^b=1`; `H≡1`. (Correct paired product `∏(1−z²/z_j²)`, no spurious
`e^{z²/z_j²}` — OB-06.)

**These corrected hypotheses are NOT proved for the Suzuki family.** (LB), (ZT_ℂ), (PL⁺),
(UG), and the odd parity of `W(a,θ;z)` are the **precise missing ingredients** for the
Suzuki convergence track — E' identifies them, it does not verify them.

---

## Links to inspect

**Link A (parity + zero/pole structure).** `W` odd; `γ_n` simple zeros; poles = zeros of
`ξ'(1/2−iz)`; non-collision (A2) needed. **Confirm** from the functional equation (a sequence
of even functions could never converge to the odd `W` — the old even-`F_N` identification was
correctly refuted).

**Link B (E'-neg jet construction).** The `Ψ_j` system, the rational Wronskian–Vandermonde
Jacobian (nonzero by distinct `x_ℓ` and `w₀∉Z(A)`), IFT branch, `J`-jet match, membership in
`𝔐_Suz`, and `F^{(c)}≠W`. **Confirm** the construction closes and the power-sum `Φ_r` route
is correctly abandoned.

**Link C (E'-neg separation, degree `2J+3`).** Odd leading discrepancy `z^{2J+3}`;
`Δ_{J+1}(c)≠0`; Cauchy estimate on `0<R<R_B`; **no `|W(iR)|→∞`**. **Confirm** the odd degree
and that separation does not rely on any growth-to-infinity claim.

**Link D (E'-pos corrected sufficiency).** The two counterexamples to the original
hypotheses; that (ZT_ℂ) closes pole-cancellation and (UG) closes the growth gap; **Montel
suffices, Marty not needed**; the contour/residue simple-pole recovery; identification via
Lemma E'.1. **Confirm** the four added ingredients are exactly what the argument consumes and
that E'-pos is honestly conditional (Suzuki-family ingredients OPEN).

---

## Gate-A questions (the deliverable)

### Q1 — Hidden gap / circularity / RH-import
Does any step assume RH, an RH-equivalent, or ζ-zero location? (`γ_n` reality is motivation
only; E'-pos *derives* the pole/zero structure of the limit.) Confirm or exhibit the leak.

### Q2 — Parity is load-bearing and correct
Confirm `W` is ODD (from the functional equation), that `γ_n` are simple **zeros** (not
poles), and that the method class correctly uses **odd** functions — a sequence of even
functions cannot converge to `W` (the old even-target identification was rightly refuted,
OB-06).

### Q3 — Normalization (`W` vs `Ξ` vs `ξ̂`)
Confirm the target is consistently the Suzuki **meromorphic** `W=z²ξ/ξ'`, never conflated
with the CCM **entire** `Ξ` (Theorem E) or `ξ̂`. Confirm Hurwitz-for-entire does **not**
apply here — the pole is recovered by a contour/residue (argument-principle) step.

### Q4 — Per-`(k,J)` framing (not sequence)
Confirm E'-neg is a per-fixed-`(k,J)` non-identifiability statement (separation on
`0<R<R_B`), the meromorphic analogue of B1/E-neg's "no uniform margin", and is a non-vacuous
information obstruction (clear of the "margin → 0" non-barrier label).

### Q5 — E'-pos is conditional; ingredients honest
Confirm the original E'-pos hypotheses are genuinely insufficient (both counterexamples
hold), that the corrected (ZT_ℂ)/(PL⁺)/(UG) close the two gaps, that **(UG) must be a uniform *conventional-order* envelope `T(r,F_n)≤C_ε r^{1+ε}+C_{0,ε}`** — NOT linear `Cr+C₀` (which excludes the maximal-type `W`, `T(r,W)≍r log r`), and NOT a per-`n` bound with `n`-dependent constant (which does not transfer), and that
E'-pos is honestly a sufficiency theorem with the Suzuki-family ingredients OPEN.

### Q6 — Citations
Confirm Lemma E'.1 rests on Hadamard/Conway XI.3.4 (`H=F/G` route); Montel is Conway VII.2.9;
Suzuki Cor. 6 is the correct source for `W` (baseline, INDEPENDENTLY-CHECKED). Flag any
citation used beyond its scope (Marty is listed as context-only, not load-bearing — confirm).

### Q7 — Gate-A verdict + novelty
Given Links A–D and Q1–Q6: is E' a correct, self-contained, non-circular, RH-free result
(E'-neg per-`(k,J)` obstruction + E'-pos conditional sufficiency for the meromorphic target)?
Should its status advance from PROOF-DRAFT toward INDEPENDENTLY-CHECKED? Is it a genuine
Suzuki-target companion to Theorem E (Paper C), or does a specific gap block it? An honest
"companion to E, publish as the meromorphic half of the Paper C convergence-track analysis"
is a valid outcome.

---

## Numerical anchor (sanity only — not an input)

- `W` odd: with mock even `X(z)=cos(0.3z)+2`, odd `Y(z)=z(1+0.1z²)+sin(0.2z)`,
  `W=z²X/Y` satisfies `W(−z)=−W(z)` to machine precision at several complex `z`
  (script-checked) — confirming the parity algebra `even/odd·z²=odd`.
- Counterexample `W·e^{z²−w₀²}`: `T(r,e^{z²−w₀²})≍r²/π`, order 2 ≠ 1 — motivating (UG).
The Gate-A deliverable is the whole-theorem judgment (Links A–D, Q1–Q7), not a re-run of §3
(OB-09-confirmed) or §4 (OB-11-confirmed).

---

## Acceptance criteria (all outcomes decisive)

1. **GATE-A PASS:** Links A–D confirmed, Q1–Q7 answered with no blocking gap; verdict
   "advance E' toward INDEPENDENTLY-CHECKED", with the novelty/positioning ruling. State any
   required textual conditions.
2. **GATE-A CONDITIONAL:** the chain is correct but a specific textual fix is required. Give
   the exact edit.
3. **GATE-A BLOCKED:** a genuine gap, circularity, RH-import, parity error, or normalization
   conflation exists. Identify it, exhibit it, give the minimal repair.

An honest "E'-neg per-`(k,J)` obstruction is correct and RH-free; E'-pos is a correct
conditional sufficiency theorem with (LB)/(ZT_ℂ)/(PL⁺)/(UG)/odd-parity unproved for the
Suzuki family; publish as the meromorphic companion to Theorem E" is a valid, first-class
outcome.
