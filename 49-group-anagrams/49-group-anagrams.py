class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = defaultdict(list) # if any element is accessed that isn't in the dictionary:
        # element will be created in the argument type - in this case "list"
        # strDict = {}
        for s in strs:
            strDict[str(sorted(s))].append(s)     
        # if str(sorted(s)) not in strDict:
        #         strDict[str(sorted(s))] = [s]
        #     else:
        #         strDict[str(sorted(s))].append(s)  
        
        return strDict.values()