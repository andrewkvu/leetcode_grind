class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum of range of all numbers supposed to be in nums - actual sum of nums
        return sum(range(len(nums) + 1)) - sum(nums)