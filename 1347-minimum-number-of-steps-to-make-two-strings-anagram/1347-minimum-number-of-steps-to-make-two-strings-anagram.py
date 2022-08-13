class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        
        sc = Counter(s)
        tc = Counter(t)
        
        for char in sc:
            if char in tc:
                if tc[char] < sc[char]:
                    res += (sc[char] - tc[char])
            else:
                res += sc[char]
        
        return res