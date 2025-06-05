"""
Implementation of the Emergency Service Location Problem with Ring Roads
as described in the paper.
"""

import numpy as np

class RingRoadOptimizer:
    def __init__(self, m, n, d, a, b):
        """
        Initialize the optimization problem
        
        Args:
            m (int): Number of callers (locations)
            n (int): Number of service centers
            d (list): Circumferences of ring roads [d_j for j in N]
            a (numpy.ndarray): Distance matrix (m x n) from callers to exits A_j
            b (numpy.ndarray): Distance matrix (m x n) from callers to exits B_j
        """
        self.m = m
        self.n = n
        self.d = np.array(d)
        self.a = np.array(a)
        self.b = np.array(b)
        
        # Validate inputs
        assert a.shape == (m, n), "Distance matrix a has incorrect shape"
        assert b.shape == (m, n), "Distance matrix b has incorrect shape"
        assert len(d) == n, "Circumference list d has incorrect length"
        
        # Precompute δ_ij = min(a_ij, b_ij)
        self.delta = np.minimum(a, b)
        
    def compute_alpha_tilde(self):
        """
        Compute α̃ as per Lemma 1
        
        Returns:
            float: α̃ = max_i(min_j δ_ij)
        """
        alpha_tilde_i = np.min(self.delta, axis=1)
        return np.max(alpha_tilde_i)
    
    def compute_rho_ij(self, alpha):
        """
        Compute ρ_ij = max_x∈[0,d_j] r_ij(x)
        
        Args:
            alpha (float): Distance threshold
            
        Returns:
            numpy.ndarray: Matrix of ρ_ij values (m x n)
        """
        return np.maximum(self.a, self.b)
    
    def compute_boundary_values(self, alpha):
        """
        Compute boundary values μ*_ij, μ**_ij, ν*_ij, ν**_ij
        
        Args:
            alpha (float): Distance threshold
            
        Returns:
            tuple: (μ*_ij, μ**_ij, ν*_ij, ν**_ij) matrices
        """
        mu_star = alpha - self.a
        mu_double_star = self.d - alpha + self.a
        nu_star = self.d/2 + self.b - alpha
        nu_double_star = alpha + self.d/2 - self.b
        return mu_star, mu_double_star, nu_star, nu_double_star
    
    def compute_V_ij(self, alpha):
        """
        Compute the feasible region V_ij(α) for each i, j
        
        Args:
            alpha (float): Distance threshold
            
        Returns:
            list: List of tuples [(i, j, V_ij)] where V_ij is the feasible region
        """
        feasible_regions = []
        
        # Compute boundary values
        mu_star, mu_double_star, nu_star, nu_double_star = self.compute_boundary_values(alpha)
        
        for i in range(self.m):
            for j in range(self.n):
                if alpha < self.delta[i, j]:
                    feasible_regions.append((i, j, []))
                elif alpha == self.delta[i, j]:
                    feasible_regions.append((i, j, [self.d[j]/2]))
                else:
                    # Determine which case we're in
                    if self.a[i, j] > self.b[i, j]:
                        if alpha < self.a[i, j]:
                            feasible_regions.append((
                                i, j, 
                                [self.d[j]/2 - (alpha - self.b[i, j]), 
                                 self.d[j]/2 + (alpha - self.b[i, j])]
                            ))
                        elif alpha == self.a[i, j]:
                            feasible_regions.append((
                                i, j, 
                                [0] + 
                                [self.d[j]/2 - (alpha - self.b[i, j]), 
                                 self.d[j]/2 + (alpha - self.b[i, j])]
                            ))
                        else:
                            feasible_regions.append((
                                i, j, 
                                [0, alpha - self.a[i, j]] + 
                                [self.d[j]/2 - (alpha - self.b[i, j]), 
                                 self.d[j]/2 + (alpha - self.b[i, j])] + 
                                [self.d[j] - (alpha - self.a[i, j]), self.d[j]]
                            ))
                    else:
                        # Case when b_ij >= a_ij
                        feasible_regions.append((
                            i, j, 
                            [0, self.d[j]]
                        ))
        
        return feasible_regions
    
    def compute_optimal_positions(self, alpha=None):
        """
        Compute the optimal positions for service centers
        
        Args:
            alpha (float, optional): Distance threshold. If None, uses α̃
            
        Returns:
            tuple: (alpha_opt, optimal_positions)
                alpha_opt: Optimal alpha value
                optimal_positions: List of optimal positions for each service center
        """
        if alpha is None:
            alpha = self.compute_alpha_tilde()
            
        # Check if alpha is feasible
        if alpha < self.compute_alpha_tilde():
            raise ValueError(f"Infeasible: α must be at least {self.compute_alpha_tilde()}")
            
        # Compute feasible regions
        V_ij = self.compute_V_ij(alpha)
        
        # Initialize optimal positions
        optimal_positions = []
        
        for j in range(self.n):
            # Find all i such that V_ij is non-empty
            P_j = [i for i in range(self.m) if any(
                (i == idx[0] and j == idx[1]) and len(idx[2]) > 0 
                for idx in V_ij
            )]
            
            if P_j:
                # Compute intersection of all V_ij for this j
                V_j = np.array([idx[2] for idx in V_ij if idx[0] in P_j and idx[1] == j])
                if V_j.size > 0:
                    # Take the intersection of all intervals
                    optimal_positions.append(np.mean(V_j))
                else:
                    optimal_positions.append(self.d[j]/2)
            else:
                # If no feasible region, place at any position
                optimal_positions.append(self.d[j]/2)
                
        return alpha, optimal_positions

def main():
    # Example from the paper
    m = 5  # neighborhoods
    n = 4  # service centers
    d = [22, 22, 22, 16]  # circumferences
    
    # Distance matrices a and b
    a = np.array([
        [3, 9, 6, 3],
        [4, 8, 7, 5],
        [6, 6, 9, 7],
        [7, 5, 3, 9],
        [8, 3, 5, 8]
    ])
    
    b = np.array([
        [3, 10, 6, 5],
        [6, 9, 8, 6],
        [7, 7, 10, 8],
        [7, 6, 2, 10],
        [8, 3, 4, 9]
    ])
    
    # Create optimizer
    optimizer = RingRoadOptimizer(m, n, d, a, b)
    
    # Scenario 1: No threshold α specified
    print("\nScenario 1: No threshold α specified")
    alpha_opt, positions = optimizer.compute_optimal_positions()
    print(f"Optimal α: {alpha_opt}")
    print(f"Optimal positions: {positions}")
    
    # Scenario 2: α = 8
    print("\nScenario 2: α = 8")
    try:
        alpha_opt, positions = optimizer.compute_optimal_positions(alpha=8)
        print(f"Optimal positions: {positions}")
    except ValueError as e:
        print(e)
    
    # Scenario 3: α = 5
    print("\nScenario 3: α = 5")
    try:
        alpha_opt, positions = optimizer.compute_optimal_positions(alpha=5)
        print(f"Optimal positions: {positions}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()