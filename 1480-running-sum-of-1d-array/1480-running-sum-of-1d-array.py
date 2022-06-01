class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumArr = [nums[0]]
        
        for i in range(1, len(nums)):
            sumArr.append(sumArr[i - 1] + nums[i]) 
        
        return sumArr