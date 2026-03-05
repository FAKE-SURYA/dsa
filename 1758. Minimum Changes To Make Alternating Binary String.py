class Solution:
    def minOperations(self, s: str) -> int:
        cost0 = 0  # make it like "010101..."
        cost1 = 0  # make it like "101010..."
        
        for i, ch in enumerate(s):
            # pattern starting with '0'
            expected0 = '0' if i % 2 == 0 else '1'
            # pattern starting with '1'
            expected1 = '1' if i % 2 == 0 else '0'
            
            if ch != expected0:
                cost0 += 1
            if ch != expected1:
                cost1 += 1
        
        return min(cost0, cost1)
