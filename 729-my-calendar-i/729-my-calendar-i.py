class MyCalendar:

    def __init__(self):
        self.res = []

    def book(self, start: int, end: int) -> bool:
        for curStart, curEnd in self.res:
            if curStart < end and curEnd > start:
                return False
        self.res.append([start, end])
        return True
        
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)