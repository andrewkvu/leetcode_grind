class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":  # bad base case where s[i] starts with 0
                return 0
            res = dfs(i + 1)  # take next character
            # case for getting 2 characters
            if (i + 1 < len(s)) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)