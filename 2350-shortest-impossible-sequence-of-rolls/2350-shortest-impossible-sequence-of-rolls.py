class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        res = 1 # min answer has to be one 
        # since you return shortest impossible 
        # which is one more than the max
        rset = set()
        
        for roll in rolls:
            rset.add(roll) # keep adding rolls until you see all numbers
            if len(rset) == k: # length of rset == k means seen all numbers == can make the sequences for it
                res += 1 # next impossible increment
                rset.clear() # find all roll numbers again
        
        return res
        
        