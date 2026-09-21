from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = -1
        # FIND THE rotten cell
        R = len(grid)
        C = len(grid[0])
        q = deque()
        dirs = [(-1,0), (1,0), (0,1),(0,-1)]
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))
        while q:
            res += 1
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr ,nc = dr + row, dc + col
                    if (0 <= nr < R and 0 <= nc < C) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2

                        q.append((nr,nc))

        # check if theres still afresh orange
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return -1
        return max(res, 0)