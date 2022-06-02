class Solution:
    def digitCount(self, num: str) -> bool:
        freqMap = {}
        
        for val in num:
            val = int(val)
            freqMap[val] = freqMap.get(val, 0) + 1
        
        for i in range(len(num)):
            if int(num[i]) != (freqMap.get(i, 0)):
                return False
        
        return True