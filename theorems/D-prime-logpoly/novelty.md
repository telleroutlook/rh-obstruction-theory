# Novelty — Theorem D' (D-prime-logpoly)

**Theorem ID:** D-prime-logpoly  
**Finding:** Escape-route audit (ESCAPE-ROUTE-OPEN)

---

## Assessment

This document audits the log-polyhomogeneous escape route from Theorem D. The result
is an ESCAPE-ROUTE-OPEN finding: the heat-trace singularity obstruction of Theorem D
**cannot** be extended to exclude 𝒞_logpoly, because the log-coefficient `c_{0,1}`
is freely tunable to `(2π)^{-1}`.

**Is this novel?** The heat-kernel expansion for log-polyhomogeneous operators is
standard (Schrohe, Lesch, Grubb–Seeley 1995). The observation that `c_{0,1} = (2π)^{-1}`
is achievable is a direct corollary of the formula. However:

- The explicit connection to the Riemann–von Mangoldt constant `(2π)^{-1}` and its
  role as a potential Hilbert–Pólya singularity target does not appear to be explicitly
  stated in the literature.
- The identification of 𝒞_logpoly as a live (unexcluded) class for the Hilbert–Pólya
  problem, with a precise statement of what would still need to be shown (Weyl law,
  spectrum matching), is a modest but precise contribution.

**Publication strategy:** This is a short observation (2–3 pages), suitable as a remark
within Paper B or as an appendix. Not a standalone paper.

**Novelty gate:** OPEN (the observation is a direct computation; independent
novelty search not yet done).
