class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M = len(text1)
        N = len(text2)

        dp = [[0 for j in range(N + 1)] for i in range(M + 1)]
        
        # go diagonal down right if char matches, else take max of right and down to compute
        # bottom up
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # print(dp)
        return dp[0][0]
