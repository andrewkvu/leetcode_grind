class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initialize res with nums[0]
        res = nums[0]
        # have a localtotal to go over subarrays
        total = 0
        # iterate through array
        for num in nums:
            total += num
            res = max(res, total)
            if total < 0:
                total = 0
        
        # if total is ever below 0, it is not the largest sum so you reset to 0
        # otherwise you update res to be the max of res and total
        # return res
        return res