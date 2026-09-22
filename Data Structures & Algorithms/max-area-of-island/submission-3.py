class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        maxArea = 0
        def dfs(r, c):
            if (r < 0 or r >= R) or (c < 0 or c >= C) or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0
            
            # Start area at 1 for the current land piece
            area = 1 
            for dr, dc in dirs:
                area += dfs(r + dr, c + dc)
                
            return area

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    # Calculate the area and update maxArea directly
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea