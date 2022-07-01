class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        capacityLeft = []
        rocksLeft = additionalRocks
        res = 0
        for i in range(len(capacity)):
            capacityLeft.append(capacity[i] - rocks[i])
        capacityLeft.sort()

        for i, num in enumerate(capacityLeft):
            if num == 0:
                res += 1
            elif 0 < num <= rocksLeft:
                rocksLeft -= num
                res += 1
            else:
                break

        # print(capacityLeft)
        return res