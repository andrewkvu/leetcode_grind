class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dd = defaultdict(list)
        res = 0

        # append based on first character
        for word in words:
            dd[word[0]].append(word)

        # iterate through each char in given string to access words that start with the character
        for char in s:
            # store the current list of dd in a var
            currentCharDD = dd[char]
            dd[char] = [] # reset dd[char] to an empty list
            for word in currentCharDD:
                if len(word) == 1: # if the word in the dd is a single character, it will 100% be a subsequence so its good
                    res += 1
                else: # redo the dictionaries such that the first char of the word is removed
                    dd[word[1]].append(word[1:])
                # print(dd)

        return res
                
            
        
        