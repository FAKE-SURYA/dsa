class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
       
        def is_inc(l, r):
            for i in range(l, r):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        
        
        def is_dec(l, r):
            for i in range(l, r):
                if nums[i] <= nums[i + 1]:
                    return False
            return True
        
        
        for p in range(1, n - 2 + 1):      
            for q in range(p + 1, n - 1): 
                if is_inc(0, p) and is_dec(p, q) and is_inc(q, n - 1):
                    return True
        
        return False
