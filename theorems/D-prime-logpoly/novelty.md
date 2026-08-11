# Novelty — Theorem D' (D-prime-logpoly)

**Theorem ID:** D-prime-logpoly  
**Finding:** Escape-route audit (ESCAPE-ROUTE-REFINED, OB-01 + OB-16, 2026-08-11)

---

## Assessment

This document audits the log-polyhomogeneous escape route from Theorem D.

**Corrected finding (OB-01 + OB-16, 2026-08-11).** The earlier assessment — that
`𝒞_logpoly` is the escape class because the log-coefficient `c_{0,1}` is freely tunable
to `(2π)^{-1}` at leading order — is **REFUTED**. For finite-log-degree `𝒞_logpoly` the
**leading** heat-trace singularity is a pure power `t^{-d/m}`; logs appear only at
subleading orders `t^k log(1/t)` (`k ≥ 1`). So `𝒞_logpoly` cannot match the leading
`Z_ζ(t) ~ (1/2π)log(1/t)/t` and is **not** the escape class.

**The actual escape class** is a log-*weighted* symbol class: `|ξ|/log|ξ|`-type
(`S^{1,-1}`, elliptic w.r.t. `w(ξ)=⟨ξ⟩/log(e+⟨ξ⟩)`), which gives `N_H(T) ~ c·T log T`
and hence a genuine leading `t^{-1}log(1/t)`. It lies outside `𝒞_ell` and outside
finite-log-degree `𝒞_logpoly`, but inside the ordinary Hörmander class `S¹_{1,0}`.

**Is this novel?** The refined finding is a *negative* audit result plus a correct
localization:
- Theorem D's heat-trace singularity obstruction **does** extend to `𝒞_logpoly` (it is
  NOT an escape) — this narrows, not widens, the escape frontier.
- The correct escape class (log-weighted `S^{1,-1}`) is identified, and the naive exact
  model `2πn/log(n+e)` is shown to fail the two-term counting law (`≍ T log log T`
  discrepancy). This is a precise placement of the Hilbert–Pólya frontier.

**Publication strategy:** A short remark (2–3 pages) within Paper B or as an appendix,
now framed as: "the heat-singularity obstruction covers `𝒞_logpoly`; the escape requires
a log-weighted class, and even there the naive model fails at the two-term scale." Not a
standalone paper.

**Novelty gate:** OPEN (the audit is a direct computation from cited results; independent
novelty search not yet done). No RH-relevant claim; the open Hilbert–Pólya realization in
the log-weighted class is explicitly a conjecture/frontier, not a theorem.