# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, largest):
            nonlocal count
            if not node:
                return 0
            if node.val >= largest:
                count += 1
                largest = node.val
            dfs(node.left, largest)
            dfs(node.right, largest)
        

        dfs(root, float('-inf'))
        return count



'''
at each node we need to compare the largest value so far along the path and then 
update couunt if its a good node. and also update largest
we want to process at each node because we are comparing nodes along the path

'''
        