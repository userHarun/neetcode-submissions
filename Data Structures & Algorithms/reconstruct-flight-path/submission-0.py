import heapq
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, dest in tickets:
            heapq.heappush(graph[start], dest)
        path = []
        # we want to explore the lexigrap smallest each time
        def dfs(node):
            while graph[node]:
                next_dest = heapq.heappop(graph[node])
                dfs(next_dest)
            path.append(node)
        dfs("JFK")

        return path[::-1]