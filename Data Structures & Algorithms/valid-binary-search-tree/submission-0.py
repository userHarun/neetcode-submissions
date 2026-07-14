# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node,low,high):
            if not node:
                return True
            
            # check if its invalid according to curr bounds
            if not (low < node.val < high):
                return False 
            
            left = dfs(node.left,low, node.val)
            right = dfs(node.right, node.val, high)

            # check if both returned true
            return left and right


        
        res = dfs(root, float('-inf'), float('inf'))
        return res

        
    


'''
we can use a dfs traversl and keep track of bounds
keep track of low and high bounds 
because we are not only comparing the immediate parent but anncestors

'''