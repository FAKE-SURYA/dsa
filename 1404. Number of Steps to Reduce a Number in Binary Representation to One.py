class Solution:
    def numSteps(self, s: str) -> int:
        # single '1' means number is already 1
        if s == "1":
            return 0
        
        steps = 0
        carry = 0
        n = len(s)
        
        # go from right to left, but stop before index 0
        for i in range(n - 1, 0, -1):
            bit = int(s[i])
            val = bit + carry  # effective bit considering carry
            
            if val == 0:
                # even (0), just divide by 2
                steps += 1
            elif val == 1:
                # odd (1), need +1 then /2
                steps += 2
                carry = 1
            else:  # val == 2
                # bit was 1 and carry 1 -> '10' effectively, even
                steps += 1
                # carry remains 1
        
        # after finishing, if carry is 1, we did one extra +1 on the MSB
        # turning '1...' into '10...', so one more step to divide by 2
        return steps + carry
