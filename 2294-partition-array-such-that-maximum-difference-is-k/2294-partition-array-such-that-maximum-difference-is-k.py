class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        partitions = 1 # by default
        last = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] - last > k:
                partitions += 1
                last = nums[i]
        
        return partitions