class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        have = Counter(hand)
        
        for num in have:
            if have[num] > 0:
                need = have[num]
                for i in range(num, num + groupSize):
                    if have[i] < need:
                        return False
                    have[i] -= need
        return True