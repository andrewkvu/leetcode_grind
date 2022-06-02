class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        countS = Counter(s)
        countT = Counter(target)
        
        localMin = float('inf')
        for char in countT:
            localMin = min(localMin, countS[char] // countT[char])
        
        return localMin