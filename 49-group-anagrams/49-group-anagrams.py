class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = {}
        
        for string in strs:
            key = "".join(sorted(string)) # converts sorted(string) list into string key
            strDict[key] = strDict.get(key, []) + [string]
        
        return list(strDict.values())