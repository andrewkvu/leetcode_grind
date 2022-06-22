class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        res = 0
        taskMap = Counter(tasks)

        for key, val in taskMap.items():
            if val == 1:
                return -1
            res += (val + 2) // 3

        return res