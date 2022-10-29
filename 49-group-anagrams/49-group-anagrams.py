class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default dictionary of anagrams
        # for each string, append the string to the sorted version of that string group
        # have to do a 
        # then return all the values in the dictionary
        
        anagrams = defaultdict(list)
        for string in strs:
            anagrams["".join(sorted(string))].append(string)
        
        return anagrams.values()