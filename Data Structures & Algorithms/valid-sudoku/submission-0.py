from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set to handle duplicates
        rows = defaultdict(set)
        boxes = defaultdict(set)
        cols = defaultdict(set)

        # loop through 9x9 grid
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                
                if cell == '.':
                    continue
                curr_box = (r // 3, c // 3)
                if cell in rows[r] or cell in cols[c] or cell in boxes[curr_box]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[curr_box].add(cell)
        return True
                    
                
'''

Look through the board.
For every board[r][c] != '' we have to do 3 checks:
check if you have seen this number in row r
check if you have seen it in col c
check if you have seen it in the curr 3x3 box

To calculate which 3 x 3 box you're in we can
divide the index of row and col by 3. Ex: board[2 // 3][3 // 3] = (0,1) (top middle box)

We can use a tuple for the boxes

'''