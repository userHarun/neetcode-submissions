class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        res = []
        board =[['.'] * n for i in range(n)]
        def backtracking(r):
            # base case 
            if r == n:
                # make a copy, join and append to res
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            # loop through each row pos
            for c in range(n):
                # check if you can put a queen there
                if c in col or (r + c) in posDiag or (r-c) in negDiag:
                    continue
                
                # add them to sets and make it a queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'
                backtracking(r + 1)
                # backtrack
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'
        
        backtracking(0)
        return res






'''
bounding condition:
queen cannot be in same row/col/and diag as other queen
or we can say same col, negative diag and positive diag



'''