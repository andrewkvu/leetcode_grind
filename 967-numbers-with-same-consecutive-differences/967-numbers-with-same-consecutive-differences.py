class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def dfs(digitsLeft, currNum):
            if digitsLeft == 0: # base case
                res.append(currNum)
                return
            lastDigit = currNum % 10 # get the last digit
            nextDigits = {lastDigit + k, lastDigit - k} # can be either +/- k for the consec diff
            for nextDig in nextDigits: # get the consec diff
                if 0 <= nextDig <= 9: # see if it lies within a single positive digit
                    newCurrNum = currNum * 10 + nextDig # basically append the nextDigit to the current one
                    dfs(digitsLeft - 1, newCurrNum) # then run the dfs again for this number

        for startingDigit in range(1, 10):
            dfs(n - 1, startingDigit)
        return res