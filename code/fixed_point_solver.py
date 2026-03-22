#!/usr/bin/env python3
"""
Fixed Point Solver and Critical Exponent Calculator for Potts Model

This module implements numerical RG flow integration, fixed point finding,
stability analysis, and critical exponent computation for the q-state Potts model.

Author: Phase 03-03 execution
Date: 2026-03-22
"""

# ASSERT_CONVENTION
# natural_units: k_B = 1
# metric_signature: Euclidean (stat mech)
# fourier_convention: exp(-ikx) forward, exp(ikx) inverse
# coupling_convention: H = -J Σ delta(s_i, s_j), J>0
# spin_basis: Potts s_i ∈ {1, ..., q}
# order_parameter: m = (qN_max - N)/[(q-1)N]

import numpy as np
from scipy.integrate import odeint
from scipy.optimize import root, fsolve
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
import json


# -----------------------------------------------------------------------------
# Constants and Phase Space Factors
# -----------------------------------------------------------------------------

def phase_space_factor(d: float) -> float:
    """
    Compute the phase space factor K_d = S_d / (2π)^d

    Args:
        d: Spatial dimension

    Returns:
        K_d: Phase space factor for dimension d
    """
    if d == 1:
        return 1.0 / (2.0 * np.pi)
    elif d == 2:
        return 1.0 / (2.0 * np.pi)
    elif d == 3:
        return 1.0 / (2.0 * np.pi**(1.5))
    elif d == 4:
        return 1.0 / (8.0 * np.pi)
    else:
        # General formula: S_d / (2π)^d
        # S_d = 2π^(d/2) / Γ(d/2)
        from scipy.special import gamma
        return (2 * np.pi**(d/2) / gamma(d/2)) / (2*np.pi)**d


def surface_area_sphere(d: float) -> float:
    """
    Compute surface area of unit d-dimensional sphere S_d

    Args:
        d: Spatial dimension

    Returns:
        S_d: Surface area
    """
    from scipy.special import gamma
    return 2 * np.pi**(d/2) / gamma(d/2)


# -----------------------------------------------------------------------------
# Fixed Point Data Structures
# -----------------------------------------------------------------------------

@dataclass
class FixedPoint:
    """Represents an RG fixed point"""
    fp_type: str  # 'gaussian', 'wilson_fisher', 'ht', 'lt'
    r: float
    u: float
    d: float
    eigenvalues: np.ndarray
    stability: str  # 'stable', 'unstable', 'saddle'

    def __str__(self) -> str:
        return f"FP({self.fp_type}): r*={self.r:.4g}, u*={self.u:.4g}, d={self.d}, stability={self.stability}"


# -----------------------------------------------------------------------------
# RG Flow Equations
# -----------------------------------------------------------------------------

def rg_flow_equations(y: np.ndarray, l: float, d: float, Lambda: float = 1.0) -> np.ndarray:
    """
    RG flow equations for the Potts/Ising model (simplified near criticality)

    Args:
        y: [r, u] state
        l: RG scale (log of scale factor b)
        d: Spatial dimension
        Lambda: UV cutoff momentum (default 1.0)

    Returns:
        [dr/dl, du/dl]
    """
    r, u = y
    K_d = phase_space_factor(d)

    # Simplified flow equations (near r << Lambda^2)
    dr_dl = 2 * r + 12 * u * K_d * Lambda**d
    du_dl = (4 - d) * u - 36 * u**2 * K_d * Lambda**d

    return np.array([dr_dl, du_dl])


def rg_flow_full(y: np.ndarray, l: float, d: float, Lambda: float = 1.0) -> np.ndarray:
    """
    Full RG flow equations including denominator corrections

    Args:
        y: [r, u] state
        l: RG scale
        d: Spatial dimension
        Lambda: UV cutoff

    Returns:
        [dr/dl, du/dl]
    """
    r, u = y
    K_d = phase_space_factor(d)

    # Full flow equations with (1 + r/Lambda^2) corrections
    denom_r = 1 + r / Lambda**2
    denom_u = (1 + r / Lambda**2)**2

    dr_dl = 2 * r + 12 * u * K_d * Lambda**d / denom_r
    du_dl = (4 - d) * u - 36 * u**2 * K_d * Lambda**d / denom_u

    return np.array([dr_dl, du_dl])


def integrate_flow(
    r0: float,
    u0: float,
    d: float,
    l_max: float = 10.0,
    n_steps: int = 1000,
    Lambda: float = 1.0,
    full: bool = False
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Integrate RG flow from initial conditions

    Args:
        r0: Initial r value
        u0: Initial u value
        d: Spatial dimension
        l_max: Maximum RG scale
        n_steps: Number of integration steps
        Lambda: UV cutoff
        full: Use full flow equations if True

    Returns:
        l_vals: Array of RG scales
        r_vals: Array of r values
        u_vals: Array of u values
    """
    flow_func = rg_flow_full if full else rg_flow_equations
    y0 = np.array([r0, u0])
    l_vals = np.linspace(0, l_max, n_steps)

    # Integrate using RK4
    y = y0.reshape(1, 2)
    r_vals = np.zeros(n_steps)
    u_vals = np.zeros(n_steps)

    for i, l in enumerate(l_vals):
        k1 = flow_func(y.flatten(), l, d, Lambda)
        k2 = flow_func(y.flatten() + k1/2, l + 0.5/n_steps, d, Lambda)
        k3 = flow_func(y.flatten() + k2/2, l + 0.5/n_steps, d, Lambda)
        k4 = flow_func(y.flatten() + k3, l + 1.0/n_steps, d, Lambda)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / (6 * n_steps)
        r_vals[i] = y[0, 0]
        u_vals[i] = y[0, 1]

    return l_vals, r_vals, u_vals


# -----------------------------------------------------------------------------
# Fixed Point Finding
# -----------------------------------------------------------------------------

def find_gaussian_fixed_point(d: float) -> FixedPoint:
    """Return the Gaussian fixed point"""
    eigenvalues = np.array([2.0, 4.0 - d])

    if d > 4:
        stability = "stable"
    elif d == 4:
        stability = "marginal"
    else:
        stability = "unstable"

    return FixedPoint(
        fp_type='gaussian',
        r=0.0,
        u=0.0,
        d=d,
        eigenvalues=eigenvalues,
        stability=stability
    )


def find_wilson_fisher_fixed_point(d: float, Lambda: float = 1.0) -> FixedPoint:
    """
    Find Wilson-Fisher fixed point using epsilon expansion

    Args:
        d: Spatial dimension (must be < 4)
        Lambda: UV cutoff

    Returns:
        FixedPoint object with Wilson-Fisher coordinates and eigenvalues
    """
    if d >= 4:
        raise ValueError(f"Wilson-Fisher FP only exists for d < 4, got d={d}")

    epsilon = 4.0 - d
    K_d = phase_space_factor(d)

    # Fixed point coordinates to O(epsilon)
    r_star = -epsilon * K_d * Lambda**2 / 6.0
    u_star = epsilon / (36.0 * K_d * Lambda**(d-4))

    # Eigenvalues at WF FP
    # y_t = 2 - epsilon/3 + O(epsilon^2)
    # y_h = (d+2-eta)/2, but eta = O(epsilon^2)
    y_t = 2.0 - epsilon / 3.0
    y_h = (d + 2.0) / 2.0  # Leading order, ignoring eta

    eigenvalues = np.array([y_t, y_h])

    return FixedPoint(
        fp_type='wilson_fisher',
        r=r_star,
        u=u_star,
        d=d,
        eigenvalues=eigenvalues,
        stability='stable'
    )


def find_all_fixed_points(d: float, Lambda: float = 1.0) -> List[FixedPoint]:
    """
    Find all fixed points for a given dimension

    Args:
        d: Spatial dimension
        Lambda: UV cutoff

    Returns:
        List of FixedPoint objects
    """
    fixed_points = []

    # Gaussian FP (always exists)
    fixed_points.append(find_gaussian_fixed_point(d))

    # Wilson-Fisher FP (only for d < 4)
    if d < 4:
        fixed_points.append(find_wilson_fisher_fixed_point(d, Lambda))

    return fixed_points


# -----------------------------------------------------------------------------
# Stability Matrix and Eigenvalues
# -----------------------------------------------------------------------------

def stability_matrix(r: float, u: float, d: float, Lambda: float = 1.0) -> np.ndarray:
    """
    Compute the stability matrix at point (r, u)

    Args:
        r: r coordinate
        u: u coordinate
        d: Spatial dimension
        Lambda: UV cutoff

    Returns:
        2x2 stability matrix
    """
    K_d = phase_space_factor(d)

    # Partial derivatives
    dr_dlr = 2.0
    dr_dlu = 12.0 * K_d * Lambda**d

    du_dlr = 0.0
    du_dlu = (4.0 - d) - 72.0 * u * K_d * Lambda**d

    return np.array([[dr_dlr, dr_dlu],
                     [du_dlr, du_dlu]])


def compute_eigenvalues(r: float, u: float, d: float, Lambda: float = 1.0) -> np.ndarray:
    """
    Compute eigenvalues of stability matrix at (r, u)

    Args:
        r, u: Coordinates
        d: Dimension
        Lambda: UV cutoff

    Returns:
        Array of eigenvalues [y1, y2]
    """
    M = stability_matrix(r, u, d, Lambda)
    return np.linalg.eigvals(M)


# -----------------------------------------------------------------------------
# Basin of Attraction Analysis
# -----------------------------------------------------------------------------

def classify_flow_destination(
    r0: float,
    u0: float,
    d: float,
    l_max: float = 20.0,
    Lambda: float = 1.0
) -> str:
    """
    Classify which fixed point the flow approaches

    Args:
        r0, u0: Initial conditions
        d: Dimension
        l_max: Maximum RG scale
        Lambda: UV cutoff

    Returns:
        'ht', 'lt', 'gaussian', 'wilson_fisher', or 'unknown'
    """
    l_vals, r_vals, u_vals = integrate_flow(r0, u0, d, l_max, Lambda=Lambda)

    # Check final values
    r_final = r_vals[-1]
    u_final = u_vals[-1]

    # Determine destination based on final values and direction
    if u_final < 1e-10:  # u flowed to zero
        if r_final > 1.0:
            return 'ht'  # r → +∞
        elif r_final < -1.0:
            return 'lt'  # r → -∞
        else:
            return 'gaussian'  # Near origin
    elif d < 4 and u_final > 0:
        return 'wilson_fisher'
    else:
        return 'unknown'


def compute_basins(
    d: float,
    r_range: Tuple[float, float],
    u_range: Tuple[float, float],
    n_r: int = 20,
    n_u: int = 20,
    Lambda: float = 1.0
) -> Dict[str, np.ndarray]:
    """
    Compute basins of attraction in (r, u) space

    Args:
        d: Dimension
        r_range: (r_min, r_max)
        u_range: (u_min, u_max)
        n_r, n_u: Grid resolution
        Lambda: UV cutoff

    Returns:
        Dictionary with 'r', 'u', 'destination' arrays
    """
    r_vals = np.linspace(r_range[0], r_range[1], n_r)
    u_vals = np.linspace(u_range[0], u_range[1], n_u)

    destinations = np.zeros((n_r, n_u), dtype=object)

    for i, r0 in enumerate(r_vals):
        for j, u0 in enumerate(u_vals):
            dest = classify_flow_destination(r0, u0, d, Lambda=Lambda)
            destinations[i, j] = dest

    return {
        'r': r_vals,
        'u': u_vals,
        'destination': destinations
    }


# -----------------------------------------------------------------------------
# Critical Exponents
# -----------------------------------------------------------------------------

def critical_exponents_epsilon(d: float, order: int = 1) -> Dict[str, float]:
    """
    Compute critical exponents via epsilon expansion

    Args:
        d: Dimension (must be ≤ 4)
        order: 1 for O(ε), 2 for O(ε²)

    Returns:
        Dictionary with exponents nu, beta, gamma, eta
    """
    if d > 4:
        return {
            'nu': 0.5,
            'beta': 0.5,
            'gamma': 1.0,
            'eta': 0.0,
            'method': 'mean-field'
        }

    epsilon = 4.0 - d

    if order == 1:
        nu = 0.5 + epsilon / 12.0
        beta = 0.5 - epsilon / 6.0
        gamma = 1.0 + epsilon / 6.0
        eta = 0.0  # Only appears at O(ε²)

        return {
            'nu': nu,
            'beta': beta,
            'gamma': gamma,
            'eta': eta,
            'epsilon': epsilon,
            'method': 'epsilon_expansion_O1'
        }
    else:
        # O(ε²) results (placeholder for now)
        # From Pelissetto & Vicari (2002) for Ising
        nu = 0.5 + epsilon / 12.0 + epsilon**2 / 144.0
        beta = 0.5 - epsilon / 6.0 - epsilon**2 / 18.0  # Approx
        gamma = 1.0 + epsilon / 6.0 + epsilon**2 * 11.0 / 108.0  # Approx
        eta = epsilon**2 / 54.0  # O(ε²) contribution

        return {
            'nu': nu,
            'beta': beta,
            'gamma': gamma,
            'eta': eta,
            'epsilon': epsilon,
            'method': 'epsilon_expansion_O2'
        }


def critical_exponents_table() -> str:
    """
    Generate markdown table of critical exponents

    Returns:
        Markdown formatted table
    """
    # Mean-field (d ≥ 4)
    mf_exponents = "ν = 1/2, β = 1/2, γ = 1, η = 0"

    # d = 3 (ε = 1)
    d3_exponents = critical_exponents_epsilon(3)
    d3_str = f"ν ≈ {d3_exponents['nu']:.4f}, β ≈ {d3_exponents['beta']:.4f}, " \
               f"γ ≈ {d3_exponents['gamma']:.4f}, η ≈ {d3_exponents['eta']:.4f}"

    # d = 2 (various q)
    d2_exponents = {
        2: "ν = 1, β = 1/8, γ = 7/4, η = 1/4",
        3: "ν = 5/6, β = 1/9, γ = 13/9, η = 4/15",
        4: "ν = 2/3, β = 1/12, γ = 7/6, η = 1/4"
    }

    table = """
## Critical Exponents by Dimension and q

### Mean-Field (d ≥ 4, all q)
| ν | β | γ | η |
|---|---|---|-----|
| 1/2 | 1/2 | 1 | 0 |

### d = 3 (ε = 1)
| ν | β | γ | η |
|-------|-------|-------|-----|
| """ + d3_str + """ |

### d = 2 (Exact Results)
| q | ν | β | γ | η | Transition |
|---|-------|-------|-------|-----|-----------|
| 2 | 1 | 1/8 | 7/4 | 1/4 | 2nd order |
| 3 | 5/6 | 1/9 | 13/9 | 4/15 | 2nd order |
| 4 | 2/3 | 1/12 | 7/6 | 1/4 | Marginal |
| > 4 | - | - | - | - | 1st order |
"""
    return table


def d2_critical_exponents(q: int) -> Dict[str, float]:
    """
    Exact d=2 Potts critical exponents from Baxter/CFT

    Args:
        q: Number of Potts states (≤ 4 for continuous transition)

    Returns:
        Dictionary with exponents or None if first-order
    """
    if q > 4:
        return {'transition': 'first_order'}

    g = 4.0 / np.sqrt(q)

    beta = (g - 2.0) / (12.0 * g)
    nu = np.sqrt(3.0) / (2.0 * np.sqrt(g))
    gamma = (7.0 * g - 12.0) / (6.0 * g)
    eta = (g - 4.0) / (2.0 * g)

    return {
        'q': q,
        'beta': beta,
        'nu': nu,
        'gamma': gamma,
        'eta': eta,
        'transition': 'second_order' if q < 4 else 'marginal'
    }


# -----------------------------------------------------------------------------
# q=4 Threshold Analysis
# -----------------------------------------------------------------------------

def q4_threshold_analysis() -> Dict:
    """
    Analyze the q=4 threshold in d=2

    Returns:
        Dictionary with analysis results
    """
    results = {
        'dimension': 2,
        'threshold_q': 4,
        'below_threshold': {
            'transition': 'second_order',
            'description': 'Continuous phase transition with power-law scaling',
            'agent_implication': 'Gradual consensus formation as T decreases'
        },
        'at_threshold': {
            'transition': 'marginal',
            'description': 'Boundary case, still second-order but with marginal operators',
            'agent_implication': 'Smooth but with critical slowing, near-boundary behavior'
        },
        'above_threshold': {
            'transition': 'first_order',
            'description': 'Discontinuous jump in order parameter, finite correlation length',
            'agent_implication': 'Abrupt consensus formation (tipping point), no warning signs'
        },
        'mechanism': 'Change in CFT central charge at q=4; marginal operator becomes relevant'
    }
    return results


def agent_system_implications() -> Dict:
    """
    Summarize implications for agent systems

    Returns:
        Dictionary with agent system implications
    """
    return {
        'low_diversity': {
            'q_range': 'q ≤ 4',
            'transition_type': 'Second-order',
            'behavior': 'Order parameter grows continuously from zero',
            'practical': 'Predictable consensus formation, early warning via susceptibility',
            'example': 'D_4 (4 diverse) agent systems'
        },
        'high_diversity': {
            'q_range': 'q > 4',
            'transition_type': 'First-order',
            'behavior': 'Order parameter jumps discontinuously at T_c',
            'practical': 'Abrupt consensus, tipping point behavior',
            'example': 'D_8, D_16 (8-16 diverse) agent systems'
        },
        'finite_size_effects': {
            'small_N': 'N < 20: Very rounded transitions, large T_c shifts',
            'medium_N': '20 < N < 100: Moderate rounding, some T_c shift',
            'large_N': 'N > 100: Approaches thermodynamic limit'
        }
    }


# -----------------------------------------------------------------------------
# Universality Check
# -----------------------------------------------------------------------------

def universality_check(
    models: List[Dict],
    d: float,
    tolerance: float = 0.05
) -> Dict:
    """
    Check if different models with same d give same exponents (universality)

    Args:
        models: List of model dicts with 'nu', 'beta', 'gamma', 'eta' keys
        d: Dimension to check
        tolerance: Acceptable relative difference

    Returns:
        Dictionary with check results
    """
    if len(models) < 2:
        return {'status': 'need_more_models', 'message': 'Need at least 2 models'}

    # Compare all pairs
    max_diff = 0.0
    all_close = True

    for i, model1 in enumerate(models):
        for model2 in models[i+1:]:
            for exp in ['nu', 'beta', 'gamma', 'eta']:
                if exp in model1 and exp in model2:
                    diff = abs(model1[exp] - model2[exp])
                    rel_diff = diff / max(abs(model1[exp]), 0.1)
                    max_diff = max(max_diff, rel_diff)
                    if rel_diff > tolerance:
                        all_close = False

    return {
        'dimension': d,
        'n_models': len(models),
        'max_relative_difference': max_diff,
        'universality_confirmed': all_close,
        'tolerance': tolerance
    }


# -----------------------------------------------------------------------------
# Main Analysis Functions
# -----------------------------------------------------------------------------

def analyze_dimension(d: float, Lambda: float = 1.0) -> Dict:
    """
    Complete fixed point analysis for a given dimension

    Args:
        d: Spatial dimension
        Lambda: UV cutoff

    Returns:
        Comprehensive analysis dictionary
    """
    # Find fixed points
    fixed_points = find_all_fixed_points(d, Lambda)

    # Analyze stability
    stability_analysis = {}
    for fp in fixed_points:
        stability_analysis[fp.fp_type] = fp.stability

    # Compute exponents
    if d < 4:
        exponents = critical_exponents_epsilon(d)
    else:
        exponents = critical_exponents_epsilon(d)  # Returns mean-field

    # Basin analysis
    r_range = (-2.0, 2.0)
    u_range = (-0.5, 1.0)
    basins = compute_basins(d, r_range, u_range, Lambda=Lambda)

    return {
        'dimension': d,
        'fixed_points': [
            {
                'type': fp.fp_type,
                'r': fp.r,
                'u': fp.u,
                'eigenvalues': fp.eigenvalues.tolist(),
                'stability': fp.stability
            }
            for fp in fixed_points
        ],
        'critical_exponents': exponents,
        'basins': basins
    }


def generate_comprehensive_report() -> str:
    """
    Generate a comprehensive markdown report of all analyses

    Returns:
        Markdown formatted report
    """
    report_parts = []

    # Header
    report_parts.append("# Fixed Point Analysis Report\n")
    report_parts.append(f"Generated: 2026-03-22\n")

    # Fixed points by dimension
    report_parts.append("## Fixed Points by Dimension\n")

    for d in [2, 3, 4, 5]:
        analysis = analyze_dimension(d)
        report_parts.append(f"\n### d = {d}\n")

        report_parts.append("**Fixed Points:**\n")
        for fp in analysis['fixed_points']:
            report_parts.append(f"- {fp['type']}: r* = {fp['r']:.6g}, u* = {fp['u']:.6g}\n")
            report_parts.append(f"  Stability: {fp['stability']}\n")
            report_parts.append(f"  Eigenvalues: {fp['eigenvalues']}\n")

        report_parts.append("\n**Critical Exponents:**\n")
        exp = analysis['critical_exponents']
        report_parts.append(f"- ν = {exp['nu']:.6f}\n")
        report_parts.append(f"- β = {exp['beta']:.6f}\n")
        report_parts.append(f"- γ = {exp['gamma']:.6f}\n")
        report_parts.append(f"- η = {exp['eta']:.6f}\n")
        report_parts.append(f"Method: {exp['method']}\n")

    # d=2 q-dependence
    report_parts.append("\n## d=2 q-Dependence\n")
    report_parts.append("| q | Transition | β | ν | γ | η |\n")
    report_parts.append("|---|-----------|-----|-----|-----|-----|\n")

    for q in [2, 3, 4]:
        if q == 4:
            exponents = d2_critical_exponents(q)
            report_parts.append(f"| {q} | {exponents['transition']} | {exponents['beta']:.6f} | "
                               f"{exponents['nu']:.6f} | {exponents['gamma']:.6f} | "
                               f"{exponents['eta']:.6f} |\n")
        elif q < 4:
            exponents = d2_critical_exponents(q)
            report_parts.append(f"| {q} | {exponents['transition']} | {exponents['beta']:.6f} | "
                               f"{exponents['nu']:.6f} | {exponents['gamma']:.6f} | "
                               f"{exponents['eta']:.6f} |\n")

    report_parts.append("| > 4 | 1st order | - | - | - | - |\n")

    # q=4 threshold
    report_parts.append("\n## q=4 Threshold Analysis\n")
    q4 = q4_threshold_analysis()
    report_parts.append(f"**Threshold:** q = {q4['threshold_q']} in d = {q4['dimension']}\n\n")
    report_parts.append("### Below Threshold (q ≤ 4)\n")
    report_parts.append(f"- Transition: {q4['below_threshold']['transition']}\n")
    report_parts.append(f"- Description: {q4['below_threshold']['description']}\n")
    report_parts.append(f"- Agent implications: {q4['below_threshold']['agent_implication']}\n\n")

    report_parts.append("### At Threshold (q = 4)\n")
    report_parts.append(f"- Transition: {q4['at_threshold']['transition']}\n")
    report_parts.append(f"- Description: {q4['at_threshold']['description']}\n")
    report_parts.append(f"- Agent implications: {q4['at_threshold']['agent_implication']}\n\n")

    report_parts.append("### Above Threshold (q > 4)\n")
    report_parts.append(f"- Transition: {q4['above_threshold']['transition']}\n")
    report_parts.append(f"- Description: {q4['above_threshold']['description']}\n")
    report_parts.append(f"- Agent implications: {q4['above_threshold']['agent_implication']}\n\n")

    report_parts.append(f"**Mechanism:** {q4['mechanism']}\n")

    # Agent system implications
    report_parts.append("\n## Agent System Implications\n")
    agent = agent_system_implications()
    report_parts.append(f"### Low Diversity (q ≤ 4)\n")
    report_parts.append(f"- Behavior: {agent['low_diversity']['behavior']}\n")
    report_parts.append(f"- Practical: {agent['low_diversity']['practical']}\n")
    report_parts.append(f"- Example: {agent['low_diversity']['example']}\n\n")

    report_parts.append(f"### High Diversity (q > 4)\n")
    report_parts.append(f"- Behavior: {agent['high_diversity']['behavior']}\n")
    report_parts.append(f"- Practical: {agent['high_diversity']['practical']}\n")
    report_parts.append(f"- Example: {agent['high_diversity']['example']}\n\n")

    report_parts.append("### Finite Size Effects\n")
    report_parts.append(f"- Small N: {agent['finite_size_effects']['small_N']}\n")
    report_parts.append(f"- Medium N: {agent['finite_size_effects']['medium_N']}\n")
    report_parts.append(f"- Large N: {agent['finite_size_effects']['large_N']}\n")

    return "".join(report_parts)


# -----------------------------------------------------------------------------
# Command Line Interface
# -----------------------------------------------------------------------------

def main():
    """Main entry point for testing"""
    print("=== Fixed Point Solver ===\n")

    # Test fixed point finding
    print("Fixed points for d=3:")
    for fp in find_all_fixed_points(3):
        print(f"  {fp}")

    print("\nFixed points for d=2:")
    for fp in find_all_fixed_points(2):
        print(f"  {fp}")

    print("\nFixed points for d=4:")
    for fp in find_all_fixed_points(4):
        print(f"  {fp}")

    # Test d=2 exponents
    print("\nd=2 critical exponents:")
    for q in [2, 3, 4]:
        exp = d2_critical_exponents(q)
        if 'transition' in exp:
            print(f"  q={q}: {exp['transition']}")
        else:
            print(f"  q={q}: ν={exp['nu']:.4f}, β={exp['beta']:.4f}, "
                  f"γ={exp['gamma']:.4f}, η={exp['eta']:.4f}")

    # Test q=4 analysis
    print("\nq=4 threshold analysis:")
    q4 = q4_threshold_analysis()
    print(f"  Threshold at q={q4['threshold_q']}")
    print(f"  Below: {q4['below_threshold']['transition']}")
    print(f"  Above: {q4['above_threshold']['transition']}")

    # Generate exponent table
    print("\n" + critical_exponents_table())


if __name__ == "__main__":
    main()
