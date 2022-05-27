class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charMapS = {}
        charMapT = {}
        
        
        # for char in s:
        #     charMapS[char] = charMapS.get(char, 0) + 1
        # for char in t:
        #     charMapT[char] = charMapT.get(char, 0) + 1
            
        # also the same as 
        for i in range(len(s)):
            charMapS[s[i]] = charMapS.get(s[i], 0) + 1
            charMapT[t[i]] = charMapT.get(t[i], 0) + 1
        
        for char in charMapS:
            if charMapS[char] != charMapT.get(char, 0):
                return False
            
        return True
            