class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPalindrome(s, i, i) # odd palindromes
            res += self.countPalindrome(s, i, i + 1) # even palindromes

        return res


    def countPalindrome(self, s, l, r): # same as longestPalindromicSubstring
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]: # palindrome checker
            count += 1
            l -= 1 # expand outwards
            r += 1
        return count
        