"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lookup = { None: None}
        dummy = Node(-1)

        dummy.next = head

        curr = head

        while curr:
            # create deep copy and add to map
            newNode = Node(curr.val)
            lookup[curr] = newNode
            curr = curr.next
        

        curr = head
        # set ptrs for copy nodes
        while curr:
            copy = lookup[curr]
            copy.next = lookup[curr.next]
            copy.random = lookup[curr.random]
            curr = curr.next

        return lookup[head]


'''
first pass we create a hashmap an map the original node to new node

2nd pass we actually link them


'''