# Research State

## Project Reference

See: .gpd/PROJECT.md

**Core research question:** Derive first-principles limits on optimal agent scaling N* = f(H, q, T) in LLM-based multi-agent systems using statistical mechanics (partition functions, Ising/Potts models, renormalization group).
**Current focus:** Preparing for Phase 4: Ising-Agent Simulation (Monte Carlo validation)

## Current Position

**Current Phase:** 04
**Current Phase Name:** Ising-Agent Simulation
**Total Phases:** 10
**Current Plan:** 04-01 (next)
**Total Plans in Phase:** 5
**Status:** active
**Last Activity:** 2026-04-03

**Progress:** [███░░░░░░░] 30%

## Active Calculations

- H = -J Σ_{⟨ij⟩} δ(s_i, s_j) with J > 0 (ferromagnetic)
- State space: s_i ∈ {1, ..., q} categorical
- Mean-field: Σ_{⟨ij⟩} → (N/2) Σ_{i≠j}
- P({s_i}) ∝ exp(-βH)/Z (lower energy = better performance)
- Free energy: F = U - TS (explains diversity bonus)
- q: Number of distinct agent types (1-16)
- J: Alignment strength (0.1-10 in k_B=1 units)
- T_eff: Stochasticity = disagreement rate / J (0.5-2.0)
- N: System size (2-100, finite-size regime)
- claim-01-hamiltonian: PASSED
- claim-02-z-mf: PASSED
- claim-03-nstar: PASSED_WITH_LIMITATION
- claim-04-critical: PASSED
- claim-05-validation: PASSED
- claim-03-01-stability: PASSED
- claim-03-01-ginzburg: PASSED
- claim-03-02-gaussian-fixed-point: PASSED
- claim-03-02-wilson-fisher: PASSED
- claim-03-02-epsilon-expansion: PASSED

## Intermediate Results

- Cataloged 8+ Ising/Potts model applications to agent systems
- Identified 4 established physics results for validation
- 1D Potts: Z = [e^{βJ} + (q-1)]^N
- 2D Potts T_c: k_B T_c/J = 1/ln(1+√q)
- Mean-field T_c: k_B T_c^{MF}/J = q/(q-1)
- Mean-field free energy structure documented
- q → Number of distinct agent types (discrete diversity)
- J → Agent alignment/communication strength
- T_eff → Noise/stochasticity in responses
- N → Agent count (finite-size effects critical for N<100)
- Retrieved arXiv:2602.03794 (fully-connected agent topology)
- Key finding: D_4 (4 diverse) ≈ 16-32 homogeneous agents
- Diversity multiplier: ~4-8× (primary validation target)
- Mean-field assumption validated by fully-connected topology
- ✅ Potts model with mean-field theory
- ✅ Hamiltonian: H = -J Σ_{⟨ij⟩} δ(s_i, s_j)
- ✅ Free energy minimization for N*
- N*(q,T) = (T/2ε) ln[e^{J/2T} + (q-1)e^{-J/2T}] — N* increases with q
- Equal-performance diversity multiplier: max ~3× from pure entropy
- Yang 4-8× requires non-entropic effects (complementarity)
- RG flow equations: dr/dl, du/dl for momentum-shell integration
- Gaussian FP: r*=0, u*=0 with y_r=2, y_u=4-d
- Wilson-Fisher FP: r*~ε, u*~ε for d<4
- Critical exponents: ν=1/2+ε/12, β=1/2-ε/6, γ=1+ε/6
- Correlation length: ξ ~ |T-T_c|^{-1/2} (ν=1/2 mean-field)
- Ginzburg criterion: Gi ~ |T-T_c|^{(4-d)/2}, d=4 upper critical dimension

## Open Questions

- How to incorporate complementarity effects into Hamiltonian?
- What is the actual T/J ratio in Yang et al.'s agent system?
- Can we calibrate ε from Yang's N* data?
- How do finite-size corrections modify N* for N < 20 agents?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| Phases Complete | 3/10 (30%) | - tasks | - files |
| Plans Complete | 11/47 (23%) | - tasks | - files |
| Deliverables Created | ~40 files across 3 phases | - tasks | - files |
| Phase 02-partition-function-derivation | 5 plans | 26 tasks | 20 files |
| Phase 03-phase-transition-analysis | 2 plans (of 5) | 4 tasks | 6 files |

## Accumulated Context

### Decisions

1. Potts model with mean-field theory chosen as framework (2026-03-16)
2. Coordination cost F_cost = εN² added for finite N* prediction (2026-03-19)
3. Yang discrepancy documented: pure entropy gives ~3× max, Yang observes 4-8× (2026-03-19)
4. ε convention corrected: [ε] = [E] since N is dimensionless count (2026-04-03)
5. N* interpretation corrected: N* increases with q (diverse systems sustain larger populations) (2026-04-03)

### Active Approximations

- Mean-field approximation: valid for fully-connected topology, O(1/d) corrections for sparse networks
- Saddle-point approximation: O(1/N) finite-size errors, breaks down at N < 10
- Gaussian fluctuations: valid away from T_c, O(u) near critical point
- Epsilon expansion: O(ε²) errors, unreliable for d ≤ 2 (ε ≥ 2)
- Scalar φ⁴ theory: valid for q=2 (Ising), q>2 requires vector field theory

**Convention Lock:**

- Metric signature: Euclidean (+---)
- Fourier convention: exp(-ikx) forward, exp(ikx) inverse
- Natural units: k_B = 1
- Coordinate system: Cartesian
- Spin basis: Potts s_i ∈ {1, ..., q}
- State normalization: Boltzmann P ∝ e^{-βE}
- Coupling convention: H = -J Σ δ(s_i, s_j), J>0 ferromagnetic

*Custom conventions:*
- Potts Hamiltonian: H = -J Σ_{⟨ij⟩} δ(s_i, s_j), J>0
- Order Parameter: m = (qN_max - N) / [(q-1)N]
- Coordination cost: F_cost = εN², [ε] = [E]

### Propagated Uncertainties

- ε parameter not empirically calibrated — affects N* magnitude but not scaling
- T/J ratio estimated from q_c analysis (1.07-1.14), needs direct measurement
- Mean-field approximation accuracy unknown for N < 50 — requires MC validation (Phase 4)

### Pending Todos

- Phase 4 Plan 04-01: Implement Monte Carlo simulation of agent system on 2D lattice
- Phase 4 Plan 04-02: Validate against mean-field predictions
- Phase 4 Plan 04-03: Finite-size scaling analysis
- Phase 4 Plan 04-04: Compare with Yang et al. empirical data
- Phase 4 Plan 04-05: Extract J and T_eff from simulation

### Blockers/Concerns

None

## Session Continuity

**Last session:** 2026-04-03
**Stopped at:** —
**Resume file:** —
