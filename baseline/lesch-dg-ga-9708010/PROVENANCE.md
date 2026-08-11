# Lesch 1999 — log-polyhomogeneous noncommutative residue (D-spectral load-bearing source)

- **File:** `arXiv-dg-ga9708010v4.tar.gz` (arXiv dg-ga/9708010, v4).
- **Paper:** Matthias Lesch, "On the noncommutative residue for pseudodifferential
  operators with log-polyhomogeneous symbols", Ann. Global Anal. Geom. 17 (1999), 151–187.
- **Verified 2026-08-11 (in-repo, extracted `sec2.tex`):**
  - Heat expansion **eq. (3.9)** [preprint label `G1-3.9`]:
    `Tr(A e^{-tP}) ~ Σ_j t^{(j-n-a)/m} c_j(log t) + Σ_j d_j t^j` as `t→0⁺`,
    with `deg c_j ≤ k` if `(j-a-n)/m ∉ ℤ₊`, else `≤ k+1` (preprint **Theorem S1-3.5**;
    published **Theorem 3.7**). Proof follows Grubb–Seeley (1995) Thm 2.7 (cited in-proof).
  - **Consequence used by Theorem D:** with `A=I` (`a=0, k=0`), `j=0` gives exponent
    `-n/m < 0 ∉ ℤ₊`, so `c_0` is constant → the LEADING term `t^{-n/m}` carries no log.
    (Subleading `t^k log t`, `k≥1`, can occur — the earlier "no log at any order" claim
    was refuted; only the leading term is log-free, which is all D needs.)
  - Meromorphic `ζ`-continuation with poles at `(a+n-j)/m` of order `k+1`: eq. (3.10).
- **Numbering note:** this v4 preprint uses custom labels (`S1-3.5`, `G1-3.9`); the
  published journal numbering is Theorem 3.7. Content is identical.
- **Dimension note:** Lesch uses `n` for the manifold dimension; D's files use `d`.
