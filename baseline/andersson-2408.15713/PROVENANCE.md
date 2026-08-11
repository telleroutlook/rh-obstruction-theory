# Andersson 2024 — Helson zeta prescribed zeros/poles (C-euler-tail load-bearing source)

- **File:** `arXiv-2408.15713v1.gz` (arXiv:2408.15713, v1; gzip of a single LaTeX file
  `Andersson_Mittag-Leffler_paper.tex`).
  - `.gz`  SHA-256: `511fa8002fe7224763760225ff58f5f34ea5292499a21449d0810760f98a67c0`
  - extracted `src/Andersson_Mittag-Leffler_paper.tex` SHA-256:
    `1b62faa668f4a57a221d27dc651ecc204267bee3f6ece51174cffd198a048744`
- **Paper:** Johan Andersson, "Mittag-Leffler's theorem, universality and the
  prescription of zeros and poles of Helson zeta functions" (arXiv:2408.15713, 2024-08-28).

## Verified 2026-08-11 (in-repo, from extracted `src/…tex`)

- **Theorem 5** (LaTeX label `thm5`, line 203 of the source), transcribed verbatim:

  > Let `U ⊆ ℂ` be an open connected set containing the half plane `Re(s) > 1` and let
  > `𝒵 ⊂ U ∩ {s : Re(s) < 1}` be any signed multiset without limit points on
  > `U ∪ (1+iℝ)`. Then there exists a completely multiplicative unimodular function `χ`
  > such that the Helson zeta-function `ζ_χ(s)` has meromorphic continuation from
  > `Re(s) > 1` to `U` with prescribed poles and zeros with given multiplicities from
  > `𝒵`. Furthermore we may choose `χ` such that the maximal domain of meromorphicity
  > is `U`.

- **Unconditional.** The source explicitly contrasts with Seip / Bochkov–Romanov, who
  reach `1/2 < Re(s) < 1` only **conditional on RH**; Andersson's Theorem 5 is valid
  **unconditionally** on the full half-plane `Re(s) < 1`. (Source, lines following
  `thm5`: "our result is valid unconditionally, and it gives prescibed [sic] poles and
  zeros on the full half plane `Re(s) < 1`.")

- **Consequence used by Theorem C:** take `U = ℂ` (or any connected `U ⊃ {Re(s) > 1}`)
  and `𝒵 = {z₁}` a single simple zero with `0 < Re(z₁) < 1`, `Re(z₁) ≠ 1/2`, no limit
  points. Theorem 5 yields a Helson `ζ_χ` (completely multiplicative unimodular `χ`)
  with a prescribed off-critical-line zero at `z₁`. Theorem C then modifies the finitely
  many `p ≤ P₀` Euler factors to the standard value `χ̃(p)=1` via the zero-free ratio
  `R(s) = Π_{p≤P₀}(1−χ(p)p^{-s})/(1−p^{-s})` (holomorphic and nowhere zero on the open
  strip; see `theorems/C-euler-tail/proof.md` §3).

## Theorem numbering (for the reviewer)

Source `\newtheorem{thm}{Theorem}` (line 18) numbers Theorems sequentially; the
prescribed-zero result is **Theorem 5** = label `thm5` (line 203). Theorems 1–4
(`thm1`..`thm4`, lines 81/123/147/176) are the corresponding function-value /
universality statements and are **not** used by Theorem C.

## Scope note (kept in C's limitations.md)

Theorem 5 is for the **Helson class** (completely multiplicative unimodular `χ`, Euler
product, meromorphic continuation) — no functional equation, no gamma factor. It does
**not** transfer to the Selberg class or to ζ itself (EXT-4a: Selberg axioms are
provably incompatible with free zero prescription). Theorem C inherits exactly this
scope.
