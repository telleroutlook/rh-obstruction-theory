# Checker — Theorem I

The analytic theorem is not validated by floating-point computation.

`gaussian_instance_check.py` is a deterministic stdlib-only exact replay for
one finite witness over `Q(sqrt(2))`. It verifies:

1. strict witness schema and exact rational/quadratic encoding;
2. positivity/nonzero/distinct-square membership conditions;
3. even polynomial membership and polynomial nonvanishing;
4. exact exponent distinctness and conjugacy;
5. independent reconstruction of the on-line pair and off-line quartet
   collapse from the raw zero data.

Adversarial mutations are in `tests/test_theorem_i_checker.py`, including every
top-level witness field and the polynomial/quartet rejection conditions.

The script does not prove Theorem I and does not check Lindemann-Weierstrass.
