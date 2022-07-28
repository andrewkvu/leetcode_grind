class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
#         # marking initial negs to 0s
#         for i in range(len(nums)):
#             if nums[i] < 0:
#                 nums[i] = 0
        
#         for i in range(len(nums)):
#             val = abs(nums[i])
#             if 1 <= val <= len(nums):
#                 if nums[val - 1] > 0: # mark negative to parallel actions of a hashset
#                     nums[val - 1] *= -1
#                 elif nums[val - 1] == 0: # 0 means was negative, mark with a special "i dont care"
#                     nums[val - 1] = -1 * (len(nums) + 1)
        
#         for i in range(1, len(nums) + 1):
#             if nums[i - 1] >= 0: # number is positive = thats the value in the hashset that it wouldve been
#                 return i
#         return len(nums) + 1 # worst case if all the numbers are positive

        s = set(nums)
        
        for i in range(1, len(nums) + 1):
            if i not in s:
                return i
        
        return len(nums) + 1
            
        
        