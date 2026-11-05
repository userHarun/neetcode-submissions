class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        dirs = [(1,0),(-1,0), (0,1),(0,-1)]
        visited = set() # stores visited cells

        def back(r,c,i):
            # base cases
            if i == len(word):
                return True
            
            if r < 0 or r>= R or c < 0 or c >= C:
                return False
            if (r,c) in visited:
                return False
            
            ch = board[r][c]
            if ch != word[i]:
                return False
            visited.add((r,c))
            # explore 
            for dr, dc in dirs:
                if back(dr + r, dc + c, i + 1):
                    return True

            
            visited.remove((r,c))
            return



        for r in range(R):
            for c in range(C):
                # check if word is in 
                if back(r, c, 0):
                    return True
        return False



        
'''
edge case  is what if we down a path and it reaches a deadend
we want to go back up that path and find the correct result
so thats why we use backtracking




'''