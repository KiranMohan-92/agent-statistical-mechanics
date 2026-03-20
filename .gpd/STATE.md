# Research State: Statistical Mechanics of Multi-Agent Systems

**Project:** Statistical Mechanics of Multi-Agent Systems
**Initialized:** 2026-03-16

---

## Session Continuity

**Current Phase:** Phase 2: Partition Function Derivation
**Status:** in_progress
**Current Plan:** 02-04 (COMPLETE), 02-05 (next)
**Last session:** 2026-03-20
**Resume file:** .gpd/phases/02-partition-function-derivation/02-04-SUMMARY.md

---

## Project Reference

**Core research question:** Derive first-principles limits on optimal agent scaling N* = f(H, q, T) in LLM-based multi-agent systems using statistical mechanics (partition functions, Ising/Potts models, renormalization group).

**Current focus:** Deriving partition function Z(N, q, T) using Potts model with mean-field theory

---

## Current Position

**Phase:** Phase 2: Partition Function Derivation
**Status:** in_progress
**Progress:** [████████░░] 80%

**Last session:** 2026-03-20
**Stopped at:** Plan 02-04 complete; ready for Plan 02-05 (validation against empirical data)
**Resume file:** .gpd/phases/02-partition-function-derivation/02-04-SUMMARY.md

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

**Next:** Plan 02-03 - Mean-field free energy minimization

### Phase 2 Plan 02-02: Mean-Field Partition Function (COMPLETE 2026-03-18)

**Partition function derived:**
- Z_MF(N, q, T) = [e^{βJ/2} + (q-1)e^{-βJ/2}]^N
- Hubbard-Stratonovich transformation used for exact evaluation
- 1D exact comparison: Z_1D = [e^{βJ} + (q-1)]^N (Baxter 1982)

**Thermodynamic quantities:**
- U = -(NJ/2) * [e^{βJ/2} - (q-1)e^{-βJ/2}] / [e^{βJ/2} + (q-1)e^{-βJ/2}]
- F = -(N/β) * ln[e^{βJ/2} + (q-1)e^{-βJ/2}]
- S = βU + ln Z
- C = N(βJ)^2 q e^{βJ} / [e^{βJ/2} + (q-1)e^{-βJ/2}]^4

**Limiting cases verified:**
- q=1: Z = e^{βJN/2} (homogeneous)
- q=2: Z = [2 cosh(βJ/2)]^N (Ising)
- β → 0: Z → q^N (high-T)
- β → ∞: Z → e^{βJN/2} (ground state)

**Contract results:**
- claim-02-z-mf: PASSED
- deliv-02-z-mf: PASSED
- deliv-02-derivation: PASSED
- test-02-1d-limit: PASSED
- test-02-q1-limit: PASSED
- ref-02-baxter: COMPLETED (read/use/compare)
- ref-02-wu: COMPLETED (read/use)
- fp-02-skip-validation: REJECTED (all limits verified)

**Next:** Plan 02-04 - Compute order parameter and critical temperature

### Phase 2 Plan 02-03: Mean-Field Free Energy and N* (COMPLETE 2026-03-19)

**Free energy with coordination costs:**
- F_total(N,q,T) = -(N/beta) ln[e^(beta*J/2) + (q-1)e^(-beta*J/2)] + epsilon*N^2
- Coordination cost epsilon*N^2 essential for finite N* (Deviation Rule 4)

**Optimal agent count:**
- N*(q,T) = (T/(2*epsilon)) ln[e^(J/2T) + (q-1)e^(-J/2T)]
- Low T: N* → J/(4*epsilon) (constant)
- High T: N* → (T ln q)/(2*epsilon) (linear in T)

**Diversity scaling:**
- N*(q=1)/N*(q=2) ≈ 1.03-1.10 (3-10% benefit)
- N*(q=1)/N*(q=4) ≈ 1.06-1.26 (6-26% benefit)
- Asymptotic limit: 2× maximum benefit from entropy alone

**Yang comparison:**
- Model predicts 1.2-2× diversity multiplier
- Yang observes 4-8× diversity multiplier
- Discrepancy indicates non-entropic complementarity effects

**Contract results:**
- claim-03-nstar: PASSED_WITH_LIMITATION (Yang ratio discrepancy documented)
- deliv-03-nstar: PASSED
- deliv-03-minimization: PASSED
- test-03-diversity-reduction: PASSED_WITH_CAVEAT (magnitude too small)
- test-03-temperature-dependence: PASSED
- ref-03-goldenfeld: COMPLETED (read/use)
- ref-03-yang: COMPLETED (read/compare, discrepancy documented)

**Next:** Plan 02-04 - Compute order parameter m(T) and critical temperature T_c(q)

### Phase 2 Plan 02-04: Critical Points and Phase Transitions (COMPLETE 2026-03-20)

**Critical temperature derived:**
- T_c^MF = Jq/(q-1) (mean-field)
- T_c^2D = J/ln(1+√q) (exact 2D, Baxter 1982)
- q=2 gives T_c=2J (correct Ising mean-field)
- q→∞ gives T_c→J (approaches coupling from above)

**Critical diversity:**
- q_c(T) = T/(T-J) for T > J
- Yang saturation at D_8-D_16 implies T/J ≈ 1.07-1.14
- q_c → ∞ as T → J+ (any diversity works at low noise)
- q_c → 1 as T → ∞ (only homogeneous works at high noise)

**Phase diagram:**
- Ordered (T < T_c): Consensus, agents align
- Disordered (T > T_c): Fragmentation, no consensus
- Mean-field underestimates T_c for q=2,3; overestimates for q≥4

**Contract results:**
- claim-04-critical: PASSED
- deliv-04-tc: PASSED
- deliv04-phasediagram: PASSED
- test-04-wu-comparison: PASSED
- test-04-baxter-limit: PASSED
- ref-04-wu: COMPLETED (read/compare/cite)
- ref-04-baxter: COMPLETED (read/compare)

**Next:** Plan 02-05 - Validate N* predictions against empirical data

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

1. **PARTIALLY ANSWERED:** Diversity multiplier from entropic effects is 1.2-2× (vs 4-8× empirical). Missing non-entropic complementarity effects.
2. How does T_eff vary with task complexity in LLM systems?
3. What are the finite-size corrections for N=2-100 agent systems?
4. How does network topology affect mean-field predictions?

---

## Performance Metrics

| Metric | Value |
|--------|-------|
| Phases Complete | 1/10 (10%) |
| Plans Complete | 4/44 (9.1%) |
| Requirements Satisfied | 8/27 (30%) |
| Deliverables Created | 16 files (160 KB total) |

---
| Phase 02-partition-function-derivation P02 | 16 | 5 tasks | 4 files |

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
| Quadratic coordination cost | All-to-all communication | Hierarchical/sparse topologies |
| Pure entropic diversity | No complementarity | Real agent systems (Yang discrepancy) |

### Propagated Uncertainties

| Source | Impact | Mitigation |
|--------|--------|------------|
| Mean-field approximation | May fail for low-d networks | Monte Carlo validation (Phase 4) |
| Diversity discretization | May miss continuous effects | Gaussian field theory backup |

### Pending Todos

- Phase 2 Plan 02-05: Validate N* predictions against empirical data
- **ANSWERED:** Critical diversity q_c = T/(T-J) explains Yang saturation at D_8-D_16
- **NEW:** Calibrate T/J ratio from Yang et al. agent disagreement data
- **NEW:** Extend Hamiltonian to include complementarity effects (address Yang discrepancy)

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

### Phase 2 Deliverables (Plan 02-02)
- 02-02-partition-function.md (459 lines) - Mean-field partition function derivation
- 02-02-LOG.md - Research log with task execution records
- 02-02-STATE-TRACKING.md - State tracking with equations and parameters
- 02-02-SUMMARY.md - Full summary with contract results

### Phase 2 Deliverables (Plan 02-03)
- 02-03-free-energy.md (450+ lines) - Free energy and optimal N* derivation
- 02-03-LOG.md - Research log with task execution records
- 02-03-STATE-TRACKING.md - State tracking with equations, parameters, numerical tables
- 02-03-SUMMARY.md - Full summary with contract results and Yang comparison

### Phase 2 Deliverables (Plan 02-04)
- 02-04-critical-points.md (400+ lines) - Critical temperature, phase transitions, critical diversity
- 02-04-LOG.md - Research log with task execution records
- 02-04-STATE-TRACKING.md - State tracking with equations, parameters, numerical tables
- 02-04-SUMMARY.md - Full summary with contract results and Wu/Baxter comparisons

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

_Last updated: 2026-03-20_
