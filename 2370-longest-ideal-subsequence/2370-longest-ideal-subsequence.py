class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = 26
        dp = [0 for i in range(N)]
        
        for char in s:
            i = ord(char) - ord('a') # int val from 0-25, convenient for arr indices
            dp[i] += 1
            # boundary that i don't fully understand
            for j in range(max(0, i - k), min(25, i + k) + 1):
                if j != i: # every character that ends with char j that can be used to append this char i
                    dp[i] = max(dp[i], 1 + dp[j])
        # print(dp)
        return max(dp)
        
#           # works but O(n^2) not good enough for boundaries
#         N = len(s)
#         dp = [1 for i in range(N)]
        
#         for i in range(N - 1, -1, -1):
#             for j in range(i + 1, N):
#                 diff = abs(ord(s[i]) - ord(s[j]))
#                 if diff <= k:
#                     dp[i] = max(dp[i], 1 + dp[j])

#         return max(dp)
    
    
        