class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = Counter(secret)

        bulls = 0
        cows = 0

        # bulls is digits in guess that are in correct position of secret
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
                count[secret[i]] -= 1

        # cows is digits in guess that are in the number but wrong position
        for i in range(len(guess)):
            # check if this number is in the counter, check that it should not be the same value in the secret though,
            # then check that there is still at least one occurrence of that letter in count to use up
            if guess[i] in count and guess[i] != secret[i] and count[guess[i]] >= 1:
                cows += 1
                count[guess[i]] -= 1

        return "{}A{}B".format(bulls, cows)