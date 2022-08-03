class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        res_l = 0
        res_r = 0
        N = len(s)
        for i in range(N):
            # odd length
            l = r = i
            while l >= 0 and r < N and s[l] == s[r]: # palindrome checker
                if 1 + r - l > resLen:
                    # res = s[l:r + 1]
                    res_l = l
                    res_r = r + 1
                    resLen = 1 + r - l
                l -= 1 # expand out from the middle i index
                r += 1

            # even length - same thing
            l, r = i, i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                if 1 + r - l > resLen:
                    # res = s[l:r + 1]
                    res_l = l
                    res_r = r + 1
                    resLen = 1 + r - l
                l -= 1
                r += 1

        return s[res_l:res_r]