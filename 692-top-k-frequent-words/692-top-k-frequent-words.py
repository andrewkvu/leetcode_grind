class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        # sort by most frequent -counter[x] then sort by lexicographical x
        res = sorted(counter, key=lambda x: (-counter[x], x))
        # print(res)
        return res[:k]