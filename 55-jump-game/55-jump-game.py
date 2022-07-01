class Solution:
    def canJump(self, nums: List[int]) -> bool:
        win = len(nums) - 1

        # approach problem in reverse
        # see if specific indexes can reach the "goal post"
        # ex: can the 2nd to last index reach the last index
        # if so, can the 3rd to last index reach the 2nd last index
        # else: can the 3rd to last index reach the last index
        for i in range(win - 1, -1, -1):
            if i + nums[i] >= win:
                win = i
            # no need for else since the i index increases regardless of whether the "win" (goal post) "moves"
            # if win is 0, this means that the goal post has moved to the start, which we can reach
        return win == 0