class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        c = collections.Counter()
        res = -1
        for i, val in enumerate(nums):
            sd = self.sumOfDigitsInNum(val)
            if sd not in c:
                c[sd] = val
            else:
                res = max(res, c[sd] + val)
                c[sd] = max(c[sd], val)

        return res




    def sumOfDigitsInNum(self, num):
        s = 0

        for digit in str(num):
            s += int(digit)
        return s
        
        