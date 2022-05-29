class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        freqMap = {}

        for char in s:
            freqMap[char] = freqMap.get(char, 0) + 1
        
        if letter in s:
            return math.floor(freqMap[letter] / len(s) * 100)
        
        return 0