class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for word in words:
            morseWord = ""
            for char in word:
                morseWord += MORSE[ord(char) - ord('a')] # gets position in MORSE array
            seen.add(morseWord)
        
        return len(seen)
                