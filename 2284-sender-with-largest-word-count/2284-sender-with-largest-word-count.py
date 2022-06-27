class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        freqMap = {}
        ans = ""
        maxWords = 0
        for i, user in enumerate(senders):
            if user not in freqMap:
                freqMap[user] = len(messages[i].split(" "))
            else:
                freqMap[user] += len(messages[i].split(" "))

        for user, val in freqMap.items():
            if val > maxWords:
                maxWords = val
                ans = user
            elif val == maxWords and user > ans:
                ans = user

        return ans
            