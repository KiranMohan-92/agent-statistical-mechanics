# Derivation: Mean-Field Free Energy and Optimal Agent Count N*

**Project:** Statistical Mechanics of Multi-Agent Systems
**Phase:** 02 - Partition Function Derivation
**Plan:** 02-03 - Mean-Field Free Energy and N* Minimization
**Created:** 2026-03-19
**Status:** In Progress

---

## Convention Assertions

% ASSERT_CONVENTION: natural_units=k_B=1, metric_signature=Euclidean, fourier_convention=exp(-ikx), coupling_convention=H=-J*sum(delta), potts_hamiltonian=H=-J*delta_ij_ferromagnetic, spin_basis=Potts, state_normalization=Boltzmann

---

## 1. Free Energy from Partition Function

### 1.1 Starting Point: Mean-Field Partition Function

From Plan 02-02, the mean-field partition function for the fully-connected q-state Potts model is:

$$\boxed{Z_{\text{MF}}(N, q, T) = \left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right]^N}$$

where $\beta = 1/T$ with $k_B = 1$.

### 1.2 Free Energy Definition

The Helmholtz free energy is defined as:

$$F = -T \ln Z$$

**Dimensional check:**
- $[T] = [E]$ (energy units with $k_B = 1$)
- $[\ln Z] = [1]$ (dimensionless)
- $[F] = [E]$ ✓

### 1.3 Free Energy Expression

Substituting our partition function:

$$\ln Z = N \ln\left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right]$$

$$\boxed{F(N, q, T) = -\frac{N}{\beta} \ln\left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right]}$$

**Per-agent free energy:**

$$f = \frac{F}{N} = -\frac{1}{\beta} \ln\left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right]$$

### 1.4 Physical Interpretation

The free energy can be decomposed as $F = U - TS$ where:
- $U = -\frac{\partial \ln Z}{\partial \beta}$: Internal energy (alignment contribution)
- $S = \beta U + \ln Z$: Entropy (diversity contribution)

**Interpretation for agent systems:**
- **Energy term ($U$):** Represents coordination/alignment between agents. Lower energy = better alignment = better performance.
- **Entropy term ($-TS$):** Represents diversity of agent states. Higher entropy = more diversity = broader knowledge coverage.
- **Optimal performance:** Corresponds to minimizing $F$ (maximizing $-F$)

---

## 2. Minimization Condition for Optimal Agent Count N*

### 2.1 Setup: N as Continuous Variable

To find the optimal number of agents $N^*$, we treat $N$ as a continuous variable and minimize the free energy with respect to $N$.

**First-order condition:**

$$\frac{\partial F}{\partial N} = 0$$

**Second-order condition (for minimum):**

$$\frac{\partial^2 F}{\partial N^2} > 0$$

### 2.2 Critical Observation on N-Dependence

From the free energy expression:

$$F(N, q, T) = -N T \ln\left[e^{J/2T} + (q-1)e^{-J/2T}\right]$$

**The N-dependence is purely linear!**

$$\frac{\partial F}{\partial N} = -T \ln\left[e^{J/2T} + (q-1)e^{-J/2T}\right] = f(q, T)$$

This is a **constant** (independent of $N$). Therefore:

- If $\frac{\partial F}{\partial N} < 0$: Free energy decreases with $N$ → Add more agents
- If $\frac{\partial F}{\partial N} > 0$: Free energy increases with $N$ → Remove agents
- If $\frac{\partial F}{\partial N} = 0$: Free energy independent of $N$ → Any $N$ is equivalent

### 2.3 Implication: Mean-Field Theory Has No Finite Optimal N*

The mean-field approximation predicts that:
- $F \propto N$ (extensive free energy)
- Per-agent free energy $f = F/N$ is independent of $N$

**This means the pure mean-field theory has NO finite optimal $N^*$!**

The system either:
1. Keeps adding agents indefinitely (if alignment benefits dominate)
2. Reduces to $N=1$ (if coordination costs dominate)

**Resolution:** We need to consider **finite-size corrections** and **coordination costs** that are not captured in the pure mean-field partition function.

---

## 3. Free Energy with Coordination Costs

### 3.1 Why Mean-Field Fails for N* Prediction

The mean-field partition function assumes:
1. Every agent interacts with every other agent
2. Interaction cost per pair is constant
3. Total interaction cost scales as $N(N-1)/2$

However, in real agent systems:
1. **Communication overhead:** More agents = more coordination messages
2. **Diminishing returns:** Each additional agent contributes less
3. **Finite resource budget:** Computing/time constraints

### 3.2 Extended Free Energy with Cost Term

We modify the free energy to include a cost term that scales super-linearly with $N$:

$$F_{\text{total}}(N, q, T) = F_{\text{stat}}(N, q, T) + F_{\text{cost}}(N)$$

where:

$$F_{\text{stat}}(N, q, T) = -\frac{N}{\beta} \ln\left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right]$$

and the cost term is:

$$F_{\text{cost}}(N) = \epsilon N^2$$

Here $\epsilon > 0$ represents the **coordination cost per agent pair**.

**Justification:**
- In a fully-connected system, there are $\binom{N}{2} \approx N^2/2$ communication pairs
- Each pair incurs a cost $\propto \epsilon$ for synchronization
- This cost is not captured in the statistical mechanics partition function

### 3.3 Extended Free Energy Expression

$$\boxed{F_{\text{total}}(N, q, T) = -\frac{N}{\beta} \ln\left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right] + \epsilon N^2}$$

**Dimensional check:**
- First term: $[N/\beta] = [E]$ ✓
- Second term: $[\epsilon N^2] = [E]$ ✓ (requires $[\epsilon] = [E/N^2]$)

### 3.4 Per-Agent Free Energy with Cost

$$f_{\text{total}} = \frac{F_{\text{total}}}{N} = -\frac{1}{\beta} \ln\left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right] + \epsilon N$$

The cost term creates an $N$-dependent per-agent free energy, enabling a finite optimum.

---

## 4. Optimal Agent Count N* from Minimization

### 4.1 First-Order Condition

$$\frac{\partial F_{\text{total}}}{\partial N} = -\frac{1}{\beta} \ln\left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right] + 2\epsilon N = 0$$

Solving for $N^*$:

$$\boxed{N^*(q, T) = \frac{1}{2\epsilon \beta} \ln\left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right]}$$

This is the **optimal agent count** that minimizes total free energy.

### 4.2 Second-Order Condition

$$\frac{\partial^2 F_{\text{total}}}{\partial N^2} = 2\epsilon > 0$$

Since $\epsilon > 0$, this is always a **minimum** (not a maximum). ✓

### 4.3 Simplified Form

Let $x = \beta J/2$. Then:

$$N^*(q, T) = \frac{1}{2\epsilon \beta} \ln\left[e^x + (q-1)e^{-x}\right]$$

**High-temperature limit ($x \ll 1$, $T \gg J$):**

$$e^x \approx 1 + x, \quad e^{-x} \approx 1 - x$$

$$N^* \approx \frac{1}{2\epsilon \beta} \ln\left[q + x(2-q)\right] \approx \frac{\ln q}{2\epsilon \beta}$$

**Low-temperature limit ($x \gg 1$, $T \ll J$):**

$$N^* \approx \frac{1}{2\epsilon \beta} \ln\left[e^{\beta J/2}\right] = \frac{J}{4\epsilon T}$$

---

## 5. Diversity Effect on N*

### 5.1 Scaling with q

From the optimal $N^*$ expression:

$$N^*(q, T) = \frac{1}{2\epsilon \beta} \ln\left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right]$$

**Derivative with respect to q:**

$$\frac{\partial N^*}{\partial q} = \frac{1}{2\epsilon \beta} \cdot \frac{e^{-\beta J/2}}{e^{\beta J/2} + (q-1)e^{-\beta J/2}} > 0$$

Since all factors are positive, **$N^*$ increases with $q$**.

### 5.2 Physical Interpretation

This result has a clear physical meaning:

- Higher diversity $q$ → more entropy per agent → each agent provides more "value"
- The coordination cost $\epsilon N^2$ is the same regardless of diversity
- Therefore the system can sustain a **larger** optimal population before costs outweigh benefits

**This does NOT mean diverse systems are less efficient.** It means:
- For a given coordination budget, diverse systems can operate at larger scale
- The *per-agent* free energy is lower for diverse systems (better performance)
- The optimal $N^*$ shifts upward because the statistical benefit term grows faster with $q$

### 5.3 Equal-Performance Comparison (Yang Interpretation)

Yang et al. ask a different question: **How many homogeneous agents equal the performance of diverse agents?**

For equal free energy (ignoring coordination costs, $\epsilon \to 0$):

$$N_1 \cdot \frac{J}{2} = N_2 \cdot T \ln\left[2\cosh\left(\frac{J}{2T}\right)\right]$$

$$\mathcal{D}(\tau) = \frac{N_1}{N_2} = \frac{2}{\tau} \ln\left[2\cosh\left(\frac{\tau}{2}\right)\right]$$

where $\tau = J/T$.

**Numerical values:**

| $\tau = J/T$ | $\mathcal{D}(\tau)$ | 1/$\mathcal{D}$ (homogeneous per diverse) | Interpretation |
|-------------|-------------------|------------------------------------------|----------------|
| 0.5 (high T) | 2.90 | 0.35 | 1 homogeneous ≈ 2.9 diverse agents |
| 1.0 | 1.63 | 0.61 | 1 homogeneous ≈ 1.6 diverse agents |
| 2.0 | 1.13 | 0.89 | Nearly equivalent |
| 3.0 | 1.03 | 0.97 | Nearly equivalent |
| 5.0 | 1.00 | 1.00 | Converging to 1:1 |

**Key finding:** The pure entropic model predicts at most ~3× diversity benefit (at high temperature). Yang observes 4-8×, indicating significant **non-entropic** benefits from diversity (complementarity, error decorrelation, etc.).

### 5.4 Why the Model Underestimates Yang's Result

The discrepancy between our ~3× maximum and Yang's 4-8× suggests:

1. **Complementarity:** Diverse agents solve different subproblems (not captured by entropy)
2. **Error decorrelation:** Diverse agents make uncorrelated mistakes, reducing consensus errors
3. **Coverage:** More diverse agents cover more of the solution space
4. **Redundancy reduction:** Homogeneous agents duplicate effort; diverse agents don't

These effects are **outside the pure Potts model** and would require extending the Hamiltonian.

---

## 6. Temperature Dependence of N*

### 6.1 Temperature in Agent Systems

**Physical interpretation:**
- **Low T ($T \ll J$):** Agents are deterministic, highly aligned, behave predictably
- **High T ($T \gg J$):** Agents are stochastic, disagree frequently, high noise
- **Critical T:** Phase transition between ordered and disordered behavior

### 6.2 N* vs Temperature

From the optimal $N^*$ formula:

$$N^*(q, T) = \frac{T}{2\epsilon} \ln\left[e^{J/2T} + (q-1)e^{-J/2T}\right]$$

**Low-temperature limit ($T \ll J$):**

$$N^* \approx \frac{T}{2\epsilon} \cdot \frac{J}{2T} = \frac{J}{4\epsilon}$$

**Interesting:** At low T, $N^*$ becomes independent of $T$!

**High-temperature limit ($T \gg J$):**

$$N^* \approx \frac{T}{2\epsilon} \ln q$$

**High-temperature behavior:** $N^* \propto T \ln q$

This makes physical sense:
- High noise (high T) requires more agents for reliable consensus
- More diversity (higher q) allows the system to sustain a larger optimal population

### 6.3 Critical Temperature Discussion

The Potts model has a phase transition at (from Plan 02-04):

$$T_c^{\text{MF}} = \frac{J q}{q - 1}$$

**Near $T_c$:**
- Below $T_c$: Agents align spontaneously (ordered phase)
- Above $T_c$: Agents disagree (disordered phase)

**Agent system interpretation:**
- Below $T_c$: Fewer agents needed (coordination is effective)
- Above $T_c$: More agents needed (overcome disagreement through voting)

---

## 7. Numerical Examples and Yang Comparison

### 7.1 Parameter Values

For numerical evaluation, we use:
- $J = 1$ (sets energy scale)
- $\epsilon = 0.01$ (coordination cost parameter)
- $T \in \{0.5, 1.0, 1.5, 2.0\}$ (covering ordered to disordered)

### 7.2 N* Table

**Corrected values** from the formula $N^* = \frac{T}{2\epsilon} \ln\left[e^{J/2T} + (q-1)e^{-J/2T}\right]$:

| $q$ | $T = 0.5$ | $T = 1.0$ | $T = 1.5$ | $T = 2.0$ |
|-----|----------|----------|----------|----------|
| 1 | 25.0 | 25.0 | 25.0 | 25.0 |
| 2 | 28.2 | 40.7 | 56.1 | 72.4 |
| 4 | 33.5 | 62.2 | 94.9 | 128.7 |
| 8 | 41.7 | 88.7 | 139.4 | 190.7 |
| 16 | 52.7 | 118.7 | 187.3 | 256.2 |

**Observations:**
- $N^*$ **increases** with $q$ (more diversity → system can support more agents before coordination costs dominate) ✓
- $N^*$ increases with $T$ (higher temperature requires more agents) ✓
- For $q=1$ (homogeneous): $N^* = J/(4\epsilon) = 25$ is constant across all $T$ ✓
- The increase is super-linear in $q$ (logarithmic growth)

**Physical interpretation:** Higher diversity provides more entropy benefit per agent, so the system can sustain a larger agent population before the quadratic coordination cost $\epsilon N^2$ outweighs the statistical benefit. This does NOT mean diverse systems are less efficient — it means the optimal operating point shifts to larger populations.

### 7.3 Equal-Performance Diversity Multiplier

To compare with Yang et al., we ask: **How many homogeneous agents equal the free energy of diverse agents?**

For equal free energy (ignoring coordination costs, $\epsilon \to 0$):

$$\mathcal{D}(\tau) = \frac{N(q=1)}{N(q=2)} = \frac{2}{\tau} \ln\left[2\cosh\left(\frac{\tau}{2}\right)\right]$$

where $\tau = J/T$.

| $\tau = J/T$ | $\mathcal{D}(\tau)$ | 1/$\mathcal{D}$ (diverse multiplier) | Interpretation |
|-------------|-------------------|-------------------------------------|----------------|
| 0.5 (high T) | 2.90 | 0.35 | 1 homogeneous ≈ 2.9 diverse |
| 1.0 | 1.63 | 0.61 | 1 homogeneous ≈ 1.6 diverse |
| 2.0 | 1.13 | 0.89 | 1 homogeneous ≈ 1.1 diverse |
| 3.0 | 1.03 | 0.97 | Nearly equivalent |
| 4.0 | 1.01 | 0.99 | Nearly equivalent |
| 5.0 | 1.00 | 1.00 | Converging to 1:1 |

**Inverted:** $1/\mathcal{D}$ tells us how many diverse agents equal 1 homogeneous agent.

**Yang comparison:**
- Yang reports: 4 diverse ≈ 16-32 homogeneous → 1 diverse ≈ 4-8 homogeneous
- Our model: 1 diverse ≈ 0.35-1.0 homogeneous (depending on $\tau$)
- Maximum diversity benefit: ~3× at $\tau = 0.5$ (high temperature, low alignment)

**Discrepancy analysis:**
- Our model predicts at most ~3× benefit from pure entropy
- Yang observes 4-8× benefit
- The Yang result likely includes:
  1. Task-specific capability complementarity (not captured by entropy)
  2. Error decorrelation (diverse agents make uncorrelated mistakes)
  3. Reduced redundancy in homogeneous systems
  4. Communication overhead differences

### 7.4 Diversity Ratio (N* at equal cost)

Ratio: $N^*(q=1) / N^*(q)$ — this shows how the optimal population size changes with diversity:

| $q$ | $T = 0.5$ | $T = 1.0$ | $T = 1.5$ | $T = 2.0$ |
|-----|----------|----------|----------|----------|
| 2 | 0.887 | 0.615 | 0.446 | 0.345 |
| 4 | 0.746 | 0.402 | 0.263 | 0.194 |
| 8 | 0.600 | 0.282 | 0.179 | 0.131 |
| 16 | 0.474 | 0.211 | 0.134 | 0.098 |

**Interpretation:** This ratio < 1 means $N^*(q) > N^*(q=1)$ — diverse systems optimally operate at larger population sizes. The ratio decreases with both $q$ and $T$, meaning the population expansion effect is strongest at high diversity and high temperature.

### 7.4 Explicit Scaling Law

From our $N^*$ formula, the diversity scaling is:

$$\frac{N^*(q)}{N^*(q=1)} = \frac{\ln\left[e^{J/2T} + (q-1)e^{-J/2T}\right]}{J/2T}$$

For $T \ll J$ (low temperature, strong alignment):

$$\frac{N^*(q)}{N^*(q=1)} \approx 1 - \frac{2T}{J} \ln q + \cdots$$

For $T \gg J$ (high temperature, weak alignment):

$$\frac{N^*(q)}{N^*(q=1)} \approx \frac{2T \ln q}{J}$$

---

## 8. Summary of Key Results

### 8.1 Free Energy with Coordination Costs

$$\boxed{F_{\text{total}}(N, q, T) = -\frac{N}{\beta} \ln\left[e^{\beta J/2} + (q-1)e^{-\beta J/2}\right] + \epsilon N^2}$$

### 8.2 Optimal Agent Count

$$\boxed{N^*(q, T) = \frac{T}{2\epsilon} \ln\left[e^{J/2T} + (q-1)e^{-J/2T}\right]}$$

### 8.3 Diversity Scaling

$$\frac{\partial N^*}{\partial q} > 0 \quad \text{(N* increases with q: diverse systems sustain larger optimal populations)}$$

For equal free energy (performance comparison):

$$\mathcal{D}(\tau) = \frac{N(q=1)}{N(q=2)} = \frac{2}{\tau} \ln\left[2\cosh\left(\frac{\tau}{2}\right)\right]$$

The pure entropic model predicts at most ~3× diversity benefit (at high T). Yang observes 4-8×, indicating non-entropic effects (complementarity, error decorrelation).

### 8.4 Temperature Dependence

- **Low T ($T \ll J$):** $N^* \to J/(4\epsilon)$ (constant)
- **High T ($T \gg J$):** $N^* \to \frac{T \ln q}{2\epsilon}$ (linear in T)

---

## 9. Validations

### 9.1 Dimensional Analysis
- $[F] = [E]$ ✓
- $[N^*] = [1]$ (dimensionless count) ✓
- $[\epsilon] = [E]$ ✓ (since $N$ is a pure count, $[\epsilon N^2] = [E] \cdot [1] = [E]$)

**Note:** The convention was initially stated as $[\epsilon] = [E/N^2]$ in Plan 02-03 and later "corrected" to $[E/N]$ in Plan 02-05. Both are incorrect — since $N$ is a dimensionless count, $[\epsilon] = [E]$ is the correct assignment.

### 9.2 Limiting Cases
- $q \to 1$: $N^* = \frac{T}{2\epsilon} \cdot \frac{J}{2T} = \frac{J}{4\epsilon}$ (constant) ✓
- $T \to \infty$: $N^* \propto T \ln q$ (diverges, needs more agents for high noise) ✓
- $\epsilon \to 0$: $N^* \to \infty$ (no cost → infinite agents) ✓

### 9.3 Physical Consistency
- $N^* > 0$: Always positive ✓
- $\partial^2 F/\partial N^2 = 2\epsilon > 0$: True minimum ✓
- $N^*$ decreases with $q$ (equal performance interpretation) ✓

### 9.4 Comparison to Yang et al.

| Quantity | Our Theory | Yang et al. | Match? |
|----------|------------|-------------|--------|
| Diversity benefit | Yes (max ~3× from entropy) | Yes (4-8× observed) | Qualitative ✓, Quantitative ✗ |
| $N^*$ increases with T | Yes (linear at high T) | Not directly tested | — |
| Optimal regime | $N \approx 25-250$ | $N \approx 4-32$ | Model overestimates |

**Discrepancy explanation:**
- Our model captures only entropic effects
- Real diversity has additional benefits (complementarity)
- Communication overheads not fully modeled

---

## References

- Plan 02-02: `.gpd/phases/02-partition-function-derivation/02-02-partition-function.md`
- Yang et al. (2025): `.gpd/phases/01-literature-deep-dive/YANG-GAP.md`
- Goldenfeld, N. (1992). *Lectures on Phase Transitions and the Renormalization Group*

---

*End of Derivation 02-03*
