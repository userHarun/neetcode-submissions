class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0), (0,1),(0,-1)]
        maxArea = 0
        currMax = 0 
        def dfs(grid, r, c):
            nonlocal currMax
            nonlocal maxArea
           # oout of bounds check
            if (r < 0 or r >= R) or (c < 0 or c >= C):
                return
            if grid[r][c] != 1:
                return
            currMax += 1
            
            grid[r][c] = '0'
            
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                dfs(grid, nr, nc)
            maxArea = max(maxArea, currMax)


        # find 1s
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    currMax = 0
                    dfs(grid,r,c)
        
        return maxArea