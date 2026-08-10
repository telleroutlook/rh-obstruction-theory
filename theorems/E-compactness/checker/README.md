# checker/ — independent replay path for Theorem E

# Theorem E-pos is purely analytic (Montel/Vitali/Hurwitz standard results).
# No finite certificate to replay.
#
# Theorem E-neg (once proof.md §3 is complete and a witness is placed in
# witness/) requires the checker to:
#
#   1. Verify the tail perturbation construction (mu_{n,N} from raw zeta ordinates).
#   2. Compute |F_N^(1) - F_N^(2)| on a grid inside |z| <= R using
#      exact or interval-certified arithmetic.
#   3. Confirm the sup-norm separation >= eps > 0.
#   4. Use NO floating-point; use exact Fraction arithmetic or python-flint/Arb.
#   5. Run offline with no network access.
#
# STATUS: empty. Quantitative E-neg estimate not yet completed.
