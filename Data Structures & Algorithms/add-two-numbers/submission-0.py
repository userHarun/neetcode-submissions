# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode(0)
        ptr = res

        while l1 or l2:
            curr_l1 = l1.val if l1 else 0
            curr_l2 = l2.val if l2 else 0

            total = (curr_l1 + curr_l2 + carry)
            carry = total // 10
            # take the total mod 10 in your curr node
            ptr.next = ListNode(total % 10)
            # move ptrs
            ptr = ptr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # append the remaining carry
        if carry:
            ptr.next = ListNode(carry)
        return res.next





'''
what happends if the sum of two digits > 9?

l1 = [1, 8]
l2 = [1, 9]

8 + 9 = 17
we need to take the 7 and carry the 1
17 mod 10 = 7
carry = 17 // 10 = 1
keep the remainder in cur node and carry the 1

what if the lists are different sizes?
just go until one hits NULL and append the last num to the end
[1, 2, 3] + [2, 1]
321 + 12 = 3

'''