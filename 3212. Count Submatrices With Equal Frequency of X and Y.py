class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        # map chars to +1, -1, 0
        def val_diff(ch: str) -> int:
            if ch == 'X':
                return 1
            if ch == 'Y':
                return -1
            return 0

        def val_x(ch: str) -> int:
            return 1 if ch == 'X' else 0

        prefDiff = [[0]*(m+1) for _ in range(n+1)]
        prefX    = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                d = val_diff(grid[i][j])
                x = val_x(grid[i][j])

                prefDiff[i+1][j+1] = (prefDiff[i][j+1]
                                      + prefDiff[i+1][j]
                                      - prefDiff[i][j]
                                      + d)
                prefX[i+1][j+1] = (prefX[i][j+1]
                                   + prefX[i+1][j]
                                   - prefX[i][j]
                                   + x)

        ans = 0
        for i in range(n):
            for j in range(m):
                if prefDiff[i+1][j+1] == 0 and prefX[i+1][j+1] >= 1:
                    ans += 1

        return ans
