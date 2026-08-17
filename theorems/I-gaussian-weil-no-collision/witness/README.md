# Witness — Theorem I

No finite witness is used as proof. The theorem is analytic and algebraic.

The finite exact replay witness is `gaussian_hermite_witness_v1.json`. It uses
the raw quadratic-field data

```
field = Q(sqrt(2))
a = 1/100
gamma = sqrt(2), 2 sqrt(2), 3
g = 2 sqrt(2)
delta = 1/2
P(z) = 16 z^4 - 48 z^2 + 12
```

It is replayed by `../checker/gaussian_instance_check.py`. Exploration-tier
high-precision PSLQ output remains in `discovery/` and is not a theorem
witness.
