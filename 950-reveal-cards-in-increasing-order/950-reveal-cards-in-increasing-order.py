class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        indexDeck = deque(range(N))
        res = [None] * N
        
        for num in sorted(deck):
            res[indexDeck.popleft()] = num  # even indices are entered in sorted order first
            if indexDeck: # if there are still card indices left
                indexDeck.append(indexDeck.popleft()) # skips the odd index by popping left again
                # and putting it at the end
        
        return res