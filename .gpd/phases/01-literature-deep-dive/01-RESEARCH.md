# Phase 1: Literature Deep-Dive - Research

**Researched:** 2026-03-16
**Domain:** Statistical Mechanics of Multi-Agent Systems (Interdisciplinary: cond-mat.stat-mech, cs.MA, physics.soc-ph)
**Confidence:** MEDIUM (web search unavailable; relying on established physics knowledge and training data)

---

## Summary

This phase maps the intersection of statistical mechanics and multi-agent systems, focusing on Ising/Potts model applications to agent-based modeling and the emerging literature on LLM-based agent systems. The core claim to validate is whether a first-principles derivation of N* = f(H, q, T) can reproduce the empirical finding that "2 diverse agents ~ 16 homogeneous agents" (Yang et al., 2025).

**Primary recommendation:** Use the Potts model partition function as the mathematical foundation for diversity quantification in multi-agent systems, with mean-field theory providing the analytical tractability needed for closed-form N* derivation. The Ising model serves as the q=2 special case (binary diversity), while the q-state Potts model generalizes to arbitrary agent diversity.

**Key insight:** The "diversity bonus" in multi-agent systems maps directly to the entropy term S = -k_B \sum p_i \ln p_i in the free energy F = U - TS. Higher diversity (larger q) increases the entropy of agent configurations, lowering free energy and potentially creating a more stable "consensus phase" at lower effective temperature.

---

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| Yang et al. (2025) "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity" | Benchmark/Claim | Provides empirical target: 2 diverse agents ≈ 16 homogeneous agents | READ, extract empirical data, compare | Plan (validation target), Execution (quantitative test), Verification (final comparison) |
| Potts model partition function | Method | Foundation for diversity quantification | Derive, apply to agent systems | Plan (core method), Execution (derivation) |
| Ising model phase transition | Baseline | q=2 special case for validation | Use as sanity check | All phases |

**Missing or weak anchors:** The Yang et al. (2025) paper (arXiv:2602.03794) could not be retrieved due to web service rate limits. This is a **critical gap** that must be resolved before planning proceeds. The paper contains:
- Empirical measurements of task performance vs. N for homogeneous vs. diverse agents
- Specific definition of "diversity" used in their experiments
- Performance metrics and task descriptions
- Potential hints at the scaling law they observed

**Action required:** User must obtain Yang et al. (2025) manually from https://arxiv.org/abs/2602.03794 and place in project references.

---

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
|----------|------------------|--------|-------------------|
| Z = \sum_{\{s_i\}} \exp\left(-\beta H[\{s_i\}]\right) | Partition function definition | Statistical Mechanics (Pathria, Ch. 1) | Central object: encodes all thermodynamic properties |
| H = -J \sum_{\langle ij \rangle} \delta(s_i, s_j) | Potts model Hamiltonian | Wu, Rev. Mod. Phys. 1982 | Describes agent alignment/interaction |
| F = -k_B T \ln Z | Free energy from partition function | Pathria Ch. 2 | Minimization determines equilibrium states |
| T_c = \frac{J}{k_B \ln(1+\sqrt{q})} | Potts model critical temperature (2D) | Baxter, Exactly Solved Models | Predicts phase transition in agent consensus |
| M = \frac{1}{N} \sum_i \delta(s_i, s_0) | Order parameter (magnetization analogue) | Statistical field theory | Measures consensus/alignment among agents |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
|-----------|--------------|---------------|-------------------|
| Mean-field theory | Approximates interactions with average field | Deriving analytic expressions for F, phase boundaries | Landau & Lifshitz, Statistical Physics, Ch. 13 |
| Transfer matrix method | Exact solution for 1D systems | Validating approximations in low dimensions | Baxter, Exactly Solved Models in Statistical Mechanics |
| Renormalization group | Understanding scaling behavior near critical points | Analyzing how N* scales with system parameters | Goldenfeld, Lectures on Phase Transitions |
| Large deviation theory | Probability of rare events in many-agent systems | Quantifying tail risks in agent performance | Touchette, Rev. Mod. Phys. 2009 |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
|---------------|-----------------|-------------------|----------------|-------------------------|
| Mean-field theory | 1/z (coordination number) | High dimensions (d ≥ 4), well-connected networks | O(1/z) | Monte Carlo simulation, exact solution in d=2 |
| High-temperature expansion | βJ << 1 | T >> T_c (disordered phase) | O((βJ)^n) | Low-temperature expansion, transfer matrix |
| Large-N limit | 1/N | Many agents, central limit theorem applies | O(1/\sqrt{N}) | Finite-size scaling corrections |

---

## Standard Approaches

### Approach 1: Potts Model with Mean-Field Theory (RECOMMENDED)

**What:** Treat each agent as a Potts spin with q states (representing agent types/capabilities), interacting via pairwise alignment coupling J. The system's partition function Z(N, q, T, J) yields free energy F, which is minimized at equilibrium.

**Why standard:** The Potts model is the canonical generalization of the Ising model for systems with more than two states. Mean-field theory provides analytical tractability while capturing the essential physics of phase transitions. This approach has been successfully applied to opinion dynamics, cultural diversity models, and social systems for decades.

**Track record:**
- Social physics: Axelrod's cultural dissemination model (1997) builds on Potts-like interactions
- Opinion dynamics: Sznajd-Wiśniewski model (2000) uses Ising-like interactions
- Swarm intelligence: Couzin et al. (2002) use statistical mechanics for collective motion
- Limitation: Mean-field overestimates ordering tendency in low dimensions

**Key steps:**

1. **Define the Hamiltonian:** H = -J \sum_{\langle ij \rangle} \delta(s_i, s_j) where s_i ∈ {1, ..., q} is agent i's type
2. **Write the partition function:** Z = \sum_{\{s_i\}} e^{-\beta H}
3. **Apply mean-field approximation:** Replace δ(s_i, s_j) ≈ m^2/q where m is the order parameter
4. **Solve for the order parameter:** Self-consistency equation m = f(m, T, q, N)
5. **Compute free energy:** F = -k_B T \ln Z
6. **Find optimal N:** Minimize F with respect to N subject to fixed performance

**Known difficulties at each step:**

- **Step 2 (Z calculation):** Exact solution only in d=2 (Baxter) and d=1 (transfer matrix). For arbitrary network topology, requires approximation.
- **Step 3 (mean-field):** Can miss fluctuations and finite-size effects important for small N (N < 50)
- **Step 6 (N optimization):** N enters through boundary conditions and finite-size effects; nontrivial dependence

### Approach 2: Monte Carlo Simulation (FALLBACK/VALIDATION)

**What:** Numerically sample the Potts model configuration space using Metropolis-Hastings or Wolff algorithm to compute Z and F for specific parameters.

**When to switch:** When mean-field predictions disagree strongly with empirical data, or when studying finite-N effects where fluctuations dominate.

**Tradeoffs:**
- **Pro:** No approximations, captures all fluctuations and finite-size effects
- **Con:** Computationally expensive, no closed-form formula for N*

### Anti-Patterns to Avoid

- **Treating agent diversity as continuous:** The Potts model is inherently discrete (q states). Continuous approximations lose the combinatorial diversity effects that drive the 2≈16 scaling.
  - *Example:* Modeling diversity as a continuous parameter d ∈ [0,1] instead of discrete q misses the entropy explosion at large q.

- **Ignoring network topology:** Agent systems in LLM frameworks (AutoGen, CrewAI) have specific interaction patterns (fully connected, hierarchical, small-world). Assuming a lattice can give qualitatively wrong phase diagrams.
  - *Fix:* Study the specific topology of the target agent system; mean-field is more accurate for well-connected networks.

- **Conflating temperature with task complexity:** While tempting to map T_eff directly to task difficulty, the relationship is more subtle. T_eff encapsulates noise, stochasticity in agent responses, and the inverse of "confidence."
  - *Fix:* Calibrate T_empirically against known benchmarks.

---

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
|--------|------------|--------|------------|
| 1D Potts model partition function | Z = [e^{βJ} + (q-1)]^N | Baxter, Exactly Solved Models (1982), Eq. (3.2.1) | Validation: test N-dependence in tractable limit |
| 2D Potts critical temperature | k_B T_c / J = 1 / ln(1 + √q) | Baxter (1982), Eq. (8.7.30) | Benchmark: check if phase transition occurs in agent systems |
| Mean-field critical temperature | k_B T_c^{MF} / J = q / (q-1) | Wu, Rev. Mod. Phys. 1982, Eq. (2.12) | First approximation for agent consensus threshold |
| Potts free energy (mean-field) | F = -k_B T N ln q - (N/2) J m^2 + k_B T N S(m) | Goldenfeld, Lectures on Phase Transitions | Starting point for N* derivation |

**Key insight:** The partition function approach is well-established. Re-deriving these textbook results would waste valuable context budget. Instead, focus on the NOVEL mapping from agent systems to the Potts model, particularly:
- How agent diversity q relates to Potts states
- How agent communication maps to the coupling J
- How task complexity determines T_eff
- The finite-N dependence specific to small multi-agent systems (N < 100)

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
|--------|-------------------|--------|------------|
| Binder cumulant | Finite-size scaling of phase transitions | Binder, Phys. Rev. Lett. 1981 | Determining if N=16 is "large" enough for thermodynamics |
| Correlation length ξ | ξ ∝ |T - T_c|^{-ν} | Critical phenomena | Establishes scale of correlated agent behavior |
| Entropy of mixing | ΔS = k_B ln(q^N/N!) | Statistical mechanics | Quantifies diversity contribution to free energy |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
|--------------|---------|------|-----------|-----------------|
| "Social impact theory of opinion formation" | Latané | 1981 | Foundational social physics | Mapping from social influence to Hamiltonian |
| "Opinion dynamics model with zealots" | Galam | 1997 | Agent-based opinion formation | Treatment of external influence, stubborn agents |
| "Cultural dissemination in a lattice" | Axelrod | 1997 | Multi-state agent model | q-state model for cultural traits |
| "Statistical mechanics of social dynamics" | Castellano, Fortunato, Loreto | 2009 | Review article | Comprehensive overview of Ising/Potts in social systems |
| "Physics of swarm intelligence" | Martinoli et al. | 2010s | Swarm statistical mechanics | Partition function for collective behavior |
| "Phase transitions in collective decision making" | Couzin et al. | 2005 | Biological consensus models | Critical slowing down near T_c |
| **Yang et al.** | **Yang et al.** | **2025** | **Benchmark for this project** | **Empirical N* scaling, diversity metric, task setup** |

---

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
|------|----------------|---------|--------------|
| **NumPy/SciPy** | 1.24+ | Numerical computation, optimization | Universal for scientific computing in Python |
| **SymPy** | 1.12+ | Symbolic algebra for partition function derivation | Handles q as symbolic variable, supports combinatorial expressions |
| **NetworkX** | 3.1+ | Agent interaction topology | Supports arbitrary network structures beyond lattices |
| **Metropolis algorithm** | Custom implementation | Sampling Potts configurations | Standard Monte Carlo approach for statistical systems |
| **Wolff algorithm** | Custom implementation | Cluster flipping for efficient sampling near T_c | Reduces critical slowing down, essential for large q |

### Supporting Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| matplotlib | Visualization of phase diagrams, order parameter plots | Diagnostic plots, validation |
| pandas | Data organization for empirical comparisons | Structuring Yang et al. benchmark data |
| seaborn | Statistical visualization | Exploratory analysis of simulation results |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Metropolis | Wolff algorithm | Wolff faster near T_c, more complex to implement |
| Mean-field analytic | Monte Carlo numerical | Analytic gives formula, numeric gives exact result for parameters |
| Python + NumPy | Julia | Julia faster for heavy numerics, Python more accessible |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
|-------------|----------------|------------|------------|
| Exact Z for N < 20 (brute force) | < 1 second | q^N states explode | Only for validation |
| Mean-field derivation | < 1 second (analytic) | Solving self-consistency equations | Numerical root-finding |
| Monte Carlo for N=100, q=10 | ~minutes | Equilibration near T_c | Use Wolff algorithm, parallel tempering |
| Finite-size scaling (multiple N) | ~hours | Many parameter combinations | Adaptive sampling, GPU acceleration |

**Installation / Setup:**
```bash
# Core scientific stack
pip install numpy scipy sympy networkx matplotlib pandas seaborn

# For GPU-accelerated Monte Carlo (optional, for large simulations)
pip install cupy-cuda12x  # if CUDA available
pip install jax  # for JIT-compiled simulations
```

---

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
|-------|-------------------|----------------|-----------------|
| q=2 reduces to Ising | Potts model special case | Set q=2 in all expressions, compare to Ising results | Exact agreement with known Ising formulas |
| N→∞ recovers thermodynamics | Finite-size effects vanish | Show F/N approaches bulk limit as N→∞ | Convergence to known bulk free energy |
| T=0 gives perfect alignment | Zero-temperature limit | All agents should be in same state at T=0 | Maximum order parameter m=1 |
| T→∞ gives random states | High-temperature limit | Uniform distribution over q^N states | Zero magnetization, maximum entropy |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
|-------|------------------|--------------|--------|
| Non-interacting limit (J=0) | J → 0 | Z = q^N, F = -k_B T N ln q | Trivial partition function |
| Strong coupling limit (J→∞) | J → ∞ | All agents align, Z = q e^{βJN(N-1)/2} | Ground state dominance |
| 1D solution | d=1, arbitrary N | Z = [e^{βJ} + (q-1)]^N, no phase transition | Exact solution, no long-range order |
| Mean-field T_c | d ≥ 4 | k_B T_c = qJ/(q-1) | Critical temperature for consensus formation |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
|------|--------|-----------|-----------------|
| Monte Carlo vs. analytic Z | Direct enumeration for N<20 | < 1% relative error | Exact enumeration |
| Finite-size scaling | Collapse of Binder cumulant | Visual collapse within error bars | Universal scaling functions |
| Yang et al. empirical | Compare predicted N* to 2 vs 16 finding | Qualitative agreement + quantitative test | N*(q=2) / N*(q=16) ≈ 8 (needs empirical calibration) |

### Red Flags During Computation

- **Partition function decreasing with N:** Z should be monotonically increasing with N (more states). If Z decreases, there's a sign error or calculation error.
- **Negative entropy:** S = -∂F/∂T must be non-negative. Negative S indicates a mathematical error.
- **Discontinuous order parameter away from T_c:** In 1D, there is no phase transition; m should vary continuously. A discontinuous jump suggests numerical issues.
- **Free energy increasing with q at fixed N:** More diversity should increase entropy, lowering F. If F increases with q, the entropy contribution is missing or mis-signed.
- **Critical temperature decreasing with q:** T_c(q) should increase with q (more states → harder to reach consensus). If T_c decreases, the formula is inverted.

---

## Common Pitfalls

### Pitfall 1: Misidentifying the Order Parameter

**What goes wrong:** Using magnetization M = (1/N)∑ s_i (valid for Ising) for the Potts model, where s_i are discrete states {1, ..., q} not signed values ±1.

**Why it happens:** The Ising model (q=2) has a natural signed order parameter. The Potts model generalization requires a different approach, typically using the largest eigenvalue of the state correlation matrix or the fraction of agents in the dominant state.

**How to avoid:** Define the order parameter for Potts model as:
```
m = (q N_max - N) / (q - 1) N
```
where N_max is the number of agents in the most common state. This ranges from 0 (uniform distribution) to 1 (all agents same state).

**Warning signs:** Order parameter not normalized to [0,1], or not reducing correctly for q=2.

**Recovery:** Re-derive the order parameter from the definition of the Potts Hamiltonian.

### Pitfall 2: Ignoring Finite-Size Effects for Small N

**What goes wrong:** Applying thermodynamic limit results (N→∞) to systems with N=2-100 agents, which is the relevant regime for multi-agent systems.

**Why it happens:** Most statistical mechanics results are derived in the thermodynamic limit. The finite-size corrections are often neglected but become crucial for small N.

**How to avoid:** Include finite-size scaling corrections explicitly:
```
F(N) = F_bulk + F_surface(N) + F_curvature(N) + ...
```
where F_surface ~ N^{(d-1)/d} and F_curvature ~ N^{(d-2)/d} for d-dimensional systems.

**Warning signs:** Predictions changing qualitatively between N=10 and N=100 without smooth interpolation.

**Recovery:** Use finite-size scaling analysis; include the Binder cumulant to assess whether N is "thermodynamic."

### Pitfall 3: Conflating Different Temperature Definitions

**What goes wrong:** Mixing up statistical temperature T (in energy units, β = 1/k_B T) with "effective temperature" as a metaphor for noise or randomness in agent behavior.

**Why it happens:** In social physics and agent-based modeling, "temperature" is often used as an analogy for stochasticity, without clear calibration to physical temperature.

**How to avoid:** Be explicit about the definition:
```
T_eff = (noise magnitude) / (coupling strength)
```
or calibrate T_eff against known benchmarks (e.g., T_eff where consensus probability = 0.5).

**Warning signs:** T_eff appearing without units or calibration procedure.

**Recovery:** Establish a clear operational definition of T_eff and relate it to measurable quantities in the agent system.

### Pitfall 4: Incorrect Entropy of Mixing

**What goes wrong:** Using the entropy expression S = k_B ln(q^N) for N indistinguishable agents, which overcounts by a factor of N!.

**Why it happens:** Forgetting the correction for indistinguishable particles (agents of the same type are interchangeable).

**How to avoid:** Use the correct entropy:
```
S = k_B [N ln q - ln N!]
    ≈ k_B N [ln q - ln N + 1]  (Stirling approximation)
```

**Warning signs:** Entropy scaling as N ln q instead of N(ln q - ln N).

**Recovery:** Include the Gibbs/N! correction factor in the partition function.

### Pitfall 5: Network Topology Mismatch

**What goes wrong:** Assuming a lattice or fully-connected network when the actual agent system has a different topology (e.g., small-world, hierarchical, or sparse connections).

**Why it happens:** Most analytical results are derived for regular lattices or mean-field (fully connected). Real multi-agent systems often have specific communication patterns.

**How to avoid:** Characterize the actual interaction topology of the target system (AutoGen, CrewAI, etc.) and use appropriate approximations:
- Fully connected → mean-field valid
- Small-world → enhanced critical temperature
- Sparse networks → percolation effects

**Warning signs:** Phase behavior qualitatively different from expected mean-field predictions.

**Recovery:** Study the specific network topology and use appropriate corrections (e.g., effective coordination number z_eff).

---

## Level of Rigor

**Required for this phase:** Physicist's proof (controlled approximation with error estimates)

**Justification:** This is an interdisciplinary domain connecting statistical mechanics (rigorous) to multi-agent systems (empirical). A full mathematical proof would be excessive, but hand-waving would miss critical finite-size effects that dominate the small-N regime. The appropriate standard is:

- Derive expressions with clear approximations
- Quantify error terms (e.g., O(1/z) for mean-field)
- Validate against known limits and benchmarks
- Compare to empirical data from Yang et al.

**What this means concretely:**

- All approximations must be explicitly stated with small parameters and error estimates
- Finite-size corrections must be included for N < 100
- Validation against special cases (q=2, J=0, T=0, T→∞) is mandatory
- Comparison to numerical simulations for intermediate parameters
- No uncontrolled "ansatz" without justification

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Phenomenological social force models | Statistical mechanics-based agent models | ~2000s (Axelrod, Sznajd-Wiśniewski) | Grounded in first principles, predictive power |
| Ising model only (q=2) | Potts model (q-state) | 1980s-1990s (Baxter, Wu) | Captures diversity beyond binary choices |
| Mean-field theory only | Renormalization group + finite-size scaling | 1970s-1980s (Wilson) | Understanding of scaling and critical exponents |
| Lattice models only | Complex network topologies | ~2000s (Watts-Strogatz, Barabási-Albert) | Realistic interaction patterns |

**Superseded approaches to avoid:**

- **Social force models without thermodynamic consistency:** Early social dynamics models (Helbing 1990s) used force-based approaches that sometimes violated energy conservation. Modern approaches ensure thermodynamic consistency.
- **Binary opinion models for multi-valued choices:** Using multiple coupled Ising variables instead of a single Potts variable adds complexity without benefit. Use Potts directly.
- **Homogeneous mixing assumption:** Assuming all agents interact equally ignores network structure. Modern approaches account for topology.

---

## Open Questions

1. **What is the precise mapping from "LLM agent diversity" to Potts q states?**
   - What we know: Yang et al. show diversity matters, but the precise definition (model types, prompt variations, fine-tuning differences) is unclear without reading the paper.
   - What's unclear: Is diversity discrete (countable types) or continuous (embedding space distance)? If continuous, how to discretize to q states?
   - Impact on this phase: The value of q (effective states) determines the entropy contribution to free energy.
   - Recommendation: User must obtain Yang et al. (2025) and extract their operational definition of diversity. For now, proceed with q as a free parameter to be calibrated.

2. **What is the effective temperature T_eff of LLM agent systems?**
   - What we know: T_eff relates to stochasticity/noise in agent responses. Higher temperature = more randomness.
   - What's unclear: How to measure T_empirically from LLM outputs? Does it vary with task complexity, model size, or sampling parameters?
   - Impact: T_eff determines whether the system is in the ordered (consensus) or disordered (diverse) phase.
   - Recommendation: Calibrate T_eff against simple consensus tasks where probability of agreement can be measured.

3. **What is the network topology of LLM multi-agent systems?**
   - What we know: AutoGen, CrewAI, and LangChain have different communication patterns. Some are fully connected (all agents see all messages), others have hierarchical structures.
   - What's unclear: Does the topology matter for N* scaling, or does mean-field capture the essential physics?
   - Impact: Topology affects the critical temperature and finite-size corrections.
   - Recommendation: Assume mean-field (fully connected) as first approximation. Validate against specific framework topologies in later phases.

4. **Is the 2≈16 result task-dependent or universal?**
   - What we know: Yang et al. report this empirical finding for their specific tasks.
   - What's unclear: Does the scaling factor vary with task complexity, domain, or evaluation metric?
   - Impact: Universal scaling would support a first-principles derivation; task-dependent scaling would require additional parameters in N*.
   - Recommendation: Extract task details from Yang et al. when available. Test for universality across multiple tasks.

---

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
|---------------|------------|-----------|-------------------|
| Mean-field Potts | Poor agreement with Yang et al. data | Monte Carlo simulation with numerical optimization | High: lose closed-form N*, gain empirical accuracy |
| Discrete q-states | Diversity is fundamentally continuous | Continuous symmetry model (O(n) model) | Medium: different analytical techniques |
| Equilibrium thermodynamics | Agent systems are inherently nonequilibrium | Master equation / Fokker-Planck approach | Very high: lose partition function framework |
| Homogeneous coupling J | Agent interactions are heterogeneous | Random bond Potts model | High: analytical intractability |

**Decision criteria:** Abandon mean-field Potts if:
- Predicted N* differs from Yang et al. by more than a factor of 2 after calibration
- Phase diagram qualitatively disagrees (e.g., no diversity bonus predicted)
- Finite-size effects dominate in a way mean-field cannot capture

---

## Sources

### Primary (HIGH confidence)

- **Baxter, R. J.** "Exactly Solved Models in Statistical Mechanics" (1982) - Potts model exact solutions, partition functions
- **Wu, F. Y.** "The Potts model" Rev. Mod. Phys. 54, 235 (1982) - Comprehensive review of Potts model theory
- **Pathria, R. K. & Beale, P. D.** "Statistical Mechanics" (3rd ed., 2011) - Standard textbook for partition functions, mean-field theory
- **Goldenfeld, N.** "Lectures on Phase Transitions and the Renormalization Group" (1992) - Renormalization group methods
- **Castellano, C., Fortunato, S., & Loreto, V.** "Statistical physics of social dynamics" Rev. Mod. Phys. 81, 591 (2009) - Review of statistical mechanics in social systems

### Secondary (MEDIUM confidence)

- **Axelrod, R.** "The dissemination of culture: A model with local convergence and global polarization" J. Conflict Resolut. 41, 203 (1997) - Multi-state agent model for cultural dynamics
- **Sznajd-Wiśniewski, K. & Sznajd, J.** "Opinion evolution in closed community" Int. J. Mod. Phys. C 11, 1157 (2000) - Ising model for opinion dynamics
- **Couzin, I. D. et al.** "Uninformed individuals promote democratic consensus in animal groups" Science 334, 1578 (2011) - Consensus in biological systems
- **Galam, S.** "Social opinion dynamics" in "Encyclopedia of Complexity and Systems Science" (2009) - Review of opinion dynamics models

### Tertiary (LOW confidence - requires validation)

- **Yang et al. (2025)** "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity" arXiv:2602.03794 - **CRITICAL: Not retrieved due to rate limit; must be obtained manually**
- LLM framework documentation (AutoGen, CrewAI, LangChain) - Architectural details for network topology
- Recent preprints on statistical mechanics of AI systems (2024-2025) - **Search failed; literature may exist that was not found**

---

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - Potts model and partition functions are well-established statistical mechanics
- Standard approaches: HIGH - Mean-field theory and Monte Carlo are standard tools
- Computational tools: HIGH - Numerical methods for Potts model are mature and well-documented
- Validation strategies: MEDIUM - Yang et al. paper not retrieved; empirical benchmarks are unavailable
- LLM agent system specifics: LOW - Without web search, details about AutoGen/CrewAI architectures are based on general knowledge

**Research limitations:**
- Web search services were rate-limited during this research phase
- Yang et al. (2025) could not be retrieved; this is a critical gap
- Recent literature (2024-2025) on LLM agent scaling may exist that was not found
- Network topology details for specific agent frameworks are based on general knowledge

**Research date:** 2026-03-16
**Valid until:** 2026-06-16 (3 months; verify recent preprints and retrieve Yang et al. paper)

**Action items for next phase:**
1. User must obtain Yang et al. (2025) from https://arxiv.org/abs/2602.03794
2. Repeat literature search after rate limit resets for recent 2024-2025 papers
3. Characterize network topology of target agent frameworks (AutoGen, CrewAI)
4. Calibrate T_eff and q from empirical data if available

---

## Caveats and Alternatives

**Self-critique (adversarial review):**

1. **What assumption might be wrong?**
   - Assumption: Agent diversity maps to discrete Potts states. Reality: LLM diversity might be continuous (embedding space) or hierarchical (fine-grained capabilities). If so, the Potts model may need modification.

2. **What alternative was dismissed too quickly?**
   - Omitted: Active matter models and Vicsek-style models for collective motion. These are relevant for spatial agent systems but less directly applicable to LLM agents (which interact via messages, not spatial coordination). Worth revisiting if spatial organization of agents proves important.

3. **What limitation is being understated?**
   - Mean-field theory is known to fail for low-dimensional systems (d < 4). If agent systems have effectively low dimensionality (e.g., hierarchical communication trees), mean-field predictions could be qualitatively wrong. This is a significant risk for the 2≈16 validation.

4. **Is there a simpler method being overlooked?**
   - Information-theoretic approach: Directly maximize mutual information between agent diversity and task performance, bypassing the statistical mechanics formalism. This would be simpler but loses the connection to phase transitions and critical phenomena that motivate the physics approach.

5. **Would a specialist disagree?**
   - A statistical mechanics specialist might question whether equilibrium thermodynamics applies to inherently nonequilibrium agent systems. A multi-agent systems specialist might question whether the Potts model captures the richness of LLM agent interactions. Both concerns are valid and should be addressed through validation against empirical data.

**Mitigation:** These caveats reinforce the need for:
- Careful empirical calibration against Yang et al. (when obtained)
- Numerical validation using Monte Carlo for specific parameters
- Explicit testing of mean-field assumptions
- Consideration of nonequilibrium extensions if equilibrium approach fails

---

## Appendix: Search Strategy Documentation

**Note:** Web search services were rate-limited during this research phase. The following searches were attempted and failed:

1. "Ising model opinion dynamics social systems multi-agent review 2020..2025" - Rate limit 429
2. "Potts model diversity agent systems collective behavior" - Rate limit 429
3. "Yang et al. 2025 Understanding Agent Scaling in LLM-Based Multi-Agent Systems arXiv:2602.03794" - Rate limit 429

**Planned searches (to retry after rate limit reset):**

1. "Ising model opinion dynamics review" physics.soc-ph
2. "Potts model cultural diversity Axelrod"
3. "partition function multi-agent systems"
4. "phase transitions collective intelligence swarm"
5. "AutoGen statistical mechanics"
6. "CrewAI agent scaling"
7. "LLM multi-agent diversity benchmark"
8. "Yang et al. 2025 agent scaling diversity"
9. "finite-size scaling small N agents"
10. "mean-field theory validation agent systems"

**Alternative retrieval methods:**
- Direct arXiv access: https://arxiv.org/abs/2602.03794
- Google Scholar searches
- Semantic Scholar API
- Request from user to provide critical references

---

*End of RESEARCH.md*
