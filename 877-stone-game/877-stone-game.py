class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # because there is an even amount of piles and Alice goes first,
        # Alice can win the 2 game pile, meaning she wins the 4 game, then etc
        # can take all even or odd piles, and one of these sets of piles 
        # will always be greater than the other
        return True