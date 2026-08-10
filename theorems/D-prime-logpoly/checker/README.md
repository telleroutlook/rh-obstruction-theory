# Checker README — Theorem D' (D-prime-logpoly)

The escape-route-open conclusion is analytic only (no finite certificate).

Independent verification steps:
1. Confirm the heat-kernel formula c_{0,1} = (1/(m*(2pi)^d)) * integral(tau_m)
   from Schrohe (1992) / Lesch (1995) / Grubb–Seeley (1995) by theorem number.
2. Verify the d=1, m=1 computation: integral_{S^1} integral_{S^0} tau_1(x,omega) domega dx
   for tau_1 = constant c gives c_{0,1} = c * (2pi * 2) / (2pi) = 2c, hence
   c_{0,1} = (2pi)^{-1} requires c = (4pi)^{-1}. [CHECK THIS ARITHMETIC — see proof.md §1]
3. Confirm that c_{0,0} > 0 does not prevent the heat trace from having leading
   behavior ~ (1/2pi)*log(1/t)/t (since log(1/t) dominates the constant as t->0+).

Status: NOT YET — checker implementation not started.
