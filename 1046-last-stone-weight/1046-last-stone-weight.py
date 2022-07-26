class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 'maxHeap' since you want the 2 heaviest stones
        myStones = [-stone for stone in stones] # [2,7,4,1,8,1] -> [-2,-7,-4,-1,-8,-1]
        heapq.heapify(myStones) # [-8, -7, -4, -1, -2, -1]
        while len(myStones) > 1:
            # pop the two greatest stones (which are negative)
            biggestStone1 = heapq.heappop(myStones)
            biggestStone2 = heapq.heappop(myStones)

            # push the difference after smashing the two stones together
            # has to be negative for the "maxHeap" to work
            heapq.heappush(myStones, -abs(biggestStone1 - biggestStone2))

        return abs(myStones[0])
