class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[right] > nums[left]:
                res = min(res, nums[left]) # for the rotated n times case
                break
            mid = (left + right) // 2
            # just checking the mid case in general
            # as per any target == nums[mid] type problem
            res = min(res, nums[mid]) 
            # ie 2 3 4 5 1 - means we know that none to the left should be min
            # other than case 1 2 3 4 5 which is covered before in nums[right] > nums[left]
            if nums[left] <= nums[mid]:
                left = mid + 1
            # ie 4 5 1 2 3 - means we know that mid is in the ascending cycle already
            # so no point in checking anything after mid since it's sorted ascending
            else: # nums[left] >= nums[mid] means 
                right = mid - 1
        
        return res
                
                
            
            
                