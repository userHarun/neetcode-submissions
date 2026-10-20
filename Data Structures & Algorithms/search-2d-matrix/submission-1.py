class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        low = 0
        high = R * C - 1
        while low <= high:
            mid = low + (high - low) // 2

            row = mid // C
            col = mid % C
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                low  = mid + 1
            else:
                high = mid - 1
        return False



'''
target is 13
binary search on matrix

think as if you flattened the matrix

if you calc mid from flattened
how to find the (row,col)? row is mid // cols
col = mid % cols
low= 0 
high = 3 * 4 - 1 = 11
mid = 0 + 11 // 2 = 6
row and col of 6 is (6//2, 6%2) = (1,2)
mat[1][2] = 12
12 > target so adjust ptrs. high = mid - 1

'''