class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binarySearch(nums, target)
        last = self.binarySearch(nums, target + 1)
        
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        return [first, last - 1]
        
    def binarySearch(self, nums, target):
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
            
        return lo