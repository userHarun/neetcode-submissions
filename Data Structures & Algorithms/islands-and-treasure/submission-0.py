from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])
        q = deque()
        visited = set()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))
        dirs = [(-1,0),(1,0), (0,1), (0,-1)]
        dist = 0
        inf = 2147483647
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist
                
                for dr, dc in dirs:
                    nr, nc = r+ dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] == inf:
                            q.append([nr,nc])
                            grid[nr][nc] = dist


            dist += 1







'''
start from 0s and bfs
 

'''