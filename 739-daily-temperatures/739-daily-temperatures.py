class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, currTemp in enumerate(temperatures):
            while stack and currTemp > stack[-1][-1]:
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([i, currTemp])
        return res
        