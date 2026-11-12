class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+ 1)]
        rank = [1] * (len(edges) + 1)
        def find(x):
            p = parent[x]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p
        def union(u, v):
            p1 = find(u)
            p2 = find(v)
            if p1 == p2:
                return False
            parent[p1] = p2

            return True
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        return []

        





        




'''

most efficient approach is probably union find
find the parent of each node
if there already exists one connection to it, then its redundant
otherwise union them
Because edges are processed in order, the first edge that fails to union is the answer.



'''