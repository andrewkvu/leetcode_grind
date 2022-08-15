class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # presum
        answer = [0] * (n + 1)
        
        for first, last, seats in bookings: # [1, 5, 100]
            answer[first - 1] += seats # [100, 0, 0, 0, 0, -100]
            answer[last] -= seats 
        for i in range(1, len(answer)):
            answer[i] += answer[i - 1] # [100, 100, 100, 100, 100, 0] # 0, 1, 2, 3, 4
        
        return answer[:n] # not including last