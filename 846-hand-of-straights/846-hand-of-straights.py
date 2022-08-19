class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        have = Counter(hand)
        
        for num in have:
            if have[num] > 0: # if you still have some of this card
                need = have[num] # use this as the base of your straight
                for i in range(num, num + groupSize): # straight from num to num + groupSize
                    if have[i] < need: # if you have less than you need, false
                        return False
                    have[i] -= need # remember to subtract out the ones you already used
        return True