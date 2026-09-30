from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R = len(board)
        C = len(board[0])
        dirs = [(1,0),(-1,0), (0,1), (0,-1)]
        safe = set()
        q = deque()

        for j in range(C):
            if board[0][j] == 'O':
                q.append((0,j))

        if R > 1:
            for j in range(C):
                if board[R - 1][j] == 'O':
                    q.append((R - 1, j))
        
        for i in range(R):
            if board[i][C - 1] == 'O':
                q.append((i, C - 1))
        if C > 1:
            for i in range(R):
                if board[i][0] == 'O':
                    q.append((i, 0))

        print(q)
        while q:
            i, j = q.popleft()
            safe.add((i,j))
            for dr, dc in dirs:
                nr, nc = dr + i, dc + j

                if 0 <= nr < R and 0 <= nc < C:
                    if board[nr][nc] == 'O' and (nr,nc) not in safe:
                        q.append((nr,nc))
        
        # scan board for any remaining O
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O' and (r,c) not in safe:
                    board[r][c] = 'X'
        




'''

It would be too costly to just do a regular loop through the board and loop for O
and check if iits on the edge

starting from the outside and wokring inwards is better


'''