class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0), (0,1),(0,-1)]
        res = 0
        
        def dfs(r, c):
           
            if not (0<= r < R and 0<= c < C) or grid[r][c] != '1':
                return 
            # mark as visited
            grid[r][c] = '0'
            
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
            
                dfs(nr, nc)


        # find 1s
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        
        return res