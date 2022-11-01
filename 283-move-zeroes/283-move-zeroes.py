class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find last non zero and place it in the array
        # then from the last non zero index to the end, set to 0
        lastNonZeroIndex = 0
        
        for i, val in enumerate(nums):
            if val != 0:
                nums[lastNonZeroIndex] = val
                lastNonZeroIndex += 1
        
        for i in range(lastNonZeroIndex, len(nums)):
            nums[i] = 0