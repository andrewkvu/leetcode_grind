class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        freq = [[] for i in range(len(nums) + 1)] # 0-6 is still 7 nums
        ans = []
        # bucket sort
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        for n, c, in freqMap.items(): # returns the key value pair in the dictionary
            freq[c].append(n) # n occurs c number of times
            
        for i in range(len(freq) - 1, 0, -1): # goes down to 0, decrements by -1 
            # basically going backwards
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
            
            
            
            
        