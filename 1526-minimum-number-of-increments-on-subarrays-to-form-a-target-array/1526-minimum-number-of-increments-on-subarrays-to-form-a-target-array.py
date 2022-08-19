class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = pre = 0
    
        # basically, have pre be the number that you need to try and reach with the level increment
        # pre will be the previous number in the array each time, 
        # so add max(num - pre, 0) to the result
        # max(0) for neg cases, but basically just increment by any jump in difference
        # 3,1,5,4,2 would be 7 because there is a positive jump in 3-0 and 5-1
        # 3,1,1,2 would be 4 because there is a positive jump in 3-0 and 2-1
        for num in target:
            res += max(num - pre, 0)
            pre = num
        return res