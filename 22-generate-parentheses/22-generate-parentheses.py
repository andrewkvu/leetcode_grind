class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open if open < n
        # can add closed if close < open
        # stack itself is valid if open == close == n
        res = []
        stack = []

        def backtrack(openCount, closeCount):
            if openCount == closeCount == n:
                res.append("".join(stack)) # joins all elements in the stack into one string, then append the string to res
                return
            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closeCount)
                stack.pop()

            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()

        backtrack(openCount=0, closeCount=0)
        return res