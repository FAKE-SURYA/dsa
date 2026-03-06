class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # If "01" appears more than once, or if pattern is 1s -> 0s -> 1s, it's bad.
        # Simpler: once "01" happens, no "10" of ones starting again.
        return "01" not in s.strip('0')
