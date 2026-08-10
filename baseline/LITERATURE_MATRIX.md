# LITERATURE_MATRIX.md — theorem · scope · prior art · unresolved delta

Maps each program target and baseline input against the closest existing theorem, so a
paper is only pursued where a genuine **delta** exists. Prior-art anchors are the ones the
program (§9, §2.4, §7–§8) already names; a paper freeze requires a fuller theorem-by-theorem
audit (`novelty.md` per theorem). References verified live via arXiv source or export API.

Legend for "delta": **OPEN** (genuine gap this program can attack) · **THIN** (likely a
corollary of prior art; publish only as note/lemma) · **EQUIV** (an RH-equivalence, not a
barrier).

---

## Baseline constructions (the objects, not our theorems)

| Result | Scope | Closest prior art | Delta |
|---|---|---|---|
| Suzuki `λ(a)` continuity + small-`a` positivity (Thm 1.3–1.4) | localized Weil form `Q_W^a`, all `a>0` | Yoshida 1992 (positivity small `a`); Connes–Consani 2021, CCM 2025 (operator `A_a`) | baseline input, not our claim |
| Suzuki `W(a,θ;z)` entire, real zeros (Thm 1.5) | finite-interval characteristic function | Bombieri Lagrangian; de Branges spaces | baseline input |
| Suzuki Cor 6 (uniform limit `→ z²ξ/ξ'` ⟹ RH) | `a→∞` meromorphic limit | CCM determinant limit (§ below) | **EQUIV** (target of Paper C escape, not a barrier) |
| CCM `det_reg = −iλ^{−iz}ξ̂`, normalized `→ Ξ` | finite spectral triples | Connes 1999 trace formula; Berry–Keating | **EQUIV** (object of study) |

---

## Program targets vs prior art

### Paper C (WP-E) — finite spectral matching ⇏ compact convergence  ·  **primary**

| Aspect | This program | Prior art | Delta |
|---|---|---|---|
| Negative theorem: finite evidence record (self-adjointness, real-rootedness, first `k_N` zeros, finite Taylor/traces, finite det identity, sampled residuals) ⇏ locally uniform convergence to the declared limit | quantify invisible tail/growth d.o.f. in the canonical product / spectral tail | folklore "finite numerics ≠ infinite theorem"; Montel/Vitali + Hurwitz standard | **OPEN** — but must beat the slogan: needs a *quantified* counterexample sequence in a fixed Suzuki/CCM normalization |
| Positive escape: normalization + local boundedness `M_R` + identification (Taylor jet w/ summable tail) + nonzero limit + effective modulus `N(R,ε)` | Montel/Vitali compactness identifies limit; Hurwitz transfers real zeros | classical complex analysis | **OPEN packaging** — value is translating to CCM/Suzuki exact normalization |
| Suzuki meromorphic transfer (`z²ξ/ξ'`, poles at zeros) | reciprocal / argument-principle version of Hurwitz | Hurwitz (entire only); Rouché | **OPEN + risky** — real technical obstacle (see risk register) |

### Paper A (WP-B) — finite observables ⇏ critical-line support  ·  conditional

| Aspect | This program | Prior art | Delta |
|---|---|---|---|
| B1: fixed finite family of strict positivity tests (first `K` Li, finite Weil family, fixed-order Hausdorff/Stieltjes) fails to discriminate | high off-line quartet, small contribution | **Báez-Duarte / Burnol**: NB approximation lower bound `~1/√log n`, sharpened by zeros; **Voros**: Li asymptotics differ off-line; internal **P21** (fixed-order Hausdorff non-discrimination) | **THIN** — fixed-`K` non-discrimination is close to known; P21 already did a version |
| B2: *exact* finite-observation collision `O_Φ(𝒵₊)=O_Φ(𝒵₋)`, `P` differs | full-rank Jacobian / implicit function; canonical product realization | truncated moment theory (**Curto–Fialkow** flat extension; **Bayer–Teichmann** Tchakaloff) | **OPEN if** collision realizable with real, positive-integer multiplicities; else collapses to B1 |
| B3: truncated moment support non-uniqueness | interior truncated moment vector has multiple representing measures | Curto–Fialkow; standard truncated moment problem | **THIN** — build on, don't reprove |

### Paper B (WP-D) — spectral-asymptotic exclusion  ·  conditional on novelty

| Aspect | This program | Prior art | Delta |
|---|---|---|---|
| Classical compact elliptic class: `N_H(T)~C T^{d/m}` ≠ `T log T` Riemann–von Mangoldt; heat trace `t^{-1}log(1/t)` vs polyhomogeneous Seeley–DeWitt | fix eigenvalue map + perturbation class | **Endres–Steiner 2010** (Berry–Keating no-go on compact quantum graphs by Weyl asymptotics) | **THIN** — raw Weyl mismatch ≈ textbook; needs exact determinant order/type obstruction or a materially broader invariant class to be new |

### Paper D (WP-F) — restricted Schur-certificate complexity  ·  exploratory

| Aspect | This program | Prior art | Delta |
|---|---|---|---|
| Lower bound `κ(a,δ) ≥ g(a,δ)` for a FROZEN certificate system (Galerkin `G_{a,N}`, `M_{a,N}`, bounded residual rank) | proof-system / numerical-analysis lower bound | SOS / Positivstellensatz degree lower bounds; complexity barriers (BGS/RR/AW) as methodology only | **OPEN but gated** — non-vacuous only after representation-invariance gate; must not become a universal `c_a` claim |

### WP-C — finite-Euler-factor freedom (Helson)  ·  supporting

| Aspect | This program | Prior art | Delta |
|---|---|---|---|
| No rule on finitely many Euler factors forces RH-like zero location across the Helson class | prescribed-zero + modify finite Euler factors | **Andersson 2024** (Mittag-Leffler for Helson zeta); **Davenport–Heilbronn** (FE without Euler product ⇒ off-line zeros) | **OPEN-ish** — standalone only if it adds a fixed-local-factor refinement to Andersson; else a section of Paper A |

### EXT-4 audit — Selberg class prescribed-zero theorem (literature gap confirmed)

| Aspect | Assessment | Source |
|---|---|---|
| Does a prescribed-zero theorem for the Selberg class S exist? | **NO** — and the Selberg axioms are **incompatible** with free zero prescription | EXT-4a search (2026-08-11) |
| Functional equation constraint | Forces zeros symmetric under Re(s)=1/2; arbitrary Z ⊂ strip not realizable | Kaczorowski-Perelli degree theory |
| Euler product + Ramanujan constraint | Ties zero density to N(T) ~ (d/2π)T log T; prescribing arbitrary Z violates this | Selberg class axioms |
| Steuding universality | Controls value-distribution, not zero-prescription; no elements of S with prescribed zeros | Voronin-type results |
| Kaczorowski-Perelli structure | S is extremely rigid (degree classification, conductor); free zero choice ≈ unsolved inverse problem | Structure theory |
| Implication for Theorem C | **Scope correctly set at Helson class.** Selberg escape route is genuine and currently unbreachable. | EXT-4a |
| Would a Selberg prescribed-zero theorem be possible? | Likely as hard as GRH itself — constructs arithmetic {a(n)} satisfying all axioms with target zeros | — |

**EXT-4a verdict:** Theorem C cannot be extended to the Selberg class by the same method (Andersson construction requires free choice of χ on primes, incompatible with Ramanujan + FE). The escape route "full Selberg class" is confirmed genuinely open. Theorem C's scope at the Helson class is correct and optimal for this method.

---

## Cross-cutting cautions (from prior art)

1. **NB/Li precedent (Burnol, Báez-Duarte, Voros).** These already show finite/asymptotic
   approximation difficulty *without* claiming the criteria cannot prove RH. Paper A's
   danger is being read as a restatement of this. Mitigation: only publish A if B2 (exact
   collision) is genuinely new; otherwise fold into a lemma of C.
2. **Davenport–Heilbronn vs finite-Euler must stay separate.** One object lacking a
   functional equation and another lacking an Euler product do NOT jointly prove off-line
   zeros survive both axioms (program §8.C.2).
3. **Ambient-class grading (program §4.3).** A theorem on symmetric zero multisets is not
   a theorem about ζ; the missing structure (exact Euler product, gamma factor,
   continuation, coefficient arithmetic) is the escape route and must be named.

## References (verified)

- Suzuki, arXiv:2606.09096 (2026) — source in `baseline/`.
- Connes–Consani–Moscovici, arXiv:2511.22755 (2025) — source in `baseline/`.
- Connes–Consani, arXiv:2006.13771, Selecta Math. 27 (2021).
- Burnol, arXiv:math/0103058, Adv. Math. 170 (2002); Báez-Duarte, arXiv:math/0205003.
- Voros, arXiv:math/0506326.
- Curto–Fialkow, Memoirs AMS 136 (1998) doi:10.1090/memo/0648; Bayer–Teichmann, arXiv:math/0502473.
- Andersson, arXiv:2408.15713 (2024).
- Endres–Steiner, J. Phys. A 43 (2010) doi:10.1088/1751-8113/43/9/095204.

> Prior-art status here is best-effort from named anchors; each `theorems/<id>/novelty.md`
> must run a fuller search before that theorem is frozen (program §9.D.5, §14.3).
