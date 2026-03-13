from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Helper: for a given time T, can we remove at least mountainHeight?
        def can(T: int) -> bool:
            total = 0
            for w in workerTimes:
                # Find max x such that w * x * (x + 1) / 2 <= T
                lo, hi = 0, mountainHeight  # no worker will remove more than mountainHeight
                while lo <= hi:
                    mid = (lo + hi) // 2
                    # use <= to avoid float
                    if w * mid * (mid + 1) // 2 <= T:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                # hi is the largest valid x
                total += hi
                if total >= mountainHeight:
                    return True
            return total >= mountainHeight

        # Binary search on answer time
        left, right = 0, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
