class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        c = Counter()
        undefeated, oneloss = set(), set()
        for winner, loser in matches:
            c[loser] += 1
        
        for winner, loser in matches:
            if winner not in c: # they haven't lost at all
                undefeated.add(winner)
        
        for player in c:
            if c[player] == 1:
                oneloss.add(player)
        return [sorted(list(undefeated)), sorted(list(oneloss))]
                