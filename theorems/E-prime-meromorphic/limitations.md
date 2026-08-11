# Limitations — Theorem E' (E-prime-meromorphic)

1. **E'-neg is PROOF-DRAFT (CONFIRMED-after-correction, OB-09).** The meromorphic IFT
   step is written out explicitly: the direct `w₀`-jet system `Ψ_j(u,c)=∂_t^j L(t₀;u,c)`
   with the rational Wronskian–Vandermonde Jacobian (proof.md §3, OB-09 §7). Not yet
   INDEPENDENTLY-CHECKED (whole-theorem Gate-A review OB-30 pending).

2. **E'-pos is PROOF-DRAFT (corrected, OB-11), not OPEN.** The proof uses **Montel**
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
