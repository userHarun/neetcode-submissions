class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        N = len(words)
        rows = len(board)
        cols = len(board[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        res = set()


        def dfs(r,c, node, word):
            if (r,c) in visited:
                return
            if r < 0 or r >= rows or  c < 0 or c >= cols:
                return
            
            ch = board[r][c]
            if ch not in node.children:
                return
            node = node.children[ch]
            visited.add((r,c))
            word += ch
            # check if end of word
            if node.end:
                res.add(word)
                # update end to false to find other  like backend
                node.end = False
            # explore neighbs
            for dr, dc in dirs:
                dfs(dr + r, dc + c, node, word)
            visited.remove((r,c))
            return
            

            
        # insert words to trie
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,trie.root, "")
                    
        
        return list(res)
'''
use a trie for efficient seaching

insert words to trie

then use backtracking/dfs to search for all words in the trie

'''