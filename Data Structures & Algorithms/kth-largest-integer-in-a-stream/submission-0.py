import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for n in nums:
            # we want our heap to hold kth elements
            if len(self.heap) < k:
                heapq.heappush(self.heap, n )
            elif self.heap[0] < n:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, n)



    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
        

'''
[3, [1, 2, 3, 3]],
k = 3
heap size of 3 min heap
[1,2,3]

len > k
so check if new eleem is > heap smallest elemt
3 > 1?
pop it and push our new number
[2,3,3]

add(3)
[2,3,3] 3 > 2
[3,3,3] return 3



'''