# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse 2nd half and seperate them
        cur = slow.next
        slow.next = None # seperates it
        prev = None
        while cur:
            temp = cur.next    
            cur.next = prev
            prev = cur
            cur = temp
        
        while prev:
            tmp1,tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head = tmp1
            prev = tmp2




'''
firsst we use fast and slow ptrs to get a ptr near the 2nd half
then reverse the 2nd half

after we swap ptrs beween first and 2nd half
[2,4,6,8,10]
       s
[2,4,6]
[10,8]

'''