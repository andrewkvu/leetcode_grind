class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # sum of gas has to be >= sum of cost in order to have solution
            return -1
        
        total = 0
        res = 0
        diff = [0] * len(gas)
        
        for i in range(len(gas)):
            diff[i] = gas[i] - cost[i]
            
        for i, val in enumerate(diff):
            total += val
            if total < 0:
                total = 0
                res = i + 1
        
        return res
            