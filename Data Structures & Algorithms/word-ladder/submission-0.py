from collections import defaultdict
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # build graph
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # create wildcard pattern
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        visited = set([beginWord])
        # (word, cost to get there)
        q = deque([(beginWord, 1)])

        # bfs
        while q:
            word,cost  = q.popleft()
            
            # generate patterns for word
            if word == endWord:
                return cost
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for neiWord in adj[pattern]:
                    if neiWord not in visited:
                        visited.add(neiWord)
                        q.append((neiWord, cost + 1))


        return 0


'''
naive approach:
I think we could just always look to transform the beginWord
so for ex: you start with cat, look for a word that has 2 matching characters and just transform it and update our beginword.
now you get bat
keep going until you reach the endWOrd

another thought:
Two words are connected if they differ in exactly one position.

so use a hashmap to store similar words:
{
cat: bat
bat:bag
bag:sag, dag
sag:bag, dag
dag:sag,bag
dot: "" 
}

so its kind of like a graph problem  now. and we can use a traversal
so now when you are going through your list follow your similar word. if you can reach the endword return min path to get there, if you exercised all possibilities and not at endWOrd return 0

wordList
   ↓
figure out which words differ by exactly 1
   ↓
build graph with defaultdict
   ↓
beginWord
   ↓
BFS
   ↓
endWord
to figure out which words differ by exactly 1 efficiently we would
for each word, generate a pattern by replacing one position with a wildcard.
then during bfs we just generate the patterns and look up which words belong to those groups.

For each word you pop from the BFS queue:
Generate all its wildcard patterns.
For each pattern, look up all words in that bucket.
Those words are your possible neighbors.
Add unvisited neighbors to the queue.
If you reach endWord, BFS guarantees that it’s the shortest transformation path.

'''
        