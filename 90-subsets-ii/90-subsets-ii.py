class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, currSub):
            # base case
            if i == len(nums):
                res.append(currSub.copy())
                return

            currSub.append(nums[i])
            backtrack(i + 1, currSub)
            currSub.pop()

            # used for skipping duplicates in nums
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                # increases the i pointer to move over duplicates
                # also increases the i + 1 above so that it terminates if it's like [1,2,2]
                i += 1
            # eventually will append the empty []
            backtrack(i + 1, currSub)

        backtrack(i=0, currSub=[])
        return res