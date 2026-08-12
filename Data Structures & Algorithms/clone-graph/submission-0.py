"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {}
        clones[node] = Node(node.val,[])
        q = deque([node])
        while q:
            
            curr = q.popleft()
            for nei in curr.neighbors:
                
                # append to q if not in clones and make the cloned node
                if nei not in clones:
                    clones[nei] = Node(nei.val, [])
                    q.append(nei)
                # add the nei if it is in clones
                clones[curr].neighbors.append(clones[nei])
                    
        return clones[node]

'''

so we are given a starting node
we need to make a clone of it
we can use a hashMap (defaultdict(list)) to hold each nodes cloned node
use bfs to traverse neighbors

ex:
clone 1: {node: cloned(node),}
explore 1 neighb
'''
