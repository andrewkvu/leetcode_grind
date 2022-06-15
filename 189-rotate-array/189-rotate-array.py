class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = collections.deque()
        for num in nums:
            queue.append(num)
        
        for i in range(k):
            val = queue.pop()
            queue.appendleft(val)
            
        for i in range(len(nums)):
            nums[i] = queue.popleft()