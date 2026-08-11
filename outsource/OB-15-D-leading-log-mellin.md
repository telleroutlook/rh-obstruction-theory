# Problem OB-15 — D: leading heat-trace singularity of a positive elliptic ΨDO is a pure power (no log)

**Type:** analysis (heat-trace / spectral zeta, Mellin transform, complex elliptic ΨDO)

**Non-circularity:** RH is not assumed and does not appear in any hypothesis. This is a
statement about the small-`t` asymptotics of `Tr(e^{-tH})` for an abstract positive
elliptic pseudodifferential operator `H` on a closed manifold. The Riemann object enters
only as the *comparison* target `Z_ζ(t)`, whose leading singularity is computed
separately and unconditionally from the Riemann–von Mangoldt counting law (no zero
locations used).

---

## All definitions (self-contained — everything is here)

### The operator class 𝒞_ell

`H ∈ 𝒞_ell` if `H` is a classical (polyhomogeneous) pseudodifferential operator on a
closed (compact, boundaryless) smooth manifold `M` of dimension `d ≥ 1`, of order
`m > 0`, positive and self-adjoint with discrete spectrum
`0 < λ_1 ≤ λ_2 ≤ … → ∞` (finite multiplicities). "Classical" means the full symbol has an
asymptotic expansion `σ(H) ~ Σ_{j≥0} σ_{m-j}(x,ξ)` with `σ_{m-j}` positively homogeneous
of degree `m-j` in `ξ` for `|ξ| ≥ 1`.

### Spectral zeta and heat trace

```
ζ_H(s) := Σ_{n≥1} λ_n^{-s}   (converges for Re s > d/m; meromorphic continuation exists),
Z_H(t) := Tr(e^{-tH}) = Σ_{n≥1} e^{-t λ_n}   (t > 0).
```
They are related by the Mellin transform:
```
Z_H(t) = (1/2πi) ∫_{(c)} Γ(s) ζ_H(s) t^{-s} ds     (c > d/m),
```
and `Γ(s) ζ_H(s) = ∫_0^∞ Z_H(t) t^{s-1} dt` on `Re s > d/m`.

### The comparison target (Riemann side)

For the (hypothetical) spectrum `{γ_n}` = positive ordinates of nontrivial ζ-zeros with
counting `N(T) = #{γ_n ≤ T} = (T/2π)log(T/2π) − T/2π + O(log T)` (Riemann–von Mangoldt,
unconditional — no zero *locations*, only the count), define
```
Z_ζ(t) := Σ_{n≥1} e^{-t γ_n}.
```

---

## The theorem to be verified

**Theorem (leading-log obstruction).** Let `H ∈ 𝒞_ell` (order `m > 0`, dimension `d ≥ 1`).
Then the leading small-`t` singularity of `Z_H(t)` is a **pure power**:
```
Z_H(t) = a_0 t^{-d/m} + o(t^{-d/m})   as t → 0⁺,   a_0 > 0.                    (T1)
```
No term `C · t^{-d/m} · log(1/t)` with `C ≠ 0` occurs as the **leading** singularity.

Consequently, since (computed separately, T2 below)
```
Z_ζ(t) = (1/2π) · log(1/t) / t + O(1/t)   as t → 0⁺,                           (T2)
```
`Z_H` and `Z_ζ` have incompatible leading singularities (pure power `t^{-d/m}` vs
`t^{-1} log(1/t)`), so no `H ∈ 𝒞_ell` has spectrum `{γ_n}`.

---

## Proof skeleton to be closed

### Step 1 — Meromorphic structure of ζ_H (cite exactly; confirm scope)

For `H ∈ 𝒞_ell`, `ζ_H(s)` continues meromorphically to `ℂ` with **at most simple** poles
located at `s = (d-k)/m`, `k = 0, 1, 2, …` (and the values at `s = 0, -1, -2, …` are
finite — the trivial `Γ`-poles are cancelled). The rightmost pole is at `s = d/m > 0`,
simple, with residue `Res_{s=d/m} ζ_H(s) = a_0·m/Γ(d/m) > 0` proportional to the
principal-symbol integral `∫_{S^*M} σ_m^{-d/m} dξ dx > 0`.

**What to close for Step 1:**
- Cite the exact theorem giving simple poles of `ζ_H` at `s=(d-k)/m` for a **classical
  ΨDO** (not merely a differential/Laplace-type operator). Candidates to verify by
  number and scope:
  - **Seeley 1967** (Amer. Math. Soc. Proc. Symp. Pure Math. 10) — complex powers,
    meromorphic continuation of `ζ_H`;
  - **Grubb–Seeley 1995** (Invent. Math. 121), Thm 2.7 — resolvent/heat expansion for
    the classical calculus;
  - **Gilkey**, *Invariance Theory…*, for the differential case (Lemma 1.8.2) — NOTE
    scope: differential operators only; confirm it is NOT the citation used for the
    general ΨDO claim.
- **Critical scope check (documented past error, PROMPT_LINT L17).** BGV Thm 2.30 covers
  only Laplace-type (order-2 differential) operators; it does NOT cover general classical
  ΨDO. The general no-leading-log result must rest on Seeley / Grubb–Seeley / Lesch, and
  Lesch 1999 Thm 3.7 is about the **weighted** trace `Tr(A e^{-tP})` with `P` classical
  and `A` log-polyhomogeneous — confirm which theorem literally gives the leading-term
  statement for `Tr(e^{-tH})`, `H ∈ 𝒞_ell`.

### Step 2 — Mellin inversion: simple pole at d/m gives pure power, no log

Pull the contour in `Z_H(t) = (1/2πi)∫_{(c)} Γ(s)ζ_H(s) t^{-s} ds` left past `s = d/m`.
The residue at `s = d/m`:
- `Γ(s)` is **regular** at `s = d/m` (since `d/m > 0`, away from `Γ`'s poles at
  `0, -1, -2, …`);
- `ζ_H(s)` has a **simple** pole there.
So the product `Γ(s)ζ_H(s)` has a **simple** pole at `s = d/m`, whose residue produces a
term `∝ t^{-d/m}` — a **pure power**, no `log(1/t)`.

A `t^{-d/m} log(1/t)` term would require a **double** pole of `Γ(s)ζ_H(s)` at `s = d/m`,
i.e. `d/m ∈ {0, -1, -2, …}` (so that `Γ`'s pole coincides with `ζ_H`'s pole). Since
`d, m > 0`, `d/m > 0`, this is impossible.

**What to close for Step 2:**
- Confirm the residue of a simple pole under `Mellin^{-1}` yields exactly `c·t^{-d/m}`
  (state the elementary computation `Res_{s=α}[Γ(s)ζ_H(s)t^{-s}] = (Res ζ_H)·Γ(α)·t^{-α}`
  for `Γ` regular at `α`).
- Confirm that a `log(1/t)` factor at the leading order requires a double pole, and that
  `d/m > 0` rules it out. (Subleading logs at `t^k`, `k ≥ 1`, from `Wres(H^k) ≠ 0`, are
  allowed and irrelevant to the *leading* singularity — state this so the argument is
  correctly scoped and does not repeat the refuted "no logs at any order" claim.)
- Justify the contour shift (growth of `Γ(s)ζ_H(s)` in vertical strips — standard
  polynomial bound on `ζ_H` times exponential decay of `Γ`).

### Step 3 — Leading singularity of Z_ζ (Riemann side, unconditional)

From `N(T) = (T/2π)log(T/2π) − T/2π + O(log T)`, by Abel summation /
Laplace–Stieltjes:
```
Z_ζ(t) = ∫_0^∞ e^{-tu} dN(u) = t ∫_0^∞ e^{-tu} N(u) du.
```
The leading term: `t∫_0^∞ e^{-tu}(u log u/2π) du`. Split `u log u = u log(1/t) + u log(tu)`:
```
t∫ e^{-tu} u log(1/t) du = log(1/t)·t·t^{-2} = log(1/t)/t,
t∫ e^{-tu} u log(tu) du = t^{-1}∫ e^{-v} v log v dv = O(1/t)   (∫e^{-v}v log v dv = 1−γ_E, finite).
```
So `Z_ζ(t) = (1/2π) log(1/t)/t + O(1/t)`. The `O(log T)` error in `N` contributes only
`O(log(1/t))`, absorbed in `O(1/t)`.

**What to close for Step 3:** Confirm the Abel-summation identity and the two integrals;
confirm the error-term bookkeeping. (This is self-contained; no zero locations used.)

### Step 4 — Incompatibility

`t^{-d/m}` (or `a_0 t^{-d/m}`, pure power) vs `(1/2π) t^{-1} log(1/t)`: even if `d/m = 1`,
the Riemann side carries a `log(1/t)` factor at the leading order that the ΨDO side
cannot. Hence `Z_H ≠ Z_ζ`, so `spec(H) ≠ {γ_n}`.

---

## Acceptance criteria

1. **CONFIRMED:** Steps 1–4 closed with **exact** theorem-number-and-scope citations for
   the meromorphic structure of `ζ_H` (Step 1) valid for the **full classical ΨDO class**,
   the Mellin residue computation (Step 2), and the Abel-summation leading term (Step 3).
   The scope caveat (BGV/Gilkey cover only differential/Laplace-type; general ΨDO needs
   Seeley/Grubb–Seeley/Lesch) is explicitly resolved.

2. **PARTIAL:** Steps 2–4 confirmed, but the Step-1 citation for the full classical class
   is not pinned to an exact theorem covering the exact object (state what is missing).

3. **REFUTED:** if a positive classical elliptic ΨDO can in fact have a leading
   `t^{-d/m} log(1/t)` term (i.e. a double pole of `Γζ_H` at `d/m`), give the explicit
   operator and symbol. (This would refute Theorem D as corrected.)

4. **INCONCLUSIVE + localization:** name any citation whose scope cannot be confirmed
   from standard references.

All outcomes decisive. "The result is standard" is not CONFIRMED without a theorem number
whose hypotheses are checked against `H ∈ 𝒞_ell`.

---

## Numerical anchor (sanity only — not an input)

For `Z_ζ(t) = (1/2π)log(1/t)/t + O(1/t)`: a numerical Abel-summation approximation of
`t∫_0^∞ e^{-tu} (u log u/2π) du` against the closed-form leading `(1/2π)log(1/t)/t` gives
ratios approaching 1 slowly (t=0.01 → 1.092, t=0.003 → 1.073, t=0.001 → 1.061 — the gap
is the `O(1/t)` term, which is only `log`-suppressed relative to the leading
`log(1/t)/t`, so convergence of the *ratio* is slow but monotone toward 1). This confirms
the leading singularity carries the `log(1/t)` factor. (Script-verified.) The Mellin/pole
side (Steps 1–2) is the analytic content; this anchor only sanity-checks the Riemann-side
leading coefficient `1/2π`.
