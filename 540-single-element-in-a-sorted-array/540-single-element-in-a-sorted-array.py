class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo < hi:
            # normally:
            # first part of pair is even, second part is odd
            mid = lo + (hi - lo) // 2
            # if this is true on mid, that means element is in right half of array
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                lo = mid + 1
            # else, element is in left half
            else:
                hi = mid
        return nums[lo]
                