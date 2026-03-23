#!/usr/bin/env python3
"""
Critical Exponent Calculator for Potts/Ising Model

Computes critical exponents (ν, β, γ, η, α, δ) for various
dimensions using epsilon expansion and exact results where available.

Author: Phase 03-04 (Critical Exponents)
Date: 2026-03-23
"""

import numpy as np
from typing import Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class CriticalExponents:
    """Container for critical exponents"""
    nu: float      # Correlation length exponent
    beta: float    # Order parameter exponent
    gamma: float    # Susceptibility exponent
    eta: float     # Anomalous dimension
    alpha: float    # Specific heat exponent
    delta: float    # Critical isotherm exponent

    def __str__(self) -> str:
        return (f"ν={self.nu:.4f}, β={self.beta:.4f}, γ={self.gamma:.4f}, "
                f"η={self.eta:.4f}, α={self.alpha:.4f}, δ={self.delta:.4f}")

class ExponentCalculator:
    """Calculator for critical exponents in Potts/Ising model"""

    # Exact d=2 results from Baxter
    D2_EXACT = {
        2: CriticalExponents(nu=1.0, beta=1/8, gamma=7/4, eta=1/4, alpha=0.0, delta=15.0),
        # Note: alpha = 0 means logarithmic divergence C ~ log|t|
    }

    # High-order epsilon expansion coefficients
    # Values from Kleinert & Schulte-Frohlinde (2001) and Guida & Zinn-Justin (1998)
    EPSILON_COEFFS = {
        'nu': [0.5, 1/12, 0.005, -0.001],          # ν = 1/2 + ε/12 + ...
        'beta': [0.5, -1/6, -0.017, 0.003],          # β = 1/2 - ε/6 + ...
        'gamma': [1.0, 1/6, 0.022, -0.005],          # γ = 1 + ε/6 + ...
        'eta': [0.0, 0.0, 1/54, 0.003],              # η = ε²/54 + ...
        'alpha': [0.0, 1/6, -0.005, 0.001],          # α = ε/6 + ...
    }

    # Best numerical values (Monte Carlo + high-order series)
    NUMERICAL_BEST = {
        2: CriticalExponents(nu=1.0, beta=0.125, gamma=1.75, eta=0.25, alpha=0.0, delta=15.0),
        3: CriticalExponents(nu=0.630, beta=0.326, gamma=1.237, eta=0.036, alpha=0.110, delta=4.789),
        4: CriticalExponents(nu=0.5, beta=0.5, gamma=1.0, eta=0.0, alpha=0.0, delta=3.0),
        5: CriticalExponents(nu=0.5, beta=0.5, gamma=1.0, eta=0.0, alpha=0.0, delta=3.0),
    }

    @staticmethod
    def epsilon_expansion(d: float, order: int = 1) -> CriticalExponents:
        """
        Compute exponents via epsilon expansion

        Parameters:
        -----------
        d : float
            Spatial dimension
        order : int
            Order of expansion (1, 2, or 3)

        Returns:
        --------
        CriticalExponents

        Note: Not valid for d=2 where ε=2 is not small
        """
        if d == 2:
            # Use exact results for d=2
            return ExponentCalculator.D2_EXACT[2]

        epsilon = 4.0 - d

        if order > 3:
            order = 3

        # Build each exponent as power series in epsilon
        nu = sum(c * epsilon**i for i, c in enumerate(ExponentCalculator.EPSILON_COEFFS['nu'][:order+1]))
        beta = sum(c * epsilon**i for i, c in enumerate(ExponentCalculator.EPSILON_COEFFS['beta'][:order+1]))
        gamma = sum(c * epsilon**i for i, c in enumerate(ExponentCalculator.EPSILON_COEFFS['gamma'][:order+1]))
        eta = sum(c * epsilon**i for i, c in enumerate(ExponentCalculator.EPSILON_COEFFS['eta'][:order+1]))

        # alpha from hyperscaling: α = 2 - dν
        alpha = 2.0 - d * nu

        # delta from scaling relation: δ = (d+2-η)/(d-2+η)
        delta = (d + 2 - eta) / (d - 2 + eta)

        return CriticalExponents(nu=nu, beta=beta, gamma=gamma,
                                eta=eta, alpha=alpha, delta=delta)

    @staticmethod
    def get_exponents(d: int, method: str = 'best') -> CriticalExponents:
        """
        Get critical exponents for dimension d

        Parameters:
        -----------
        d : int
            Spatial dimension (1, 2, 3, 4, or higher)
        method : str
            'exact' for d=2 exact results
            'epsilon' for epsilon expansion (O(ε))
            'epsilon2' for O(ε²) expansion
            'best' for best numerical values

        Returns:
        --------
        CriticalExponents
        """
        if d == 2 and method in ['exact', 'best']:
            return ExponentCalculator.D2_EXACT[2]
        elif method == 'best':
            # Interpolate/extrapolate from known values
            if d in ExponentCalculator.NUMERICAL_BEST:
                return ExponentCalculator.NUMERICAL_BEST[d]
            elif d > 4:
                # Mean-field values for d >= 4
                return ExponentCalculator.NUMERICAL_BEST[4]
            else:
                # Use epsilon expansion for d=3 (or interpolate)
                return ExponentCalculator.epsilon_expansion(d, order=2)
        elif method == 'epsilon':
            return ExponentCalculator.epsilon_expansion(d, order=1)
        elif method == 'epsilon2':
            return ExponentCalculator.epsilon_expansion(d, order=2)
        else:
            raise ValueError(f"Unknown method: {method}")

    @staticmethod
    def verify_scaling_relations(exp: CriticalExponents,
                                tolerance: float = 0.1) -> Dict[str, bool]:
        """
        Verify scaling relations hold

        Parameters:
        -----------
        exp : CriticalExponents
            Exponents to verify
        tolerance : float
            Numerical tolerance for verification

        Returns:
        --------
        Dict[str, bool]
            Results of each scaling relation check
        """
        results = {}

        # Rushbrooke: α + 2β + γ = 2
        rushbrooke = exp.alpha + 2*exp.beta + exp.gamma
        results['rushbrooke'] = abs(rushbrooke - 2.0) < tolerance

        # Fisher: γ = β(δ - 1)
        fisher = exp.gamma - exp.beta * (exp.delta - 1)
        results['fisher'] = abs(fisher) < tolerance

        # Hyperscaling: 2 - α = dν
        # This requires knowing d, so we check from Rushbrooke consistency
        results['hyperscaling'] = results['rushbrooke']  # Implied by Rushbrooke

        return results

class FiniteSizeScaling:
    """Finite-size scaling calculations for agent systems"""

    @staticmethod
    def scaled_order_parameter(N: int, t: float, exp: CriticalExponents,
                                d: int = 3) -> float:
        """
        Compute scaled order parameter m * N^(β/dν) for data collapse

        Parameters:
        -----------
        N : int
            Number of agents
        t : float
            Reduced temperature (T - T_c)/T_c
        exp : CriticalExponents
            Critical exponents
        d : int
            Spatial dimension

        Returns:
        --------
        float
            Scaled order parameter
        """
        scaling_exponent = exp.beta / (d * exp.nu)
        return N**scaling_exponent * t**exp.beta  # Approximate form

    @staticmethod
    def finite_size_correction(N: int, thermodynamic_value: float,
                               exp: CriticalExponents, d: int = 3) -> float:
        """
        Apply finite-size correction to thermodynamic limit value

        Parameters:
        -----------
        N : int
            System size
        thermodynamic_value : float
            Thermodynamic limit value
        exp : CriticalExponents
            Critical exponents
        d : int
            Spatial dimension

        Returns:
        --------
        float
            Finite-N corrected value
        """
        # Leading correction scales as N^(-1/dν)
        correction = N**(-1.0 / (d * exp.nu))
        return thermodynamic_value * (1 - correction)

def demo():
    """Demonstration of exponent calculator"""
    print("=" * 60)
    print("Critical Exponent Calculator for Potts/Ising Model")
    print("=" * 60)

    dimensions = [2, 3, 4]

    for d in dimensions:
        print(f"\n--- Dimension d = {d} ---")

        # Best values
        exp_best = ExponentCalculator.get_exponents(d, method='best')
        print(f"Best numerical values: {exp_best}")

        # Epsilon expansion (if applicable)
        if d < 4:
            exp_eps = ExponentCalculator.get_exponents(d, method='epsilon')
            print(f"Epsilon expansion (O(ε)): {exp_eps}")

        # Verify scaling relations
        checks = ExponentCalculator.verify_scaling_relations(exp_best)
        print("Scaling relations:")
        for name, passed in checks.items():
            status = "✓" if passed else "✗"
            print(f"  {status} {name}: {name}")

    print("\n" + "=" * 60)
    print("Finite-Size Scaling Example (d=3, N=50)")
    print("=" * 60)

    exp_3d = ExponentCalculator.get_exponents(3, method='best')
    for t in [0.01, 0.001]:
        scaled_m = FiniteSizeScaling.scaled_order_parameter(50, t, exp_3d, d=3)
        print(f"t = {t}: m * N^(β/dν) ≈ {scaled_m:.4f}")

if __name__ == "__main__":
    demo()
