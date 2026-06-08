from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >  n - 1:
            return False
        adj = defaultdict(list)
        visited = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(v, parent):
            visited.add(v)
            
            for nei in adj[v]:
                # skip if parent
                if nei == parent:
                    continue
                # not parent and in visited
                if nei in visited:
                    return False
                # propogate decision immediately if invalid
                res = dfs(nei, v)
                if res == False:
                    return False
                
            return True

        if not dfs(0 , -1):
            return False
        # check if we explored all nodes
        return len(visited) == n
                
                

                
            
            


'''
similar to cycle detection 
can use union find

or graph traversal and use a visited set/bool arr
DFS:
visited = (0 , 1, 2, 3)
start at node 0
traverse its values list
1->0 (in visited so skip)
1->2 (explore it)
2->1 (skip)
3->2 ( skip)
3-> 1 (invalid case for a tree)
**if neighbor is in visited and its not the parent return False**
Also if there some unvisited node:
return False

or we can do level by level (BFS)
**if a Node has an edge to a level we already completed,
then return False**


'''