# Novelty — Theorem D (D-spectral-asymptotic)

**Theorem ID:** D-spectral-asymptotic  
**Program ref:** §9.D.5, LITERATURE_MATRIX.md §Paper B

---

## Prior art landscape

### Endres–Steiner (2010), J. Phys. A 43, 095204 — Theorems 15.4–15.6

Prove a Weyl-law no-go for the **two Berry–Keating families** `H_BK` and `H_BK²` on
**compact metric graphs** (comparing `N_H(T) ~ (L/π) T` with `N_ζ(T) ~ T log T / 2π`).
This is NOT a statement about all compact quantum-graph operators, and metric graphs are
not closed smooth manifolds.

### Watson–Valentinuzzi (2026), Bull. Sci. Math. 211, 103824 (arXiv:2604.00052) — Thm 1.4, Prop 6.2, Thm 7.2

State a **closely related leading-log obstruction for elliptic differential operators on
compact manifolds**, via a Tauberian argument: superlinear counting `N(λ) ~ λ L(λ)` forces
heat trace `Θ(t) ~ t⁻¹ L(1/t)`, incompatible with a `t^{-1/4}` fourth-order kernel limit
(spectral-dimension separation). **Existence/title/DOI/authors verified 2026-08-11.** This
is a **near-direct precedent** to D and MUST be disclosed (OB-25 Q5). It is **not imported**
as a premise: the accessible arXiv v1 uses two-sided `|γ|≤T` counting alongside the
one-sided `1/2π` coefficient (a factor-2 mismatch) and RH-style `1/2+iγ_n` phrasing in
§7.2, so it is not a clean RH-free source.

### Program §9.D.5 judgment

> "The raw Weyl mismatch is close to a standard corollary.  Before claiming a
> new paper, complete a theorem-by-theorem prior-art audit.  A paper is justified
> only if it supplies a materially broader, sharply defined invariant class or
> an exact determinant obstruction not already in the literature."

## New content assessment

| Aspect | Novel? | Notes |
|---|---|---|
| Weyl leading term for C_ell | NO | Standard corollary of classical Weyl theorem |
| Extensions: sums, polynomials, perturbations | THIN | Routine from Courant-Weyl |
| Compact quantum graphs | NO | Endres-Steiner already proved this |
| Leading-log obstruction, elliptic differential operators | NO | Watson–Valentinuzzi 2026 (near-direct precedent) |
| Heat-trace vs Weyl "stronger" claim | NO | Same leading-order fact via Abel/Tauber transform of the counting measure (OB-25 Q5) |
| Extension to full classical elliptic ΨDO class | YES (increment) | via Lesch Thm 3.7 `Tr(Ae^{-tP})`; beyond differential (WV) and graphs (ES) |
| Leading-vs-subleading-log distinction | YES (increment) | impossible leading `t^{-d/m}log(1/t)` vs permissible subleading `t^k log t` (`Wres(H^k)≠0`) |
| Spectral zeta pole obstruction (proof.md §5) | DEFERRED | future work |

## Verdict and publication strategy (OB-25 Q5)

**SCOPE-EXTENSION / COROLLARY — not standalone novelty.** OB-25 refuted the earlier
"strictly stronger than Endres–Steiner / novelty gate CLEARED" claim on two grounds:

1. **The heat-trace argument is not stronger within `𝒞_ell`.** Given a positive spectrum,
   `Z(t) = ∫ e^{-tT} dN(T)`, so the Weyl-counting leading term and the heat-trace leading
   singularity are the **same** leading-order fact in two languages (Abel/Tauber for
   regularly varying `N`; see proof.md §4). The heat trace gives cleaner "leading-type"
   language and exposes subleading logs, but excludes no operator the Weyl mismatch misses.
2. **A near-direct precedent exists (Watson–Valentinuzzi 2026)** for the leading-log
   obstruction on elliptic **differential** operators — so D's leading-log idea is not new
   in itself.

**D's honest, identifiable increment:**
- extends the exclusion from elliptic **differential** operators (WV 2026) and quantum
  graphs (ES 2010) to the **full classical elliptic ΨDO class** on a closed manifold, via
  Lesch's `Tr(A e^{-tP})` expansion (Thm 3.7); and
- cleanly separates the **impossible leading** `t^{-d/m}log(1/t)` from **permissible
  subleading** `t^k log t` (`k≥1`).

**Citation status (Lesch, OB-15 + OB-25).** The leading-log fact for the full classical
elliptic ΨDO class is pinned to **Lesch 1999 Theorem 3.7** (Ann. Global Anal. Geom. 17,
151–187), heat expansion **published (3.18)** / degree bound **(3.19)** / Mellin **(3.20)**
(= preprint `(3.9)`/`(3.10)`; a bare "(3.9)" is a *different* equation in the published
version — see baseline PROVENANCE.md), with `A=I`, extending **Grubb–Seeley 1995 Theorem
2.7**. Scope caveat (PROMPT_LINT L17): **BGV Thm 2.30** (Laplace-type only) and **Gilkey
Lemma 1.8.2** (differential only; NOT "Thm 1.8.1") do not suffice and are not load-bearing.
This is a standard result at the pinned references, not a new mathematical claim.

**Publication strategy:** a **proposition / appendix / short note inside a larger paper**,
positioned as a classical-ΨDO scope-extension of the ES/WV leading-log obstruction, with
the Weyl mismatch as context and both precedents cited. NOT a standalone "new barrier."
(Global novelty cannot be proved by a finite literature search; this records the honest
positive claim and the disclosed precedents.) The spectral-zeta pole obstruction (proof.md
§5) is deferred.
