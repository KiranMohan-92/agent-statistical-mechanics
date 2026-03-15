# Statistical Mechanics of Multi-Agent Systems

## What This Is

A physics research project applying statistical mechanics (Ising/Potts models, partition functions, renormalization group) to derive fundamental limits on optimal agent scaling in LLM-based multi-agent systems. Goal: produce a first-principles derivation of when adding agents helps vs. hurts, validated against real-world production data.

## Core Research Question

**Can we derive the optimal number and diversity of AI agents from the partition function of a multi-agent system, analogous to how thermodynamics emerges from statistical mechanics?**

## Scoping Contract Summary

### Contract Coverage

- **Claim**: Derivation of N* = f(H, q, T) — closed-form formula for optimal agent count from first principles
- **Acceptance signal**: Reproduces Yang et al. (2025) "2 diverse agents ≈ 16 homogeneous agents" as special case
- **False progress to reject**: Qualitative trend matches without quantitative comparison to partition function predictions

### User Guidance To Preserve

- **User-stated observables**: Critical agent density ρ_c, diversity threshold q*, correlation length ξ
- **User-stated deliverables**: Closed-form N* formula, phase transition diagrams, validation plots
- **Must-have references**: Yang et al. (2025) "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity"
- **Stop/rethink conditions**: If model fails R² > 0.8 on Content Factory data or fails to predict ≥30/38 ING jurisdictions

### Scope Boundaries

**In scope**
- Statistical mechanics formalism applied to LLM agent systems
- Partition function derivation for N-agent systems
- Ising/Potts model simulations
- Validation against Content Factory and ING AML production data
- First-principles derivation of optimal agent scaling

**Out of scope**
- Training or fine-tuning LLMs
- Building new agent frameworks (AutoGen, CrewAI)
- Quantum multi-agent systems
- Biological swarm intelligence (except as analogy)

### Active Anchor Registry

- **Yang et al. 2025**: "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity" (arXiv:2602.03794)
  - Why it matters: Empirical result (2 diverse agents match 16 homogeneous) that we aim to derive theoretically
  - Carry forward: planning, verification, writing
  - Required action: compare, cite, reproduce as limiting case

### Carry-Forward Inputs

- Content Factory production metrics (tasks completed, agent diversity, collaboration patterns)
- ING AML system data from 38 jurisdictions
- Phase structure from AGENT-STATISTICAL-MECHANICS-PLAN.md

### Skeptical Review

- **Weakest anchor**: Assumption that Ising/Potts Hamiltonian correctly models LLM agent interactions
- **Unvalidated assumptions**: Agent interactions are short-range, system near equilibrium, task-assignment maps to spin states
- **Competing explanation**: Optimal agent count emerges from network topology (graph theory) rather than statistical mechanics
- **Disconfirming observation**: If Content Factory data shows no phase transition signature, the statistical mechanics analogy may be invalid
- **False progress to reject**: Empirical agent counting without theoretical framework

### Open Contract Questions

- What is the correct "temperature" T_eff for an agent system? (Maps to task complexity, communication cost?)
- How to handle non-equilibrium dynamics? (Agents adapt during task execution)
- Does the partition function converge as N → ∞ for agent systems?

## Research Questions

### Answered

(None yet — investigate to answer)

### Active

- [ ] Can we derive optimal agent diversity q* from Potts model free energy minimization?
- [ ] What is the critical agent density ρ_c for phase transition in collective task performance?
- [ ] Does the correlation length ξ scale with system size as predicted by renormalization group?
- [ ] Can we validate the theoretical model against real-world multi-agent data?

### Out of Scope

- [ ] Training dynamics of individual LLMs — requires ML expertise outside statistical mechanics
- [ ] Agent communication protocols — network science domain, not physics

## Research Context

### Physical System

LLM-based multi-agent systems (AutoGen, CrewAI, LangChain) where agents:
- Have internal states (opinions, task assignments)
- Interact via message passing
- Collaborate on shared goals

### Theoretical Framework

**Statistical Mechanics**: Partition functions, free energy minimization, phase transitions, renormalization group
**Models**: Ising model (agent alignment), Potts model (agent diversity), mean-field theory

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
|-----------|--------|--------|-------|
| Agent count | N | 1-1000+ | From Yang et al.: 2-16 studied |
| Diversity states | q | 2-∞ | Agent types/capabilities |
| Effective temperature | T_eff | T > 0 | Task complexity, noise |
| Coupling strength | J | -∞ to +∞ | Interaction strength between agents |
| Correlation length | ξ | 1-N | Spatial/temporal scale of correlations |

### Known Results

- **Yang et al. 2025**: "2 diverse agents match or exceed performance of 16 homogeneous agents" (empirical)
- **Ising model**: Phase transition at critical temperature T_c for ferromagnetic ordering
- **Potts model**: q-state generalization; critical behavior depends on q
- **Mean field theory**: Predicts phase transitions but misses fluctuations in low dimensions

### What Is New

- **First-principles derivation** of optimal agent scaling (not empirical)
- **Partition function approach** to multi-agent systems
- **Statistical physics validation** of real-world agent deployment data

### Target Venue

**Primary**: Physical Review E (Statistical Physics)
**Backup**: Nature Machine Intelligence, NeurIPS, ICLR, AAMAS

Rationale: PRL E publishes statistical mechanics breakthroughs; Nature MI and ML conferences value rigor + practical relevance.

### Computational Environment

- Local workstation for derivations (Jupyter, Python)
- Optional: Cloud/cluster for large-scale simulations
- Content Factory: Production multi-agent system for validation
- ING AML systems: 38-jurisdiction deployment data

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for all notation and sign conventions.
See `.gpd/NOTATION_GLOSSARY.md` for symbol definitions.

## Unit System

Natural units for statistical mechanics: k_B = 1 (Boltzmann constant set to 1)
Temperature T in energy units (or dimensionless when working with T/T_c ratios)

## Requirements

See `.gpd/REQUIREMENTS.md` for the detailed requirements specification.

## Key References

Mirror of contract-critical anchors only:

- **Yang et al. 2025**: "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity" (arXiv:2602.03794) — Primary empirical anchor

## Constraints

- **Data access**: Content Factory and ING data require proper sanitization (38 jurisdictions, production systems)
- **Computational**: Large-scale simulations (Monte Carlo) may require cluster resources
- **Timeline**: 16-week target for first paper submission

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|----------|
| Statistical mechanics framework | Unified theory for agent systems | — Active |
| Ising/Potts models | Well-understood, tractable | — Active |
| Validation against real data | Ensures practical relevance | — Active |

Full log: `.gpd/DECISIONS.md`

---

_Last updated: 2026-03-16 after initialization_
