# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def preOrder(self, root, arr):
        if root is None:
            arr.append("N")
            return

        arr.append(str(root.val))
        self.preOrder(root.left, arr)
        self.preOrder(root.right, arr)

    def serialize(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        arr = []
        self.preOrder(root, arr)
        return ",".join(arr)

    def deserializePreorder(self, i, arr):
        if arr[i[0]] == "N":
            i[0] += 1
            return None

        root = TreeNode(int(arr[i[0]]))
        i[0] += 1

        root.left = self.deserializePreorder(i, arr)
        root.right = self.deserializePreorder(i, arr)

        return root

    def deserialize(self, data):
        """
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        i = [0]
        return self.deserializePreorder(i, arr)
'''
serialization:
Perform preorder traversal, store node values and insert -1 wherever a node is null.
preorder : go node, left , right
Deserialization: 
Rebuild the tree by reading values in preorder order. If the value is -1, return null. Otherwise, create a node and recursively build its left and right children.
'''
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))