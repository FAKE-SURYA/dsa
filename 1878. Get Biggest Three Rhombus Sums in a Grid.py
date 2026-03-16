class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        vals = set()

        for i in range(m):
            for j in range(n):
                max_k = min(i, m - 1 - i, j, n - 1 - j)
                for k in range(max_k + 1):
                    if k == 0:
                        s = grid[i][j]
                    else:
                        s = 0
                        # top -> right
                        for d in range(k):
                            s += grid[i - k + d][j + d]
                        # right -> bottom
                        for d in range(k):
                            s += grid[i + d][j + k - d]
                        # bottom -> left
                        for d in range(k):
                            s += grid[i + k - d][j - d]
                        # left -> top
                        for d in range(k):
                            s += grid[i - d][j - k + d]
                    vals.add(s)

        ans = sorted(vals, reverse=True)
        return ans[:3]
