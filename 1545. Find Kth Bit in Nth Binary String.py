class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def solve(n, k):
            if n == 1:
                return '0'
            
            length = (1 << n) - 1  # 2^n - 1
            mid = (length + 1) // 2  # 2^(n-1)
            
            if k == mid:
                return '1'
            elif k < mid:
                return solve(n - 1, k)
            else:
                # mirror index in left part
                mirrored = length - k + 1
                bit = solve(n - 1, mirrored)
                # invert
                return '1' if bit == '0' else '0'
        
        return solve(n, k)
