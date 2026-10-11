class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, ((-dist), (x,y)))
            # pop largest one in heap
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            dist, (x, y) = heapq.heappop(heap)
            res.append((x,y))
        return res


'''

heap
store dist in heap and point
so tuple
use max ehap so easy to remove point that is not important


'''