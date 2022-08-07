class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        MOD = 10 ** 9 + 7

        for z in range(2, n + 1):
            a, e, i, o, u = (e + i + u) % MOD, (a + i) % MOD, (e + o) % MOD, i, (i + o) % MOD
            # all computations at the same time, so no need for prev or curr DP

        return (a + e + i + o + u) % MOD