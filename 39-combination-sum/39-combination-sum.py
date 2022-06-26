class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, currTotal):
            # base case
            if sum(currTotal) == target:
                res.append(currTotal.copy())
                return
            # if the recursion goes too far then break the backtrack
            if i >= len(candidates) or sum(currTotal) > target:
                return

            currTotal.append(candidates[i]) # append to current combination
            backtrack(i, currTotal) # goes in depth until it cant recursively
            currTotal.pop() # take it out
            backtrack(i + 1, currTotal) # go to the next candidate by increasing the index

        backtrack(0, currTotal=[])
        return res