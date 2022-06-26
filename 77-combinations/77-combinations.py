class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, currComb):
            # base case
            if len(currComb) == k:
                res.append(currComb.copy())
                return

            for i in range(start, n + 1):
                currComb.append(i)
                backtrack(i + 1, currComb)
                currComb.pop()

        backtrack(start=1, currComb=[])
        return res