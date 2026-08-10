# Limitations — Theorem D' (D-prime-logpoly)

**Theorem ID:** D-prime-logpoly  
**Finding:** ESCAPE-ROUTE-OPEN (log-polyhomogeneous class is a live candidate)

---

## What this document does NOT prove

1. **Does not produce any Hilbert–Pólya operator.** Matching the heat-trace singularity
   type is necessary but far from sufficient for an operator to have spectrum `{γ_n}`.

2. **Does not refute Theorem D.** Theorem D correctly excludes 𝒞_ell. This document
   only confirms that 𝒞_logpoly ⊋ 𝒞_ell is a genuine escape from Theorem D.

3. **Does not determine the Weyl law for 𝒞_logpoly.** Whether the eigenvalue counting
   function for `H ∈ 𝒞_logpoly` can satisfy `N_H(T) ~ T log T / (2π)` (rather than
   `~ C·T^{d/m}`) is an open question. This is the key bottleneck for any Hilbert–Pólya
   candidate in 𝒞_logpoly.

4. **Does not show that c_{0,0} can be made to vanish.** The argument in proof.md §2
   shows that even with `c_{0,0} > 0`, the leading heat-trace behavior is `~ (1/2π)·log(1/t)/t`,
   but controlling lower-order terms would require further analysis.

5. **Does not extend to non-compact manifolds.** The log-polyhomogeneous calculus here
   is for compact manifolds. Non-compact versions require additional trace-class conditions.

6. **Does not prove c_{0,1} = (2π)^{-1} for any natural/arithmetic operator.** The
   coefficient is freely tunable in principle, but a "natural" operator built from
   arithmetic data whose log-symbol happens to integrate to the Riemann–von Mangoldt
   constant is not known.
