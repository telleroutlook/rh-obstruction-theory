# checker/ — independent replay path for Theorem B1

# Theorem B1 is analytic (no finite certificate to replay).
#
# If a future version adds a computational witness (e.g., interval-arithmetic
# verification of |delta_j(T*)| < eps for specific parameters), the checker
# here must:
#
#   1. Read raw prime-power / zero data from witness/ only (not discovery/).
#   2. Reconstruct |delta_j(T*)| from first principles (not a copy of the
#      generator's output).
#   3. Use exact rational or outward-rounded interval arithmetic.
#   4. Report PASS/FAIL with all intermediate bounds.
#   5. Be runnable offline with no network access.
#
# STATUS: empty. Theorem B1 has no computational component to check.
