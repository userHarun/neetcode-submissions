# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap  = []
        dummy = ListNode(-1)
        for i, node in enumerate(lists):
            # add to heap
            if node:
                heapq.heappush(heap, (node.val, i, node))

        curr = dummy
        while heap:
            val, idx, smallestNode = heapq.heappop(heap)
            curr.next = smallestNode
            curr = curr.next
            if smallestNode.next:
                heapq.heappush(heap, (smallestNode.next.val, idx, smallestNode.next))
        
        return dummy.next
'''
use heap to keep a track of smallest numbers and pop to add to res



'''