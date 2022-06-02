class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = {}
        
        for string in strs:
            key = "".join(sorted(string)) # converts sorted(string) list into string key
            strDict[key] = strDict.get(key, []) + [string]
            # sets the initial value as an empty [] but then adds the array string version
            # similar to the .get(char, 0) + 1 but with a []
        
        return list(strDict.values())