# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(-1)
        groupPrev = dummy
        dummy.next = head
        
        def moveKth(groupEnd):
            count = k
            while groupEnd and count > 0:
                groupEnd = groupEnd.next
                count -= 1
            
            
            return groupEnd

        while True:
            groupEnd = moveKth(groupPrev)
            if not groupEnd:
                break
            


            # reverse
            prev = groupEnd.next # saves rest of list each iteration
            curr = groupPrev.next
            groupNext = groupEnd.next # where we should stop
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            # make it the last node before new group
            groupPrev.next = groupEnd
            groupPrev = tmp
        return dummy.next 

'''
we need to keep track of several references
if reversing:
We need to keep track of the tail of the previous reversed group, because that's the node whose next pointer needs to change.
also keep track of the next nodes

we need a sentinel node for our first group

we need to count nodes to create k 
'''