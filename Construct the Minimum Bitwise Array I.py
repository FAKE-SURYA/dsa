from typing import List
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result=[]
        for num in nums:
            first=num
            current=-1
            for j in range(1, first) :
                if(j|(j+1))==first:
                    current=j
                    break
                result.append(current)
            return result