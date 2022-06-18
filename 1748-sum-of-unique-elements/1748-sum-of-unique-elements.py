class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        
        freqMap = Counter(nums)
        
        for key in freqMap:
            if freqMap[key] == 1:
                res += key
        
        return res