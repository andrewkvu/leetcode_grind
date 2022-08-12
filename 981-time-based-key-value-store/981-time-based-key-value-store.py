class TimeMap:

    def __init__(self):
        self.timeMap = {} # key: [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        valtime = self.timeMap.get(key, []) # get value from key or default to []
        left, right = 0, len(valtime) - 1
        # {"foo": [["bar", 1], ["bar2", 4]}

        while left <= right:
            mid = left + (right - left) // 2
            if valtime[mid][1] <= timestamp:
                res = valtime[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)