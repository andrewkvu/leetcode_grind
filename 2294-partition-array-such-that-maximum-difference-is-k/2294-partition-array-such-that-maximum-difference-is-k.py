class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        partitions = 1 # by default
        last = nums[0]
        
        for num in sorted(nums):
            if num - last > k:
                partitions += 1
                last = num
        
        return partitions