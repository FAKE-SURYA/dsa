class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # total number of happy strings of length n
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""

        chars = ['a', 'b', 'c']
        res = []
        prev = ''

        for i in range(n):
            for c in chars:
                if c == prev:
                    continue
                remaining = n - i - 1
                count = 1 << remaining  # number of strings if we choose c here

                if k > count:
                    k -= count  # skip this block
                else:
                    res.append(c)
                    prev = c
                    break

        return "".join(res)
