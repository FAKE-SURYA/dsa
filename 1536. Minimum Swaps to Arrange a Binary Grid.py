from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 1. compute last 1 index for each row
        last = []
        for row in grid:
            pos = -1
            for j in range(n - 1, -1, -1):
                if row[j] == 1:
                    pos = j
                    break
            last.append(pos)

        swaps = 0

        # 2. for each row position i, find suitable row j >= i
        for i in range(n):
            target = i    # we need last_one <= i
            j = i
            # find first row j whose last 1 is at col <= i
            while j < n and last[j] > target:
                j += 1
            if j == n:
                return -1  # impossible

            # 3. bubble row j up to i
            while j > i:
                last[j], last[j - 1] = last[j - 1], last[j]
                swaps += 1
                j -= 1

        return swaps
