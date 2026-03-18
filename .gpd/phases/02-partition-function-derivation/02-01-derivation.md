# Derivation: Potts Model Hamiltonian for Multi-Agent Systems

**Project:** Statistical Mechanics of Multi-Agent Systems
**Phase:** 02 - Partition Function Derivation
**Plan:** 02-01 - Define Hamiltonian and State Space
**Created:** 2026-03-18
**Status:** In Progress

---

## Convention Assertions

% ASSERT_CONVENTION: natural_units=k_B=1, metric_signature=Euclidean, fourier_convention=exp(-ikx), coupling_convention=H=-J*sum(delta), potts_hamiltonian=H=-J*delta_ij_ferromagnetic, spin_basis=Potts

---

## 1. Agent State Space Definition

### 1.1 Formal Definition

Each agent in the multi-agent system is represented by a discrete state variable:

$$s_i \in \{1, 2, \ldots, q\}$$

where:
- $i = 1, \ldots, N$ indexes the agents
- $q$ is the number of available states (diversity parameter)
- The states are **categorical** (not ordinal), consistent with the Potts model formalism

### 1.2 LLM Agent Interpretation

The discrete state space maps to LLM agent diversity in three equivalent ways:

| Interpretation | Physical Meaning | Example |
|----------------|-----------------|---------|
| **Model types** | Different base LLM architectures | $\{q=1\}$: 16 identical GPT-4 agents<br>$\{q=2\}$: 8 GPT-4 + 8 Claude |
| **Prompt templates** | Distinct agent personas/prompts | $\{q=4\}$: Analyst, Critic, Synthesizer, Validator |
| **Embedding clusters** | Effective clusters from semantic analysis | $q_{\text{eff}}$ from $k$-means on response embeddings |

### 1.3 Homogeneous vs. Diverse Systems

- **Homogeneous baseline ($q=1$):** All agents are identical
  - Example: 16 copies of GPT-4 with the same prompt
  - Entropy contribution: minimal (only configurational entropy from agent permutations)

- **Diverse systems ($q>1$):** Multiple agent types present
  - Example: 4 agents each of 4 different models ($q=4$)
  - Entropy contribution: substantial (states can be assigned to multiple categories)

### 1.4 Categorical Nature of States

The Potts model uses **categorical** states, meaning:
- There is no ordering relation between states
- State 1 is not "less than" state 2
- The distance between states is binary: either equal or not equal

This is captured by the Kronecker delta function:

$$\delta(s_i, s_j) = \begin{cases} 1 & \text{if } s_i = s_j \\ 0 & \text{if } s_i \neq s_j \end{cases}$$

This categorical nature is appropriate for LLM agent systems where different models or prompts represent genuinely distinct approaches rather than points on a continuous spectrum.

---

## 2. Interaction Topology and Coupling Strength

### 2.1 Interaction Pairs

For a system of $N$ agents, the interaction structure is defined by the set of pairs $\langle ij \rangle$.

**Mean-field approximation (fully-connected):**
$$\sum_{\langle ij \rangle} \rightarrow \frac{N}{2} \sum_{i \neq j}$$

This assumes every agent interacts with every other agent, which is valid for:
- Small teams with shared communication channels
- Systems with broadcast or all-to-all message passing
- Analytical tractability in the thermodynamic limit

### 2.2 Coupling Strength $J > 0$

The coupling constant $J$ represents the strength of interaction between agents:

$$J = (\text{alignment probability}) \times (\text{interaction bandwidth})$$

**Physical interpretation:**
- $J > 0$: Ferromagnetic coupling (alignment is energetically favored)
- Larger $J$: Stronger tendency for agents to reach consensus
- $J$ captures: communication quality, shared context, coordination protocols

**Dimensions:** $[J] = [E]$ (energy units, with $k_B = 1$ in natural units)

### 2.3 Kronecker Delta $\delta(s_i, s_j)$

The alignment operator measures whether two agents are in the same state:

$$\delta(s_i, s_j) = \begin{cases} 1 & \text{if agents } i, j \text{ have the same state (agree)} \\ 0 & \text{if agents have different states (disagree)} \end{cases}$$

**Properties:**
- Dimensionless: $[\delta] = [1]$
- Symmetric: $\delta(s_i, s_j) = \delta(s_j, s_i)$
- Idempotent: $\delta(s_i, s_j)^2 = \delta(s_i, s_j)$

### 2.4 Hamiltonian Sign Convention

The Potts Hamiltonian with ferromagnetic coupling:

$$H = -J \sum_{\langle ij \rangle} \delta(s_i, s_j)$$

**Key implications of the negative sign:**
- **Lower energy ($H < 0$):** More agent agreements $\rightarrow$ favored state
- **Higher energy ($H > 0$):** More agent disagreements $\rightarrow$ unfavored state
- **Energy minimization** corresponds to **consensus formation**

**Performance mapping hypothesis:**
$$\text{Task Performance } \mathcal{P} \propto e^{-\beta H} / Z$$

where low $H$ (high alignment) corresponds to high performance.

---

## 3. Effective Temperature $T_{\text{eff}}$

### 3.1 Boltzmann Factor

With $k_B = 1$ (natural units), the inverse temperature is:

$$\beta = \frac{1}{T_{\text{eff}}}$$

### 3.2 Operational Definition

The effective temperature captures the noise/stochasticity in the system:

$$T_{\text{eff}} = \frac{\text{disagreement rate}}{\text{coupling strength}}$$

**Physical interpretation:**
| $T_{\text{eff}}$ regime | System behavior | Agent system analogy |
|-----------------------|-----------------|---------------------|
| $T_{\text{eff}} \to 0$ | Fully ordered (ground state) | Perfect consensus, deterministic responses |
| $0 < T_{\text{eff}} < T_c$ | Ordered phase | Strong consensus with occasional fluctuations |
| $T_{\text{eff}} \approx T_c$ | Critical point | Phase transition, maximal fluctuations |
| $T_{\text{eff}} > T_c$ | Disordered phase | No consensus, random agent behavior |
| $T_{\text{eff}} \to \infty$ | Fully disordered | Complete randomness, no coordination |

### 3.3 Entropy-Based Alternative Definition

An equivalent definition based on information entropy:

$$T_{\text{eff}} = \frac{S}{k_B} = -\sum_{k=1}^{q} p_k \ln p_k$$

where $p_k$ is the probability of an agent being in state $k$.

This connects $T_{\text{eff}}$ directly to the diversity of agent responses in the system.

### 3.4 Sources of Stochasticity in LLM Systems

| Source | Effect on $T_{\text{eff}}$ |
|--------|--------------------------|
| LLM sampling temperature parameter | Direct: $T_{\text{eff}} \propto T_{\text{LLM}}$ |
| Task ambiguity/prompt variability | Increases uncertainty → higher $T_{\text{eff}}$ |
| Model stochasticity (different seeds) | Increases variance → higher $T_{\text{eff}}$ |
| Clear shared context | Reduces disagreement → lower $T_{\text{eff}}$ |

### 3.5 Dimensional Check

$$[T_{\text{eff}}] = [E] \quad \text{(same units as } J\text{)}$$

This ensures the Boltzmann factor $\beta J = J/T_{\text{eff}}$ is dimensionless.

---

## 4. Energy-Performance Mapping

### 4.1 Hypothesis

The probability of observing a particular agent configuration with energy $H$ follows the Boltzmann distribution:

$$P(\{s_i\}) = \frac{e^{-\beta H(\{s_i\})}}{Z}$$

where $Z$ is the partition function.

**Performance-energy relationship:**
$$\mathcal{P}(\{s_i\}) \propto P(\{s_i\}) = \frac{e^{-\beta H(\{s_i\})}}{Z}$$

**Implications:**
- Low $H$ configurations (high alignment) are more probable and perform better
- High $H$ configurations (disagreement) are less probable and perform worse
- The temperature $T_{\text{eff}}$ controls the trade-off between energy and entropy

### 4.2 Free Energy Interpretation

The Helmholtz free energy:

$$F = U - TS = -J \sum_{\langle ij \rangle} \langle \delta(s_i, s_j) \rangle - T_{\text{eff}} \ln \Omega$$

where:
- $U = \langle H \rangle$ is the average internal energy (alignment term)
- $S = \ln \Omega$ is the entropy (diversity term)
- $\Omega$ is the number of accessible microstates

**Optimal agent count $N^*$:**
$$N^* = \arg\min_N F(N, q, T_{\text{eff}})$$

The optimal system balances:
1. **Alignment energy:** Favors many agents of the same type (low $q$, high coordination)
2. **Diversity entropy:** Favors many different agent types (high $q$, many perspectives)

### 4.3 Connection to Yang et al. (2025) Results

The empirical finding from Yang et al.:
> "4 diverse agents ($D_4$) perform equivalently to 16-32 homogeneous agents"

**Statistical mechanics explanation:**

Diverse systems have higher entropy $S$, which can compensate for lower alignment energy:

$$F_{\text{diverse}} = U_{\text{diverse}} - T S_{\text{diverse}} \approx F_{\text{homogeneous}} = U_{\text{homogeneous}} - T S_{\text{homogeneous}}$$

For $q=4$ diverse agents vs $q=1$ homogeneous:
$$S_{\text{diverse}} \approx \ln(4) > S_{\text{homogeneous}} \approx 0$$

The entropy advantage allows fewer agents to achieve the same free energy (performance).

---

## 5. Complete Parameter Mapping Table

| Potts Parameter | Symbol | Agent System Property | Operational Definition | Measurement Method | Expected Scale |
|-----------------|--------|----------------------|----------------------|-------------------|----------------|
| **State space** | $s_i$ | Agent type/role | Categorical choice from $\{1, \ldots, q\}$ | Agent metadata assignment | Discrete, $s_i \in [1, q]$ |
| **Diversity** | $q$ | Number of distinct agent types | Effective number of clusters | $k$-means on response embeddings | $q=1$ (homogeneous) to $q=16$ (high diversity) |
| **Coupling** | $J$ | Alignment strength | $P(\text{agreement}) \times \text{bandwidth}$ | Pairwise agreement measurement | $J \sim 0.1 - 10$ (dimensionless, $k_B=1$) |
| **Temperature** | $T_{\text{eff}}$ | Stochasticity/noise | Disagreement rate $/ J$ | Variance across random seeds | $T_{\text{eff}} \sim 0.5 - 2.0$ |
| **System size** | $N$ | Number of agents | Direct count | Direct count | $N = 2 - 100$ |
| **Interaction pairs** | $\langle ij \rangle$ | Communication topology | Who communicates with whom | Network analysis of message logs | All pairs (mean-field) |
| **Hamiltonian** | $H$ | System energy | $-J \sum_{\langle ij \rangle} \delta(s_i, s_j)$ | Computed from configuration | $[H] = [E]$ |
| **Alignment operator** | $\delta(s_i, s_j)$ | Agreement indicator | $1$ if same state, $0$ otherwise | Computed from agent outputs | Dimensionless |
| **Free energy** | $F$ | Performance predictor | $U - TS$ | Derived from partition function | $[F] = [E]$ |

### 5.1 Calibration Notes

**Calibrating $q$:**
1. Run agents on diverse tasks
2. Collect outputs and compute embeddings
3. Apply clustering with silhouette score optimization
4. Set $q = \text{optimal cluster count}$

**Calibrating $J$:**
1. Design tasks with ground truth
2. Measure pairwise agreement rates $A_{ij}$
3. Subtract random baseline: $A_{ij}^{\text{corr}} = A_{ij} - A_{\text{random}}$
4. Fit to Potts model predictions to extract $J$

**Calibrating $T_{\text{eff}}$:**
1. Run consensus task with multiple random seeds
2. Compute state distribution $p_k$
3. Calculate entropy $S = -\sum p_k \ln p_k$
4. Set $T_{\text{eff}} = S$ (with $k_B = 1$)

### 5.2 Connection to Yang et al. Empirical Results

| Yang et al. Finding | Potts Model Interpretation |
|---------------------|----------------------------|
| $D_4$ (4 diverse) $\approx$ 16-32 homogeneous | Entropy bonus: $S(q=4) \approx \ln(4) \approx 1.39$ |
| Diversity multiplier $\sim 4-8\times$ | Free energy equivalence: $F_{\text{diverse}} \approx F_{\text{homogeneous}}$ |
| Fully-connected topology | Justifies mean-field approximation |
| Performance plateau at high $N$ | Finite-size effects and diminishing returns |

---

## 6. Summary

### 6.1 Hamiltonian Definition

The Potts model Hamiltonian for LLM-based multi-agent systems:

$$\boxed{H = -J \sum_{\langle ij \rangle} \delta(s_i, s_j)}$$

where:
- $s_i \in \{1, \ldots, q\}$: Agent state (discrete agent type)
- $J > 0$: Coupling strength (alignment favors low energy)
- $\delta(s_i, s_j)$: Kronecker delta (1 if agents agree, 0 otherwise)
- $\langle ij \rangle$: Interacting agent pairs (mean-field: all pairs)

### 6.2 Energy-Performance Hypothesis

$$\boxed{\mathcal{P}(\{s_i\}) \propto \frac{e^{-\beta H(\{s_i\})}}{Z}}$$

Lower energy (more alignment) corresponds to higher task performance.

### 6.3 Key Parameters

| Parameter | Meaning | LLM Interpretation |
|-----------|---------|-------------------|
| $q$ | State space dimension | Number of distinct agent types |
| $J$ | Coupling strength | Communication quality/coordination |
| $T_{\text{eff}}$ | Temperature | Noise/stochasticity in responses |
| $N$ | System size | Number of agents |

### 6.4 Next Steps

With the Hamiltonian defined, the next phase will:
1. Derive the partition function $Z(N, q, T)$
2. Compute the free energy $F = -\ln Z$
3. Find the optimal agent count $N^*(q, T)$

---

## References

- Wu, F. Y. (1982). The Potts Model. *Reviews of Modern Physics, 54*(2), 235-268.
- Baxter, R. J. (1982). *Exactly Solved Models in Statistical Mechanics*. Academic Press.
- Yang, L. et al. (2025). Diversity Matters in LLM Multi-Agent Systems. arXiv:2602.03794.
- Phase 1 Mapping Document: `.gpd/phases/01-literature-deep-dive/MAPPING-AGENT-TO-POTTS.md`

---

*End of Derivation 02-01*
