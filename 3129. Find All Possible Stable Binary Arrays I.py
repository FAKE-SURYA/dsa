class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]

        # base: pure zeros and pure ones
        # z zeros, 0 ones: valid iff z <= limit (otherwise runs > limit)
        for z in range(1, min(zero, limit) + 1):
            dp0[z][0] = 1
        # 0 zeros, o ones: valid iff o <= limit
        for o in range(1, min(one, limit) + 1):
            dp1[0][o] = 1

        # prefix sums to speed up range sums
        pre0 = [[0]*(one+1) for _ in range(zero+1)]
        pre1 = [[0]*(one+1) for _ in range(zero+1)]

        # init prefix for row/col 0
        for z in range(zero+1):
            pre0[z][0] = dp0[z][0]
            pre1[z][0] = dp1[z][0]
            if z > 0:
                pre1[z][0] = (pre1[z][0] + pre1[z-1][0]) % MOD
        for o in range(one+1):
            pre0[0][o] = dp0[0][o]
            pre1[0][o] = dp1[0][o]
            if o > 0:
                pre0[0][o] = (pre0[0][o] + pre0[0][o-1]) % MOD

        for z in range(zero+1):
            for o in range(one+1):
                if z == 0 and o == 0:
                    continue
                if o == 0 and z <= limit:
                    # already handled pure zeros base
                    continue
                if z == 0 and o <= limit:
                    # already handled pure ones base
                    continue
                if z == 0 or o == 0:
                    # other pure cases are invalid (run > limit)
                    continue

                # dp0[z][o] = sum_{k=1..min(limit,z)} dp1[z-k][o]
                loz = max(0, z - limit)
                hiz = z - 1
                s0 = pre1[hiz][o]
                if loz - 1 >= 0:
                    s0 = (s0 - pre1[loz-1][o]) % MOD
                dp0[z][o] = (dp0[z][o] + s0) % MOD

                # dp1[z][o] = sum_{k=1..min(limit,o)} dp0[z][o-k]
                loo = max(0, o - limit)
                hio = o - 1
                s1 = pre0[z][hio]
                if loo - 1 >= 0:
                    s1 = (s1 - pre0[z][loo-1]) % MOD
                dp1[z][o] = (dp1[z][o] + s1) % MOD

                # update prefix sums online
                pre0[z][o] = dp0[z][o]
                pre1[z][o] = dp1[z][o]
                if z > 0:
                    pre1[z][o] = (pre1[z][o] + pre1[z-1][o]) % MOD
                if o > 0:
                    pre0[z][o] = (pre0[z][o] + pre0[z][o-1]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
