class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(" ")

        # print(s)
        res = s[-1]

        for i in range(len(s) - 2, -1, -1):
            if s[i] != "":
                res += " "
                res += s[i]

        return res