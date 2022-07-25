class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [self.findFirst(nums, target), self.findLast(nums, target)]
        return res
        
    def findFirst(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        index = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                index = mid
                hi = mid - 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return index
    
    
    def findLast(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        index = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                index = mid
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
                
        return index