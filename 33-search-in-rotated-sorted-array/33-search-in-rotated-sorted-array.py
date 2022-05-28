class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            
            if nums[lo] <= nums[mid]:
                if target < nums[lo] or target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            else: 
                if target > nums[hi] or target < nums[mid]:
                    # since the right will be greater than the middle
                    # no point in checking the right side, just check the left
                    hi = mid - 1
                    # since target is greater, can't check the right because no value between
                    # nums[mid] and nums[hi] will be used, so check left
                else:
                    lo = mid + 1
                    
        return -1        