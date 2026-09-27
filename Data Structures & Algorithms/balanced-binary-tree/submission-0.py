# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        diff = 0
        def dfs(node):
            if not node:
                return 0 
            l = dfs(node.left)
            if l == -1:
                return -1
            r = dfs(node.right)
            if r == -1:
                return - 1
            if abs(l - r) > 1:
                return -1
            
            # return height up
            return 1 + max(l, r)

        return dfs(root) != -1

            


'''
check height at each node
make sure it diff <= 1


'''