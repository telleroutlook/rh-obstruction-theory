# checker/ — independent replay path for Theorem B2

# When a computational witness is available (exact Jacobian + solution), the
# checker here must independently verify:
#
#   1. J_{jk} = phi_j(1/2+it_k) + phi_j(1/2-it_k)  computed from scratch
#      using the exact formula for each test type (Li, Weil-W2, moment).
#   2. det J != 0 via exact rational arithmetic (no floats).
#   3. alpha = -J^{-1} delta^off(T*) solved exactly or with certified bounds.
#   4. |O_j(Z_-) - O_j(Z_+)| = 0 verified symbolically or with interval width 0.
#   5. Z_- in X_sym: conjugation + FE symmetry holds by construction (checkable).
#   6. P(Z_-) = 0: sigma_0 != 1/2 (trivially checkable).
#
# Checker must not import discovery/ outputs.
# Must be runnable offline with no network access.
# Must use stdlib or whitelisted exact-arithmetic libraries only.
#
# STATUS: empty. Rank analysis not yet attempted.
