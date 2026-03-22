# Phase 3: Phase Transition Analysis - Research

**Researched:** 2026-03-21
**Domain:** Critical Phenomena / Renormalization Group / Statistical Mechanics
**Confidence:** MEDIUM (established physics with novel agent-system application)

---

## Summary

This phase researches the mathematical methods for analyzing phase transitions in multi-agent systems using the q-state Potts model. The core challenge is to go beyond mean-field theory (completed in Phase 2) and characterize the critical behavior: correlation length scaling, critical exponents (ν, β, γ), finite-size effects for small N (2-100 agents), and the complete phase diagram structure.

**Primary recommendation:** Use momentum-space renormalization group (RG) at the Gaussian fixed point for mean-field critical exponents, supplemented by finite-size scaling analysis to capture small-N effects. For the 2D Potts model, exact critical exponents are known from conformal field theory and should be used for validation. The Ginzburg criterion determines when mean-field theory breaks down and fluctuation corrections become essential.

**Key insight:** Multi-agent systems operate in the small-N regime (N < 100) where finite-size corrections are large. Standard thermodynamic limit results must be supplemented with explicit finite-size scaling forms. The correlation length ξ provides the natural scale: when N ≲ ξ^d, the system exhibits finite-size rounding of the phase transition.

---

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| Baxter (1982) - Exactly Solved Models | Method/Validation | Exact 2D Potts critical exponents for comparison | CITE exact β, ν, γ values | Plan (RG validation), Execution (comparison) |
| Wu (1982) - The Potts Model | Method | Mean-field RG approach, q-dependence of critical exponents | CITE mean-field results | Plan (starting point), Execution (benchmark) |
| Goldenfeld (1992) - Lectures on Phase Transitions | Method | RG formalism, epsilon expansion, Ginzburg criterion | USE for RG flow equations | Plan (RG derivation), Execution (exponent calculation) |
| Phase 2 Results (02-04-SUMMARY.md) | Prior Artifact | T_c^MF = Jq/(q-1), T_c^2D = J/ln(1+√q) | BUILD upon these results | Plan (starting point), Execution (RG around T_c) |
| Yang et al. (2025) - arXiv:2602.03794 | Benchmark | "2 diverse ≈ 16 homogeneous" empirical target | COMPARE phase predictions | Plan (validation target), Verification (final test) |

**Missing or weak anchors:**
- **Yang et al. (2025) full paper:** Could not be retrieved due to web search rate limits. Critical for empirical validation of phase diagram predictions.
- **Agent-system finite-size scaling studies:** No prior work found on finite-size scaling specifically for LLM multi-agent systems. This is novel territory requiring careful validation.

---

## User Constraints

No CONTEXT.md exists for this phase. All decisions are at the agent's discretion based on:
- Project conventions locked in CONVENTIONS.md
- Phase 2 mean-field results that must be built upon
- Requirements DERV-03, DERV-04, CALC-01, CALC-02, CALC-03 from REQUIREMENTS.md

**Locked conventions from prior phases:**
- k_B = 1 (natural units)
- Potts Hamiltonian: H = -J Σ_{⟨ij⟩} δ(s_i, s_j), J > 0 (ferromagnetic)
- Order parameter: m = (qN_max - N) / [(q-1)N]
- Fourier: exp(-ikx) forward, exp(ikx) inverse

---

## Conventions

| Choice           | Convention         | Alternatives   | Source             |
| ---------------- | ------------------ | -------------- | ------------------ |
| Metric signature | Euclidean (stat mech) | Minkowski     | CONVENTIONS.md     |
| Units            | Natural (k_B = 1)  | SI, Gaussian   | CONVENTIONS.md     |
| Temperature      | β = 1/T            | β = 1/(k_B T)  | CONVENTIONS.md     |
| Potts coupling   | H = -J Σ δ(s_i, s_j) | H = +J Σ δ    | CONVENTIONS.md     |
| Order parameter  | m = (qN_max - N)/[(q-1)N] | Magnetization | Phase 2 established |
| Fourier transform | exp(-ikx) forward | exp(ikx)       | CONVENTIONS.md     |

**CRITICAL: All equations and results below use these conventions. Converting from sources with different conventions requires:**
- Sign changes in Hamiltonian if using H = +J Σ δ convention
- Factors of k_B in temperature-dependent quantities
- Normalization of order parameter affects β exponent definition

---

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
|----------|------------------|--------|-------------------|
| T_c^MF = Jq/(q-1) | Mean-field critical temperature | Wu (1982), Phase 2 derived | Starting point for RG expansion around T_c |
| T_c^2D = J/ln(1+√q) | Exact 2D critical temperature | Baxter (1982) | Validation target for 2D systems |
| ξ ∼ |T - T_c|^{-ν} | Correlation length scaling | Critical phenomena (standard) | Defines scale for finite-size effects |
| m ∼ (T_c - T)^β | Order parameter scaling | Critical phenomena (standard) | Characterizes ordered phase |
| χ ∼ |T - T_c|^{-γ} | Susceptibility scaling | Critical phenomena (standard) | Measures fluctuations |
| G(r) ∼ r^{-(d-2+η)} | Correlation function at T_c | Critical phenomena (standard) | Defines anomalous dimension η |
| R_g = (u_c - u)/u_c | Ginzburg criterion | Goldenfeld (1992) | Determines mean-field validity |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
|-----------|--------------|---------------|-------------------|
| **Linear stability analysis** | Determines when mean-field solution becomes unstable | Near T_c, identifying instability onset | Goldenfeld Ch. 5, Pathria Ch. 12 |
| **Momentum-space RG** | Integrates out short-wavelength fluctuations, derives flow equations | Critical exponent calculation | Goldenfeld Ch. 9-10, Wilson-Kogut (1974) |
| **Real-space RG (Migdal-Kadanoff)** | Coarse-grains lattice by bond-moving | Cross-check for discrete systems | Goldenfeld Ch. 8 |
| **Finite-size scaling** | Extrapolates finite-N behavior to thermodynamic limit | Small agent systems (N < 100) | Cardy (1996), Binder (1981) |
| **Epsilon expansion** | Calculates critical exponents in d = 4 - ε dimensions | Systematic improvement over mean-field | Wilson-Fisher fixed point |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
|---------------|-----------------|-------------------|----------------|-------------------------|
| **Mean-field theory** | 1/z (inverse coordination) | d ≥ 4 or fully-connected | O(1/z) | Monte Carlo, exact 2D results |
| **Gaussian fluctuations** | u = (T - T_c)/T_c | Very close to T_c | O(u^{1/2}) | Full φ^4 theory |
| **Epsilon expansion** | ε = 4 - d | Near upper critical dimension | O(ε²) | Exact 2D results (Baxter) |
| **Finite-size scaling** | L^{-1/ν} (L = system size) | N ≫ 1 but N < ∞ | O(N^{-ω/ν}) | Exact enumeration for N < 20 |

---

## Standard Approaches

### Approach 1: Momentum-Space RG for Potts Model (RECOMMENDED)

**What:** Apply Wilson's momentum-shell renormalization group to the q-state Potts model, treating it as a φ^4 field theory in the limit of large q (or using the vector Potts representation). The RG flow equations yield critical exponents and determine the stability of the mean-field solution.

**Why standard:** This is the textbook approach for calculating critical exponents beyond mean-field. The epsilon expansion (d = 4 - ε) provides systematic corrections to mean-field values and has been extensively validated against exact results.

**Track record:**
- Successfully predicts Ising (q=2) exponents: β = 1/8, ν = 1, γ = 7/4 in d=2 (exact)
- Mean-field exponents valid for d ≥ 4: β = 1/2, ν = 1/2, γ = 1
- Epsilon expansion: β = 1/2 - ε/6 + O(ε²), ν = 1/2 + ε/12 + O(ε²)
- Potts model exhibits q-dependent critical exponents in d=2 (conformal field theory)

**Key steps:**

1. **Write Landau-Ginzburg-Wilson free energy functional:**
   ```
   F[φ] = ∫ d^d x [½(∇φ)² + ½rφ² + uφ⁴]
   ```
   where φ is the vector order parameter for q-state Potts (or scalar for q=2 Ising)

2. **Identify Gaussian fixed point:** r* = 0, u* = 0 (mean-field)

3. **Calculate RG flow equations using momentum-shell integration:**
   ```
   dr/dl = 2r + 4uK_d Λ^d/(1+r) - ...
   du/dl = (4-d)u - 36u²K_d Λ^d/(1+r)² + ...
   ```
   where l = ln(b) is the RG scale, K_d is phase space factor

4. **Find Wilson-Fisher fixed point:** r* ∝ ε, u* ∝ ε (non-trivial)

5. **Linearize around fixed point, extract eigenvalues:** y_t = 1/ν (thermal), y_h = (d+2-η)/2 (magnetic)

6. **Calculate critical exponents from eigenvalues:**
   ```
   ν = 1/y_t,  β = (d-2+η)y_h/2y_t,  γ = (2η - d)y_h/y_t
   ```

**Known difficulties at each step:**

- **Step 1 (field representation):** The q-state Potts model has a discrete symmetry, not continuous O(n). The correct field theory is more complex (vector Potts or q → 1 limit of clock model). For q=2 (Ising), the standard φ^4 theory applies.
- **Step 3 (loop integrals):** Momentum-shell integration requires careful handling of divergences. Dimensional regularization is cleaner but obscures the physical picture.
- **Step 4 (fixed point structure):** The Potts model has a first-order transition for q > 4 in d=2. The RG flow must capture this change. The fixed point becomes unstable for large q.
- **Step 6 (exponent extraction):** For d=2, exact results from conformal field theory are more accurate than epsilon expansion. Use Baxter's results for validation.

### Approach 2: Exact 2D Results from Conformal Field Theory (VALIDATION)

**What:** Use known exact critical exponents for the 2D Potts model from Baxter's solution and conformal field theory. These provide benchmark values to test RG calculations and Monte Carlo simulations.

**When to use:** For validation of numerical results, for comparison with mean-field predictions, and for understanding the q-dependence of critical behavior.

**Exact 2D critical exponents (Baxter, 1982):**

| q | β | ν | γ | η | Transition order |
|---|-----|-----|-----|-----|------------------|
| 2 (Ising) | 1/8 | 1 | 7/4 | 1/4 | Second-order |
| 3 | 1/9 | 5/6 | 13/9 | 4/15 | Second-order |
| 4 | 1/12 | 2/3 | 7/6 | 1/4 | Second-order (marginal) |
| > 4 | - | - | - | - | First-order |

**Conformal field theory formula (Nienhuis, 1982):**
```
β = (g-2)/(12g),  ν = √(3)/(2√(g)),  γ = (7g-12)/(6g)
where g = 4/√q for q ≤ 4
```

**Key insight:** The change from second-order to first-order at q=4 is crucial for agent systems. For q > 4 (high diversity), the transition is discontinuous—there's a jump in the order parameter rather than continuous growth. This predicts an abrupt consensus formation at T_c rather than gradual alignment.

### Approach 3: Finite-Size Scaling for Small N (REQUIRED for Agent Systems)

**What:** Apply finite-size scaling theory to systems with N = 2-100 agents. Standard thermodynamic limit results fail when N is comparable to ξ^d.

**Why essential:** Multi-agent systems operate in the small-N regime where finite-size corrections are large. The correlation length ξ diverges at T_c, but the system size limits ξ to ∼N^{1/d}. This rounds the phase transition and shifts apparent T_c.

**Finite-size scaling forms (Cardy, 1996):**

```
m(N, t) = N^{-β/dν} f_m(t N^{1/dν})
χ(N, t) = N^{γ/dν} f_χ(t N^{1/dν})
ξ(N, t) = N^{1/d} f_ξ(t N^{1/dν})
```

where t = (T - T_c)/T_c is the reduced temperature and f_i are universal scaling functions.

**Key predictions:**

1. **Rounded transition:** No true singularity at finite N; the specific heat peak has finite height
2. **Shifted critical temperature:** T_c(N) = T_c(∞)[1 + a N^{-1/dν} + ...]
3. **Correlation length saturation:** ξ_max ∼ N^{1/d} at T_c

**For agent systems (N = 2-100):**
- The transition is significantly rounded for N < 50
- T_c can shift by 10-30% from thermodynamic limit
- The Binder cumulant helps identify the effective T_c for finite N

### Anti-Patterns to Avoid

- **Applying thermodynamic limit results to N < 20:** The finite-size corrections are O(1) and qualitative behavior can differ. Always include finite-size scaling for small agent systems.
  - _Example:_ Predicting a sharp phase transition at T_c for N=4 agents is unphysical; the system has only 2^4=16 microstates.

- **Using mean-field exponents for d=2:** Mean-field overestimates ordering tendency. For 2D lattices, use exact Baxter results or epsilon expansion to at least O(ε²).
  - _Example:_ Mean-field predicts β = 1/2, but exact 2D Ising has β = 1/8—a factor of 4 difference.

- **Ignoring the q=4 special case:** The Potts model changes from second-order to first-order at q=4 in d=2. This qualitatively changes the phase transition behavior.
  - _Example:_ For q=8 (high diversity agent systems), the transition is first-order—expect abrupt jumps, not continuous growth.

- **Conflating different exponent definitions:** Different authors define β, γ with different normalizations. Always specify the order parameter convention.
  - _Example:_ If using m = M/M_0 vs. m = M/N, the exponent β differs by a factor.

---

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
|--------|------------|--------|------------|
| **Mean-field critical exponents** | β = 1/2, ν = 1/2, γ = 1, η = 0 | Landau theory (any textbook) | Valid for d ≥ 4 or fully-connected networks |
| **2D Ising (q=2) exponents** | β = 1/8, ν = 1, γ = 7/4, η = 1/4 | Onsager (1944), Baxter (1982) | Validation target for q=2 agent systems |
| **2D Potts critical exponents** | β = (g-2)/(12g), ν = √3/(2√g) | Baxter (1982), Nienhuis (1982) | Validation for general q (q ≤ 4) |
| **Ginzburg criterion** | Gi ∼ (T_c - T)^{(4-d)/2} | Goldenfeld (1992) | Determines mean-field validity |
| **Finite-size scaling forms** | m(N,t) = N^{-β/dν} f_m(t N^{1/dν}) | Cardy (1996) | Essential for small agent systems |
| **Correlation length at T_c** | ξ(T_c) ∼ ∞ (diverges) | Standard critical phenomena | Saturates at ξ_max ∼ N^{1/d} for finite N |

**Key insight:** Re-deriving these textbook results wastes context budget. The planner should reference these formulas and focus on the NOVEL application: how these exponents affect optimal agent scaling N*(q, T) and the interpretation for multi-agent systems.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
|--------|-------------------|--------|------------|
| **Scaling relations** | α + 2β + γ = 2, γ = β(δ-1) | Rushbrooke, Widom identities | Universal (any system) |
| **Hyperscaling** | 2-α = dν | Valid for d < d_c | Modified above d_c |
| **Binder cumulant** | U_4 = 1 - ⟨m⁴⟩/(3⟨m²⟩²) | Binder (1981) | Identifies T_c for finite N |
| **Finite-N T_c shift** | T_c(N) = T_c(∞)(1 + a N^{-1/dν}) | Finite-size scaling | a is non-universal |
| **RG eigenvalues (Ising)** | y_t = 1/ν, y_h = (d+2-η)/2 | Wilson-Fisher fixed point | d = 4 - ε expansion |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
|--------------|---------|------|-----------|-----------------|
| "Exactly Solved Models in Statistical Mechanics" | Baxter | 1982 | Exact 2D Potts T_c and exponents | Critical exponents for q ≤ 4, phase transition order change at q=4 |
| "The Potts Model" | Wu | 1982 | Comprehensive Potts review | Mean-field results, q-dependence |
| "Lectures on Phase Transitions and the RG" | Goldenfeld | 1992 | RG methodology | RG flow equations, Ginzburg criterion |
| "Scaling and Renormalization in Statistical Physics" | Cardy | 1996 | Finite-size scaling | Scaling forms, Binder cumulant |
| "Renormalization Group and Critical Phenomena" | Wilson, Kogut | 1974 | RG foundation | Momentum-shell method, epsilon expansion |
| "Finite Size Scaling" | Barber | 1983 | Small systems review | Finite-size corrections, shift of T_c |
| "Conformal Invariance and Critical Exponents" | Nienhuis | 1982 | 2D Potts from CFT | Exact exponent formulas for q ≤ 4 |

---

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
|------|----------------|---------|--------------|
| **NumPy/SciPy** | 1.24+ | Numerical root-finding, optimization | Solving RG flow equations, fitting scaling forms |
| **SymPy** | 1.12+ | Symbolic algebra for RG equations | Deriving flow equations, extracting eigenvalues |
| **matplotlib** | 3.7+ | Phase diagram visualization | Plotting T_c(q) curves, RG flow diagrams |
| **NumBA/JAX** | Latest | Accelerated Monte Carlo (for validation) | Finite-size scaling verification |

### Supporting Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **NetworkX** | Generate agent interaction topologies | Testing finite-size effects on different networks |
| **pandas** | Organize simulation results | Comparing multiple q values, temperatures |
| **seaborn** | Statistical visualization | Plotting scaling collapse plots |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
|-------------|----------------|------------|------------|
| **RG flow equation integration** | < 1 second (analytic/numeric ODE) | Extracting fixed points analytically | Use symbolic algebra, verify numerically |
| **Critical exponent from epsilon expansion** | < 1 second (symbolic) | Tracking terms to O(ε²) | Use SymPy with series expansion |
| **Finite-size scaling plots** | < 1 minute | Generating data for multiple N, q | Vectorize operations |
| **Monte Carlo validation** | ~minutes to hours | Equilibration near T_c | Use Wolff algorithm for q > 2 |

**Installation / Setup:**
```bash
# Core scientific stack (should already be installed)
pip install numpy scipy sympy matplotlib pandas seaborn

# For GPU acceleration (optional, for Monte Carlo in Phase 4)
pip install numba jax jaxlib
```

---

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
|-------|-------------------|----------------|-----------------|
| **Scaling relations** | Universality of critical exponents | Verify α + 2β + γ = 2, γ = β(δ-1) | Holds within numerical error |
| **q=2 reduces to Ising** | Potts model special case | Compare q=2 results to Onsager values | Exact agreement for d=2 |
| **Mean-field limit** | High-dimensional behavior | Compare d ≥ 4 results to Landau theory | β → 1/2, ν → 1/2 as d → ∞ |
| **Ginzburg criterion** | Mean-field validity | Check Gi ≪ 1 for mean-field regime | Mean-field valid for d ≥ 4 |
| **Finite-size sum rules** | Partition function normalization | Z(N) → Z(∞) as N → ∞ | Convergence to thermodynamic limit |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
|-------|------------------|--------------|--------|
| **q=2 (Ising) d=2** | Exact solution | β = 1/8, ν = 1, γ = 7/4 | Onsager (1944), Baxter (1982) |
| **q=3 d=2** | Exact CFT | β = 1/9, ν = 5/6 | Baxter (1982) |
| **q=4 d=2** | Marginal case | β = 1/12, ν = 2/3 | Baxter (1982) |
| **Mean-field (d ≥ 4)** | Landau theory | β = 1/2, ν = 1/2, γ = 1 | Any textbook |
| **q → ∞** | Potts → percolation | T_c → 0, first-order | Wu (1982) |
| **T → 0** | Zero temperature | Perfect order (m = 1) | Ground state |
| **T → ∞** | High temperature | Complete disorder (m = 0) | Paramagnetic phase |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
|------|--------|-----------|-----------------|
| **T_c comparison** | Compare mean-field to exact 2D | Ratio documented | T_c^MF/T_c^2D from Phase 2 |
| **Exponent comparison** | RG vs. exact Baxter | < 5% relative | β, ν, γ from Baxter |
| **Finite-size scaling collapse** | Data collapse of m(N, t) | Visual collapse | Universal scaling function |
| **Binder cumulant crossing** | Identify T_c for finite N | Crossing point | T_c(N) from crossing |

### Red Flags During Computation

- **Negative critical exponents:** β, ν, γ must be positive. Negative values indicate a sign error in the RG eigenvalue calculation.
- **Violation of scaling relations:** If α + 2β + γ ≠ 2, there's an error in exponent extraction or calculation.
- **β > 1 for d=2:** The maximum β in d=2 is 1/8 (Ising). Larger values indicate incorrect formula or misapplication of mean-field.
- **ν < 1/d:** Correlation length exponent has a lower bound from causality. ν < 1/d is unphysical.
- **Discontinuity at q=4:** For q > 4 in d=2, the transition is first-order. Continuous exponents should not be calculated for q > 4.
- **T_c decreasing with q:** T_c should decrease with q (harder to reach consensus with more diversity). Increasing T_c(q) indicates an error.

---

## Common Pitfalls

### Pitfall 1: Misapplying Mean-Field Theory in Low Dimensions

**What goes wrong:** Using mean-field critical exponents (β = 1/2, ν = 1/2) for d=2 or d=3 systems where fluctuation corrections are large.

**Why it happens:** Mean-field theory is simple and gives clean formulas. The temptation is to apply it universally.

**How to avoid:** Check the Ginzburg criterion Gi = (T_c - T)^{(4-d)/2}. For d < 4, Gi diverges as T → T_c, indicating mean-field failure. Use:
- d=2: Exact Baxter results or conformal field theory
- d=3: Epsilon expansion to O(ε²) or numerical exponents
- d ≥ 4: Mean-field theory is valid

**Warning signs:** Mean-field predictions disagreeing significantly with known results (e.g., β = 1/2 vs. exact 1/8 for 2D Ising).

**Recovery:** Switch to dimension-appropriate method: exact results for d=2, epsilon expansion for d=3, mean-field for d ≥ 4.

### Pitfall 2: Ignoring the q=4 Threshold in 2D Potts

**What goes wrong:** Treating all q values the same and calculating critical exponents for q > 4 in d=2, where the transition is first-order (no continuous critical exponents).

**Why it happens:** Most RG methods assume continuous (second-order) transitions. The first-order case is qualitatively different.

**How to avoid:** Explicitly check q before applying critical exponent formulas:
```
if (d == 2 and q > 4):
    # First-order transition: discontinuous jump in order parameter
    # No critical exponents β, ν, γ in the usual sense
    # Characterize by latent heat and correlation length (finite)
else:
    # Second-order: continuous transition with well-defined exponents
    # Apply RG or exact formulas
```

**Warning signs:** Calculation of β, ν, γ for q=8 or q=16 in d=2. These transitions are first-order.

**Recovery:** For q > 4 in d=2, characterize the transition by the jump in order parameter Δm, not by critical exponents. The correlation length remains finite at T_c.

### Pitfall 3: Neglecting Finite-Size Effects for Small N

**What goes wrong:** Applying thermodynamic limit results to systems with N < 50 agents, where finite-size corrections are large.

**Why it happens:** Most statistical mechanics textbooks focus on the N → ∞ limit. The small-N regime is rarely discussed.

**How to avoid:** Always include finite-size scaling for agent systems:
```
T_c(N) = T_c(∞)[1 + a N^{-1/dν} + O(N^{-2/dν})]
m(N, T) = N^{-β/dν} f_m((T - T_c)N^{1/dν})
```

For N < 20, consider exact enumeration of all microstates rather than scaling approximations.

**Warning signs:** Predictions that change qualitatively between N=4 and N=8 without smooth interpolation. Sharp phase transitions at N < 20.

**Recovery:** Use finite-size scaling forms. For very small N (N < 10), enumerate all configurations explicitly.

### Pitfall 4: Confusing Different Order Parameter Definitions

**What goes wrong:** Using formulas for β, γ derived with one order parameter convention (e.g., m = M/M_0) while calculating with a different convention (e.g., m = M/N).

**Why it happens:** Different sources use different normalizations. The exponent β depends on how m is defined.

**How to avoid:** Explicitly state the order parameter convention:
```
m = (qN_max - N) / [(q-1)N]  # Project convention, ranges from 0 to 1
```

When comparing to literature, account for the normalization. If the source uses m' = M/N, convert:
```
m = m' / m'_max  # Normalize to [0, 1]
```

**Warning signs:** β > 1, or β changing when the order parameter is rescaled (it shouldn't for the correctly defined exponent).

**Recovery:** Re-derive the exponent relation with the specific order parameter definition. The scaling form m ∼ (T_c - T)^β assumes a specific normalization.

### Pitfall 5: Incorrect Ginzburg Criterion Application

**What goes wrong:** Misapplying the Ginzburg criterion and incorrectly concluding that mean-field is valid (or invalid) for a given system.

**Why it happens:** The Ginzburg criterion has different forms in different sources, and the numerical coefficient depends on the model details.

**How to avoid:** Use the general form:
```
Gi = (k_B T_c)^2 / [(ΔC) ξ^4]
```
where ΔC is the specific heat jump. Mean-field is valid when Gi ≪ 1.

For the Potts model in d dimensions:
```
Gi ∼ (T_c - T)^{(4-d)/2}
```
For d < 4, Gi diverges at T_c, indicating mean-field failure.

**Warning signs:** Claiming mean-field is valid in d=2 or d=3 without acknowledging large fluctuation corrections near T_c.

**Recovery:** For d < 4, use epsilon expansion or exact results. Mean-field can be used qualitatively but not for precise exponent values.

---

## Level of Rigor

**Required for this phase:** Physicist's proof (controlled approximation with error estimates)

**Justification:** This phase derives critical exponents and phase diagrams that will be used to make quantitative predictions about multi-agent systems. Full mathematical rigor would be excessive, but hand-waving would miss important corrections that affect small-N behavior.

**What this means concretely:**

- All RG flow equations must be derived or cited with specific references
- Critical exponents must be calculated with explicit error estimates (e.g., "β = 1/2 - ε/6 + O(ε²)")
- Finite-size scaling forms must be stated with the scaling functions explicitly defined
- Validations against known limits (q=2 Ising, Baxter's results) are mandatory
- Mean-field results must be accompanied by Ginzburg criterion analysis

**Hierarchy of rigor:**
1. **Exact results** (Baxter, Onsager): Highest confidence, use for validation
2. **Epsilon expansion:** Systematic approximation, error controlled by ε
3. **Mean-field theory:** Qualitative guide, quantitative errors O(1) for d < 4
4. **Finite-size scaling:** Well-established framework, non-universal parameters need fitting

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| **Mean-field only** | RG + finite-size scaling | 1970s-1980s (Wilson, Cardy) | Understanding of scaling and corrections |
| **Numerical RG** | Analytic epsilon expansion | 1970s (Wilson-Fisher) | Systematic calculation of exponents |
| **Phenomenological scaling** | Conformal field theory (2D) | 1980s (Baxter, Nienhuis) | Exact 2D exponents for Potts model |
| **Thermodynamic limit only** | Finite-size scaling standard | 1980s (Barber, Cardy, Binder) | Essential for small systems like agent groups |

**Superseded approaches to avoid:**

- **Pure mean-field for d=2:** Mean-field qualitatively fails in 2D. Use Baxter's exact results.
- **Critical exponent tables without context:** Old tables don't specify d or q dependence. Always specify dimensionality and q value.
- **Ignoring the q=4 threshold:** Earlier work treated all q uniformly. Modern understanding recognizes q=4 as special in d=2.

---

## Open Questions

1. **What is the effective dimensionality of LLM multi-agent systems?**
   - What we know: Fully-connected networks have mean-field behavior (d = ∞ effectively)
   - What's unclear: Do real agent systems have low-dimensional effective topology?
   - Impact: Determines whether to use mean-field or exact 2D exponents
   - Recommendation: Assume mean-field (fully-connected) for first approximation, validate with Monte Carlo

2. **How does finite-size scaling work for N < 10?**
   - What we know: Standard finite-size scaling assumes N ≫ 1
   - What's unclear: Are there additional corrections for very small systems?
   - Impact: Agent systems often have N < 10
   - Recommendation: Use exact enumeration for N < 10, finite-size scaling for N > 10

3. **What is the q-dependence of critical exponents for d=3?**
   - What we know: Exact results only for d=2; d=3 requires numerical or epsilon expansion
   - What's unclear: How do exponents vary with q in d=3?
   - Impact: If agent systems are effectively 3D, need d=3 exponents
   - Recommendation: Use epsilon expansion at d=3 (ε=1) or consult Monte Carlo literature

4. **Is the agent system equilibrium or nonequilibrium?**
   - What we know: Statistical mechanics assumes equilibrium
   - What's unclear: Do LLM agents reach equilibrium during task execution?
   - Impact: Nonequilibrium systems can have different critical behavior
   - Recommendation: Assume quasistatic equilibrium for task timescales; validate with empirical data

---

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
|---------------|------------|-----------|-------------------|
| **Momentum-space RG** | Field theory too complex for discrete Potts | Real-space RG (Migdal-Kadanoff) | Medium: different formalism, cruder results |
| **Analytic RG** | Exponent calculations too involved | Monte Carlo finite-size scaling | High: lose analytic insight, gain numerical accuracy |
| **Mean-field theory** | Poor agreement with validation data | Exact 2D results (Baxter) | Low: just cite, but limited to d=2 |
| **Standard Potts model** | Agent systems have different interactions | Modified Potts (heterogeneous coupling) | Very high: analytical intractability |
| **Equilibrium assumption** | Agent systems are nonequilibrium | Master equation / Fokker-Planck | Very high: lose partition function framework |

**Decision criteria:** Abandon momentum-space RG if:
- The field theory representation of q-state Potts proves too complex
- Epsilon expansion gives unphysical results (negative exponents, etc.)
- Validation against Baxter's q=2 results fails

In these cases, switch to numerical finite-size scaling or exact results as appropriate.

---

## Dimensional Analysis

### Natural Scales and Dimensionless Parameters

**Natural scales for the agent system:**
- Energy scale: J (coupling strength)
- Temperature scale: T_c (critical temperature)
- Length scale: ξ (correlation length) or a (lattice spacing)
- System size: N (number of agents)

**Dimensionless parameters governing critical behavior:**

1. **Reduced temperature:** t = (T - T_c)/T_c
   - Controls distance from critical point
   - Relevant scaling variable: y_t = 1/ν

2. **System size scaling:** L/ξ where L ∼ N^{1/d}
   - Finite-size scaling parameter
   - When L ≫ ξ: thermodynamic limit
   - When L ≲ ξ: finite-size effects dominate

3. **Diversity parameter:** q (discrete) or continuous analog
   - Number of agent states
   - Affects universality class (different q → different exponents in 2D)

4. **Dimensionality:** d
   - Spatial dimension of effective lattice
   - d=2: exact results available
   - d=4: upper critical dimension for mean-field

**Scaling combinations:**
```
t N^{1/dν}  # Finite-size scaling variable
m N^{β/dν}  # Scaled order parameter
χ N^{-γ/dν} # Scaled susceptibility
```

### Dimensional Consistency Checks

All derived formulas must satisfy:
- [T_c] = [J] (energy)
- [ξ] = [length] = a (lattice spacing units)
- [m] = dimensionless (0 ≤ m ≤ 1)
- [χ] = [βJ N] (dimensionless when k_B = 1)
- Exponents β, ν, γ, η are dimensionless

---

## Phase Diagram Structure

### Ordered vs Disordered Regimes

**Phase diagram in (T, q) space:**

1. **Ordered phase (T < T_c):**
   - Nonzero order parameter: m > 0
   - Consensus/alignment among agents
   - Correlation length ξ ∼ |T_c - T|^{-ν} (diverges at T_c)
   - For agent systems: high agreement, efficient coordination

2. **Disordered phase (T > T_c):**
   - Zero order parameter: m = 0 (in thermodynamic limit)
   - No consensus; agents fluctuate independently
   - Finite correlation length ξ ∼ (T - T_c)^{-ν}
   - For agent systems: low agreement, diverse opinions

3. **Critical point (T = T_c):**
   - Scale-free fluctuations: ξ → ∞
   - Power-law correlations: G(r) ∼ r^{-(d-2+η)}
   - Universal scaling behavior
   - For agent systems: phase transition between consensus and fragmentation

### Critical Diversity q_c(T)

From Phase 2, inverting T_c(q) = T gives the critical diversity:
```
q_c(T) = T / (T - J)  (mean-field)
q_c(T) = exp(2J/T) - 1  (exact 2D, from T_c = J/ln(1+√q))
```

**Physical interpretation:**
- For fixed T, if q < q_c: system can reach consensus (ordered)
- For fixed T, if q > q_c: too much diversity for consensus (disordered)
- As T → J+: q_c → ∞ (critical temperature approaches coupling from above)
- As T → ∞: q_c → 1 (no diversity tolerated at high noise)

**Connection to Yang saturation:**
- Yang et al. observe saturation at D_8-D_16 (diversity 8-16)
- This suggests q_c ≈ 8-16 for their system
- Implies T/J ≈ 1.07-1.14 (close to coupling strength)

### First-Order vs Second-Order Transitions

**For d=2 Potts model:**
- q ≤ 4: Second-order (continuous) transition
  - Well-defined critical exponents β, ν, γ
  - Universal scaling functions
  - Smooth evolution of order parameter

- q > 4: First-order (discontinuous) transition
  - Jump in order parameter at T_c
  - Latent heat
  - Finite correlation length at T_c
  - No critical exponents in the usual sense

**For agent systems:**
- q ≤ 4: Gradual approach to consensus as T decreases
- q > 4: Abrupt consensus formation at T_c (tipping point)

**For mean-field (d ≥ 4):**
- All q: Second-order transition
- Critical exponents are q-independent (mean-field universality)

---

## Sources

### Primary (HIGH confidence)

- **Baxter, R. J.** "Exactly Solved Models in Statistical Mechanics" (1982) - Exact 2D Potts critical exponents, T_c formula, q-dependence
- **Wu, F. Y.** "The Potts Model" Rev. Mod. Phys. 54, 235 (1982) - Comprehensive Potts review, mean-field theory
- **Goldenfeld, N.** "Lectures on Phase Transitions and the Renormalization Group" (1992) - RG methodology, Ginzburg criterion
- **Cardy, J.** "Scaling and Renormalization in Statistical Physics" (1996) - Finite-size scaling, scaling forms
- **Wilson, K. G., Kogut, J.** "The Renormalization Group and the ε Expansion" Phys. Rep. 12, 75 (1974) - RG foundation

### Secondary (MEDIUM confidence)

- **Nienhuis, B.** "Exact Critical Point and Critical Exponents of O(n) Models in Two Dimensions" Phys. Rev. Lett. 49, 1062 (1982) - Conformal field theory formulas
- **Barber, M. N.** "Finite Size Scaling" in "Phase Transitions and Critical Phenomena" Vol. 8 (1983) - Finite-size review
- **Binder, K.** "Finite Size Scaling Analysis of Ising Model Block Distribution Functions" Phys. Rev. Lett. 47, 693 (1981) - Binder cumulant
- **Onsager, L.** "Crystal Statistics I" Phys. Rev. 65, 117 (1944) - Exact 2D Ising solution (q=2 case)

### Tertiary (LOW confidence - requires validation)

- **Yang et al. (2025)** "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity" arXiv:2602.03794 - **CRITICAL: Not retrieved due to rate limit; must be obtained manually**
- Recent Monte Carlo studies of Potts model finite-size scaling (2010s-2020s) - **Search failed; literature may exist**
- Agent-system specific applications of RG theory - **Novel territory; no prior work found**

---

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - RG theory, critical phenomena are well-established
- Standard approaches: HIGH - Momentum-space RG, finite-size scaling are textbook methods
- Critical exponents for 2D Potts: HIGH - Exact results from Baxter, conformal field theory
- Finite-size scaling: HIGH - Cardy, Barber provide rigorous framework
- Agent-system application: MEDIUM - Mapping from agents to Potts is novel, requires validation
- Yang et al. validation: LOW - Paper not retrieved; empirical comparison pending

**Research limitations:**
- Web search services were rate-limited during this research phase
- Yang et al. (2025) could not be retrieved; this is a critical gap for validation
- Recent literature (2020s) on finite-size scaling for small systems may exist that was not found
- Agent-system specific RG applications are novel; no prior work to build upon

**Research date:** 2026-03-21
**Valid until:** 2026-06-21 (3 months; verify recent preprints and retrieve Yang et al. paper)

**Action items for next phase:**
1. User must obtain Yang et al. (2025) from https://arxiv.org/abs/2602.03794
2. Repeat literature search after rate limit resets for recent finite-size scaling work
3. Characterize effective dimensionality of target agent systems (fully-connected vs. lattice)
4. Begin RG flow equation derivation in planning phase

---

## Caveats and Alternatives

**Self-critique (adversarial review):**

1. **What assumption might be wrong?**
   - Assumption: Agent systems can be modeled with equilibrium statistical mechanics. Reality: LLM agent systems may be inherently nonequilibrium (agents adapt during tasks). If so, the equilibrium partition function approach may need modification (e.g., nonequilibrium steady states, master equations).

2. **What alternative was dismissed too quickly?**
   - Omitted: Nonequilibrium RG methods and dynamical critical phenomena. These are relevant if agent systems have intrinsic dynamics that don't relax to equilibrium. Worth revisiting if equilibrium predictions fail validation.

3. **What limitation is being understated?**
   - The q=4 threshold for first-order transitions in d=2. This is a major qualitative change that affects how we interpret agent diversity. For q > 4, the transition is abrupt—this predicts "tipping points" in agent systems that could be important for practical applications.

4. **Is there a simpler method being overlooked?**
   - Numerical finite-size scaling directly from Monte Carlo, bypassing RG calculations. This would give numerical exponents without analytic derivation. However, this loses the predictive power of analytic formulas for N*(q, T).

5. **Would a specialist disagree?**
   - A critical phenomena specialist might question whether the Potts model is the right universality class for agent systems. Agent interactions might have different symmetries (e.g., directed communication, hierarchical structure) that place them in a different universality class. An agent-systems specialist might question whether the phase transition metaphor is useful for practical agent deployment.

**Mitigation:** These caveats reinforce the need for:
- Careful empirical validation against Yang et al. (when obtained)
- Numerical Monte Carlo validation for specific parameters
- Explicit testing of mean-field assumptions
- Consideration of network topology effects

---

*End of Phase 3 Research*
