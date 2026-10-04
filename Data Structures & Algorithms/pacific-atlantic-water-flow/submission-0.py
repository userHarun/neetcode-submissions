from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])
        dirs = [(-1,0), (0, 1), (1, 0),(0,-1)]
        # store bordering
        pacific = []
        atlantic = []


        def bfs(ocean):
            q = deque()
            possible = set() 
            for x, y in ocean:
                q.append((x,y))
                possible.add((x,y))
            
            while q:
                i, j = q.popleft()

                for dr, dc in dirs:
                    nr, nc = i + dr, j + dc
                    if (0 <= nr < R and 0 <= nc < C):
                        if heights[nr][nc] >= heights[i][j] and (nr,nc) not in possible:
                            possible.add((nr,nc))
                            q.append((nr,nc))

            return possible # possible intersections

        # Left and right borders
        for r in range(R):
            pacific.append((r, 0))       # left column
            atlantic.append((r, C - 1))  # right column

        # Top and bottom borders
        for c in range(C):
            pacific.append((0, c))       # top row
            atlantic.append((R - 1, c))  # bottom row

        P = bfs(pacific)
        A = bfs(atlantic)
        return list((P & A))
'''
we can visit  cells with height <=

brute force approach with be too slow exploring if a node can reach the other side of the grid

optimal approach would be starting from the pacific / atlantic and working inwards

so store the cells bordering pacific and atlantic
So we are doing bfs backwards. 
Since its reverse bfs the condition is backwards too. neighb height >= curr height
then return the intersection of both A and B


'''