class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        phoneMap = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}
        
        def backtrack(i, curStr):
            # base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for char in phoneMap[digits[i]]:
                backtrack(i + 1, curStr + char)
        
        if digits:
            backtrack(i=0, curStr="")
        return res
            