class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        seen = set()
        for i in range(len(s) - 9):
            substring = s[i: i + 10]
            if substring in seen and substring not in res:
                res.append(substring)
            seen.add(substring)
        
        return res
            