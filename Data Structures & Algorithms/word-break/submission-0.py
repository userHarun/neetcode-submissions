class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.head = TrieNode()
    

    def addWord(self,word):
        # curr node
        curr = self.head
        for ch in word:
            # create node
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        # mark end of word
        curr.isEnd = True
    def search(self, word):
        curr = self.head
        for ch in word:
            if ch not in curr.chidlren:
                return False
            curr = curr.children[ch]
        # check if you reached end of word
        return self.isEnd
    
    def prefix(self, key):
        curr = self.head
        for c in key:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()

        for word in wordDict:
            trie.addWord(word)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        # build bottom up
        for i in range(n - 1, -1, -1):
            curr = trie.head
            # walk trie
            for j in range(i, n):
                # break early if not in trie
                ch = s[j]
                if ch not in curr.children:
                    break
                
                curr = curr.children[ch]
                # check if end of word
                if curr.isEnd and dp[j + 1]:
                    dp[i] = True
        return dp[0]

        