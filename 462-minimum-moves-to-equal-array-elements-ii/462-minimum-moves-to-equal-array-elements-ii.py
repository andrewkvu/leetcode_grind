class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        middle = len(nums) // 2
            
        for i in range(len(nums)):
            count += abs(nums[i] - nums[middle])
        return count
    
    # initial thought - though above is essentially the same thing but with abs value so you don't have to check
    # lower or higher
#         for num in nums:
#             while num != nums[middle]:
#                 if num < nums[middle]:
#                     num += 1
#                 elif num > nums[middle]:
#                     num -= 1
#                 count += 1
        
#         return count