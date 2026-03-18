# State Tracking: Phase 02-01

**Project:** Statistical Mechanics of Multi-Agent Systems
**Phase:** 02 - Partition Function Derivation
**Plan:** 02-01
**Last Updated:** 2026-03-18

---

## Equations

| ID | Equation | Description | Confidence | Reference |
|----|----------|-------------|------------|-----------|
| E01 | $s_i \in \{1, 2, \ldots, q\}$ | Agent state space definition | HIGH | Definition |
| E02 | $H = -J \sum_{\langle ij \rangle} \delta(s_i, s_j)$ | Potts Hamiltonian | HIGH | Wu 1982 |
| E03 | $\delta(s_i, s_j) = \begin{cases} 1 & s_i = s_j \\ 0 & s_i \neq s_j \end{cases}$ | Kronecker delta | HIGH | Definition |
| E04 | $\sum_{\langle ij \rangle} \rightarrow \frac{N}{2} \sum_{i \neq j}$ | Mean-field approximation | MEDIUM | Approximation |
| E05 | $\beta = 1/T_{\text{eff}}$ | Inverse temperature (k_B=1) | HIGH | Natural units |
| E06 | $P(\{s_i\}) = \frac{e^{-\beta H}}{Z}$ | Boltzmann distribution | HIGH | Statistical mechanics |
| E07 | $F = U - TS$ | Helmholtz free energy | HIGH | Thermodynamics |
| E08 | $T_{\text{eff}} = \frac{\text{disagreement rate}}{J}$ | Operational T_eff definition | MEDIUM | Proposed mapping |
| E09 | $S = -\sum_{k=1}^{q} p_k \ln p_k$ | Shannon entropy | HIGH | Information theory |

---

## Parameters

| Symbol | Description | Value/Range | Units | Status | Notes |
|--------|-------------|-------------|-------|--------|-------|
| q | Diversity (number of agent types) | 1 - 16 | dimensionless | MAPPED | q=1: homogeneous; q>1: diverse |
| J | Coupling strength | 0.1 - 10 | energy (k_B=1) | MAPPED | J>0: ferromagnetic |
| T_eff | Effective temperature | 0.5 - 2.0 | energy (k_B=1) | MAPPED | T_eff = S (entropy definition) |
| N | Number of agents | 2 - 100 | dimensionless | MAPPED | Finite-size regime |
| s_i | Agent state | {1, ..., q} | dimensionless | MAPPED | Categorical (not ordinal) |
| δ(s_i, s_j) | Alignment operator | 0 or 1 | dimensionless | MAPPED | Kronecker delta |
| H | Hamiltonian (energy) | Depends on config | energy | DERIVED | H = -J Σ δ |
| β | Inverse temperature | 1/T_eff | 1/energy | DERIVED | β = 1/T_eff |
| F | Free energy | -ln Z | energy | DERIVED | F = U - TS |

---

## Approximations

| ID | Approximation | Validity | Break Condition | Check Method |
|----|--------------|----------|-----------------|--------------|
| A01 | Mean-field (fully-connected) | N < 50, all-to-all communication | Sparse/low-dimensional networks | Monte Carlo in Phase 4 |
| A02 | Discrete q (not continuous) | Countable agent types | Fundamental continuous diversity | Gaussian field theory backup |
| A03 | Thermodynamic equilibrium | Stationary distributions | Strong nonequilibrium driving | Time-dependent studies |
| A04 | Categorical states | Distinct agent types | Continuous capability spectrum | Embedding cluster analysis |

---

## Figures

| ID | Figure | Description | File | Status |
|----|--------|-------------|------|--------|
| N/A | N/A | No figures generated in this plan (theory only) | N/A | N/A |

---

## Verification Checklist

### Plan-Level Verification

- [x] Hamiltonian form matches standard Potts model definition
- [x] All dimensions are consistent (k_B=1 natural units)
- [x] Mean-field assumption is explicitly stated
- [x] Energy-performance mapping is logically coherent
- [x] Parameter mapping is complete and operational

### Acceptance Tests

- [x] test-01-mapping: All Potts parameters have operational definitions
- [x] test-01-energy: [H] = [energy], [δ] = [dimensionless]

### Forbidden Proxies

- [x] fp-01-implicit: Hamiltonian includes explicit parameter definitions (avoided)

---

## Convention Compliance

| Convention | Value | Status |
|------------|-------|--------|
| natural_units | k_B = 1 | ✅ Applied |
| fourier_convention | exp(-ikx) | ✅ Stated |
| coupling_convention | H = -J Σ δ, J>0 | ✅ Applied |
| spin_basis | Potts s_i ∈ {1, ..., q} | ✅ Applied |
| state_normalization | Boltzmann P ∝ e^{-βE} | ✅ Applied |

---

## References Cited

| ID | Citation | Used For |
|----|----------|----------|
| R01 | Wu, F. Y. (1982). The Potts Model. Rev. Mod. Phys. | Hamiltonian definition |
| R02 | Baxter, R. J. (1982). Exactly Solved Models | Potts model reference |
| R03 | Yang et al. (2025). arXiv:2602.03794 | Empirical validation |
| R04 | Phase 1 MAPPING-AGENT-TO-POTTS.md | Parameter mappings |

---

## Next Steps

After 02-01 completion:

1. **Plan 02-02:** Derive 1D Potts partition function
2. **Plan 02-03:** Derive mean-field free energy approximation
3. **Plan 02-04:** Compute order parameter and phase transition
4. **Plan 02-05:** Find optimal agent count N*

---

## Issues/Concerns

None. All tasks completed without deviations.

---

*End of State Tracking 02-01*
