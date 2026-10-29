# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow = dummy
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        
        # slow.next we need to remove
        slow.next = slow.next.next
        return dummy.next


            
        
        
        
        
        



'''
could reverse and then remove nth node

we need to point the node before n to the node after n

have 2 ptrs
one on head
and other moves n times
the first ptr is on a dummy node (terminal)

after moving fast ptr
move each one by one


'''