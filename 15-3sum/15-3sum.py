class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        # [-4,-1,-1,0,1,2]
        # a is value, and also is the fixed first number of 3
        for a in range(len(nums)):
            # if not the first number AND its the same value as the previous, skip this iteration of the loop
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            left = a + 1
            right = len(nums) - 1
            
            while left < right:
                threesum = nums[a] + nums[left] + nums[right]
                if threesum == 0:
                    res.append([nums[a], nums[left], nums[right]])
                    left += 1 # move over
                    while nums[left] == nums[left - 1] and left < right: # if the next is still the same as prev left
                        left += 1
                elif threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
        
        return res
                    
                
                
        