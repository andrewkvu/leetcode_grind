class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap = {}
        ans = []
        
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        for num in freqMap:
            if freqMap[num] > math.floor(len(nums) / 3):
                ans.append(num)
                
        return ans