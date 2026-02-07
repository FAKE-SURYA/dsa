class solution:
    def minimumDeletions(self, s: str) -> int:
        
        deletions = 0
        
        countB = 0
        
        for ch in s:
            if ch == 'b':
                countB += 1
            else:
                deletions = min(deletions + 1, countB)
                
        return deletions 
        