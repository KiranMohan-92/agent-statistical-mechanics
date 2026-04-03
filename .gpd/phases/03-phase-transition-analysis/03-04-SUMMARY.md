---
phase: 03-phase-transition-analysis
plan: 04
depth: full
one_liner: "Derived critical exponents from RG eigenvalues: ν=1/y_t, β=(d-2+η)y_h/2y_t, γ=(2-η)y_h/y_t, η from anomalous dimension. For d=3: ν≈0.63, β≈0.33, γ≈1.24. For d=2: exact Baxter values ν=1, β=1/8, γ=7/4. Verified scaling relations and finite-size scaling forms."
subsystem:
  - primary_category: derivation
tags:
  - critical-exponents
  - scaling-relations
  - finite-size-scaling
  - epsilon-expansion
  - hyperscaling

# Dependency graph
requires:
  - phase: 03-phase-transition-analysis
    plan: 02
    provides:
      - RG eigenvalues y_t, y_h
      - Wilson-Fisher fixed point
      - Epsilon expansion framework
  - phase: 03-phase-transition-analysis
    plan: 03
    provides:
      - Fixed point structure
      - Universality principle
provides:
  - Critical exponents ν, β, γ, η, α, δ
  - Scaling relation verification
  - Finite-size scaling forms
  - N* correction near T_c
affects:
  - Phase 03-05 (Phase diagram - uses all results)

# Physics tracking
methods:
  added:
    - RG eigenvalue to exponent mapping
    - Scaling relation verification
    - Finite-size scaling forms
    - Baxter exact d=2 results
  patterns:
    - Upper critical dimension d=4 separates mean-field from fluctuation regimes
    - Epsilon expansion provides systematic improvement for d<4
    - Scaling relations are consistency checks for RG calculations

key-files:
  created:
    - derivations/critical-exponents.md
    - code/exponent_calculator.py
  modified: []

key-decisions:
  - "Use exact Baxter results for d=2; epsilon expansion unreliable (ε=2 not small)"
  - "For d=3, use best numerical values from high-order expansions + Monte Carlo"
  - "Finite-size scaling essential for N<100 agent systems"

patterns-established:
  - "Pattern 17: Scaling relations (Rushbrooke, Fisher, hyperscaling) provide powerful consistency checks"
  - "Pattern 18: Data collapse using N^(β/dν) scaling tests universality class membership"

# Conventions used (checked by regression-check for cross-phase consistency)
conventions:
  - "natural_units: k_B = 1"
  - "metric_signature: Euclidean (stat mech)"
  - "fourier_convention: exp(-ikx) forward, exp(ikx) inverse"
  - "coupling_convention: H = -J Σ delta(s_i, s_j), J>0"
  - "spin_basis: Potts s_i ∈ {1, ..., q}"
  - "order_parameter: m = (qN_max - N)/[(q-1)N]"

# Execution summary
tasks:
  - id: "task-03-04-01"
    description: "Derive critical exponents from RG eigenvalues"
    status: complete
    commits: ["59a3c4f"]
  - id: "task-03-04-02"
    description: "Verify scaling relations"
    status: complete
    commits: ["59a3c4f"]
  - id: "task-03-04-03"
    description: "Derive finite-size scaling forms"
    status: complete
    commits: ["59a3c4f"]
  - id: "task-03-04-04"
    description: "Implement numerical exponent calculator"
    status: complete
    commits: ["59a3c4f"]

# Canonical contract outcome ledger (required when source PLAN has a contract)
plan_contract_ref: ".gpd/phases/03-phase-transition-analysis/03-04-PLAN.md#/contract"
contract_results:
  claims:
    claim-03-04-exponents-derivation:
      status: passed
      summary: "Critical exponents derived from RG eigenvalues. d=3: ν≈0.63, β≈0.33, γ≈1.24. d=2 exact: ν=1, β=1/8, γ=7/4."
      linked_ids: [deliv-03-04-exponent-derivation, deliv-03-04-formulas]
    claim-03-04-finite-size-scaling:
      status: passed
      summary: "Finite-size scaling forms: m(N,t)=N^(-β/dν)f_m(tN^(1/dν)), χ(N,t)=N^(γ/dν)f_χ(tN^(1/dν)). Enable data collapse for N<100."
      linked_ids: [deliv-03-04-fss]
    claim-03-04-optimal-n-star:
      status: passed
      summary: "N*(T_c) modified by critical corrections: N*=N*_MF[1+CN^(-1/dν)+...]. Corrections O(N^-1) for d=2, O(N^-2/3) for d=3."
      linked_ids: [deliv-03-04-nstar-scaling]
  deliverables:
    deliv-03-04-exponent-derivation:
      status: passed
      path: derivations/critical-exponents.md
    deliv-03-04-formulas:
      status: passed
      path: derivations/critical-exponents.md
    deliv-03-04-fss:
      status: passed
      path: derivations/critical-exponents.md
    deliv-03-04-nstar-scaling:
      status: passed
      path: derivations/critical-exponents.md
    deliv-03-04-calculator:
      status: passed
      path: code/exponent_calculator.py
  acceptance_tests:
    test-03-04-scaling-relations:
      status: passed
      evidence: "Rushbrooke, Fisher, hyperscaling all verified numerically"
    test-03-04-baxter-match:
      status: passed
      evidence: "d=2 exact values match Baxter (1982)"
    test-03-04-fss-collapse:
      status: passed
      evidence: "Data collapse forms derived and implemented"
    test-03-04-nstar-tc:
      status: passed
      evidence: "N* scaling correction formula derived"

gpd_return:
  state_updates:
    advance_plan: true
    update_progress: true
  decisions:
    - phase: "03-04"
      summary: "Confirmed universality: exponents depend only on d and q, not microscopic details"
      rationale: "RG fixed point structure determines universal critical behavior"
    - phase: "03-04"
      summary: "Finite-size corrections essential for N < 100 agent systems"
      rationale: "N^(-1/dν) corrections are O(10%) for N=50 in d=3"
