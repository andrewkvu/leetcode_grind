class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        N = len(arr)
        M = len(arr) // 2
        res = 0
        s = sorted(c, key = lambda x: c[x])
        # print(c)
        
        for i in range(len(s) - 1, -1, -1):
            print(s[i])
            N -= c[s[i]]
            res += 1
            if N <= M:
                return res
        # return 1