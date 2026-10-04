import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        i = 0 # ptr for intervals

        heap = [] # (length, end)
        
        res = [-1] * len(queries)
        '''
        
            [[1, 3], [2, 3], [3, 7], [6, 6]]
                                            i
            [(2, 1), (0, 2), (1, 3), (4, 6), (3, 7), (5, 8)]
                                                         q
            heap = [(1,6), (2, 3), (3,3), (5, 7)]
            -> heap = []
            res = [2,2,3,5,1,-1]
        '''
        for idx, q in sorted_queries:
            # add eligible intervals
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(heap, (e - s + 1, e)) 
                i += 1
                
            # remove expired 
            while heap and q > heap[0][1]:
                heapq.heappop(heap)

            # get res
            if heap:

                res[idx] = heap[0][0] # smallest length

            

        return res

'''
sorting it can help

Brute force:
sort it

loop through queries
look for queries[j] inside intervals
then find all intervals that hold queries[j]
then find the min length.
time would be super slow 

optimized:
1. Sort intervals by start
2. Sort queries (while remembering original indices)
3. Process queries from smallest → largest
4. If interval.start <= query:
       it can become a candidate
5. If interval.end < query:
       it can no longer be a candidate
6. Use a min-heap so the smallest candidate interval is on top


heap holds (length, right)


[[1, 3], [2, 3], [3, 7], [6, 6]]
[(2, 1), (0, 2), (1, 3), (4, 6), (3, 7), (5, 8)]


'''