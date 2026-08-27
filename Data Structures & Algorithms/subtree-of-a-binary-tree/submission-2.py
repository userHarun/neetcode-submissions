# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root, subRoot):
            return True
        # compare subRoot with left of root or right of root 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        # compare nodes values
        if p.val != q.val:
            return False
        # compare trees structures
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        

        


'''
so we have two roots given to us
we want to find the exact subroot in root
all have to match and there cant be any other descendents

we can use a tree traversal

DFS would be the best
so first start at root: 1
then go down left process
we would use a pre order traversal
process the node, then go down left, then right
1: != 2
dfs(left)-> 2 == subroot
when they equal, you would also traverse subroot and compare them
if we find a node that doesnt equal from then on we know to return
false



'''