# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            res = 0
            def dfs(node):
                if not node:
                    return 0
                nonlocal res
                left = dfs(node.left)
                right = dfs(node.right)
                res = max(left+ right, res)
                return 1 + max(left,right)

            dfs(root)
            return res
'''

return larger path upwards that the parent can use
store largest in a global var




'''