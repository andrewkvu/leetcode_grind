class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount = Counter(s)
        tCount = Counter(t)
        
        for key in tCount:
            if tCount[key] != sCount.get(key, 0):
                return key