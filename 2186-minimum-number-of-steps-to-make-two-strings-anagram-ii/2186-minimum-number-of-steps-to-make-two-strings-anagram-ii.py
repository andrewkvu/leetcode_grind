class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        
        sc = Counter(s)
        tc = Counter(t)
        
        for char in sc:
            if char not in tc:
                res += sc[char]
            else:
                res += abs(sc[char] - tc[char])
        
        for char in tc:
            if char not in sc:
                res += tc[char]
        
        
        return res