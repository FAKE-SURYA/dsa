class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s

        # build alternating patterns for length 2n
        alt1 = []
        alt2 = []
        for i in range(2 * n):
            if i % 2 == 0:
                alt1.append('0')
                alt2.append('1')
            else:
                alt1.append('1')
                alt2.append('0')
        alt1 = ''.join(alt1)
        alt2 = ''.join(alt2)

        diff1 = diff2 = 0
        ans = n  # max flips can't exceed n

        left = 0
        for right in range(2 * n):
            # include right in window
            if t[right] != alt1[right]:
                diff1 += 1
            if t[right] != alt2[right]:
                diff2 += 1

            # shrink if window size > n
            if right - left + 1 > n:
                if t[left] != alt1[left]:
                    diff1 -= 1
                if t[left] != alt2[left]:
                    diff2 -= 1
                left += 1

            # when window size == n, update answer
            if right - left + 1 == n:
                ans = min(ans, diff1, diff2)

        return ans
