# Novelty — Theorem G (G-fredholm-certificate)

**Theorem ID:** G-fredholm-certificate  
**Program ref:** §9.G

---

## Prior art

### Sibling repository (absolute-arithmetic-spectral-verification)

The sibling repo documents the CORE-4 [OBL] as an engineering observation
(`proof/m5/determinant_approximation.py`): the kappa_toeplitz construction cannot
close CORE-4 because the S(T) eigenvalue error is present. This is recorded as a
technical obstacle, not a theorem. It does not:
- give a precise method class definition (𝔐_FC);
- prove a no-go theorem for any class of methods;
- explicitly exhibit the observation collision as a mathematical object.

Theorem G lifts this engineering observation to a scoped mathematical theorem
(at PROOF-DRAFT level for G-info).

### Titchmarsh, Davenport (classical references)

The S(T) gap identity and Hadamard uniqueness are classical. Theorem G's contribution
is NOT the individual lemmas but their combination into an information-obstruction
theorem for the Fredholm certificate method class.

### Connes–Consani–Moscovici (arXiv:2511.22755)

The CCM framework is a Fredholm-type spectral approach but targets the entire Ξ
function via a different construction (spectral triples, not kappa_toeplitz). The
E-neg/E-pos theorems (Theorem E) already analyze the CCM approach. Theorem G is
specific to the theta-level observation class (which includes kappa_toeplitz but
is not the same as CCM).

---

## New content assessment

| Aspect | Status |
|---|---|
| 𝔐_FC method class definition with syntactic non-anticipation constraint | NEW |
| Theorem G information obstruction (S(T) gap + Hadamard uniqueness → CORE-4 [OBL]) | NEW (PROOF-DRAFT) |
| Explicit adversary pair (𝒵_RH vs 𝒵_ε, observation collision) | NEW |
| Connection to sibling repo CORE-4 obstruction engineering record | NEW |
| G-hard conjecture (S(T) irrecoverable from zero-free primes) | NEW (CONJECTURE) |

---

## Novelty gate decision

**NOVELTY GATE: OPEN (pending independent review of G-info argument).**

The argument is structurally sound and the new content (method class 𝔐_FC + S(T) obstruction
theorem) does not appear in prior literature. However, because G-info is PROOF-DRAFT
(the explicit ε̃_n exhibit in Prop. G.3 is the open step), the novelty gate stays OPEN
until G-info is independently confirmed.

The theorem adds genuine value: it converts the sibling repo's engineering stop condition
into a precise information-obstruction theorem with a named class, observation map,
and adversary pair — exactly the §14 acceptance test structure.
