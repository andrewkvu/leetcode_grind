class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        nodupes = set(words) # no need for duplicates
        
#   The discard() method removes the specified item from the set.
#   The remove() method will raise an error if the specified item does not exist
#   discard() method will not.
        
        for word in words:
            for suffix in range(1, len(word)):
                nodupes.discard(word[suffix:]) # removes any word, just doesn't raise error if item not in set
                # ie: removes "me" from the set after going its suffix in "time"
        
        return sum(len(word) + 1 for word in nodupes)
#         res = 0
        
#         for word in nodupes:
#             res += (len(word) + 1)
#         return res