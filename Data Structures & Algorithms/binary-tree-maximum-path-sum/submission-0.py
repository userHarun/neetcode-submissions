# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node):
            if not node:
                return 0

            nonlocal res

            # go down left and right and get largest(ignore negatives)
            left_path = dfs(node.left)
            right_path = dfs(node.right)

            left = max(left_path, 0)
            right = max(right_path,0)


            # store your res after each node before you return it up
            res = max(res, node.val +left + right)
            # return to the parent the max left or right + itself
            return node.val + max(left,right)

        dfs(root)
        return res
'''



'''