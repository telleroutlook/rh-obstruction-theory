# Witness README — Theorem G (G-fredholm-certificate)

## Required witnesses

### W-G-1: Eigenvalue error computation

A verified computation showing that for kappa_toeplitz (or any P ∈ 𝔐_FC):
```
|kappa_n^smooth - 1/(1/4 + gamma_n^2)| / |1/(1/4 + gamma_n^2)| ~ S(gamma_n) * 2pi / (gamma_n log(gamma_n/2pi))
```
for a range of n values, with the error not tending to 0.

Source: sibling repo `discovery/` outputs are acceptable as EXPLORATORY evidence;
for REPRODUCIBLE status they must be recomputed by an independent script here.

Status: NOT YET (depends on sibling repo numerical results).

### W-G-2: Explicit perturbed-zero exhibit

Per Prop. G.3: construct a specific sequence {ε̃_n} with |ε̃_n| ≤ |S(gamma_n)/N'(gamma_n)|,
show the resulting Ξ_ε is distinct from Ξ on a compact set, and confirm that O_θ maps
both 𝒵_RH and 𝒵_ε to the same (d_n) sequence.

This is the main open step for G-info PROOF-DRAFT → INDEPENDENTLY-CHECKED.

Status: NOT YET.

### W-G-3: S(T) table (first 30 zeros)

A table of γ_n, d_n = θ_level(n), γ_n − d_n, and S(γ_n) for n = 1, ..., 30,
showing the discrepancy is nonzero and matches the theoretical formula.

Source: may use known zero tables (Odlyzko) for γ_n; d_n is computable from
the theta function alone (zero-free). The comparison is the witness.

Status: NOT YET.

## Data provenance

All discovery-tier data (sibling repo outputs) must be clearly labeled EXPLORATORY
and must not be referenced by the analytic proof steps. The proof (proof.md) is
self-contained from REFEREED lemmas; the witnesses are corroborating evidence only.
