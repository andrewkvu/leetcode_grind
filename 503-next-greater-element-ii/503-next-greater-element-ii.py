class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # initialize array of -1's
        res = [-1] * len(nums)
        # initialize stack
        stack = []
        currMax = 0
        # loop over values in nums
        for i in range(len(nums)):
        # while stack is nonempty and current value in nums is greater than the top of the stack
            while stack and nums[i] > stack[-1][-1]:
                # pop from the stack
                stackIndex, stackVal = stack.pop()
                # change the value from the popped stack into res
                res[stackIndex] = nums[i]
            # append to the stack
            stack.append([i, nums[i]])
            
        for i in range(len(nums)):
        # while stack is nonempty and current value in nums is greater than the top of the stack
            while stack and nums[i] > stack[-1][-1]:
                # pop from the stack
                stackIndex, stackVal = stack.pop()
                # change the value from the popped stack into res
                res[stackIndex] = nums[i]
            # append to the stack
            stack.append([i, nums[i]])
        # return res
        return res