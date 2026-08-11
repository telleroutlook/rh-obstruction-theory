# Checker README — Theorem E' (E-prime-meromorphic)

E' is purely analytic (no finite numerical certificate). These are the analytic
check-items, updated after OB-06/09/11.

C-E'-1: Lemma E'.1 (meromorphic Hadamard uniqueness) — CONFIRMED (OB-06) via the
        `H := F/G` entire-zero-free route + Hadamard (Conway XI.3.4). No separate
        Weierstrass-product computation needed (the old P,P',Q,Q' route had a canonical-
        product error; the ratio route avoids it).

C-E'-2: Meromorphic IFT for E'-neg — CONFIRMED-after-correction (OB-09 §7): the direct
        `w₀`-jet system `Ψ_j(u,c)=∂_t^j L(t₀;u,c)` with rational Wronskian–Vandermonde
        Jacobian `det = (−t₀)^J (∏ j!) ∏_{p<q}(x_q−x_p) / ∏(1−x_ℓ t₀)^J ≠ 0`. Written out
        in proof.md §3. (The earlier power-sum system Φ_r was REFUTED — it matches the
        z=0 expansion, not the `w₀`-jet.)

C-E'-3: WITHDRAWN. The `|W(iR)| → ∞` claim was REFUTED (OB-09 §2.2): false in general
        (counterexample `A=sin(πz)/(πz)`, `B=z cos(2πz)` gives `|W(iR)| → 0`). Separation
        is by a Cauchy coefficient estimate on the leading `z^{2J+3}` discrepancy, NOT by
        any growth-to-infinity argument.

Whole-theorem Gate-A review: OB-30 (pending).
