from typing import List

class Solution:
    def minimumRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()                      # sort the array

        L = 1                             # longest balanced subarray length
        i = 0                             # left pointer
        j = 0                             # right pointer

        while j < n:
            minEl = nums[i]
            maxEl = nums[j]

            # shrink window from left while it's not balanced
            while i < j and maxEl > k * minEl:
                i += 1
                minEl = nums[i]

            # update best length
            L = max(L, j - i + 1)
            j += 1

        return n - L     
    
  
# minimum deletions
