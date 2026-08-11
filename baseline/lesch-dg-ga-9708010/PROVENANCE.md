# Lesch 1999 — log-polyhomogeneous noncommutative residue (D-spectral load-bearing source)

- **File:** `arXiv-dg-ga9708010v4.tar.gz` (arXiv dg-ga/9708010, v4).
- **Paper:** Matthias Lesch, "On the noncommutative residue for pseudodifferential
  operators with log-polyhomogeneous symbols", Ann. Global Anal. Geom. 17 (1999), 151–187.
- **Verified 2026-08-11 (in-repo, extracted `sec2.tex`); cross-checked against OB-25 review 2026-08-11:**
  - Load-bearing result is **Theorem 3.7** (version-independent anchor; preprint label
    `S1-3.5`). The heat expansion, degree bound, and Mellin relation are, **by numbering scheme**:
    | object | preprint arXiv v4 (this tarball) | published journal (Ann. Global Anal. Geom. 17) |
    |---|---|---|
    | heat expansion `Tr(Ae^{-tP})~…` | eq. `(3.9)` (label `G1-3.9`) | eq. **(3.18)** |
    | `deg c̃_j` degree bound | the display right after `(3.9)` (unnumbered in preprint) | eq. **(3.19)** |
    | generalized-ζ / Mellin + poles | eq. `(3.10)` (label `G1-3.10`) | eq. **(3.20)** |
    In the **published** version the number `(3.9)` denotes a *different* equation (a local
    symbol/kernel decomposition inside the resolvent-expansion proof), so cite **Theorem 3.7
    together with (3.18)/(3.19)/(3.20)** — never a bare "(3.9)" — to be unambiguous for a
    reader holding the journal version. (The preprint `(3.9)` transcription below is correct
    *for this tarball*; the discrepancy is a preprint-vs-published renumbering, not an error.)
  - Heat expansion (preprint `(3.9)` = published **(3.18)**):
    `Tr(A e^{-tP}) ~ Σ_j t^{(j-n-a)/m} c̃_j(log t) + Σ_j d̃_j t^j` as `t→0⁺`,
    with (published **(3.19)**) `deg c̃_j ≤ k` if `(j-a-n)/m ∉ ℤ₊`, else `≤ k+1`
    (Theorem 3.7 = preprint `S1-3.5`). Proof follows Grubb–Seeley (1995) Thm 2.7 (cited in-proof).
  - **Consequence used by Theorem D:** with `A=I` (`a=0, k=0`), `j=0` gives exponent
    `-n/m < 0 ∉ ℤ₊`, so `c̃_0` is constant → the LEADING term `t^{-n/m}` carries no log.
    (Subleading `t^k log t`, `k≥1`, can occur — the earlier "no log at any order" claim
    was refuted; only the leading term is log-free, which is all D needs.)
  - Meromorphic `ζ`-continuation `Tr(AP^{-s})` with poles at `(a+n-j)/m` of order `k+1`:
    preprint eq. `(3.10)` = published **(3.20)**.
- **Numbering note:** this v4 preprint uses custom labels (`S1-3.5`, `G1-3.9`, `G1-3.10`);
  the published journal numbering is **Theorem 3.7**, **(3.18)** heat expansion, **(3.19)**
  degree bound, **(3.20)** Mellin/poles. Content is identical; only the equation numbers differ.
- **Dimension note:** Lesch uses `n` for the manifold dimension; D's files use `d`.
