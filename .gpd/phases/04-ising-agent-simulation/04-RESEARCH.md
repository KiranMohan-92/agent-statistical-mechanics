# Phase 4: Ising-Agent Simulation - Research

**Researched:** 2026-03-23
**Domain:** Computational Statistical Mechanics / Monte Carlo Methods / Critical Phenomena
**Confidence:** HIGH (established methods with novel agent-system application)

---

## Summary

This phase researches computational methods for implementing Monte Carlo simulations of the Ising-Potts agent model on 2D lattices. The core challenge is to implement efficient, validated Monte Carlo code that (1) reproduces known exact results for the 2D Ising model, (2) measures correlation functions and identifies phase transitions, and (3) performs finite-size scaling analysis to extract critical parameters. The simulation must handle small-N systems (N = 2-100 agents) where finite-size effects are large, and must be efficient enough to explore the parameter space of temperature T and diversity q.

**Primary recommendation:** Use the Wolff cluster algorithm for q=2 (Ising) and Swendsen-Wang for general q, supplemented with Metropolis for validation. Implement equilibration diagnostics (autocorrelation time, Binder cumulant crossing) and bootstrap error analysis. For finite-size scaling, use the Binder cumulant crossing method to locate T_c(N) and data collapse to extract critical exponents.

**Key insight:** Multi-agent systems operate in the small-N regime (N < 100) where standard Monte Carlo equilibration criteria fail. The correlation length ξ saturates at ξ_max ~ N^(1/d), so the transition is rounded. The Binder cumulant U4 = 1 - <m^4>/(3<m^2>^2) provides a robust finite-size estimator of T_c through its crossing point.

---

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| Baxter (1982) - Exactly Solved Models | Validation | Exact 2D Ising/Potts T_c and exponents | COMPARE simulation T_c to exact values | Execution (benchmark), Verification (final test) |
| Onsager (1944) - 2D Ising solution | Benchmark | Exact T_c = 2J/ln(1+√2) ≈ 2.269J for validation | VERIFY code reproduces T_c within statistical error | Plan (test case), Execution (first validation) |
| Phase 3 RESEARCH.md | Prior Artifact | Finite-size scaling forms, critical exponents | USE scaling relations m(N,t) = N^(-β/dν)f_m(tN^(1/dν)) | Plan (analysis methodology), Execution (data collapse) |
| Yang et al. 2025 (arXiv:2602.03794) | Benchmark | "2 diverse ≈ 16 homogeneous" empirical target | REPRODUCE this scaling relationship | Verification (final validation) |
| Newman & Barkema (1999) - Monte Carlo Methods | Method | Standard algorithms, equilibration criteria | IMPLEMENT Metropolis, Wolff, Swendsen-Wang | Plan (algorithm selection), Execution (code) |

**Missing or weak anchors:**
- **Yang et al. (2025) full paper:** Rate-limited during research; could not retrieve detailed methodology. This is needed to understand exactly how "2 diverse ≈ 16 homogeneous" was measured.
- **Agent-system specific MC studies:** No prior literature found on Monte Carlo for LLM multi-agent systems. This is novel territory requiring careful validation.

---

## Conventions

| Choice           | Convention         | Alternatives   | Source             |
| ---------------- | ------------------ | -------------- | ------------------ |
| Units            | Natural (k_B = 1)  | SI, Gaussian   | CONVENTIONS.md     |
| Potts Hamiltonian | H = -J Σ δ(s_i, s_j) | H = +J Σ δ    | CONVENTIONS.md     |
| Order parameter  | m = (qN_max - N)/[(q-1)N] | Magnetization | CONVENTIONS.md     |
| Lattice geometry | Square 2D with periodic BC | Open, other lattices | This phase (standard) |
| Neighbor definition | von Neumann (4 neighbors) | Moore (8), other | Standard 2D Ising |
| RNG seed         | Fixed for reproducibility | Time-based | Reproducibility requirement |

**CRITICAL: All equations and results below use these conventions. Converting from other conventions requires:**
- T_c values scale with J (if source uses J=1, multiply by actual J)
- Order parameter normalization affects β exponent interpretation
- Different neighbor counts (z) change mean-field T_c = Jz/(q-1)

---

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
|----------|------------------|--------|-------------------|
| H = -J Σ_<ij> δ(s_i, s_j) | Potts Hamiltonian | CONVENTIONS.md | Energy function for MC |
| T_c^2D = J/ln(1+√q) | Exact 2D critical temperature | Baxter (1982) | Validation target for q=2,3,4 |
| T_c^MF = Jq/(q-1) | Mean-field critical temperature | Wu (1982) | Comparison, high-d limit |
| P(s) ∝ exp(-βE[s]) | Boltzmann distribution | Standard stat mech | MC acceptance probability |
| ΔE = E_new - E_old | Energy change | MC formalism | Metropolis acceptance |
| A = min(1, exp(-βΔE)) | Metropolis acceptance | Metropolis (1953) | Local update rule |
| G(r) = <s_i s_j> - <s_i><s_j> | Spin-spin correlation | Standard | Correlation function measurement |
| U4 = 1 - <m^4>/(3<m^2>^2) | Binder cumulant | Binder (1981) | Finite-size T_c estimation |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
|-----------|--------------|---------------|-------------------|
| **Metropolis-Hastings** | Local spin-flip updates with detailed balance | All T regimes, simple validation | Metropolis et al. (1953) |
| **Wolff algorithm** | Cluster flips via random growth, reduces critical slowing | Near T_c, q=2 (Ising) | Wolff (1989) |
| **Swendsen-Wang** | Bond formation and cluster flips | General q, all T | Swendsen-Wang (1987) |
| **Bootstrap resampling** | Statistical error estimation for correlated data | All observables | Efron (1979), Newman & Barkema |
| **Binder cumulant crossing** | T_c estimation for finite systems | Finite-size scaling | Binder (1981) |
| **Autocorrelation analysis** | Equilibration checking, error estimation | All MC runs | Newman & Barkema Ch. 3 |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
|---------------|-----------------|-------------------|----------------|-------------------------|
| **Finite-size scaling** | N^(-1/dν) | N ≫ 1, N < ∞ | O(N^(-ω/dν)) | Exact enumeration for N < 10 |
| **Critical slowing correction** | τ_int ~ ξ^z | Near T_c | Use cluster algorithms | Wang-Landau, parallel tempering |
| **Thermodynamic limit** | N → ∞ | N ≫ ξ^d | O(N^(-1/dν)) | Explicit finite-size forms |
| **Linear response** | h → 0 | Small external field | O(h²) | Full field-dependent simulation |

---

## Standard Approaches

### Approach 1: Wolff Cluster Algorithm for Ising (RECOMMENDED for q=2)

**What:** Build a cluster of aligned spins via random growth, then flip the entire cluster. The algorithm starts from a random seed site and adds neighboring sites with probability p_add = 1 - exp(-2βJ) if they have the same spin value. The cluster is then flipped.

**Why standard:** Wolff algorithm dramatically reduces critical slowing down. The dynamic critical exponent is z ≈ 0.25-0.35 for Wolff compared to z ≈ 2 for Metropolis near T_c. This means equilibration time scales as τ ~ L^z, so Wolff is ~L^(1.65) times faster near T_c.

**Track record:**
- Standard method for 2D Ising simulations since 1989
- Validated against exact Onsager solution in countless studies
- Easily extended to 3D and other lattices
- Provides excellent statistics near T_c where Metropolis struggles

**Key steps:**

1. **Initialize:** Choose random initial configuration (hot start for high T, cold start for low T)
2. **Pick seed:** Select random lattice site (i, j)
3. **Grow cluster:** For each site in cluster, check neighbors. If neighbor has same spin, add to cluster with probability p_add = 1 - exp(-2βJ)
4. **Flip cluster:** Invert all spins in cluster (↑ → ↓, ↓ → ↑)
5. **Measure:** After each cluster flip, measure observables (energy, magnetization, etc.)
6. **Repeat:** Perform N_cluster flips for equilibration, then N_measure flips for production

**Known difficulties at each step:**

- **Step 1 (initialization):** Hot start (random spins) is slower to equilibrate below T_c. Cold start (all aligned) is slower above T_c. Use appropriate initial condition for target T.
- **Step 3 (cluster growth):** Stack overflow risk for large clusters in recursive implementation. Use iterative (queue-based) implementation instead.
- **Step 5 (measurement):** Measurements after each cluster flip are correlated. Use binning or bootstrap to account for autocorrelation.
- **Equilibration detection:** Near T_c, autocorrelation times diverge. Use multiple diagnostics: energy stability, magnetization stability, and autocorrelation function.

### Approach 2: Swendsen-Wang for General q (RECOMMENDED for q > 2)

**What:** Place bonds between neighboring aligned spins with probability p_bond = 1 - exp(-βJ). Identify connected clusters via these bonds. Flip each cluster to a randomly chosen new Potts state.

**Why standard for q > 2:** Wolff algorithm was designed for Ising (q=2). For q-state Potts with q > 2, the Swendsen-Wang algorithm is the natural generalization and is widely used.

**Key steps:**

1. **Place bonds:** For each neighboring pair with s_i = s_j, place bond with probability p_bond = 1 - exp(-βJ)
2. **Identify clusters:** Use Hoshen-Kopelman or Union-Find to identify connected components
3. **Flip clusters:** For each cluster, choose new spin value uniformly from {1, ..., q} and assign to all sites
4. **Measure:** After each sweep, measure observables

**Known difficulties:**

- **Cluster identification:** Union-Find data structure required for efficiency. Path compression is essential for O(N) performance.
- **Measurement frequency:** One Swendsen-Wang sweep updates the entire lattice. Measure after each sweep.
- **q → 1 limit:** Potts model becomes percolation. Specialized algorithms may be more efficient.

### Approach 3: Metropolis Algorithm (VALIDATION and Small-N)

**What:** Select random spin site, propose flip to new value, accept with probability A = min(1, exp(-βΔE)). Repeat N times for one "sweep."

**When to use:**
- Validation against Wolff/Swendsen-Wang results
- Very small systems (N < 20) where cluster overhead is unnecessary
- Teaching/demonstration purposes (algorithmic simplicity)

**Tradeoffs:**
- Pro: Simple implementation, works for any q and any lattice
- Con: Critical slowing down (z ≈ 2) makes it inefficient near T_c
- Pro: Local updates easier to understand for debugging
- Con: Autocorrelation times diverge at T_c

**Known difficulties:**
- **Near T_c:** Autocorrelation time τ ~ L^z with z ≈ 2. For L=100, τ ~ 10,000 sweeps.
- **Acceptance rate:** Near T_c, acceptance rate ~50%. Far from T_c, most proposals are rejected (low T) or accepted trivially (high T).

### Approach 4: Finite-Size Scaling Analysis (REQUIRED for Agent Systems)

**What:** Use finite-size scaling theory to extract critical exponents from simulations of finite systems. The key idea is that near T_c, all thermodynamic quantities obey scaling forms when expressed in terms of the scaling variable x = tN^(1/dν).

**Why essential:** Multi-agent systems have N = 2-100 agents, far from the thermodynamic limit. Standard infinite-N results don't apply. Finite-size scaling provides the framework for analyzing small-N data.

**Scaling forms:**

```
m(N, t) = N^(-β/dν) f_m(t N^(1/dν))
χ(N, t) = N^(γ/dν) f_χ(t N^(1/dν))
U4(N, t) = f_U(t N^(1/dν))  # Binder cumulant is dimensionless
```

where t = (T - T_c)/T_c is the reduced temperature.

**Key technique: Binder cumulant crossing**

The Binder cumulant U4 = 1 - <m^4>/(3<m^2>^2) has a special property: at T = T_c, U4 is independent of system size (for sufficiently large N). Therefore, plotting U4 vs T for different N values, the curves cross at T_c.

**Steps for finite-size scaling:**

1. **Simulate multiple sizes:** Run simulations for N = 4, 8, 16, 32, 64, 128 (or as feasible)
2. **Measure Binder cumulant:** Compute U4(T) for each N
3. **Find crossing:** Locate T* where U4(N1, T*) = U4(N2, T*) for neighboring sizes
4. **Estimate T_c:** Extrapolate crossing points to N → ∞
5. **Data collapse:** Plot m N^(β/dν) vs t N^(1/dν) with trial exponents, adjust for best collapse

### Anti-Patterns to Avoid

- **Measuring every sweep:** Measurements are highly correlated. This underestimates statistical errors. Always use binning or bootstrap to account for autocorrelation.
  - _Example:_ Reporting σ = σ_0/√N when measurements are correlated gives false precision.

- **Insufficient equilibration:** Assuming the system is equilibrated after a fixed number of sweeps. Equilibration time depends on T and system size.
  - _Example:_ Using 1000 sweeps for both L=10 and L=100. The latter needs ~10× more sweeps near T_c.

- **Ignoring finite-size effects at small N:** Applying thermodynamic limit formulas to N < 20 agents.
  - _Example:_ Predicting a sharp phase transition at T_c for N=4. The system has only 2^4=16 microstates.

- **Using only Metropolis near T_c:** Critical slowing down makes Metropolis extremely inefficient near the phase transition.
  - _Example:_ Spending hours equilibrating with Metropolis when Wolff would converge in minutes.

- **Single RNG seed for all runs:** Different runs should use different seeds for proper error estimation.

---

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
|--------|------------|--------|------------|
| **2D Ising T_c** | k_B T_c / J = 2/ln(1+√2) ≈ 2.269 | Onsager (1944) | Validation target for simulation |
| **2D Potts T_c** | k_B T_c / J = 1/ln(1+√q) | Baxter (1982) | Validation for q=2,3,4 |
| **2D Ising exponents** | β = 1/8, ν = 1, γ = 7/4, η = 1/4 | Onsager, Baxter | Finite-size scaling benchmark |
| **Internal energy per site** | U/N = -J coth(2βJ)[1 + (2/π) κ' K(κ)] | Onsager | Energy validation |
| **Spontaneous magnetization** | m = [1 - sinh^(-4)(2βJ)]^(1/8) | Onsager (Yang) | Order parameter validation |
| **Correlation length** | ξ = [2 sinh(2J/k_B T)]^(-1) | Exact 2D | Correlation function validation |

**Key insight:** Re-deriving these exact results wastes computation time. The simulation should reproduce these values within statistical error (typically 1-3 σ). Disagreement indicates a bug in the code.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
|--------|-------------------|--------|------------|
| **Mean-field T_c** | k_B T_c / J = q/(q-1) | Bragg-Williams | High-d or fully-connected limit |
| **Ginzburg criterion** | Gi ∼ (T_c - T)^((4-d)/2) | Goldenfeld (1992) | Mean-field validity check |
| **Finite-size shift** | T_c(N) = T_c(∞)[1 + a N^(-1/dν)] | Finite-size scaling | Small-N correction |
| **Dynamic exponent z** | z ≈ 2 (Metropolis), z ≈ 0.25 (Wolff) | Literature | Equilibration time estimate |
| **Autocorrelation time** | τ_int = 1/2 + Σ ρ(t) | Standard | Error estimation |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
|--------------|---------|------|-----------|-----------------|
| "Monte Carlo Methods in Statistical Physics" | Newman, Barkema | 1999 | Standard MC textbook | Algorithms, equilibration, error analysis |
| "Critical Slowing Down" | Wolff | 1989 | Cluster algorithm | Wolff implementation details |
| "Monte Carlo Study of the Potts Model" | Swendsen, Wang | 1987 | Potts cluster algorithm | Bond formation, cluster flip |
| "Finite Size Scaling" | Binder | 1981 | Binder cumulant method | U4 crossing for T_c |
| "Spin-spin correlation functions" | McCoy, Wu | 1973 | Exact correlations | G(r) validation |

---

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
|------|----------------|---------|--------------|
| **NumPy** | 1.24+ | Lattice arrays, vectorized operations | Efficient array manipulation |
| **NumBA** | Latest | JIT compilation for critical loops | 10-100× speedup for MC updates |
| **SciPy** | 1.10+ | Sparse matrices (cluster ID), optimization | Union-Find, curve fitting |
| **matplotlib** | 3.7+ | Visualization (phase diagram, scaling collapse) | Publication-quality plots |
| **pandas** | 2.0+ | Data organization for multiple runs | Efficient data analysis |

### Supporting Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **seaborn** | Statistical visualization | Plotting confidence intervals, error bars |
| **tqdm** | Progress bars | Long MC runs, user feedback |
| **joblib** | Parallel execution | Running multiple (T, q) parameter points |

### Existing Code to Reuse

From Phase 3 code analysis:

```python
# These modules can be imported for Phase 4:
from code.exponent_calculator import CriticalExponents, ExponentCalculator
from code.rg_integration import critical_exponents
```

**Reuse strategy:**
- `ExponentCalculator.get_exponents(d, method='best')` → Use for finite-size scaling forms
- `CriticalExponents` dataclass → Standardize exponent handling
- `critical_exponents()` → Compare theoretical vs. numerical exponents

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
|-------------|----------------|------------|------------|
| **Single MC run (L=32, 10^5 sweeps)** | ~1-10 seconds (NumBA) | Near T_c (slow equilibration) | Use Wolff algorithm |
| **Temperature scan (50 T values, L=32)** | ~1-5 minutes | Multiple independent runs | Parallelize over T |
| **Finite-size scaling (6 sizes, 50 T)** | ~10-60 minutes | Total sweeps required | Use cluster algorithms |
| **Critical exponent extraction** | ~1 minute (curve fitting) | Quality of collapse | Use bootstrapping for errors |

**Installation / Setup:**
```bash
# Core scientific stack
pip install numpy scipy matplotlib pandas seaborn tqdm joblib

# For acceleration (highly recommended for MC)
pip install numba

# For reproducibility
pip install watermark
```

---

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
|-------|-------------------|----------------|-----------------|
| **Energy conservation** | MC algorithm correctness | Check H after each sweep | Should fluctuate around equilibrium value |
| **Detailed balance** | Reversibility of MC dynamics | Verify P(A→B)/P(B→A) = exp(-βΔE) | Holds for all transitions |
| **Periodic boundary symmetry** | Boundary condition implementation | Check G(r) across boundary | Correlation wraps correctly |
| **Symmetry under global flip** | Ising symmetry (q=2) | m → -m statistics | Symmetric distribution at T > T_c |
| **Sum rule** | Normalization | Σ_i P(s_i) = 1 | Holds to machine precision |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
|-------|------------------|--------------|--------|
| **T → 0** | Zero temperature | Perfect order (m = 1, E = -NJz/2) | Ground state |
| **T → ∞** | High temperature | Complete disorder (m = 0, E = 0) | Paramagnetic phase |
| **q=2, L→∞** | 2D Ising thermodynamic | T_c = 2.269J, β = 1/8 | Onsager (1944) |
| **q=3, L→∞** | 2D 3-state Potts | T_c = 1.986J, β = 1/9 | Baxter (1982) |
| **d ≥ 4** | Mean-field dimension | β = 1/2, ν = 1/2 | Landau theory |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
|------|--------|-----------|-----------------|
| **T_c for q=2** | Binder cumulant crossing | < 1% relative | T_c = 2.269185J |
| **β for q=2** | Log-log fit of m vs t | < 5% relative | β = 0.125 |
| **ν for q=2** | Correlation length scaling | < 5% relative | ν = 1.0 |
| **Internal energy** | Direct comparison to Onsager | < 1% relative | Exact U(T) formula |
| **Specific heat peak** | C = d<U>/dT location | Consistent with T_c | Should peak at T_c |

### Red Flags During Computation

- **T_c deviating > 5% from exact value:** Indicates bug in Hamiltonian, boundary conditions, or measurement. Check energy calculation.
- **Negative specific heat:** C = d<U>/dT should be positive. Negative values indicate numerical differentiation error or insufficient sampling.
- **Order parameter m > 1:** The normalized order parameter should satisfy 0 ≤ m ≤ 1. Values >1 indicate normalization error.
- **Energy drift:** Energy should fluctuate around equilibrium, not drift. Drift indicates insufficient equilibration.
- **Autocorrelation not decaying:** If ρ(t) doesn't decay to 0 within available lag, measurements are highly correlated. Increase run length.
- **Different results on different runs (beyond statistical error):** Indicates RNG seed issue or non-deterministic code (e.g., using sets/dicts with undefined iteration order).

---

## Common Pitfalls

### Pitfall 1: Insufficient Equilibration

**What goes wrong:** Measuring observables before the system reaches equilibrium, leading to biased estimates.

**Why it happens:** Equilibration time τ_eq depends on temperature and system size. Near T_c, τ_eq ~ L^z diverges. Using fixed equilibration sweeps fails for large systems or near criticality.

**How to avoid:**
- Use multiple diagnostics: energy stability, magnetization stability, and autocorrelation function
- Monitor running averages: when they stabilize, system is likely equilibrated
- Use hot start (random) for T > T_c and cold start (aligned) for T < T_c
- For safety, use τ_eq = 10 × τ_int (integrated autocorrelation time)

**Warning signs:** Drift in energy or magnetization, different results from hot vs cold start, high variance between independent runs.

**Recovery:** Increase equilibration time by factor of 2-10. Use cluster algorithms near T_c to reduce τ_eq.

### Pitfall 2: Ignoring Autocorrelation in Error Analysis

**What goes wrong:** Reporting statistical errors as σ = σ_0/√N where N is number of measurements, ignoring that measurements are correlated.

**Why it happens:** Standard error formula assumes independent samples. MC measurements are correlated over autocorrelation time τ_int.

**How to avoid:**
```
σ_corrected = σ_0 × √(2τ_int/N)
```
where τ_int is the integrated autocorrelation time:
```
τ_int = 1/2 + Σ_{t=1}^{M} ρ(t)
```
and ρ(t) is the autocorrelation function.

Alternatively, use binning: divide data into bins of size > τ_int, compute bin averages, use standard error on bins.

**Warning signs:** Error bars that decrease as 1/√N even when taking more data from same run, inconsistencies between independent runs.

**Recovery:** Compute autocorrelation function, use corrected error formula or binning.

### Pitfall 3: Metropolis Near T_c (Critical Slowing Down)

**What goes wrong:** Using Metropolis algorithm near the phase transition, resulting in extremely slow equilibration and highly correlated samples.

**Why it happens:** Near T_c, the correlation length ξ diverges. For local update algorithms like Metropolis, the dynamic critical exponent is z ≈ 2, so τ ~ ξ^z ~ L^z. For L=100, τ ~ 10,000 sweeps!

**How to avoid:**
- Use Wolff algorithm (q=2) or Swendsen-Wang (q>2) for T near T_c
- Use Metropolis only for T far from T_c or for validation
- For teaching/demonstration, use small systems (L < 20) where critical slowing is manageable

**Warning signs:** Autocorrelation time increasing with system size, energy fluctuating wildly, poor mixing of spin configurations.

**Recovery:** Switch to cluster algorithm. The speedup can be factors of 100-1000× near T_c.

### Pitfall 4: Boundary Condition Bugs

**What goes wrong:** Incorrect implementation of periodic boundary conditions, leading to edge effects and broken translation invariance.

**Why it happens:** Periodic boundaries require modular arithmetic: (i+1) % L. Off-by-one errors are common. For correlation functions, must account for minimum image convention.

**How to avoid:**
```python
# Correct neighbor access with periodic BC
def neighbors(i, j, L):
    return [((i+1)%L, j), ((i-1)%L, j), (i, (j+1)%L), (i, (j-1)%L)]

# Minimum image convention for distance
def distance(r1, r2, L):
    dr = abs(r1 - r2)
    return min(dr, L - dr)
```

**Warning signs:** Edge sites showing different statistics, correlation functions not symmetric, magnetization gradients.

**Recovery:** Verify boundary implementation with small test cases. Check that all sites have exactly z neighbors.

### Pitfall 5: Incorrect Cluster Algorithm Implementation

**What goes wrong:** Wolff or Swendsen-Wang algorithm giving incorrect critical temperature or critical exponents.

**Why it happens:** Cluster algorithms are more complex than Metropolis. Common bugs:
- Incorrect bond probability: should be p = 1 - exp(-2βJ) for Ising
- Forgetting to flip the seed site in Wolff
- Inefficient cluster growth (recursion stack overflow)
- Not recomputing bond probability when T changes

**How to avoid:**
- Test against Metropolis for small systems (should give same results)
- Validate that cluster algorithm reproduces exact T_c
- Use iterative (queue-based) cluster growth, not recursion
- Recompute p_add whenever β changes

**Warning signs:** Different results from Metropolis, T_c shifted from exact value, memory errors for large L.

**Recovery:** Debug with small systems (L < 10) where exact enumeration is possible. Verify detailed balance.

---

## Level of Rigor

**Required for this phase:** Physicist's proof (controlled approximation with quantitative error estimates)

**Justification:** This phase produces numerical results that will be used for quantitative predictions about multi-agent systems. While full mathematical rigor is impossible for numerical simulations, we must provide rigorous error estimates and validation against exact results.

**What this means concretely:**

- All observables must include statistical error bars (typically 1σ confidence intervals)
- Error bars must account for autocorrelation (use integrated autocorrelation time or bootstrap)
- Critical exponents must be extracted with confidence intervals (use bootstrapping)
- Validation against exact results (Onsager T_c, Baxter exponents) is mandatory
- Finite-size scaling collapse must be demonstrated visually
- At least two independent algorithms (e.g., Metropolis and Wolff) should agree

**Quality criteria:**

- T_c measured within 1% of exact value for q=2
- Critical exponents within 5% of exact values for d=2
- Statistical errors < 1% for primary observables
- Data collapse with χ²/ndof < 2 for finite-size scaling

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| **Metropolis only** | Cluster algorithms (Wolff, SW) | 1980s (Wolff 1989) | Dramatic speedup near T_c |
| **Simple error analysis** | Bootstrap, autocorrelation-corrected | 1990s (Newman & Barkema) | Reliable error estimates |
| **Thermodynamic limit only** | Finite-size scaling standard | 1980s (Cardy, Binder) | Essential for small systems |
| **Single-size analysis** | Multi-size scaling collapse | 1980s | Robust exponent extraction |

**Superseded approaches to avoid:**

- **Pure Metropolis near T_c:** Obsolete for production work. Use cluster algorithms.
- **Uncorrelated error estimates:** Reporting σ = σ_0/√N without autocorrelation correction is now considered incorrect practice.
- **Single system size:** Modern analysis requires multiple sizes for finite-size scaling.

---

## Open Questions

1. **What is the optimal lattice geometry for agent systems?**
   - What we know: Square lattice is standard for 2D Ising studies
   - What's unclear: Do agent interactions map to 2D square lattice, or is the effective topology different?
   - Impact: Determines choice of lattice and neighbor count
   - Recommendation: Start with square 2D lattice; explore other topologies in follow-up work

2. **How small can N be before finite-size scaling breaks down?**
   - What we know: Finite-size scaling assumes N ≫ 1
   - What's unclear: Is N=2 too small for any scaling analysis?
   - Impact: Agent systems may have very few agents
   - Recommendation: Use exact enumeration for N < 10, finite-size scaling for N > 10

3. **What is the optimal number of Monte Carlo sweeps for equilibration?**
   - What we know: τ_eq depends on T, L, and algorithm
   - What's unclear: Generic formula for τ_eq across parameter space
   - Impact: Under-equilibrated data gives biased results
   - Recommendation: Use adaptive equilibration (monitor energy stability)

4. **How to handle q > 4 (first-order transition)?**
   - What we know: Potts model has first-order transition for q > 4 in d=2
   - What's unclear: Standard MC algorithms for first-order transitions (two-phase coexistence)
   - Impact: Standard cluster algorithms may not efficiently sample first-order transitions
   - Recommendation: For q > 4, consider multicanonical or Wang-Landau sampling

---

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
|---------------|------------|-----------|-------------------|
| **Wolff algorithm** | Implementation bugs or poor performance | Metropolis with careful equilibration | Low: simpler code, but much slower near T_c |
| **Finite-size scaling** | Data collapse fails for small N | Exact enumeration for N < 20 | Medium: different algorithm, limited to small N |
| **Standard MC** | Critical slowing down unbearable | Wang-Landau or multicanonical | High: more complex algorithm |
| **2D lattice** | Agent topology is not 2D-like | Fully-connected (mean-field) simulation | Low: simpler, no spatial structure |
| **Bootstrap error analysis** | Too computationally expensive | Binning method | Low: simpler, but less rigorous |

**Decision criteria:** Abandon Wolff algorithm if:
- T_c differs from exact value by > 5% after extensive debugging
- Cluster growth fails (e.g., infinite loops, memory errors)
- Performance is worse than Metropolis (unexpected, but possible for very small systems)

---

## Sources

### Primary (HIGH confidence)

- **Newman, M. E. J., Barkema, G. T.** "Monte Carlo Methods in Statistical Physics" (1999) - Comprehensive MC textbook, algorithms, equilibration, error analysis
- **Wolff, U.** "Collective Monte Carlo Updating for Spin Systems" Phys. Rev. Lett. 62, 361 (1989) - Wolff cluster algorithm
- **Swendsen, R. H., Wang, J.-S.** "Nonuniversal Critical Dynamics in Monte Carlo Simulations" Phys. Rev. Lett. 58, 86 (1987) - Swendsen-Wang algorithm
- **Binder, K.** "Finite Size Scaling Analysis of Ising Model Block Distribution Functions" Phys. Rev. Lett. 47, 693 (1981) - Binder cumulant method
- **Baxter, R. J.** "Exactly Solved Models in Statistical Mechanics" (1982) - Exact 2D Potts results for validation
- **Onsager, L.** "Crystal Statistics I" Phys. Rev. 65, 117 (1944) - Exact 2D Ising solution

### Secondary (MEDIUM confidence)

- **Landau, D. P., Binder, K.** "A Guide to Monte Carlo Simulations in Statistical Physics" (2000) - Practical MC guide
- **Cardy, J.** "Scaling and Renormalization in Statistical Physics" (1996) - Finite-size scaling theory
- **Efron, B.** "Bootstrap Methods: Another Look at the Jackknife" Ann. Statist. 7, 1 (1979) - Bootstrap method
- **Hoshen, J., Kopelman, R.** "Percolation and Cluster Distribution" Phys. Rev. B 14, 3438 (1976) - Cluster labeling algorithm

### Tertiary (LOW confidence - requires validation)

- **Yang et al. (2025)** "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity" arXiv:2602.03794 - **CRITICAL: Not retrieved due to rate limit; must be obtained manually**
- Recent GPU-accelerated MC implementations (2010s-2020s) - **Search failed; literature may exist**
- Agent-system specific MC studies - **Novel territory; no prior work found**

---

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - Monte Carlo methods are well-established
- Standard approaches: HIGH - Wolff, Swendsen-Wang, Metropolis are standard algorithms
- Critical exponents for 2D Potts: HIGH - Exact results from Baxter, Onsager
- Finite-size scaling: HIGH - Cardy, Binder provide rigorous framework
- Computational tools: HIGH - NumPy, NumBA, SciPy are well-documented
- Agent-system application: MEDIUM - Mapping from agents to Potts is novel, requires validation
- Yang et al. validation: LOW - Paper not retrieved; empirical comparison pending

**Research limitations:**

- Web search services were rate-limited during this research phase
- Yang et al. (2025) could not be retrieved; this is a critical gap for validation
- Recent literature (2020s) on GPU-accelerated MC may exist that was not found
- Agent-system specific MC applications are novel; no prior work to build upon

**Research date:** 2026-03-23
**Valid until:** 2026-06-23 (3 months; verify recent preprints and retrieve Yang et al. paper)

**Action items for next phase:**

1. User must obtain Yang et al. (2025) from https://arxiv.org/abs/2602.03794
2. Repeat literature search after rate limit resets for recent MC methods
3. Begin implementation of Wolff and Swendsen-Wang algorithms in planning phase
4. Design validation test suite (exact T_c, exponent extraction)

---

## Caveats and Alternatives

**Self-critique (adversarial review):**

1. **What assumption might be wrong?**
   - Assumption: Agent systems can be modeled with equilibrium MC on a 2D lattice. Reality: LLM agent systems may have different interaction topologies (fully-connected, hierarchical, or time-dependent). If so, the 2D lattice results may not apply directly.

2. **What alternative was dismissed too quickly?**
   - Omitted: Wang-Landau sampling and multicanonical methods. These are important for first-order transitions (q > 4) and for computing density of states. Worth considering if standard MC fails for high diversity.

3. **What limitation is being understated?**
   - The computational cost of finite-size scaling. To properly extract exponents, we need simulations at multiple sizes (6-8 values of N) and multiple temperatures (50-100 points). This could take hours to days of computation. The research should acknowledge this cost.

4. **Is there a simpler method being overlooked?**
   - Exact enumeration for small N (N < 20). For very small agent systems, we can enumerate all q^N microstates and compute observables exactly. This avoids MC entirely and provides exact results for validation.

5. **Would a specialist disagree?**
   - An MC specialist might question the choice of Wolff vs Swendsen-Wang. Some studies find Swendsen-Wang more efficient for certain parameter regimes. There's also the question of whether to use newer algorithms like geometric cluster or worm algorithms.

**Mitigation:** These caveats reinforce the need for:
- Careful validation against exact results
- Benchmarking multiple algorithms before choosing primary
- Considering exact enumeration for very small N
- Clear documentation of computational costs
- Flexibility to switch algorithms if needed

---

## Dimensional Analysis

### Natural Scales for Monte Carlo

**Dimensionless parameters that govern the simulation:**

1. **Reduced temperature:** t = (T - T_c)/T_c
   - Controls distance from critical point
   - t = 0: critical point
   - t < 0: ordered phase
   - t > 0: disordered phase

2. **System size:** L = N^(1/d)
   - In lattice units (lattice spacing = 1)
   - For N agents on 2D square lattice: L = √N
   - Finite-size scaling parameter: L/ξ

3. **Coupling strength:** βJ = J/(k_B T)
   - In natural units (k_B = 1): βJ = J/T
   - Determines correlation strength

4. **Diversity:** q (discrete)
   - Number of Potts states
   - Affects universality class in d=2

**Scaling combinations for data collapse:**
```
x = t L^(1/ν)           # Scaling variable
y = m L^(β/ν)           # Scaled order parameter
χ L^(-γ/ν)              # Scaled susceptibility
ξ L^(-1)                # Scaled correlation length
```

---

## Phase 4-Specific Implementation Notes

### Code Structure Recommendation

```python
# Suggested module structure for Phase 4:

ising_agent/
├── __init__.py
├── lattice.py           # Lattice initialization, boundary conditions
├── algorithms.py        # Metropolis, Wolff, Swendsen-Wang
├── observables.py       # Energy, magnetization, correlation functions
├── analysis.py          # Binder cumulant, finite-size scaling
├── validation.py        # Comparison to exact results
└── runner.py            # Main simulation orchestration
```

### Key Observable Measurements

| Observable | Formula | Physical Meaning |
|------------|---------|------------------|
| **Energy per site** | e = H/(N) | Average interaction energy |
| **Specific heat** | C = β²(<e²> - <e>²) | Energy fluctuations |
| **Magnetization** | m = (qN_max - N)/[(q-1)N] | Order parameter |
| **Susceptibility** | χ = βN(<m²> - <m>²) | Magnetization fluctuations |
| **Binder cumulant** | U4 = 1 - <m⁴>/(3<m²>²) | Finite-size T_c estimator |
| **Correlation function** | G(r) = <s_0 s_r> | Spatial correlations |
| **Correlation length** | ξ² = Σ_r r² G(r) / Σ_r G(r) | Correlation scale |

### Simulation Parameters for Agent Systems

| Parameter | Range for Agent Systems | Rationale |
|-----------|------------------------|-----------|
| **N (system size)** | 4, 8, 16, 32, 64, 128 | Covers small-N regime |
| **q (diversity)** | 2, 4, 8, 16 | Test Yang saturation prediction |
| **T (temperature)** | 0.5J to 4.0J in steps of 0.05J | Covers ordered, critical, disordered |
| **Equilibration sweeps** | 10³ to 10⁵ depending on L, T | Adaptive based on autocorrelation |
| **Measurement sweeps** | 10⁴ to 10⁶ depending on required precision | Balance speed vs accuracy |

---

*End of Phase 4 Research*
