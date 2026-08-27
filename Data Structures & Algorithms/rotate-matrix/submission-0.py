class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        # now reverse cols
        for row in matrix:
            row.reverse()

            



        

'''
similar to taking transpose of a matrix
but its in opposite order
in transpose diagnoals stay the same

then at the end reverse it

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

matrix = [
  [1,2,3],
  [2,5,6],
  [3,8,9]
]
matrix[0,1] = matrix[1,0], matrix[0,2] = matrix[2,0]
matrix[1,0] already swapped, matrix[1,1] (i == j so skip), matrix[1,2]
= matrix[2,1]....
matrix = [
  [1,4,7],
  [2,5,8],
  [3,6,9]
]
so to skip already swapped elemenets we start from i + 1, in the 2nd loop

now reverse each elem in rows

'''