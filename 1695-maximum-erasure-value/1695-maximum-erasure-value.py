class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # sliding window
        hset = set()
        windowL, windowR = 0, 0
        ans = 0
        runningSum = 0
        
        while windowR < len(nums):
            if nums[windowR] in hset:
                hset.remove(nums[windowL])
                runningSum -= nums[windowL]
                windowL += 1
            else:
                hset.add(nums[windowR])
                runningSum += nums[windowR]
                windowR += 1
                ans = max(ans, runningSum)

        return ans