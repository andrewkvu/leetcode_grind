class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        ans = []
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else: 
                freqMap[num] = 1
                
        for i in range(k):
            localMax = 0
            localMaxKey = -1
            for x in freqMap:
                if freqMap[x] > localMax:
                    localMax = freqMap[x]
                    localMaxKey = x
            localMax = 0
            ans.append(localMaxKey)
            freqMap[localMaxKey] = -1
        
        return ans
            
            
            
            
        