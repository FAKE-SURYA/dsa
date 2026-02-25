class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bits(x: int) -> int:
            return bin(x).count("1")      # or x.bit_count()
        
        arr.sort(key=lambda x: (bits(x), x))
        return arr
