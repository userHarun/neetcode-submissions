# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        res = []
        flag = False
        def dfs(node):
            nonlocal res
            nonlocal flag
            if not node:
                return 0
            if flag:
                return
            dfs(node.left)
            if len(res) == k:
                flag = True
            else:
                res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return res[k - 1]
'''

in order traversal visits in sorted order for a bst
[2,3,4,5]
stop when len arr == k


'''
