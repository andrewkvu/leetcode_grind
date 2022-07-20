class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:  # insert a word into the trie
        cur = self.root
        for char in word:
            if char not in cur.children:  # means not inserted yet
                cur.children[char] = TrieNode()  # create new empty set for children
            cur = cur.children[char]  # otherwise move to this char's set of children

        cur.endOfWord = True  # end of for loop = set to the last char in the word

    def search(self, word: str) -> bool:  # search if word is in the Trie
        cur = self.root
        for char in word:
            if char not in cur.children:  # if char does not exist in the tree
                return False  # then search is false
            cur = cur.children[char]  # otherwise, keep going through the rest of the chars in word

        return cur.endOfWord  # since endOfWord has to be true in order for it to count as a searched word

    def startsWith(self, prefix: str) -> bool:  # check if theres a word that starts with this prefix
        # same as search but you don't have to check if endOfWord is true
        cur = self.root
        for char in prefix:
            if char not in cur.children:  # if char does not exist in tree
                return False
            cur = cur.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)