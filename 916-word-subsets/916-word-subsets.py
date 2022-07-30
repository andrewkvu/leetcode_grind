class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        
        words2final = Counter()
        for word2 in words2:
            count2 = Counter(word2)
            for char in count2:
                words2final[char] = max(words2final[char], count2[char])
        
        for word1 in words1:
            count1 = Counter(word1)
            for char in words2final:
                if char not in count1 or count1[char] < words2final[char]:
                    break
            else:
                res.append(word1)
        
        return res