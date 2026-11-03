class Node:
    def __init__(self):
        self.tree = {} # children
        self.isEnd = False
class PrefixTree:

    def __init__(self):
        self.head = Node()
        

    def insert(self, word: str) -> None:
        curr = self.head
        for ch in word:
            if ch not in curr.tree:
                # create node
                curr.tree[ch] = Node()
            curr = curr.tree[ch]
        #  mark end of word
        curr.isEnd = True



    def search(self, word: str) -> bool:
        curr = self.head
        for ch in word:
            if ch not in curr.tree:
                return False
            curr = curr.tree[ch]
        
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for ch in prefix:
            if ch not in curr.tree:
                return False
            curr = curr.tree[ch]
        
        return True
        
        