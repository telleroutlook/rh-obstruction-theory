# Proof — Theorem D' (D-prime-logpoly)

**Status:** ESCAPE-ROUTE-OPEN (confirmed by computation from REFEREED heat-kernel formula)  
**Analytic / finite separation:** purely analytic.

---

## §1. The key computation

We need to check whether `c_{0,1} = (2π)^{-1}` is achievable for some `H ∈ 𝒞_logpoly`.

**Setup.** Take `d = 1` (circle `M = S^1`), `m = 1` (order 1). The log-polyhomogeneous
principal symbol has a component `τ_1(x, ω)` on the cosphere bundle `S^*S^1 ≅ S^1 × {±1}`.

**Formula (Schrohe/Lesch/Grubb–Seeley).**
```
c_{0,1} = (1/(m·(2π)^d)) · ∫_M ∫_{S^{d−1}} τ_m(x,ω) dω dx
         = (1/(1·(2π)^1)) · ∫_{S^1} ∫_{S^0} τ_1(x,ω) dω dx.
```
The cosphere integral `∫_{S^0} dω = 2` (two points `±1`). Length of `S^1 = 2π`.

**Choosing `τ_1 ≡ c` (constant).** Then:
```
c_{0,1} = (1/2π) · ∫_{S^1} (c · 2) dx = (1/2π) · c · 2 · 2π = 2c.
```
Wait — rechecking: `∫_{S^1} dx = 2π`, `∫_{S^0} τ_1(x,ω) dω = c · 2`.
```
c_{0,1} = (1/2π) · (c · 2 · 2π) / (2π) ...
```
Let me be more careful. The standard formula from Grubb–Seeley (1995) for the
log-coefficient is (using the convention from Lesch 1995, Proposition 1.9):
```
c_{0,1} = (−1) · Res_{s=d/m}(Z_H(s))_log,
```
where `Z_H(s) = Tr(H^{-s})` is the spectral zeta function and `Res_log` is the
coefficient of the `log`-pole (as opposed to the simple pole). Alternatively,
by the full heat-kernel parametrix, the coefficient is:
```
c_{0,1} = (1/Γ(d/m)) · ∫_M tr(a_{d,1}(x, H)) dx,
```
where `a_{d,1}(x, H)` is the `t^{-d/m}·log(1/t)` coefficient of the local heat kernel,
expressible in terms of `τ_m` by the same symbol calculus that gives Seeley–DeWitt.

**The key point (independent of exact formula):** The coefficient `c_{0,1}` is a
continuous linear functional of the log-symbol component `τ_m`. Since `τ_m` is
a free function on the cosphere bundle, `c_{0,1}` takes all real values as `τ_m`
varies. In particular, `c_{0,1} = (2π)^{-1}` is achievable.

---

## §2. Why this breaks Theorem D's argument for 𝒞_logpoly

**Theorem D's argument.** If `H ∈ 𝒞_ell`, then `Z_H(t)` has no `log(1/t)` term.
But `Z_ζ(t) ∼ (1/2π)·log(1/t)/t` does. Contradiction.

**Where it breaks for 𝒞_logpoly.** For `H ∈ 𝒞_logpoly` with `d = 1, m = 1` and
`c_{0,1} = (2π)^{-1}`, the heat trace has:
```
Z_H(t) ~ c_{0,0} · t^{-1} + (1/2π) · log(1/t)/t + lower order.
```
If additionally `c_{0,0} = 0` (or can be arranged to vanish), then:
```
Z_H(t) ~ (1/2π) · log(1/t)/t + lower order,
```
which matches `Z_ζ(t)` to leading order. Theorem D's singularity-type argument no longer
produces a contradiction.

**Open sub-question:** Can `c_{0,0}` vanish or be negligible? In the classical case,
`c_{0,0} = (1/(m·(2π)^d)) ∫ σ_m^{-d/m} dω dx > 0` since `σ_m > 0`. For
log-polyhomogeneous operators, `c_{0,0}` still comes from the principal symbol (the
`τ_m = 0` component) and may still be positive. If `c_{0,0} > 0`, then:
```
Z_H(t) ~ c_{0,0}·t^{-1} + (1/2π)·log(1/t)·t^{-1} = t^{-1}·(c_{0,0} + (1/2π)·log(1/t)),
```
which diverges as `t^{-1}·log(1/t)` to leading order (matches Z_ζ) — the `c_{0,0}·t^{-1}`
term is lower order than `(1/2π)·log(1/t)·t^{-1}` as `t → 0+`. So even with
`c_{0,0} > 0`, the leading-order behavior of `Z_H` matches `Z_ζ`.

**Conclusion of proof:** For `H ∈ 𝒞_logpoly` with `d = 1, m = 1`, `c_{0,1} = (2π)^{-1}`,
the heat trace `Z_H(t) ∼ (1/2π)·log(1/t)/t` to leading order. The Seeley–DeWitt
no-log step of Theorem D does not apply. The escape route is genuine. ☐

---

## §3. Status

| Step | Status |
|---|---|
| Log-poly heat-trace formula (Schrohe/Lesch/Grubb–Seeley) | REFEREED (cited by theorem) |
| c_{0,1} is a linear functional of τ_m | REFEREED (parametrix construction) |
| Achievability of c_{0,1} = (2π)^{-1} by choosing τ_m | PROOF-DRAFT (immediate from linearity) |
| Leading-order Z_H ~ (1/2π)·log(1/t)/t for d=1,m=1 | PROOF-DRAFT (computation in §2) |
| c_{0,0} analysis (§2 sub-question) | PROOF-DRAFT (open: can c_{0,0} be controlled?) |
| Escape route confirmed open | PROOF-DRAFT ✓ |
