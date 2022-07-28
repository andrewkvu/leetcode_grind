class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        slow = fast = 2
        
        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow

#         left = 2
        
#         for right in range(2, len(nums)):
#             if nums[left - 2] != nums[right]:
#                 nums[left] = nums[right]
#                 left += 1
        
#         return left