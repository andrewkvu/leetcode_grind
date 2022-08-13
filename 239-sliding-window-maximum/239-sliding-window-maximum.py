class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        res, q = [], deque()
        left = right = 0

        for right in range(len(nums)):
            # keep popping until all top values are greater than current arr value
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right) # append index, not value

            # remove left val from window 
            if left > q[0]:
                q.popleft()
            if (right + 1) >= k: # means the window size is good enough now
                res.append(nums[q[0]]) # max will be in the first spot of the queue since we keep popping the lesser values
                left += 1 # adjust window

        return res