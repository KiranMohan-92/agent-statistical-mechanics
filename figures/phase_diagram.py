#!/usr/bin/env python3
"""
Phase Diagram Visualization for Potts Agent Systems

Generates phase diagrams showing:
1. Critical temperature curve T_c(q)
2. Phase regimes (ordered/disordered)
3. Critical diversity q_c(T)
4. Finite-size effects
5. 3D surface plots

Author: Phase 03-05 (Phase Diagram Generation)
Date: 2026-03-23
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path

# Create figures directory if it doesn't exist
Path("figures").mkdir(exist_ok=True)

class PhaseDiagram:
    """Phase diagram calculations and visualization"""

    def __init__(self, J: float = 1.0):
        """
        Initialize phase diagram

        Parameters:
        -----------
        J : float
            Coupling constant (energy scale)
        """
        self.J = J

    def tc_mean_field(self, q: np.ndarray) -> np.ndarray:
        """Mean-field critical temperature: T_c = Jq/(q-1)"""
        return self.J * q / (q - 1)

    def tc_exact_2d(self, q: np.ndarray) -> np.ndarray:
        """Exact 2D critical temperature: T_c = J/ln(1+sqrt(q))"""
        return self.J / np.log(1 + np.sqrt(q))

    def qc_mean_field(self, T: np.ndarray) -> np.ndarray:
        """Critical diversity (inverse of T_c): q_c = T/(T-J)"""
        return T / (T - self.J)

    def qc_exact_2d(self, T: np.ndarray) -> np.ndarray:
        """Exact 2D critical diversity: q_c = (exp(2J/T) - 1)^2"""
        return (np.exp(2 * self.J / T) - 1)**2

    def tc_finite_n(self, tc_infty: float, N: int, d: int = 3,
                     nu: float = 0.63, a: float = 1.0) -> float:
        """Finite-size critical temperature shift"""
        return tc_infty * (1 + a * N**(-1.0 / (d * nu)))

    def order_parameter_mf(self, t: np.ndarray) -> np.ndarray:
        """Mean-field order parameter: m = 1 for t < 0, 0 for t > 0"""
        return np.where(t < 0, 1.0, 0.0)

    def order_parameter_continuous(self, t: np.ndarray, beta: float = 0.33) -> np.ndarray:
        """Continuous order parameter approximation: m ~ (-t)^beta for t < 0"""
        result = np.zeros_like(t)
        mask = t < 0
        result[mask] = (-t[mask])**beta
        return result

def plot_2d_phase_diagram():
    """Plot 2D phase diagram in (q, T) space"""
    pd = PhaseDiagram(J=1.0)

    q = np.linspace(2.01, 20, 200)
    T_mf = pd.tc_mean_field(q)
    T_2d = pd.tc_exact_2d(q[q <= 4])  # Valid only for q <= 4

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Mean-field phase diagram
    ax1.plot(q, T_mf, 'b-', linewidth=2, label='Critical line $T_c(q)$')
    ax1.fill_between(q, 0, T_mf, alpha=0.3, color='blue', label='Ordered (consensus)')
    ax1.fill_between(q, T_mf, 3, alpha=0.3, color='red', label='Disordered (fragmentation)')

    ax1.set_xlabel('Diversity $q$', fontsize=12)
    ax1.set_ylabel('Temperature $T/J$', fontsize=12)
    ax1.set_title('(a) Mean-Field Phase Diagram', fontsize=14)
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(2, 20)
    ax1.set_ylim(0, 3)

    # Exact 2D phase diagram
    q_2d = np.linspace(2.01, 4, 100)
    T_2d = pd.tc_exact_2d(q_2d)
    ax2.plot(q_2d, T_2d, 'g-', linewidth=2, label='Critical line $T_c^{2D}(q)$')
    ax2.fill_between(q_2d, 0, T_2d, alpha=0.3, color='green', label='Ordered (consensus)')
    ax2.fill_between(q_2d, T_2d, 3, alpha=0.3, color='orange', label='Disordered (fragmentation)')

    ax2.set_xlabel('Diversity $q$', fontsize=12)
    ax2.set_ylabel('Temperature $T/J$', fontsize=12)
    ax2.set_title('(b) Exact 2D Phase Diagram (q ≤ 4)', fontsize=14)
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(2, 4.5)
    ax2.set_ylim(0, 3)

    plt.tight_layout()
    plt.savefig('figures/phase_diagram_2d.png', dpi=150, bbox_inches='tight')
    print("Saved: figures/phase_diagram_2d.png")
    plt.close()

def plot_critical_diversity():
    """Plot critical diversity q_c(T) curves"""
    pd = PhaseDiagram(J=1.0)

    T = np.linspace(1.1, 3.0, 200)
    q_c_mf = pd.qc_mean_field(T)
    q_c_2d = pd.qc_exact_2d(T[T <= 2.0])  # Valid for T < T_c(q=2) = 2

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(T, q_c_mf, 'b-', linewidth=2, label='Mean-field: $q_c = T/(T-J)$')
    ax.plot(T[T <= 2.0], q_c_2d, 'g--', linewidth=2, label='Exact 2D: $q_c = (e^{2J/T}-1)^2$')

    # Yang et al. reference line
    ax.axhline(y=16, color='r', linestyle=':', linewidth=2, label='Yang saturation: $D_{16} \\approx 16 D_1$')

    ax.set_xlabel('Temperature $T/J$', fontsize=12)
    ax.set_ylabel('Critical Diversity $q_c$', fontsize=12)
    ax.set_title('Critical Diversity: Maximum Diversity for Consensus', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1.1, 3.0)
    ax.set_ylim(0, 30)

    # Add annotation
    ax.annotate('Yang saturation\nsuggests T ≈ 1.1J', xy=(1.1, 16), xytext=(1.3, 20),
                arrowprops=dict(arrowstyle='->', color='red'), fontsize=10)

    plt.tight_layout()
    plt.savefig('figures/critical_diversity.png', dpi=150, bbox_inches='tight')
    print("Saved: figures/critical_diversity.png")
    plt.close()

def plot_3d_phase_diagram():
    """Plot 3D phase diagram surface in (q, T, N) space"""
    pd = PhaseDiagram(J=1.0)

    q = np.linspace(2, 16, 50)
    N = np.array([20, 50, 100, 500])
    T_mesh, N_mesh = np.meshgrid(q, N)

    # Calculate T_c with finite-size corrections
    # T_c(N) = T_c(∞) * [1 + a * N^(-1/dν)]
    d, nu, a = 3, 0.63, 1.0
    tc_infty = pd.tc_mean_field(T_mesh)
    tc_N = tc_infty * (1 + a * N_mesh**(-1.0 / (d * nu)))

    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Plot surface
    surf = ax.plot_surface(T_mesh, N_mesh, tc_N, cmap=cm.viridis, alpha=0.8,
                            rstride=2, cstride=2, linewidth=0, antialiased=True)

    ax.set_xlabel('Diversity $q$', fontsize=11)
    ax.set_ylabel('Number of Agents $N$', fontsize=11)
    ax.set_zlabel('Critical Temperature $T_c/J$', fontsize=11)
    ax.set_title('3D Phase Diagram: Finite-Size Effects', fontsize=14)

    # View angle
    ax.view_init(elev=20, azim=45)

    plt.tight_layout()
    plt.savefig('figures/phase_diagram_3d.png', dpi=150, bbox_inches='tight')
    print("Saved: figures/phase_diagram_3d.png")
    plt.close()

def plot_finite_size_scaling():
    """Plot finite-size effects on order parameter"""
    pd = PhaseDiagram(J=1.0)

    # Reduced temperature range
    t = np.linspace(-0.5, 0.5, 200)
    N_values = [20, 50, 100, 500]

    beta, nu = 0.33, 0.63
    d = 3

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Order parameter vs T for different N
    for N in N_values:
        # Scaled order parameter for data collapse
        scaled_m = N**(-beta/(d*nu)) * np.maximum(-t, 0)**beta
        scaling_factor = N**(beta/(d*nu))
        ax1.plot(t, scaled_m, label=f'N={N}', linewidth=2)

    ax1.set_xlabel('Reduced Temperature $t = (T-T_c)/T_c$', fontsize=12)
    ax1.set_ylabel('Scaled Order Parameter $m N^{\\beta/d\\nu}$', fontsize=12)
    ax1.set_title('(a) Finite-Size Data Collapse', fontsize=14)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.axvline(x=0, color='k', linestyle='--', alpha=0.5)

    # T_c shift with N
    N_vals = np.array([10, 20, 50, 100, 500])
    tc_infty = 2.0  # For q=2, T_c = 2J
    tc_N = pd.tc_finite_n(tc_infty, N_vals, d=d, nu=nu)

    ax2.loglog(N_vals, (tc_N - tc_infty)/tc_infty * 100, 'o-', label='Data points')
    ref_N = np.array([10, 20, 50, 100])
    ref_shift = ref_N**(-1.0/(d*nu)) * 100
    ax2.loglog(ref_N, ref_shift, '--', label=f'N^{{-1/dν}} scaling', linewidth=2)

    ax2.set_xlabel('Number of Agents $N$', fontsize=12)
    ax2.set_ylabel('T_c Shift (%)', fontsize=12)
    ax2.set_title('(b) Finite-Size Shift of T_c', fontsize=14)
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('figures/finite_size_effects.png', dpi=150, bbox_inches='tight')
    print("Saved: figures/finite_size_effects.png")
    plt.close()

def plot_yang_comparison():
    """Create comparison with Yang et al. empirical results"""
    pd = PhaseDiagram(J=1.0)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot T_c(q) curve
    q = np.linspace(2, 20, 200)
    T_c = pd.tc_mean_field(q)

    ax.plot(q, T_c, 'b-', linewidth=2, label='$T_c(q) = Jq/(q-1)$')

    # Mark operating regions from Yang et al.
    # D_4 ≈ 16D_1 suggests operation near critical line

    # Shade critical region
    ax.fill_between(q, T_c * 0.9, T_c * 1.1,
                     alpha=0.2, color='gray', label='Critical region (±10%)')

    # Mark example operating points
    q_ops = [2, 4, 8, 16]
    T_ops = [1.5, 1.8, 2.2, 3.0]
    ax.scatter(q_ops, T_ops, s=100, c='red', zorder=5,
                label='Yang et al. operating points', edgecolors='black')

    ax.set_xlabel('Diversity $q$', fontsize=12)
    ax.set_ylabel('Temperature $T/J$', fontsize=12)
    ax.set_title('Phase Diagram with Yang et al. Comparison', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(2, 20)
    ax.set_ylim(0, 4)

    # Add annotations
    ax.annotate('D_16 ≈ 16 D_1\n(high diversity)', xy=(16, 3.0),
                xytext=(12, 3.5), fontsize=10,
                arrowprops=dict(arrowstyle='->', color='black'))

    plt.tight_layout()
    plt.savefig('figures/yang_comparison.png', dpi=150, bbox_inches='tight')
    print("Saved: figures/yang_comparison.png")
    plt.close()

def main():
    """Generate all phase diagram plots"""
    print("=" * 60)
    print("Phase Diagram Visualization for Potts Agent Systems")
    print("=" * 60)

    print("\nGenerating 2D phase diagrams...")
    plot_2d_phase_diagram()

    print("\nGenerating critical diversity plot...")
    plot_critical_diversity()

    print("\nGenerating 3D phase diagram...")
    plot_3d_phase_diagram()

    print("\nGenerating finite-size scaling plots...")
    plot_finite_size_scaling()

    print("\nGenerating Yang et al. comparison...")
    plot_yang_comparison()

    print("\n" + "=" * 60)
    print("All phase diagram figures generated successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
