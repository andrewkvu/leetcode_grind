class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[-1] = True
        
        for i in range(N - 1, -1, -1):
            for word in wordDict:
                # start of a possible word and this word is the right word
                # one word has to be correct at the end since you need to
                # segment into ONLY words in the dict
                # i = 4 + len(word) 4 <= 8 and [4:8} is jus]
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)] 
                if dp[i]: # optional but slightly faster so 
                    break # you don't have to check other words in the wordDict
        return dp[0]
                    