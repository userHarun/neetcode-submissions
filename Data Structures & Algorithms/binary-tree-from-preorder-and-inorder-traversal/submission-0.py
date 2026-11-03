# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {val: i for i, val in enumerate(inorder)}
        # keep track of nodes
        self.preIdx = 0
        # helper to build nodes using recurison
        def helper(left,right):
            if left > right:
                return None
            # get root
            root_val = preorder[self.preIdx]
            self.preIdx += 1
            # create node
            root = TreeNode(root_val)

            # find your splits
            
            mid = in_map[root.val] # idx for split

            # recurse into left and right splits

            root.left = helper(left,mid - 1)

            root.right = helper(mid + 1, right)

            return root
        

        res = helper(0, len(preorder) - 1)
        return res


'''

first node in preorder is a root
everything before root in inorder belongs to left subtree


'''