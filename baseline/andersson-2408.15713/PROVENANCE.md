# Andersson 2024 — Helson zeta prescribed zeros/poles (C-euler-tail load-bearing source)

- **File:** `arXiv-2408.15713v1.gz` (arXiv:2408.15713, v1; gzip of a single LaTeX file
  `Andersson_Mittag-Leffler_paper.tex`).
  - `.gz`  SHA-256: `511fa8002fe7224763760225ff58f5f34ea5292499a21449d0810760f98a67c0`
  - extracted `src/Andersson_Mittag-Leffler_paper.tex` SHA-256:
    `1b62faa668f4a57a221d27dc651ecc204267bee3f6ece51174cffd198a048744`
- **Paper:** Johan Andersson, "Mittag-Leffler type theorems for Helson zeta-functions"
  (arXiv:2408.15713v1, 2024-08-28) — title from the source `\title{...}` (line 16).

## Verified 2026-08-11 (in-repo, from extracted `src/…tex`); citation re-checked OB-26 2026-08-11

- **Theorem 5** (LaTeX label `thm5`, line 204 of the source), faithfully transcribed with
  the source's apparent `f → ζ_χ` typo explicitly corrected (the source's last sentence
  writes "maximal domain of meromorphicity of `f`", clearly meaning `ζ_χ`; this sentence is
  not load-bearing for Theorem C, which takes `U = ℂ`):

  > Let `U ⊆ ℂ` be an open connected set containing the half plane `Re(s) > 1` and let
  > `𝒵 ⊂ U ∩ {s : Re(s) < 1}` be any signed multiset without limit points on
  > `U ∪ (1+iℝ)`. Then there exists a completely multiplicative unimodular function `χ`
  > such that the Helson zeta-function `ζ_χ(s)` has meromorphic continuation from
  > `Re(s) > 1` to `U` with prescribed poles and zeros with given multiplicities from
  > `𝒵`. Furthermore we may choose `χ` such that the maximal domain of meromorphicity
  > [of `ζ_χ`] is `U`.

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

## Corollary 3 (optional `P_S = 1` companion for C — OB-26 Q3)

**Corollary 3** (LaTeX label `cor3`, source line 196): "There exist some entire zero-free
Helson zeta-function `ζ_χ`." Verified in-source. Used optionally by C (`proof.md §4.5`) to
supply, unconditionally, a `P_S = 1` fiber-mate (`ζ_0` zero-free on `S`, then `ζ_0·R_a`);
not needed for C's one-sided non-forcing claim.

## Helson class references (OB-26 mod5 — citation correction)

The Helson class `ζ_χ(s) = Σ χ(n) n^{-s}` (`χ` completely multiplicative, `|χ|=1`) is a
published research class; the correct primary reference is **Henry Helson, "Compact groups
and Dirichlet series", Ark. Mat. 8 (1969), 139–143** (source `\bibitem{Helson}`, line 444;
some indices list 1970). Not "Helson 1954". Modern references in the source: Seip (J. Anal.
Math. 141, 2020), Bochkov–Romanov (J. Funct. Anal. 282, 2022). (Bayart 2002 is Hardy-space /
composition-operator background, not a load-bearing source for Theorem C.)

## Theorem numbering (for the reviewer)

Source `\newtheorem{thm}{Theorem}` (line 18) numbers Theorems sequentially; the
prescribed-zero result is **Theorem 5** = label `thm5` (line 204). Theorems 1–4
(`thm1`..`thm4`) are the corresponding function-value / universality statements and are
**not** used by Theorem C.

## Scope note (kept in C's limitations.md)

Theorem 5 is for the **Helson class** (completely multiplicative unimodular `χ`, Euler
product, meromorphic continuation) — no functional equation, no gamma factor. It does
**not** transfer to the Selberg class or to ζ itself. C neither constructs nor claims a
Selberg-class member, so it draws no conclusion there. (A general "prescribed-zero theorem
for the Selberg class is provably impossible" claim would need its own precise theorem /
citation and is **not** asserted here — see limitations.md; earlier "EXT-4a: provably
incompatible" wording is narrowed to this honest form.)
