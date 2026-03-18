# Research State: Statistical Mechanics of Multi-Agent Systems

**Project:** Statistical Mechanics of Multi-Agent Systems
**Initialized:** 2026-03-16

---

## Session Continuity

**Current Phase:** Phase 2: Partition Function Derivation
**Status:** in_progress
**Current Plan:** 02-01 (COMPLETE), 02-02 (next)
**Last session:** 2026-03-18
**Resume file:** .gpd/phases/02-partition-function-derivation/02-01-SUMMARY.md

---

## Project Reference

**Core research question:** Derive first-principles limits on optimal agent scaling N* = f(H, q, T) in LLM-based multi-agent systems using statistical mechanics (partition functions, Ising/Potts models, renormalization group).

**Current focus:** Deriving partition function Z(N, q, T) using Potts model with mean-field theory

---

## Current Position

**Phase:** Phase 2: Partition Function Derivation
**Status:** in_progress
**Progress:** 15% complete (1/10 phases, 2/44 plans)

**Last session:** 2026-03-18
**Stopped at:** Plan 02-01 complete; ready for Plan 02-02 (1D partition function)
**Resume file:** .gpd/phases/02-partition-function-derivation/02-01-SUMMARY.md

---

## Active Calculations

### Phase 2 Plan 02-01: Hamiltonian Definition (COMPLETE 2026-03-18)

**Hamiltonian established:**
- H = -J Σ_{⟨ij⟩} δ(s_i, s_j) with J > 0 (ferromagnetic)
- State space: s_i ∈ {1, ..., q} categorical
- Mean-field: Σ_{⟨ij⟩} → (N/2) Σ_{i≠j}

**Energy-performance mapping:**
- P({s_i}) ∝ exp(-βH)/Z (lower energy = better performance)
- Free energy: F = U - TS (explains diversity bonus)

**Parameter mappings complete:**
- q: Number of distinct agent types (1-16)
- J: Alignment strength (0.1-10 in k_B=1 units)
- T_eff: Stochasticity = disagreement rate / J (0.5-2.0)
- N: System size (2-100, finite-size regime)

**Contract results:**
- claim-01-hamiltonian: PASSED
- deliv-01-hamiltonian: PASSED
- deliv01-state-space: PASSED
- test-01-mapping: PASSED
- test-01-energy: PASSED
- fp-01-implicit: REJECTED (explicit definitions provided)

**Next:** Plan 02-02 - Derive 1D Potts partition function

---

## Intermediate Results

### Phase 1 Literature Deep-Dive (2026-03-16)

**Literature Survey:**
- Cataloged 8+ Ising/Potts model applications to agent systems
- Identified 4 established physics results for validation
  - 1D Potts: Z = [e^{βJ} + (q-1)]^N
  - 2D Potts T_c: k_B T_c/J = 1/ln(1+√q)
  - Mean-field T_c: k_B T_c^{MF}/J = q/(q-1)
  - Mean-field free energy structure documented

**Agent-to-Potts Mapping:**
- q → Number of distinct agent types (discrete diversity)
- J → Agent alignment/communication strength
- T_eff → Noise/stochasticity in responses
- N → Agent count (finite-size effects critical for N<100)

**Yang et al. (2025) Analysis:**
- Retrieved arXiv:2602.03794 (fully-connected agent topology)
- Key finding: D_4 (4 diverse) ≈ 16-32 homogeneous agents
- Diversity multiplier: ~4-8× (primary validation target)
- Mean-field assumption validated by fully-connected topology

**Framework Decision:**
- ✅ Potts model with mean-field theory
- ✅ Hamiltonian: H = -J Σ_{⟨ij⟩} δ(s_i, s_j)
- ✅ Free energy minimization for N*

---

## Open Questions

1. What is the precise value of the diversity multiplier from first-principles derivation?
2. How does T_eff vary with task complexity in LLM systems?
3. What are the finite-size corrections for N=2-100 agent systems?
4. How does network topology affect mean-field predictions?

---

## Performance Metrics

| Metric | Value |
|--------|-------|
| Phases Complete | 1/10 (10%) |
| Plans Complete | 1/44 (2.3%) |
| Requirements Satisfied | 4/27 (15%) |
| Deliverables Created | 4 files (60 KB total) |

---

### Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-16 | Potts model with mean-field theory | Yang et al. fully-connected topology validates mean-field |
| 2026-03-16 | q as discrete diversity parameter | Maps to D_1, D_4, D_8, D_16 from Yang paper |
| 2026-03-16 | Free energy minimization for N* | F = U - TS; diversity contributes to entropy |
| 2026-03-16 | k_B = 1 natural units | Simplifies thermodynamic expressions |

### Active Approximations

| Approximation | Validity | Breaks When |
|--------------|----------|-------------|
| Mean-field theory | Fully-connected networks | Low-dimensional/sparse networks |
| Discrete diversity states | Countable agent types | Diversity fundamentally continuous |
| Thermodynamic equilibrium | Stationary distributions | Strong nonequilibrium driving |

### Propagated Uncertainties

| Source | Impact | Mitigation |
|--------|--------|------------|
| Mean-field approximation | May fail for low-d networks | Monte Carlo validation (Phase 4) |
| Diversity discretization | May miss continuous effects | Gaussian field theory backup |

### Pending Todos

- Phase 2 Plan 02-02: Derive 1D Potts partition function Z(N, q, T)
- Phase 2 Plan 02-03: Derive mean-field free energy approximation
- Phase 2 Plan 02-04: Compute order parameter and critical temperature
- Phase 2 Plan 02-05: Find optimal agent count N* from free energy minimization

### Blockers/Concerns

(None)

---

## Accumulated Context

### Phase 1 Deliverables
- LITERATURE-SURVEY.md (22 KB) - Ising/Potts applications catalog
- MAPPING-AGENT-TO-POTTS.md (16 KB) - Parameter mappings
- YANG-GAP.md (12 KB) - Yang et al. analysis
- 01-01-SUMMARY.md (10 KB) - Phase summary

### Phase 2 Deliverables (Plan 02-01)
- 02-01-derivation.md (317 lines) - Hamiltonian and state space definition
- 02-01-LOG.md - Research log with task execution records
- 02-01-STATE-TRACKING.md - State tracking with equations and parameters
- 02-01-SUMMARY.md - Full summary with contract results

### Key References for Phase 2
- Baxter (1982) - Exact Potts solutions
- Wu (1982) - Potts model review
- Goldenfeld (1992) - Phase transitions and RG
- Yang et al. (2025) - Empirical validation target

---

**Convention Lock:**
- **k_B = 1** (natural units)
- **Fourier:** exp(-ikx) forward, exp(ikx) inverse
- **Potts Hamiltonian:** H = -J Σ_{⟨ij⟩} δ(s_i, s_j), J>0
- **Order parameter:** m = (qN_max - N) / [(q-1)N]

---

_Last updated: 2026-03-18_
