class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # if the array were to be continuous, nums[left] would be less than nums[right] - len + 1
        # if the gap in numbers is really big like 1, 10, 100, 1000, 
        # the 10 itself would be the one to change to 2
        # and this would be accounted for by the N - windowsize

        N = len(nums)
        nums = sorted(set(nums))
        res = float('inf')
        left = 0

        # kinda sliding window, basically increment left until either left == right or
        # the gap between nums[left] and nums[right] is smaller than N + 1
        for right, val in enumerate(nums):
            while left < right and nums[left] < (nums[right] - N + 1):
                left += 1
            # keep track of windowsize, and the answer is len - windowsize
            windowSize = 1 + right - left
            res = min(res, N - windowSize)
        return res