import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 * stone)
        while len(heap) > 1:
            x = -1 * heapq.heappop(heap)
            y = -1 * heapq.heappop(heap)
            remainder = abs(x - y)
            if remainder > 0:
                heapq.heappush(heap ,-1 * remainder)
        

        if heap:
            return heap[0] * -1
        return 0
            





'''
we always want the 2 largest stones
[6,4,3,2,2]
[2,3,2,2]
[2,2,1]
[1]

heap = [-6,-4,-3,-2,-2]
pop first 2 
calc difference 
6 - 4 = 2
2 > 0 so push into heap
[-3,-2,-2,-2]
3 - 2 = 1 > 0
[-2,-2,-1]
2 - 2 = 0 ignore

heap is <= 1
so stop
and pop it if its not empty
return it

'''