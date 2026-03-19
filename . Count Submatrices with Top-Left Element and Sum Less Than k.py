class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        pref = [[0]*n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                up = pref[i-1][j] if i > 0 else 0
                left = pref[i][j-1] if j > 0 else 0
                diag = pref[i-1][j-1] if i > 0 and j > 0 else 0

                pref[i][j] = grid[i][j] + up + left - diag

                if pref[i][j] <= k:
                    ans += 1

        return ans