from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_heap = []
        res = []
        for key, val in freq.items():
            heapq.heappush(max_heap, (-val, key))
        for i in range(k):
            freq, val = heapq.heappop(max_heap)
            res.append(val)

        return res





'''
First approach im thinking of:
freq = {1: 3, 2: 2, 3: 1} k = 2. so maybe we ca sort the in freq in
decreasing order and return 2 key values

Heap approach:
Initialize a heap. in python it is a minheap by default
build freq map again
push all unique elements
pop k elements

We want to push the tuples into the heap with the freq first so (-freq, key)
negative for max heap
(-3, 1), (-2, 2), (-1, 3)

so when we pop k elements it pops 1 first and 2 after.



'''