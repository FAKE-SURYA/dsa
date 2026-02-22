class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        ans = 0
        for i in range(32):
            if (n>>i) & 1:
                if last >= 0:
                    ans = max(ans, i-last)
                last = i
        return ans