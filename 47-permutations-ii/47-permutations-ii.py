class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        res = []

        def backtrack(comb, c):
            if len(comb) == len(nums): # base case
                res.append(comb.copy()) # has to be a copy since python objects do that 
                return

            for key, val in c.items():
                if val > 0: # if you can still use this as a choice
                    comb.append(key)
                    c[key] -= 1
                    backtrack(comb, c) # explore deepest

                    comb.pop() # pop the last one and add it back to the hashmap
                    c[key] += 1

        backtrack([], c)
        return res