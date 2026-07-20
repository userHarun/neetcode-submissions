class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        res = []
        while top <= bottom and left <= right:
            # from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            #top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            # edge case for single row/ col
            if top <= bottom:
                for i in range(right,left  - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res

            





'''
we create 4 bounds and maintain the bounds and update them until they cross each other
effectively shrinking the bounds each traverse
cross each other condition is:
if top > bottom or left > right

edge is that theres no bottom row left or no left column left
so we have to take care of that



'''