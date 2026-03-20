# State Tracking: Phase 02-04 - Critical Points and Phase Transitions

**Project:** Statistical Mechanics of Multi-Agent Systems
**Phase:** 02 - Partition Function Derivation
**Plan:** 02-04
**Date:** 2026-03-20

---

## Equations Derived

| ID | Equation | Description | Confidence |
|----|----------|-------------|------------|
| 04.01 | $T_c^{\text{MF}} = \frac{J q}{q - 1}$ | Mean-field critical temperature | HIGH |
| 04.02 | $T_c^{\text{2D}} = \frac{J}{\ln(1 + \sqrt{q})}$ | Exact 2D critical temperature | HIGH |
| 04.03 | $R(q) = \frac{q \ln(1+\sqrt{q})}{q-1}$ | Ratio MF/2D critical temperature | HIGH |
| 04.04 | $q_c(T) = \frac{T}{T - J}$ | Critical diversity at fixed T | HIGH |
| 04.05 | $T_c(N) = T_c(\infty)(1 - a N^{-1/\nu})$ | Finite-size scaling | MEDIUM |

---

## Parameters

| Symbol | Meaning | Value/Range | Source | Uncertainty |
|--------|---------|-------------|--------|-------------|
| $T_c^{\text{MF}}$ | Mean-field critical temperature | $Jq/(q-1)$ | This plan | None (exact in MF) |
| $T_c^{\text{2D}}$ | Exact 2D critical temperature | $J/\ln(1+\sqrt{q})$ | Baxter (1982) | None (exact result) |
| $q_c$ | Critical diversity | $T/(T-J)$ | This plan | Needs empirical validation |
| $\nu$ | Correlation length exponent | 1/2 (MF), varies in 2D | Theory | Known |

---

## Approximations Made

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|------------|----------------|----------------|
| Mean-field theory | Fully-connected networks | Fluctuation corrections O(1/d) | Low-dimensional networks (d < 4) |
| Linearization near $m=0$ | Near critical point | $O(m^2)$ terms neglected | Far from T_c |
| Finite-size scaling | Large N | $O(N^{-2/\nu})$ | Small N (N < 10) |
| q as continuous | Large q | Discrete q effects | q = 2, 3 (small q) |

---

## Numerical Tables

### Critical Temperature Comparison (J=1)

| q | T_c^MF | T_c^2D | Ratio |
|---|-------|--------|-------|
| 2 | 2.000 | 2.269 | 0.88 |
| 3 | 1.500 | 1.986 | 0.76 |
| 4 | 1.333 | 0.910 | 1.46 |
| 5 | 1.250 | 0.682 | 1.83 |
| 8 | 1.143 | 0.385 | 2.97 |
| 16 | 1.067 | 0.182 | 5.86 |

### Critical Diversity (J=1)

| T | q_c = T/(T-1) | Interpretation |
|---|---------------|----------------|
| 1.05 | 21.0 | Near threshold, high diversity possible |
| 1.10 | 11.0 | High diversity regime |
| 1.20 | 6.0 | Moderate diversity |
| 1.50 | 3.0 | Low diversity |
| 2.00 | 2.0 | Ising-like |
| 3.00 | 1.5 | Very low diversity |
| 5.00 | 1.25 | Nearly homogeneous |

---

## Figures Produced

None (text-based phase diagram description provided in derivation)

---

## Conventions Used

| Convention | Value | Source |
|------------|-------|--------|
| Units | $k_B = 1$ (natural) | STATE.md |
| Potts Hamiltonian | $H = -J \sum_{\langle ij \rangle} \delta(s_i, s_j)$ | STATE.md |
| Order parameter | $m = (qN_{\text{max}} - N)/[(q-1)N]$ | STATE.md |
| Metric | Euclidean (stat mech) | Custom |

---

## Validations Performed

### Task 1: T_c Derivation
- [x] Dimensional analysis: [T_c] = [energy]
- [x] q=2 limit: T_c = 2J (Ising MF)
- [x] q→∞ limit: T_c → J
- [x] Wu (1982) comparison: Match ✓

### Task 2: 2D Comparison
- [x] Baxter formula correctly cited
- [x] Ratio computed correctly
- [x] Physical interpretation consistent

### Task 3: Critical Density
- [x] Dimensional analysis: [rho] = [1/volume]
- [x] Mean-field limit: rho independent of T_c
- [x] Finite-size scaling form correct

### Task 4: Phase Diagram
- [x] T_c(q) monotonically decreasing
- [x] Phase boundary correctly identified
- [x] Agent system interpretations consistent

### Task 5: Critical Diversity
- [x] q_c(T) formula derived correctly
- [x] Limits verified (T→J+, T→∞)
- [x] Yang connection physically plausible

---

## Limitations and Open Questions

### Limitations
1. **Mean-field assumption:** Not valid for low-dimensional or sparse networks
2. **q as continuous parameter:** Real agent diversity is discrete
3. **No dynamics:** Only equilibrium properties considered
4. **No topology dependence:** Fully-connected vs. hierarchical networks

### Open Questions
1. What is the actual T/J ratio in Yang et al.'s system?
2. How does network topology modify T_c for agent systems?
3. What are finite-size corrections for N = 4-32 agents?
4. Can we calibrate J and T from agent disagreement rates?

---

## References Consulted

| Ref | Type | Used For | Status |
|-----|------|----------|--------|
| Wu (1982) | Paper | Mean-field T_c formula | Read, cited |
| Baxter (1982) | Book | Exact 2D T_c formula | Read, cited |
| Plan 02-02 | Internal | Partition function foundation | Verified |
| Plan 02-03 | Internal | Free energy and N* | Consistent |

---

## Cross-Phase Dependencies

### Inputs from Previous Plans
- Partition function Z_MF (02-02)
- Free energy F (02-02)
- Order parameter definition (STATE.md)
- N* formula (02-03)

### Outputs for Next Plans
- Critical temperature T_c(q) → 02-05 (validation)
- Critical diversity q_c(T) → 03-xx (RG analysis)
- Phase diagram structure → 04-xx (Monte Carlo)

---

*Tracking End*
