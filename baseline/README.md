# Baseline literature — source-verified

This directory holds the **source-of-truth** for every external theorem the program uses
as a premise. Rule (CLAUDE.md): *no cited theorem supports a claim here until it is
checked against the arXiv source, by theorem number.* Abstracts and memory are not enough.

The arXiv source tarballs are committed so the verification is reproducible offline.

## Verified inputs

### Suzuki 2606.09096 — `suzuki-2606.09096-weil-screw-function.tar.gz`
*M. Suzuki, "Weil's quadratic form via the screw function", arXiv:2606.09096, 2026-06-08.*
Source file inside: `screwzelf_7.tex`. Checked statements (quoted by theorem number):

- **Thm 1.3** — "The lowest eigenvalue `λ_a` is continuous in `a`." (no parity restriction)
- **Thm 1.4** — "For sufficiently small `a>0`, the lowest eigenvalue `λ_a` is positive,
  simple, and satisfies `λ_a = log(1/a) + μ₁ − log(2π) + ψ(2) − 1 + O(a)` as `a→0⁺`, for
  some constant `μ₁>0`. Furthermore, the corresponding eigenfunction is even."
- **Thm 1.5** — `W(a,θ;z) = (z−i)∫v₊e^{izx}dx + e^{iθ}(z+i)∫v₋e^{izx}dx` is entire in `z`;
  the eigenvalues of the self-adjoint `𝒟̄_{a,θ}` are precisely the zeros of `W(a,θ;z)`;
  **all zeros of `W(a,θ;z)` are real.**
- **Cor 6** — If one can choose `θ=θ(a)` and `φ(a,z)` (finite for all `a>0`, `z∈ℂ`) with
  `lim_{a→∞} e^{φ(a,z)} W(a,θ;z) = z² ξ(1/2−iz)/ξ'(1/2−iz)` uniformly on every compact
  `K⊂ℂ`, then RH holds.
- Background (from the associated operator `A_a`, via [4, Thm 3.6 / Cor 3.7]): spectrum
  bounded below and discrete, `+∞` the only accumulation point; `λ_a` is the largest
  lower bound and is an eigenvalue.

**Load-bearing consequences for this program:**
1. `λ(a)` (the lowest Rayleigh quotient) is the correct **representation-invariant**
   margin — replacing basis-dependent pivots / Schur residuals / `−c_L` shifts.
2. The `log(1/a)` in Thm 1.4 is the **positive** leading term of `λ(a)`, i.e. the same
   `log` scale that read as a *negative* shift in an unnormalized decomposition. Direct
   evidence the `c_L`-margin picture was a representation artifact.
3. The Suzuki convergence target (Cor 6) is **meromorphic** (`z²ξ/ξ'`, poles at the
   zeros). Entire-function Hurwitz does not transfer real-zero location; a pole/residue
   (reciprocal / argument-principle) version is required. This is a real obstacle for the
   Paper C escape theorem.

### CCM 2511.22755 — `ccm-2511.22755-zeta-spectral-triples.tar.gz`
*A. Connes, C. Consani, H. Moscovici, "Zeta Spectral Triples", arXiv:2511.22755, 2025-11-27.*
Source file inside: `mc2arXiv.tex`. Checked statements:

- Regularized determinant: `det_reg(𝔇 − z) = −i λ^{−iz} ξ̂(z)`, where `ξ̂` is the Fourier
  transform of `ξ`; `ξ̂(z)` is entire, **all its zeros are real and coincide with the
  spectrum** of `𝔇`.
- Numerical spectra of `𝔇` converge to the zeros of `ζ(1/2+is)` as `N,λ→∞`; "a rigorous
  proof of this convergence would establish the Riemann Hypothesis."
- The decisive open step: the **suitably normalized** regularized determinants converge
  toward the Riemann **Ξ** function. (§"missing steps".)

**Load-bearing consequence:** the phase factor `λ^{−iz}` preserves zeros but **not** the
locally uniform limit — "suitably normalized" is doing real work. This is a normalization
trap distinct from the Suzuki `ξ/ξ'` target. Suzuki (meromorphic) and CCM (entire `ξ̂`/`Ξ`)
must never be conflated.

### Andersson 2408.15713 — `andersson-2408.15713/arXiv-2408.15713v1.gz`
*J.-F. Andersson (Helson zeta prescribed zeros), arXiv:2408.15713.*
Single LaTeX doc. Checked statement (Theorem C dependency, Gate A CLEARED):
- **Theorem 5** (`\label{thm5}`, line 203; 5th `\begin{thm}`): for any open connected
  `U ⊇ {Re s>1}` and any signed multiset `Z ⊂ U∩{Re s<1}` without limit points on
  `U∪(1+iℝ)`, there is a completely multiplicative unimodular `χ` whose Helson zeta
  `ζ_χ` continues meromorphically to `U` with prescribed poles/zeros (with multiplicity)
  from `Z`, and `U` is the maximal domain. Exact match to C's cited premise.

### Lesch 1999 (dg-ga/9708010) — `lesch-dg-ga-9708010/arXiv-dg-ga9708010v4.tar.gz`
*M. Lesch, "On the noncommutative residue for pseudodifferential operators with
log-polyhomogeneous symbols", Ann. Global Anal. Geom. 17 (1999), 151–187.*
Multi-file LaTeX (`sec2.tex`). Checked statement (Theorem D load-bearing citation,
SOURCE-VERIFIED; see `lesch-dg-ga-9708010/PROVENANCE.md`):
- Heat expansion **eq. (3.9)** [preprint `G1-3.9`, published **Thm 3.7**]:
  `Tr(A e^{-tP}) ∼ Σ_j t^{(j-n-a)/m} c_j(log t) + Σ_j d_j t^j`, `deg c_j ≤ k` if
  `(j-a-n)/m ∉ ℤ₊` (else `k+1`). With `A=I` (`a=0,k=0`), `j=0`: exponent `-n/m<0 ∉ ℤ₊`,
  so `c_0` constant → **leading term `t^{-n/m}` carries no log** (exactly D's need).
- Proof follows Grubb–Seeley 1995 (Invent. Math. 121) Thm 2.7 (cited in-proof).

## To re-verify
```bash
mkdir -p /tmp/v && tar xzf suzuki-2606.09096-weil-screw-function.tar.gz -C /tmp/v
grep -n "lowest eigenvalue\|is continuous in\|all zeros of\|z^2\|xi(1/2" /tmp/v/screwzelf_7.tex
# Lesch heat expansion:
mkdir -p /tmp/vl && tar xzf lesch-dg-ga-9708010/arXiv-dg-ga9708010v4.tar.gz -C /tmp/vl
grep -n "Tr(A e^{-tP})\|deg .*c\|G1-3.9\|S1-3.5" /tmp/vl/sec2.tex
```

## Pending (Gate A, program §6.A.3)
`REFERENCE_BASELINE.md` — exact `a`, `Q_W^a`, `λ(a)` conventions in one place; map every
legacy `L`, `c_L`, block, and support threshold onto them. Not yet written.
