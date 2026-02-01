import math
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        
        # 1. Coordinate Compression
        # We need to process values in order, but they can be large.
        # Compress them to range [0, unique_count-1]
        unique_vals = sorted(list(set(val for row in grid for val in row)))
        val_map = {val: i for i, val in enumerate(unique_vals)}
        num_unique = len(unique_vals)
        
        # Create a compressed grid for fast rank lookups
        comp_grid = [[val_map[grid[r][c]] for c in range(C)] for r in range(R)]

        # dp[r][c] stores the min cost to reach cell (r, c)
        dp = [[math.inf] * C for _ in range(R)]
        
        # CORRECTION 1: Base case starts at 0 (start cell value is ignored)
        dp[0][0] = 0
        
        # Helper to propagate normal moves (Right/Down)
        def propagate(current_dp):
            for r in range(R):
                for c in range(C):
                    if r == 0 and c == 0: continue
                    
                    min_prev = math.inf
                    if r > 0: min_prev = min(min_prev, current_dp[r-1][c])
                    if c > 0: min_prev = min(min_prev, current_dp[r][c-1])
                    
                    if min_prev != math.inf:
                        # Normal move adds the destination cell's value
                        current_dp[r][c] = min(current_dp[r][c], min_prev + grid[r][c])

        # Initial pass (k=0)
        propagate(dp)
        
        for _ in range(k):
            next_dp = [row[:] for row in dp]
            
            # --- Teleportation Logic ---
            # We can teleport FROM (r,c) TO (x,y) if grid[x][y] <= grid[r][c].
            # This is equivalent to: To reach target (x,y), we need a source with val >= grid[x][y].
            
            # A. Find min cost for each value rank in the current DP state
            min_cost_by_rank = [math.inf] * num_unique
            for r in range(R):
                for c in range(C):
                    rank = comp_grid[r][c]
                    min_cost_by_rank[rank] = min(min_cost_by_rank[rank], dp[r][c])
            
            # B. Compute Suffix Minimums
            # suffix_min[v] = min cost among all sources with rank >= v
            suffix_min = [math.inf] * num_unique
            running_min = math.inf
            for rank in range(num_unique - 1, -1, -1):
                running_min = min(running_min, min_cost_by_rank[rank])
                suffix_min[rank] = running_min
                
            # C. Apply Teleportation
            for r in range(R):
                for c in range(C):
                    rank = comp_grid[r][c]
                    best_source_cost = suffix_min[rank]
                    
                    if best_source_cost != math.inf:
                        # CORRECTION 2: Teleport cost is exactly 0. 
                        # We do NOT add grid[r][c]. The new cost is just the source cost.
                        next_dp[r][c] = min(next_dp[r][c], best_source_cost)
            
            # D. Propagate normal moves after teleporting
            propagate(next_dp)
            
            dp = next_dp

        return dp[R-1][C-1]