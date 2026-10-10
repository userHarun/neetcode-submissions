# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # def dfs(node):
        #     # pre order style
        #     # process, then left, then right
        #     if not node:
        #         return None
        #     if node == p or node == q:
        #         return node
        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     # if on both sides means root is lca
        #     if left and right:
        #         return node
        #     # if on one side return that sides node
        #     if not left and right:
        #         return right
        #     else:
        #         return left        
        # return dfs(root)
            
        cur = root
        while cur:
            if p.val > cur.val and q .val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q .val < cur.val:
                cur = cur.left
            else:
                return cur


''' 

if p and q on differnet subtrees
lca is is first node you called
if p and q on same side
just return whatever you find first

use preorder

we can optimize since its a bst and compare values
same idea tho
'''