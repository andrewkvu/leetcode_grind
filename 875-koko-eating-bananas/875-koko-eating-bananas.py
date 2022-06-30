class Solution:    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) # creating range of [1, max of piles]
        speed = 0

        # all of this is based on the idea that instead of a linear search where you go through
        # multiple values to compute the same thing and see if it's good enough or not,
        # you use binary search and have your own range (no nums[right] nums[left])
        while left <= right:
            hours = 0
            mid = left + (right - left) // 2
            for pile in piles:
                hours += math.ceil(pile / mid) # computing how many hours a pile would take with this "mid" speed
            if hours <= h:
                speed = mid # speed = mid since technically it's good enough for the amount of hours
                right = mid - 1 # slow it down it's too fast
            else:  # hours > h
                left = mid + 1 # speed it up too many hours taken
        return speed
    
#     brute force:

#     def minEatingSpeed(piles, h):
#     speed = 1

#     while True:
#         hours = 0
#         for pile in piles:
#             hours += math.ceil(pile / speed)

#         if hours <= h:
#             return speed
#         else:
#             speed += 1