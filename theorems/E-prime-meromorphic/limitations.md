# Limitations — Theorem E' (E-prime-meromorphic)

## 0. GATE-A BLOCKED (OB-30, 2026-08-12) — primary limitation

The independent Gate-A review **BLOCKED** E' as a Suzuki-target theorem. Three genuine,
independent errors (statement.md §0):
- **Separation degree wrong.** The claimed `z^{2J+3}` leading discrepancy is false; matching
  a `J`-jet at `w₀≠0` gives `O((t−t₀)^J)`, not vanishing of the first `J` power-sums at 0. A
  `J=1` counterexample (`A=sin πz/πz`, `B=sinh z`, `w₀=i`) yields leading `z³`. Only "some
  nonzero Taylor coefficient of order ≥3 exists" is defensible.
- **(A2) false for the real target.** `B=iξ'(1/2−iz)`; Rolle between real `ξ`-zeros forces
  real `B`-zeros, so `Z(B)∩ℝ≠{0}`. (A1)–(A3) hold only for an *abstract* pair; and (A1) over
  the real `A` is RH+simplicity.
- **Suzuki is entire; moving poles incompatible.** `W(a,θ;z)` is entire (Thm 1.5); a moving-
  pole (PL⁺) approximation cannot converge to the meromorphic `W` on pole-encircling compacts.

**Withdrawn:** the Suzuki-target E'-neg/E'-pos claims, the fixed degree, and the
"(LB)/(ZT_ℂ)/(PL⁺)/(UG) OPEN" framing (PL⁺ is *incompatible*, not open). **Survives:** an
abstract odd-meromorphic jet lemma (given abstract (A1)–(A3), corrected separation) + the
meromorphic uniqueness Lemma E'.1. E' is NOT a Suzuki companion.

## 1. (superseded — see §0) Prior per-round status

The items below record the OB-06/09/11 per-round corrections; they are **subsumed** by the
§0 BLOCKED verdict and retained only for history.

1. **E'-neg per-round history (OB-09).** The meromorphic IFT
   step is written out explicitly: the direct `w₀`-jet system `Ψ_j(u,c)=∂_t^j L(t₀;u,c)`
   with the rational Wronskian–Vandermonde Jacobian (proof.md §3, OB-09 §7). **The separation
   degree it claimed (`z^{2J+3}`) is now REFUTED (OB-30 §0).**

2. **E'-pos per-round history (OB-11), not OPEN.** The proof uses **Montel**
   (Conway VII.2.9) — **not Marty** (OB-11 established Marty is not needed) — plus Hurwitz,
   a contour/residue argument for the genuine simple pole, Ahlfors–Shimizu + (UG) for order
   transfer, then Lemma E'.1. The corrected hypotheses are (P), (LB), (ZT.1), (ZT_ℂ),
   (PL⁺), (N), (UG). The **original** hypotheses (LB*)/(H'-pole-sep)/(H'-tail)/(H'-norm)
   were REFUTED (growth gap + pole-cancellation gap, each with a counterexample).

3. **Suzuki-family ingredients OPEN.** This theorem identifies the precise missing
   ingredients for the Suzuki track — (LB), (ZT_ℂ), (PL⁺), (UG), and the odd parity of
   `W(a,θ;z)` — but does not prove or disprove that Suzuki's framework satisfies them.

4. **Does not prove or disprove RH.** E'-neg is a per-fixed-`(k,J)` non-identifiability
   obstacle to a class of convergence arguments; it says nothing about the location of
   Riemann zeros. The reality of the `γ_n` is motivation, never a hypothesis.

5. **Parity/target discipline.** `W(z) = z²ξ(1/2−iz)/ξ'(1/2−iz)` is **ODD** (OB-06), its
   `γ_n` are **simple zeros** (not poles), and its poles come from zeros of `ξ'(1/2−iz)`.
   Lemma E'.1's identity step uses `F/G` even (both `F,G` odd suffices). `W` (Suzuki
   meromorphic) must never be conflated with the CCM entire `Ξ` or its Fourier transform
   `ξ̂` (REFERENCE_BASELINE §5).
