class TrieNode:
    def __init__(self):
        self.children = {} # a : TrieNode
        self.isWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # same as the trie insert word
    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                char = word[i]
                if char == '.': # we would have to go through each of the paths of the children of the word
                    for child in cur.children.values(): # have to go through the .values of children since the key is one letter
                        # values is the rest of the letters attached
                        if dfs(i + 1, child): # recall the function with the next indexed value for the word and the child itself
                            return True # return True if we know the whole path is true
                    return False # return False if there is no path that follows this

                else: # c is a regular character, search as normal with Tries
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.isWord

        return dfs(0, self.root)     


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)