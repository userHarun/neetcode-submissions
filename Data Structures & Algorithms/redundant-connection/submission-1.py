class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        
        def dfs(u,v, visited):

            if u == v:
                return True
            
            visited.add(u)

            for nei in adj[u]:
                if nei not in visited:
                    if dfs(nei, v, visited):
                        return True
            
            return False
                
        for u, v in edges:
            visited = set()
            if u in adj and v in adj and dfs(u, v, visited):
                return [u, v]
            adj[u].append(v)
            adj[v].append(u)
    
        return []





'''

most efficient approach is probably union find
find the parent of each node
if there already exists one connection to it, then its redundant
keep track of the most recent reduandant connection

anotheer approach:
dfs

'''