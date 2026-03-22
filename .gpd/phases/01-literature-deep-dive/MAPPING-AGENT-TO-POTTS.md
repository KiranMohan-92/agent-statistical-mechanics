# Mapping: Multi-Agent Systems to Potts Model

**Project:** Statistical Mechanics of Multi-Agent Systems
**Phase:** 1 - Literature Deep-Dive
**Created:** 2026-03-16
**Status:** Initial mapping - subject to refinement as empirical data emerges

---

## Overview

This document establishes the explicit mapping between LLM-based multi-agent system properties and the q-state Potts model parameters. The Potts model serves as the statistical mechanical framework for understanding phase transitions, consensus formation, and diversity effects in multi-agent systems.

**Hamiltonian (Potts model):**
```
H = -J \sum_{\langle ij \rangle} \delta(s_i, s_j)
```
where:
- `s_i ∈ {1, 2, ..., q}` is the state of agent `i`
- `J > 0` is the coupling strength (ferromagnetic alignment favored)
- `\langle ij \rangle` denotes interacting agent pairs
- `\delta(s_i, s_j) = 1` if agents are in the same state, `0` otherwise

**Key insight:** The energy is minimized when agents align (same state), which maps to higher task performance when diverse agents successfully coordinate their expertise.

---

## 1. Diversity Parameter `q`

### Definition
The number of distinct states available to each agent in the Potts model.

### Agent System Interpretations

| Interpretation | Physical Meaning in LLM Agents | Operationalization | Challenges |
|----------------|-------------------------------|-------------------|------------|
| **Model types** | Different base LLMs (GPT-4, Claude, Gemini, Llama) | Count distinct models in the system | Discrete, but models have overlapping capabilities |
| **Prompt templates** | Structured prompts defining agent roles | Count unique prompt configurations | Continuous spectrum of prompt variations |
| **Fine-tuning variations** | Models fine-tuned on different domains | Count distinct fine-tuning sources | Gradient of similarity between fine-tunes |
| **Tool specializations** | Agents with access to different tools/APIs | Count distinct tool sets | Tools may be partially overlapping |
| **Embedding clusters** | Clusters in LLM embedding space | Apply k-means to agent outputs | Requires defining similarity metric |

### Discrete vs Continuous Diversity

**Open Question:** Is agent diversity fundamentally discrete or continuous?

- **Arguments for discrete:**
  - LLMs are deployed as discrete model versions
  - Tools/APIs are discrete endpoints
  - Prompt templates are discrete artifacts

- **Arguments for continuous:**
  - Embedding spaces are continuous
  - Fine-tuning creates a continuum of capabilities
  - Semantic similarity between prompts varies continuously

### Decision: Discrete q with Coarse-Graining

**Approach:** Treat q as discrete, but recognize that "effective diversity" may require coarse-graining continuous dimensions:

```
q_eff = number of clusters after applying similarity threshold
```

where clusters are defined by:
```
similarity(agent_i, agent_j) > threshold ⇒ same state
```

### Example Mapping

| System | Physical q | Effective q | Notes |
|--------|-----------|-------------|-------|
| 16 identical GPT-4 agents | 1 | 1 | Homogeneous baseline |
| 2 agents: GPT-4 + Claude | 2 | 2 | Binary diversity |
| 8 agents: 2 each of GPT-4, Claude, Gemini, Llama | 4 | 4 | Model-type diversity |
| 16 agents: each with unique prompt | 16 | 2-8 (depending on prompt similarity) | Prompt diversity (clustered) |

### Calibration Question

**What is the q value that corresponds to "2 diverse agents ≈ 16 homogeneous agents"?**

- If q=2 for diverse (binary: GPT-4 vs Claude) and q=1 for homogeneous, the entropy ratio suggests:
  ```
  S_diverse / S_homogeneous ≈ ln(2) / ln(1) → diverges
  ```
  This implies the mapping is not simply q itself, but how q enters the partition function through entropy terms.

---

## 2. Coupling Strength `J`

### Definition
The strength of interaction between neighboring agents, favoring alignment when `J > 0` (ferromagnetic).

### Agent System Interpretations

| Interpretation | Physical Meaning | Measurement Approach | Expected Scale |
|----------------|-----------------|---------------------|----------------|
| **Communication frequency** | How often agents exchange information | Messages per unit time | High frequency → high J |
| **Shared context** | Overlap in information available to agents | Jaccard similarity of context windows | Large overlap → high J |
| **Collaborative protocols** | Strength of coordination mechanisms | Presence of debate, voting, consensus | Strong protocols → high J |
| **Task interdependence** | Degree to which agents must coordinate | Task structure analysis | High interdependence → high J |

### Operational Definition

For multi-agent systems, we propose:

```
J = (alignment probability) × (interaction strength)
```

where:
- **Alignment probability:** Probability that two agents agree on a given task
- **Interaction strength:** Normalized measure of communication bandwidth

### Measurement Protocol

**To extract J empirically:**

1. **Pairwise agreement measurement:** For each agent pair `(i, j)`, measure:
   ```
   A_{ij} = P(agent_i and agent_j produce same output)
   ```

2. **Baseline correction:** Subtract random baseline:
   ```
   A_{ij}^{corrected} = A_{ij} - A_{random}
   ```

3. **Normalize:** Scale to [0, 1] range (or identify via maximum likelihood fit to Potts model predictions)

### Open Questions

- How does J vary with task complexity?
- Is J symmetric (J_{ij} = J_{ji}) for all agent pairs?
- Does J depend on temporal factors (e.g., early vs late in a task)?

---

## 3. Effective Temperature `T_eff`

### Definition
The noise/stochasticity in the system, controlling the balance between energy minimization (alignment) and entropy maximization (diversity).

### Agent System Interpretations

| Interpretation | Physical Meaning | Measurement Approach | Relationship |
|----------------|-----------------|---------------------|-------------|
| **LLM sampling temperature** | The `temperature` parameter in LLM generation | Direct parameter value | Linear: T_eff ∝ T_LLM |
| **Prompt variability** | Variance in agent responses across runs | Measure response entropy | Positive correlation |
| **Task ambiguity** | Inherent uncertainty in the task specification | Task entropy measures | Higher ambiguity → higher T_eff |
| **Model stochasticity** | Inherent randomness in LLM outputs | Measure variance across seeds | Direct mapping |

### Operational Definition

**Proposed operational definition:**
```
T_eff = (disagreement rate) / (coupling strength)
```

where:
- **Disagreement rate:** Fraction of agent pairs that disagree on outputs
- **Coupling strength J:** As defined above

This definition ensures:
- High T_eff when agents disagree frequently (disordered phase)
- Low T_eff when agents strongly align (ordered phase)
- Normalizes for the communication structure

### Alternative Definition (Entropy-Based)

```
T_eff = S / k_B
```
where `S = -\sum_i p_i \ln p_i` is the Shannon entropy of agent state distribution.

### Calibration Protocol

**To measure T_eff empirically:**

1. **Consensus task:** Design a task with a ground truth answer
2. **Measure agreement:** For each agent, record their response
3. **Compute state distribution:** Count responses in each "state" (answer choice)
4. **Fit to Potts:** Match observed state distribution to Potts model prediction to infer T_eff

### Open Questions

- Does T_eff vary across different tasks?
- How does T_eff relate to the LLM's sampling temperature parameter?
- Is T_eff static for a given system, or does it evolve during task execution?

---

## 4. Agent Count `N`

### Definition
The total number of agents in the multi-agent system.

### Finite-Size Effects

Multi-agent systems operate in the regime `N = 2 - 100`, which is **small** compared to typical statistical mechanics (N → ∞). This has important implications:

| Effect | Description | Relevance to N < 100 |
|--------|-------------|----------------------|
| **Finite-size scaling** | Critical behavior modified by system size | Critical temperature shifted from bulk value |
| **Surface effects** | Boundary agents have different coordination | Important for small N, irregular topologies |
| **Fluctuations** | Relative fluctuations ~ 1/√N | Large (10% for N=100, 25% for N=16) |
| **Thermodynamic limit** | N → ∞ results may not apply | Cannot assume bulk behavior |

### Boundary Conditions

The physical arrangement of agents determines their interaction structure:

| Topology | Description | Mean-Field Validity | Example |
|----------|-------------|---------------------|---------|
| **Fully connected** | Every agent interacts with every other | Excellent | Small teams with shared chat |
| **Hierarchical** | Tree or pyramid structure | Poor (low coordination) | Manager-subordinate structures |
| **Small-world** | Local connections + occasional long-range | Good | Social networks |
| **Sparse** | Each agent interacts with few neighbors | Poor (depends on geometry) | Distributed systems |

### Decision: Mean-Field First Approximation

For initial analysis, assume **mean-field (fully connected)** topology:

```
\sum_{\langle ij \rangle} → (N/2) \sum_{i \neq j}
```

This is justified for:
- Small N where all agents may communicate
- Systems with shared context (chat channels, shared memory)
- Analytical tractability

**Validation required:** Test against specific topologies in later phases.

---

## 5. Hamiltonian Interpretation

### Energy in Agent Systems

The Potts Hamiltonian:
```
H = -J \sum_{\langle ij \rangle} \delta(s_i, s_j)
```

**Physical meaning in agent context:**

| Term | Physics Interpretation | Agent System Interpretation |
|------|-----------------------|----------------------------|
| `H` | Energy of the configuration | Cost/misalignment in agent system |
| `-J` | Negative (favoring alignment) | Alignment is beneficial |
| `\delta(s_i, s_j)` | Kronecker delta (1 if same state) | Agents agree/are compatible |
| `H < 0` | Low energy (favored) | High task performance |
| `H > 0` | High energy (unfavored) | Low task performance, conflict |

### Energy-Performance Mapping

**Hypothesis:** There is an inverse relationship between energy (H) and task performance (P):

```
P ∝ exp(-βH) / Z
```

where:
- Low H (high alignment, many agreements) → High performance
- High H (disagreement, fragmentation) → Low performance

### Critical Insight: Diversity-Allocation Tradeoff

The Hamiltonian reveals a fundamental tradeoff:

1. **Energy term (-J Σ δ):** Favors alignment (low diversity)
2. **Entropy term (k_B T ln Ω):** Favors diversity (high q)

The free energy balance:
```
F = U - TS = -J \sum \delta(s_i, s_j) - k_B T \ln Ω
```

**Interpretation:** Diverse systems (high q) have higher entropy, which can compensate for lower alignment energy. This is the statistical mechanical origin of the "diversity bonus."

---

## 6. Complete Parameter Mapping Summary

| Potts Parameter | Agent System Property | Operational Definition | Measurement Method |
|-----------------|----------------------|----------------------|-------------------|
| **q** (states) | Agent diversity | Effective number of distinct agent types | Cluster analysis of agent outputs |
| **J** (coupling) | Alignment strength | Probability of agent agreement × interaction bandwidth | Pairwise agreement measurement |
| **T_eff** (temperature) | Stochasticity/noise | Disagreement rate / coupling strength | Variance across random seeds |
| **N** (system size) | Number of agents | Direct count | Direct count |
| **⟨ij⟩** (neighbors) | Interaction topology | Communication graph edges | Network analysis of message logs |

---

## 7. Open Questions from Research Phase

### Q1: What is the precise mapping from "LLM agent diversity" to Potts q states?

**Current status:** Multiple interpretations possible (model types, prompts, embeddings)

**Resolution path:**
1. Obtain Yang et al. (2025) and extract their diversity definition
2. If Yang uses model diversity: q = number of distinct models
3. If Yang uses prompt diversity: q = effective number of prompt clusters
4. If Yang uses semantic diversity: discretize embedding space via clustering

**Calibration target:**
```
q=2, N=2  ≈  q=1, N=16
```
in performance. This suggests q enters nonlinearly (likely through entropy).

### Q2: What is the effective temperature T_eff of LLM agent systems?

**Current status:** No direct measurement exists

**Resolution path:**
1. Design consensus tasks with ground truth
2. Measure agent disagreement rates
3. Fit disagreement distribution to Potts model predictions
4. Extract T_eff from best-fit parameters

**Expected range:** T_eff ~ 0.5 - 2.0 (in units of J/k_B), based on typical LLM variability

### Q3: What is the network topology of LLM multi-agent systems?

**Current status:** Framework-dependent (AutoGen vs. CrewAI vs. custom)

**Resolution path:**
1. Characterize default topologies of major frameworks
2. Extract interaction graphs from message logs
3. Compute effective coordination number z_eff
4. Apply topological corrections to mean-field predictions if needed

**Working assumption:** Mean-field (fully connected) for N < 50

---

## 8. Calibration Procedures

### Calibrating J (Coupling Strength)

**Experiment:** Pairwise agreement measurement

1. Select M agents with various diversity configurations
2. Present each agent with K identical tasks
3. Record agent responses and compute pairwise agreement matrix A_{ij}
4. Fit to Potts model prediction:
   ```
   ⟨δ(s_i, s_j)⟩ = f(T_eff, q, J, topology)
   ```
5. Extract J via maximum likelihood

### Calibrating T_eff (Effective Temperature)

**Experiment:** Consensus task variance

1. Select fixed agent set (known q, J)
2. Run consensus task with R random seeds
3. Measure state distribution {n_1, ..., n_q} (counts per state/answer)
4. Compute entropy: S = -Σ (n_i/N) ln(n_i/N)
5. Fit to Boltzmann distribution: P(s) ∝ exp(-βE_s)
6. Extract T_eff from β = 1/(k_B T_eff)

### Calibrating q (Effective Diversity)

**Experiment:** Output clustering

1. Run agents on diverse tasks
2. Collect agent outputs
3. Embed outputs (e.g., using sentence embeddings)
4. Apply clustering (k-means, hierarchical)
5. Determine optimal cluster count via silhouette score or gap statistic
6. Set q = number of clusters

---

## 9. Testable Predictions

Based on this mapping, the following testable predictions emerge:

| Prediction | Statement | How to Test |
|------------|-----------|-------------|
| **P1: Diversity-Entropy** | Task performance increases with q at fixed N (up to optimal q) | Vary number of distinct agent types, measure performance |
| **P2: Phase Transition** | Abrupt change in consensus behavior at critical T_eff | Vary task difficulty/noise, measure agreement rate |
| **P3: Finite-Size Scaling** | Optimal N* scales as N* ~ q^α f(T_eff) with α < 1 | Measure N* for different q, fit scaling law |
| **P4: Coupling Threshold** | Minimum J required for consensus below T_c | Vary communication frequency, measure alignment |
| **P5: Topology Effect** | Hierarchical topologies require higher J for same consensus | Compare flat vs hierarchical agent structures |

---

## 10. Validation Checklist

This mapping is considered validated when:

- [ ] Each parameter (q, J, T_eff) has an operational definition
- [ ] Each parameter can be measured from agent system logs
- [ ] The Potts model with these parameters reproduces key empirical findings
- [ ] The "2 diverse ≈ 16 homogeneous" result is reproduced or explained
- [ ] Finite-size effects for N < 100 are quantified
- [ ] Mean-field assumptions are tested against specific topologies
- [ ] T_eff calibration is demonstrated on at least one consensus task
- [ ] The mapping is documented with clear measurement protocols

---

## 11. Revision History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2026-03-16 | 1.0 | Initial mapping document | gpd-executor |

---

*End of MAPPING-AGENT-TO-POTTS.md*
