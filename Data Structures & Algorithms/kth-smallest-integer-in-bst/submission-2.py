# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stk = []
        curr = root

        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left

            curr = stk.pop()
            count += 1

            if count == k:
                return curr.val

            curr = curr.right
'''

in order traversal visits in sorted order for a bst
[2,3,4,5]
stop when len arr == k


'''
