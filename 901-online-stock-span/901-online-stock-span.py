# monotonic stack with a streak and price
# compute answer by add the streak of popped stack to return, append at end

class StockSpanner:

    def __init__(self):
        self.stack = [] # [streak, price]

    def next(self, price):
        streak = 1
        while self.stack and price >= self.stack[-1][-1]:
            stackStreak, stackPrice = self.stack.pop()
            streak += stackStreak
        self.stack.append([streak, price])

        return streak
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)