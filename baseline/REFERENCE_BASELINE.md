# REFERENCE_BASELINE.md — canonical definitions and notation

**Purpose (Gate A, program §6.A.3).** One place fixing the exact definitions and
conventions the whole program uses, so that every legacy symbol (`L`, `c_L`, matrix
blocks, support thresholds from the earlier Weil-window work) is mapped onto the current
literature's `a`, `Q_W^a`, `λ(a)` baseline. **All formulas below are transcribed from the
arXiv source in `baseline/` and cited by equation/theorem number** — not from memory.

Sources: Suzuki 2606.09096 (`screwzelf_7.tex`), CCM 2511.22755 (`mc2arXiv.tex`).

---

## 1. The Weil functional (Suzuki, Introduction)

For test functions `f`,
```
W(f) := ∫_{-∞}^{∞} f(x)(e^{x/2}+e^{-x/2}) dx
        − Σ_{n≥1} Λ(n)/√n · f(log n)
        − Σ_{n≥1} Λ(n)/√n · f(−log n)
        − (log 4π + C₀) f(0)
        − ∫_0^∞ { f(x) + f(−x) − 2e^{−x/2} f(0) } · e^{x/2} dx / (e^x − e^{−x}),
```
where `Λ` is the von Mangoldt function and `C₀` the Euler–Mascheroni-type constant of the
functional. The associated quadratic form is `Q_W(v) := W(v * ṽ)`, `ṽ(x) = conj(v(−x))`.

**Legacy-notation map.** In the earlier finite-window work the "prime layer" was
indexed by `p^m ≤ e^{2L}` and the archimedean/pole terms were split off separately. Here:
- support radius `L` (legacy) ⟷ **`a`** (baseline). The convolution `v * ṽ` is supported
  in `(−2a, 2a)`, so the prime term of `Q_W^a` involves only `n ≤ e^{2a}` — the finite
  prime data is a *consequence* of localization, not a separate cutoff choice.
- the archimedean/pole pieces are **not** a separate matrix block to be balanced against
  the prime block; they are the smooth terms of the single functional `W(f)` above.
- the "Weil constant" `c_L = log(2πL) + γ_E` (legacy, appearing as `−c_L I` in an
  unnormalized Schur reduction) has **no invariant status**. See §4.

---

## 2. Localized form, operator, and the invariant margin (Suzuki §1–§4)

**Localized form** (following Connes–Consani, Connes–Consani–Moscovici):
```
Q_W^a := Q_W |_{L²(−a,a)}                                    [Suzuki, after eq. before EQ_101]
```
is lower bounded and lower semicontinuous [CC23 §2]. There is a canonical densely defined
self-adjoint operator `A_a` on `L²(−a,a)` with
```
Q_W^a(v) = ⟨A_a v, v⟩_{L²}   for v ∈ 𝔇(A_a) ⊂ 𝔇(Q_W^a) ⊂ L²(−a,a).   (EQ_101)
```
`A_a` is the **Friedrichs extension** of the symmetric (non-self-adjoint) operator
`B_a := D* G_a D`, `𝔇(B_a) = H₀¹(−a,a)` (EQ_106, Thm 1.1). `𝔇(A_a)` is strictly larger
than `H₀¹(−a,a)` and contains constants.

**The representation-invariant margin** (the object this program treats as canonical):
```
λ(a) ≡ λ_a := inf_{0 ≠ v ∈ 𝔇(Q_W^a)}  Q_W^a(v) / ‖v‖²_{L²}.        (EQ_107)
```
Equivalently `λ_a = inf ⟨A_a v,v⟩/‖v‖²`; by Cor 2 the infimum may be taken over
`C_c^∞(−a,a)` in the form norm. Spectrum of `A_a` is bounded below and discrete with `+∞`
the only accumulation point, so `λ_a` is attained (an eigenvalue).

**Form norm** used throughout:
```
‖v‖²_{Q_W^a} := Q_W^a(v) + (1 − λ_a)‖v‖²_{L²}.
```

---

## 3. The screw function (Suzuki §1, eq. EQ_103; Su23 Thm 1.2)

```
g(t) = −4(e^{t/2}+e^{−t/2}−2)
       + Σ_{n ≤ exp(|t|)} Λ(n)/√n · (|t| − log n)
       − (|t|/2)(ψ(1/4) − log π)
       − ¼( Φ(1,2,1/4) − e^{−|t|/2} Φ(e^{−2|t|}, 2, 1/4) ),
```
`ψ` = digamma, `Φ(z,s,a) = Σ_{n≥0} z^n/(n+a)^s` (Lerch). `g` is a *screw function* (kernel
`g(t−u) − g(t) − g(−u) + g(0) ≥ 0`) in the Krein–Langer sense **iff RH holds** [Su23
Thm 1.2]. `Q_W^a` is built from this kernel; `G_a` in `B_a = D*G_a D` is the associated
integral operator.

> Note the internal `Σ_{n ≤ exp(|t|)}` cutoff: the prime data entering `g` at "time" `|t|`
> is again finite and tied to the localization, echoing the `n ≤ e^{2a}` fact for `Q_W^a`.

---

## 4. Why `c_L` / `−c_a I` is NOT the invariant (the core correction)

Suzuki Thm 1.4: for sufficiently small `a>0`,
```
λ(a) = log(1/a) + μ₁ − log(2π) + ψ(2) − 1 + O(a),      μ₁ > 0,   (a → 0⁺)
```
`λ(a) > 0`, simple, even eigenfunction.

- The **`log(1/a)`** here is the *leading positive term* of the invariant margin — it is
  what makes `Q_W^a` positive for small `a`.
- The legacy **`−c_L I = −(log(2πL)+γ_E) I`** appeared as a *negative* shift eroding a
  basis-dependent pivot/Schur residual.
- Same `log` scale, opposite sign of effect, under a change of representation. Therefore
  the "growing `c_L` exhausts the margin" picture was a **representation artifact**, not a
  statement about the invariant. `λ(a)` is smooth and (for small `a`) large-and-positive.

**Rule for any `−c_a` argument (program §11.F.3):** it may be used only after (i) the
exact identity in the standard `Q_W^a` normalization, (ii) invariance under every allowed
congruence/preconditioner, (iii) an upper bound on the compensating positive operator in
the same norm, (iv) a conclusion stronger than "margin → 0", and (v) consistency with the
`λ(a)` asymptotic above. Absent these it is a frozen-system diagnostic only.

---

## 5. Characteristic function and the two convergence targets

**Suzuki `W(a,θ;z)` (Thm 1.5).** With `v_±(a,x)` the eigenfunctions of `𝒟_a*` for
eigenvalues `±i`, normalized `‖v_+‖_{T_a} = ‖v_−‖_{T_a}`:
```
W(a,θ;z) := (z−i) ∫_{−a}^a v_+(a,x) e^{izx} dx + e^{iθ}(z+i) ∫_{−a}^a v_−(a,x) e^{izx} dx.
```
Entire in `z`; eigenvalues of the self-adjoint `𝒟̄_{a,θ}` are exactly its zeros; **all
zeros real**.

**Suzuki convergence target (Cor 6), MEROMORPHIC.** RH holds if `∃ θ(a), φ(a,z)` (finite)
with
```
lim_{a→∞} e^{φ(a,z)} W(a,θ;z) = z² · ξ(1/2 − iz) / ξ'(1/2 − iz)   (uniform on compacts).
```
The target `z²ξ/ξ'` has **poles at the zeros** of `ξ`.

**CCM convergence target (2511.22755), ENTIRE.**
```
det_reg(𝔇 − z) = −i λ^{−iz} ξ̂(z),      ξ̂ entire, zeros real = spectrum of 𝔇.
```
Open step: the **suitably normalized** `det_reg` → Riemann `Ξ`. The phase `λ^{−iz}`
preserves zeros but **not** the locally uniform limit.

**Consequence for the convergence track (Paper C).** Entire-function Hurwitz transfers
real-zero location for the CCM target; for the Suzuki meromorphic target it does **not** —
use a reciprocal / argument-principle (pole/residue) version. Never conflate the two
normalizations.

---

## 6. Symbol table

| Symbol | Meaning | Source |
|---|---|---|
| `a` | localization radius; test functions supported in `(−a,a)` | Suzuki |
| `Q_W^a` | `Q_W` restricted to `L²(−a,a)`; lower bounded, l.s.c. | EQ (pre-101) |
| `A_a` | canonical self-adjoint operator, `Q_W^a(v)=⟨A_a v,v⟩`; Friedrichs ext. of `B_a` | EQ_101, Thm 1.1 |
| `λ(a)=λ_a` | **invariant margin** = inf Rayleigh quotient of `Q_W^a` | EQ_107 |
| `g(t)` | screw function assoc. to `ζ`; screw ⟺ RH | EQ_103, Su23 |
| `W(a,θ;z)` | entire characteristic fn; zeros real = spectrum | Thm 1.5 |
| `Λ(n)` | von Mangoldt | — |
| `ξ, ξ̂, Ξ` | completed zeta; its Fourier transform; `Ξ(z)=ξ(1/2+iz)` | — |
| `c_L` (legacy) | `log(2πL)+γ_E`; **not invariant**, diagnostic only | §4 |

---

## 7. Deprecated legacy conventions (do not reintroduce)

- ❌ treating the archimedean kernel as a separate matrix block "balanced" against a prime
  block — it is the smooth part of the single functional `W`.
- ❌ a scalar "`−c_L I`" as a method-class obstruction — see §4.
- ❌ a fixed prime cutoff chosen independently of `a` — the cutoff `n ≤ e^{2a}` is forced
  by localization.
- ❌ "margin → 0 as `L→∞`" as evidence of a barrier — `λ(a)` is a smooth invariant; its
  behavior must be read in the invariant norm, and RH ⟺ `λ(a) ≥ 0` for all `a`
  (equivalently: RH fails ⟺ `∃a: λ(a)<0`, and by continuity + small-`a` positivity this
  forces `Q_W^a` degeneracy at some `a`).
