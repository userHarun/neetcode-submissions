class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        
        for a, b in prerequisites:
            adj[b].append(a)
        white = set(adj.keys())
        gray = set()
        black = set()
        def dfs(node):
            gray.add(node)
            for course in adj[node]:
                if course in black:
                    continue
                if course in gray:
                    return False
                if not dfs(course):
                    return False
                
            
            gray.remove(node)
            black.add(node)
            return True
        
        while white:
            course = white.pop()
            if not dfs(course):
                return False
        return True
