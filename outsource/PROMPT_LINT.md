# outsource/PROMPT_LINT.md — standing adversarial checklist for RH-obstruction outsource prompts

Every recurring defect a referee found in `OB-01..OB-13` is listed here as a **check that
must actually be RUN** — a script, a `grep`, or an explicit derivation — never a prose
"looks fine". Run **all applicable** checks on every new or edited prompt before it ships,
and record the run in the prompt's pre-send note.

**Re-scan rule (load-bearing).** The same conceptual error was repeatedly copied across
prompts *and into the theorem files themselves* (e.g. the order-definition error hit OB-05
and the parity error hit OB-06; the growth-transfer gap hit OB-11 **and** was then found in
E-compactness E-pos by re-scan). When a referee surfaces a new defect class: (1) add it
here, (2) re-scan **every** active prompt AND every `theorems/*/statement.md|proof.md` for
the same error, (3) fix all copies. A defect is never assumed independent.

This complements the five-point pre-send checklist in `../CLAUDE.md`
("Outsource-prompt pre-send checklist"); that checklist is the meta-gate, this file is the
domain-specific defect catalog.

---

## L1 — Order: conventional/Nevanlinna order ≠ finite exponential type (hit OB-05)
NEVER write "order ≤ 1" as `|f(z)| = O(e^{C|z|})`. That is **finite exponential type**,
strictly stronger. CHECK: state which you mean. Conventional order is
`ρ(f) = limsup_{r→∞} log log M_f(r) / log r`; Nevanlinna order uses `T(r,f)`. The Riemann
`Ξ` has conventional order 1 but is **NOT** of finite exponential type
(`log|Ξ(iy)| ∼ (y/2)log(y/2)`). If a Hadamard/uniqueness step needs order ≤ 1, cite the
conventional/Nevanlinna definition, not a pointwise exponential bound.

## L2 — Parity of the target, recomputed from the functional equation (hit OB-06)
NEVER assert the target's parity; DERIVE it. CHECK by script/hand from `ξ(s)=ξ(1−s)`:
`X(z)=ξ(1/2−iz)` is even; differentiating gives `ξ'(s)=−ξ'(1−s)`, so `ξ'(1/2−iz)` is
**odd**; hence `W(z)=z²ξ(1/2−iz)/ξ'(1/2−iz)` is **ODD**. A sequence of even functions
cannot converge to an odd target. Verify: `W(−z) =? −W(z)` symbolically at a sample point.

## L3 — Zero vs pole role of γ_n (hit OB-06)
NEVER assume `γ_n` (a zero of ξ) is a pole of a derived function. CHECK the local
expansion: for `W=z²ξ/ξ'`, an order-`m` zero of ξ at `1/2−iγ` gives a **simple zero** of
W at `z=γ`: `W(z) = −iγ²/m·(z−γ)+O((z−γ)²)` — no residue there. Poles of W come from zeros
of `ξ'` not cancelled by ξ. Compute the leading Laurent/Taylor coefficient before calling
anything a pole or writing a residue.

## L4 — Canonical product genus / spurious exponential (hit OB-06)
For symmetric zeros `±z_j` with `Σ|z_j|^{-2}<∞`, the correct paired product is
`∏(1−z²/z_j²)`. CHECK: `∏(1−z²/z_j²)·e^{z²/z_j²}` inserts a spurious `exp(z²·Σz_j^{-2})`
of **order 2** — verify via `E_1(z/a)E_1(z/−a) = (1−z/a)e^{z/a}(1+z/a)e^{−z/a} = 1−z²/a²`
(the exponentials cancel in the pair). Never carry an unpaired `e^{z²/z_j²}` factor.

## L5 — RH imported via the divisor (hit OB-05, OB-08)
Writing `Ξ(z) = Ξ(0)∏(1−z²/γ_n²)` with `γ_n` **real** and exhausting the zero divisor
**IS RH**. CHECK: is the divisor asserted real/on-line? If so, that is a hypothesis, and it
is RH — forbidden (CLAUDE.md, no RH-equivalent as premise). Use the unconditional **complex**
divisor `ω_n ∈ ℂ` (`ω_ρ = γ − i(β−1/2)`), and keep `F_γ ≠ Ξ_R` unless RH is separately
invoked. grep the prompt for "real zeros", "on the critical line", "γ_n real".

## L6 — Vacuous target: real atoms / free-parameter inflation (hit OB-07)
CHECK the ambient class does not admit atoms invisible to both the observation and the
predicate. Real atoms `{1/4, 3/4}` are invisible to a positive-imaginary-part observation
and flip the predicate → trivial collision. Impose `(NR): 𝒵∩ℝ=∅` or fold real atoms into
the observation. Also: pin comparison scales to a fixed arithmetic quantity (`o(log λ)`),
never `o(g(N))` with free `N`. Exhibit the trivial counterexample and confirm the class
excludes it.

## L7 — Counting-function factor/sign, recomputed (hit OB-07)
Recompute every count. CHECK: one on-line pair `L(t)` contributes **one** point with
`Im>0`; one quartet `Q(3/4,T)` contributes **two**. So `N_{A_+}(x)=mM`, not `2mM`; and
`N_{A_-}−N_{A_+}=Σn_k+2R`, which **need not be positive** (n_k may be negative). Verify the
displayed counting formula against a direct enumeration for a 2-atom example.

## L8 — Global observation map + Σ' convention defined (hit OB-07, OB-13)
CHECK `O_j` is defined on an **arbitrary** finite multiset, not only on `L(t)`/`Q`. The
factor (4 vs 2) in orbit formulas is fixed **only** by the global definition
`O_j(𝒵)=Σ_{ρ∈𝒵}[φ_j(ρ)+φ_j(1−ρ)]`. Also state the reality hypothesis `φ_j(z̄)=φ_j(z)‾`
(needed for `O_j∈ℝ`) and, for infinite multisets, an orbit-decay bound (OD) for absolute
convergence. Write the convention in the "All definitions" block; do not leave it implicit.

## L9 — Growth is DERIVED not assumed; |W(iR)|→∞ is often false (hit OB-09)
NEVER assume the target blows up along a ray. CHECK: `|W(iR)|` can → 0 — explicit
counterexample `A=sin(πz)/(πz)`, `B=z cos(2πz)` gives `|W(iR)|=sinh(πR)/(π cosh 2πR)→0`.
Any separation argument must use a Cauchy coefficient estimate on a **finite** disk (radius
`< dist(0, poles)`), not a growth-to-∞ claim. Follow "grows / blows up" remarks to their
arithmetic end.

## L10 — Power-sum matching ≠ Taylor jet at a nonzero base point (hit OB-09)
CHECK: matching power sums `P_r` controls the expansion of `log(A^{(c)}/A)` **at z=0**
(gives `A^{(c)}−A = O(z^{2J+2})` near 0). It does **NOT** give `A^{(c)}(w₀)=A(w₀)` at a
nonzero `w₀`, nor the `w₀`-Taylor jet. If the method matches a jet at `w₀≠0`, build the IFT
system from `Ψ_j(u,c)=∂_t^j L(t₀;u,c)` (a Wronskian–Vandermonde Jacobian), not from `Φ_r`.
Verify the base point actually satisfies the stated system: `Φ(u⁰,0) =? 0` (frozen first-k
terms are a common omission — see L11).

## L11 — Frozen terms dropped from the IFT/matching system (hit OB-09)
CHECK the base point is a zero of the stated equations. If the first `k` objects are frozen,
the matching functional must subtract only the **free** tail: `Σ_{ℓ}u_ℓ^r + Σ_m b_m(c)^r −
Σ_{n>k}a_n^r = 0`. A system summing over all `n≥1` gives `Φ(u⁰,0) = −Σ_{n≤k}a_n^r ≠ 0` —
IFT cannot start. Also verify the perturbation denominator matches the definition
(`b_m'(0) = −2y_m/(J+m)`, not `/m`).

## L12 — Odd/even parity of the leading discrepancy degree (hit OB-09)
CHECK the first nonzero term's degree matches the function's parity. If `F−W` is **odd**,
its leading term is `z^{2J+3}` (odd), NOT `z^{2J+2}`. A claimed even leading degree for an
odd difference is a sign the assembly dropped the `z²/B(z)` parity factor. Recompute the
leading coefficient including all factors.

## L13 — Fredholm determinant zeros and normalization target (hit OB-08)
CHECK: `det(I−z²K) = ∏(1−z²λ_j)` has zeros at `z=±λ_j^{-1/2}`, NOT `±λ_j^{1/2}`. A diagonal
`κ_n=1/(1/4+d_n²)` gives determinant zeros at `±√(1/4+d_n²)`, NOT `±d_n`. And `det(I−0·K)=1`
forces the local-uniform-limit target to satisfy `f(0)=1`: normalize to `Ξ̂=ξ(1/2+iz)/ξ(1/2)`,
never unnormalized `ξ`. Verify the zero locations and `f(0)` by a 1-term example.

## L14 — Per-n bound ≠ uniform bound; divisor+normalization ≠ identity; envelope must match the target's type (hit OB-11; re-scan hit E-pos; OB-14 refined)
CHECK two distinct things before claiming a limit `G` equals the target:
(a) **Growth transfer.** Local uniform boundedness (even uniform in n on each compact) does
NOT bound the order of `G`. Counterexample: `F_n ≡ Target·e^{z²−w₀²}` is a constant sequence,
bounded on every disk, same divisor, `F_n(w₀)=Target(w₀)` — but its limit has order 2 ≠
target. A **uniform** order envelope is required; a per-n bound with n-dependent constant is
insufficient (OB-14 §5: even Taylor polynomials of the order-2 `G`, each order 0, converge
to `G`).
(b) **The envelope must match the target's type (L1 again!).** Use `T(r,F_n) ≤ C_ε r^{1+ε}
+ C_{0,ε}` (uniform *conventional order* ≤ 1), NOT `T(r,F_n) ≤ Cr+C_0` (uniform *finite
exponential type*). A uniform *linear* bound transfers to `T(r,Target) ≤ Cr+C_0`, forcing
finite exponential type — **incompatible with Ξ**, which has infinite type
(`log|Ξ(iy)| ∼ (y/2)log(y/2)`), making the theorem vacuous (OB-14 §4.3). This is the L1
error wearing a "uniform bound" disguise; it bit the E-pos fix and had to be re-corrected.
(c) **Identity.** Same complete divisor + one-point normalization only give `G = Target·H`
with `H` zero-free (`H(w₀)=1`); they do NOT force `H≡1` without the order envelope in (a)/(b).
(d) **Divisor convergence must be two-sided + multiplicity-complete.** A one-sided
"no-intrusion" clause is vacuous for zero-free approximants (OB-14 §4.1: `F_n ≡ Target(w₀)`
satisfies it). Require the disk form: zeros of `F_n` in `|z|<R` converge to those of the
target *with multiplicity, and no others* (Rouché). Run: does `Target·e^{z²−w₀²}` (and the
constant `Target(w₀)`) satisfy every stated hypothesis? If yes, the hypotheses are insufficient.

## L20 — Fourier multiplier on ℝ has continuous spectrum; discrete/trace-class needs a compact manifold or ℓ² model (hit OB-16)
NEVER attach a discrete eigenvalue count or trace-class heat kernel to a Fourier multiplier
`h(D)` on `L²(ℝ)`. CHECK the Hilbert space: on `L²(ℝ)`, `h(D)` is unitarily multiplication
by `h(ξ)`, spectrum = essential range, **purely continuous** (every level set has measure
zero), and `e^{-tH}` is a nonzero multiplication operator on a nonatomic space — **not
compact, not trace class**. Discrete `λ_n`, `N_H(T)`, `Tr(e^{-tH})` are undefined there.
For a discrete spectrum use a **closed manifold** (e.g. `S¹`: frequencies `n ∈ ℤ`) or a
diagonal `ℓ²(ℕ)` model. Only the closed-manifold realization is relevant to membership in a
ΨDO class `𝒞_ell`/`𝒞_logpoly`. Also: classify the symbol correctly — `|ξ|/log|ξ| ∈ S¹_{1,0}`
(Hörmander), a log-weighted `S^{1,-1}` class; "outside all standard calculi" is usually too
strong (it is outside `𝒞_ell` and finite-log-degree `𝒞_logpoly`, but inside `S^m_{1,0}`).

## L15 — Zeros-in-Ω vs zeros-in-ℂ; pole non-cancellation (hit OB-11)
CHECK that tail/zero-control covers the target's **poles**, not just `Ω=ℂ∖poles`. A zero of
`F_n` sliding onto a target pole `p` can cancel it, so the limit drops `p` from its polar
divisor while satisfying an Ω-only zero condition. Require full-plane tail no-intrusion
(`ZT_ℂ`: every zero in `{|z|≤R}`, including at poles, is a matched zero) **and** a local
"no zeros in the pole disk" condition (`PL⁺`). Exhibit the rational-multiplier
pole-cancellation family and confirm the hypotheses now exclude it.

## L16 — Representation invariance / measure collapse (hit OB-12; CLAUDE.md discipline)
NEVER let a "complexity" or "margin" be a basis/representation artifact. CHECK: is the
proposed measure invariant under every transformation the method class allows (orthogonal
congruence, rescaling, preconditioning)? If it is orthogonally invariant it factors through
the **eigenvalue multiset** (spectral theorem) — so it cannot detect eigenvector
localization, and a "growth from delocalization" claim is false. If it is basis-dependent,
it can be reduced to a constant by choosing the eigenbasis — a representation artifact, not
a lower bound. Also CHECK the measure does not collapse to a constant (`1`, `N`, `⌈N/b⌉`) or
to `{k, +∞}`: exhibit its value on 2–3 explicit matrices. A margin that stays provable while
→ 0, or a `−c_a` shift, is a diagnostic, not a barrier (reconcile with `λ(a)`).

## L17 — Cited black boxes: exact theorem number AND scope (hit OB-01, OB-10)
For every "may be used freely" citation: verify author/year/**exact number** and that its
hypotheses cover the object used. Known live corrections:
- Hurwitz zero-free corollary: **Conway VII.§2 Cor. 2.6** (Thm 2.5 is zero-counting);
  Ahlfors 3rd ed. **p. 178** (not 176). Montel: **Conway VII.2.9**.
- Hadamard factorization: **Conway XI.3.4**.
- Heat-trace no-log: **BGV Thm 2.30** covers only **Laplace-type** (order-2 differential);
  **Gilkey Lemma 1.8.2** (not Thm 1.8.1) covers **differential** operators only; general
  classical ΨDO need **Grubb–Seeley 1995 Thm 2.7** / **Lesch 1999 Thm 3.7** — and Lesch's
  theorem is about `Tr(A·e^{-tP})` (weighted, `P` classical), NOT `Tr(e^{-tH})` for
  log-polyhomogeneous `H`. Confirm the citation's object is literally the object used.
- Suzuki Cor. 6 target is **meromorphic** `z²ξ/ξ'`; CCM target is **entire** `Ξ̂` — distinct
  normalizations, never conflated.

## L18 — Numerical anchor verified by script, labeled "sanity only" (hit all; discipline)
Every numerical anchor must be (a) recomputed by an independent script before shipping,
(b) labeled "sanity only, not an input" unless the task IS a reconstruction (OB-13), and
(c) exact (rational/interval), never a float when a rational is available. For
reconstruction tasks, also require: independent re-derivation (not the producer's script),
closed-form nonsingularity (not just numerical `det≠0`), and an adversarial mutation guard
(perturb one field → residual must become nonzero).

## L19 — Verdict space allows honest inconclusive (hit OB-11 pattern; CLAUDE.md #4)
CHECK the acceptance criteria admit CONFIRMED / PARTIAL / REFUTED / **INCONCLUSIVE +
precise localization**. Never force a prove-X-or-prove-obstruction dichotomy. A referee
finding "hypotheses insufficient for step N + here is the minimal fix" must be a valid,
first-class outcome.

---

### Self-containment gate (CLAUDE.md checklist #5, always)
Every symbol/formula/premise defined in-file; proved results inlined as premises; full
formulas written out (not point values); no "see other file" for load-bearing content
(`grep -n "see .*\.md"` must return only provenance references). Run:
`grep -n "see .*\.md\|see statement\|see proof" outsource/OB-NN*.md`.
