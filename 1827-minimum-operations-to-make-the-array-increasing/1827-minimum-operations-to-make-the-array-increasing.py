class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        N = len(nums)
        for i in range(1, N):
            if nums[i] <= nums[i - 1]:
                # basically add the difference of the current and previous element, add one to increase
                operations += nums[i - 1] + 1 - nums[i] 
                nums[i] = nums[i - 1] + 1 # set the new nums[i] to the previous + 1
                
        return operations