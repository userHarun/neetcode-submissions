class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # add words letter by letter
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            # update curr
            curr = curr.children[ch]
        # mark end of word

        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j, node):

            curr = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # go through each node in trie
                    for child in curr.children.values():
                        # skip the dot and pass it node to function
                        if dfs(i + 1, child):
                            return True

                    return False

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endOfWord

        return dfs(0, self.root)


"""
trie class approach with prefix check is the best

when searching the trie:
if we encounter a . we have to backtrack/dfs and try every letter to see if it creates a valid
word. 

"""
