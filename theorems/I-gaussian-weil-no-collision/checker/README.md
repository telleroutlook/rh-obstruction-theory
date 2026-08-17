# Checker — Theorem I

The analytic theorem is not validated by floating-point computation.

`gaussian_instance_check.py` is a finite exact-rational sanity check for one
pure Gaussian instance. It verifies:

1. the exponent list has no duplicates;
2. the polynomial nonvanishing assumptions hold;
3. the displayed observation formulas agree exactly on that instance;
4. the checker fails under adversarial exponent mutation.

The script does not prove Theorem I and does not check Lindemann-Weierstrass.

