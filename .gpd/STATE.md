# Research State

## Project Reference

See: .gpd/PROJECT.md

**Core research question:** Derive first-principles limits on optimal agent scaling N* = f(H, q, T) in LLM-based multi-agent systems using statistical mechanics (partition functions, Ising/Potts models, renormalization group).
**Current focus:** Deriving partition function Z(N, q, T) using Potts model with mean-field theory

## Current Position

**Current Phase:** Phase 2: Partition Function Derivation
**Current Phase Name:** —
**Total Phases:** —
**Current Plan:** 02-01 (COMPLETE), 02-02 (next)
**Total Plans in Phase:** —
**Status:** in_progress
**Last Activity:** —

**Progress:** [█████░░░░░] 50%

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
- deliv-01-hamiltonian: PASSED
- deliv01-state-space: PASSED
- test-01-mapping: PASSED
- test-01-energy: PASSED
- fp-01-implicit: REJECTED (explicit definitions provided)

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

## Open Questions

None yet.

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| Phases Complete | 1/10 (10%) | - tasks | - files |
| Plans Complete | 1/44 (2.3%) | - tasks | - files |
| Requirements Satisfied | 4/27 (15%) | - tasks | - files |
| Deliverables Created | 4 files (60 KB total) | - tasks | - files |
| Phase 02-partition-function-derivation P02 | 12 | 5 tasks | 4 files |

## Accumulated Context

### Decisions

None yet.

### Active Approximations

None yet.

**Convention Lock:**

- Metric signature: Euclidean (+---)
- Fourier convention: exp(-ikx) forward, exp(ikx) inverse
- Natural units: k_B = 1
- Coordinate system: Cartesian

*Custom conventions:*
- Fourier: ** exp(-ikx) forward, exp(ikx) inverse
- Potts Hamiltonian: ** H = -J Σ_{⟨ij⟩} δ(s_i, s_j), J>0
- Order Parameter: ** m = (qN_max - N) / [(q-1)N]

### Propagated Uncertainties

None yet.

### Pending Todos

- Phase 2 Plan 02-02: Derive 1D Potts partition function Z(N, q, T)
- Phase 2 Plan 02-03: Derive mean-field free energy approximation
- Phase 2 Plan 02-04: Compute order parameter and critical temperature
- Phase 2 Plan 02-05: Find optimal agent count N* from free energy minimization

### Blockers/Concerns

None

## Session Continuity

**Last session:** 2026-03-18
**Stopped at:** —
**Resume file:** .gpd/phases/02-partition-function-derivation/02-01-SUMMARY.md
