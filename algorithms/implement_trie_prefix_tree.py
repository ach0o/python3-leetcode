# https://leetcode.com/problems/implement-trie-prefix-tree/


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._trie = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        for i in range(1, len(word)):
            if word[:i] not in self._trie:
                self._trie[word[:i]] = False
        self._trie[word] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self._trie.get(word, False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        """
        return prefix in self._trie


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
