class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}

        def dfs(i, j):
            # returns: longest increasing path STARTING at (i,j)
            if (i, j) in memo:
                return memo[(i, j)]

            longest = 1
            for nr, nc in dirs:
                new_row, new_col = i + nr, j + nc

                if (0 <=  new_row < rows) and (0 <= new_col < cols) and matrix[new_row][new_col] > matrix[i][j]:
                    longest = max(longest, 1 + dfs(new_row, new_col))
            memo[(i, j)] = longest
            return memo[(i,j)]

        res = 0
        for i in range(rows):
            for j in range(cols):
                # get the largest
                res = max(res, dfs(i, j))

        return res


"""
we could start at a cell, and if one of the neighbs are greater, add it to path and explore that neigh. if we encounter a path that decreases our current path, we just ignore it

keep track of our largest path
store longest path that cell leads to in our memo for fast lookup
dfs(i, j) will ask what is the longest increasing path starting from cell [i,j]


ex 1:
start a 9 neighs are < 9 so next cell
we get to 4, 4 -> 9, or 4->8, take 4-> 9 store it (2)
4 -> 9 no more neighbs can be appended
start fresh at next row 6, only increasing num is 9 but we know it leads to dead end.
.
.
.
we get to 2, the longeset path we can go from 2 is 2- >6 -> 9 (3 > 2) store it

we get to 1, 1->6->8, 1->6->9 or 1->2->6-9 and hit base case so return out
len is greater than currr max so store it (4 > 3)

so we end with 4 

"""
