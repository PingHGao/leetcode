class Node:
    def __init__(self):
        self.isWord = False
        self.next = dict()

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        n = self.root
        for c in word:
            if c not in n.next:
                n.next[c] = Node()
            n = n.next[c]
        n.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        res = False
        n = self.root
        for c in word:
            if c not in n.next:
                break
            n = n.next[c]
        else:
            if n.isWord:
                res = True
        
        return res
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = self.root
        for c in prefix:
            if c not in n.next:
                return False
            n = n.next[c]
           
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
