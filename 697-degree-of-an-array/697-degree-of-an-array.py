class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # map indices to the values in nums with hashmap
        # also use a counter to find the max key and max degree
        # then subtract the first and last ocurrence of each key
        
        
        
        c = Counter(nums)
        degree = max(c.values())
        res = float('inf')
        for key, val in c.items():
            if val == degree:
                left = 0
                right = 0
                for i, x in enumerate(nums):
                    if key == x:
                        left = i
                        break
                for i in range(len(nums) - 1, -1 ,-1):
                    if key == nums[i]:
                        right = i
                        break
                res = min(res, right - left + 1)
        
        return res