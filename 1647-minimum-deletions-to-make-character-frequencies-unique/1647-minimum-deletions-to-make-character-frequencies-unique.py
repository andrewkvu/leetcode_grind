class Solution:
    def minDeletions(self, s: str) -> int:
        charCount = Counter(s)
        seenFreq = set()
        res = 0

        for char, freq in charCount.items():
            if freq not in seenFreq:
                seenFreq.add(freq)
            else:
                while freq in seenFreq and freq > 0:
                    res += 1
                    freq -= 1
                seenFreq.add(freq)

        return res