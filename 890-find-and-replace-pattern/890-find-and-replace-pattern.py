class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        
        # map each character in word to the char in pattern and vice versa
        # check if the current characters are the right mappings
        # if they are, they fit the pattern, else don't append
        def match(word):
            m1, m2 = {}, {}
            for wchar, pchar in zip(word, pattern):
                if wchar not in m1:
                    m1[wchar] = pchar
                if pchar not in m2:
                    m2[pchar] = wchar
                if (m1[wchar], m2[pchar]) != (pchar, wchar):
                    return False
            return True

        for word in words:
            if match(word):
                res.append(word)
        return res