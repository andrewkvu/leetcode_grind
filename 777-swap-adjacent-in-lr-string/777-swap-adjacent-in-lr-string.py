class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace("X", "") != end.replace("X", ""):
            return False
        i = j = 0
        N = len(start)
        
        while i < N and j < N:
            # finding the first L/R
            while i < N and start[i] == 'X':
                i += 1
            while j < N and end[j] == 'X':
                j += 1
            
            if i < N and j < N:
                if start[i] == 'L' and j > i:
                    return False
                if start[i] == 'R' and i > j:
                    return False
            i += 1
            j += 1
        
        return True
            