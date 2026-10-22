class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        flag1 = False
        flag2 = False

        #check if first row alr has 0
        for j in range(m):
            if matrix[0][j] == 0:
                flag1 = True
        # check col now
        for i in range(n):
            if matrix[i][0] == 0:
                flag2 = True

        # now loop through matrix and create first row and first col markers
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        # now loop through submatrix and mark zeros accordingly
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            
        
        if flag1 == True:
            # set first row to zeros
            for j in range(m):
                matrix[0][j] = 0
            
        if flag2 == True:
            # set first col to 0
            for i in range(n):
                matrix[i][0] = 0

                                
        
      

        

'''
Brute Approach:
create a visited matrix of same size
traverse the matrix and if you find a zero, traverse the cols and set it to zero in visited
then do the same for the rows.
lastly, copy all rows,cols from the visited matrix

Hashset approach:
store the row pos that contained a 0 in a row hashset
store the col pos that had 0 in a col hashset
then loop through a 2nd time, and if the row or col index is inside the hashsets, set it == 0.
Time/space complexity is O(nm)
------------------------------------------------------
O(1) approach:

use the first row and col as markers
traverse matrix beside first row and col, then compare it to the first row and col markers corresponding to that cell,
if its equal to 0, change that cell to 0.

edge case:
we need to flag if we already had 0s in the first row and col and deal with that.



'''