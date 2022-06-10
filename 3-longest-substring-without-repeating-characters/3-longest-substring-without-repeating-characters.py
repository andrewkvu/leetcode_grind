class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        maxLength = 0
        hset = set()
        windowLeft = 0
        
        for windowRight in range(len(s)):
            while s[windowRight] in hset:
                hset.remove(s[windowLeft])
                windowLeft += 1
            hset.add(s[windowRight])
            maxLength = max(maxLength, windowRight - windowLeft + 1)
        
        return maxLength
        
        