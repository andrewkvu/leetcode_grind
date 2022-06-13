class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqMap = Counter(s)
        for idx, val in enumerate(s):
            if freqMap[val] == 1:
                return idx
        
        return -1