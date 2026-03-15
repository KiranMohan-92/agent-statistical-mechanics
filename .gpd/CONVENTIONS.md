# Conventions: Statistical Mechanics of Multi-Agent Systems

**Domain:** Statistical Mechanics applied to Multi-Agent Systems
**Established:** 2026-03-16

---

## Sign Conventions

### Metric Signature
- Not applicable (Euclidean/statistical mechanics context)

### Fourier Transforms
- Forward: $\tilde{f}(k) = \int dx \, e^{-ikx} f(x)$
- Inverse: $f(x) = \frac{1}{2\pi} \int dk \, e^{ikx} \tilde{f}(k)$

### Boltzmann Distribution
- $P_i \propto e^{-\beta E_i}$ where $\beta = 1/k_B T$

---

## Unit System

**Natural units:** $k_B = 1$ (Boltzmann constant set to unity)
- Temperature $T$ in energy units
- All thermodynamic quantities dimensionless or in energy units

---

## Notation Standards

| Symbol | Meaning | Context |
|--------|---------|---------|
| $N$ | Number of agents | System size |
| $q$ | Number of diversity states (Potts model) | Agent diversity |
| $T$ | Temperature (effective) | Task complexity/noise |
| $\beta$ | $1/k_B T$ | Inverse temperature |
| $Z$ | Partition function | Statistical mechanics |
| $F$ | Free energy ($F = -k_B T \ln Z$) | Thermodynamics |
| $J$ | Coupling strength | Interaction energy |
| $\rho$ | Agent density ($N/V$) | Density |
| $\rho_c$ | Critical agent density | Phase transition |
| $\xi$ | Correlation length | Spatial correlations |
| $s_i$ | Spin state at site $i$ | Ising/Potts model |
| $\langle \cdot \rangle$ | Thermal average | Expectation value |
| $H$ | Hamiltonian | Energy function |
| $S$ | Entropy | Information content |

---

## Critical Phenomena

### Critical Exponents
| Exponent | Definition | Standard Mean-Field Value |
|----------|------------|--------------------------|
| $\alpha$ | Heat capacity: $C \sim |T-T_c|^{-\alpha}$ | 0 (jump) |
| $\beta$ | Order parameter: $m \sim (T_c-T)^\beta$ | 1/2 |
| $\gamma$ | Susceptibility: $\chi \sim |T-T_c|^{-\gamma}$ | 1 |
| $\delta$ | Critical isotherm: $m \sim h^{1/\delta}$ | 3 |
| $\nu$ | Correlation length: $\xi \sim |T-T_c|^{-\nu}$ | 1/2 |
| $\eta$ | Correlation function: $G(r) \sim r^{-(d-2+\eta)}$ | 0 |

---

## Potts Model Convention

- **q-state Potts Hamiltonian:** $H = -J \sum_{\langle ij \rangle} \delta_{\sigma_i, \sigma_j}$
- **Spins:** $\sigma_i \in \{1, 2, \dots, q\}$
- **Coupling:** $J > 0$ (ferromagnetic alignment favored)

---

## Phase Diagram Conventions

- **Ordered phase:** $T < T_c$ (agents aligned/synchronized)
- **Disordered phase:** $T > T_c$ (agents independent)
- **Critical point:** $T = T_c$, $\rho = \rho_c$

---

## Assert Conventions

All files in this project should assert:
```latex
% ASSERT_CONVENTION: k_B=1, beta=1/T
% ASSERT_CONVENTION: metric=euclidean
% ASSERT_CONVENTION: fourier=exp(-ikx)
```

---

_Last updated: 2026-03-16_
