import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        l = 0
        r = 0
        n = len(nums)
        heap = []

        while r < n:
            
            heapq.heappush(heap, (-nums[r], r)) 

            while r - l + 1 == k:
                while heap and heap[0][1] < l:
                    heapq.heappop(heap)
                largest = heap[0][0] * (-1)
                res.append(largest)
                l += 1
            r += 1

        return res

'''

prob want to use a heap

largest element at top of heap
[2,1,1] -> largest = 2
shift ptrs
[2,1,0]
we also need index so if we know if its not valid 
well, we know that the left ptr will always will always be removed from heap
maybe use a tuple
heap = (val, idx)
[(-2,1), (-1,0), (-1,2)]


checl if the index of this heap element still >= L
if not pop it
ex:
l = 2
[(2,1)]
1 <= 2 so pop it
'''