"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start) 
        if len(intervals) < 1:
            return 0
        # heap
        meetings = []
        heapq.heappush(meetings, intervals[0].end)

        for interval in intervals[1:]:
            s, e = interval.start, interval.end
            smallest = meetings[0]
            if s >= smallest:
                heapq.heappop(meetings)
                heapq.heappush(meetings, e)
            else:
                heapq.heappush(meetings, e)
        
        return len(meetings)

        


'''
[0 ....40]
start with one meeting room
then check the next one. check if they overlap. 

if next meeting start time starts before the other ends it overlaps
so, [5....10] 5 < 40, so they overlap. and increase meeting rooms count.
store it in hashmap that you needed to add another room so:

well we dont need hashmap because we dont care about previous meetings
we can just use heap because we need to know which rooms become free the earliest


ex: (0, 30), (10, 40), (35, 60)
maybe we can store a tuple for our heap value. (room #, end time)
heap : [(0, 30),(1, 40)]
35 > 30 so we can re use that room. 
if we cant we just append it to the heap with another room because if it wasnt
greater than the smallest in our curr heap, then it doesnt start after any other meetings.

well, we dont actually need to store tuple. we just care about min number of meeting rooms. so just pass it end times to our heap.


ex: intervals = [(0,40),(5,10),(15,20)]
heap = [40]
iterate from 1 onwards
intervals[1]: 5 > 40? no append to heap, [40,10] heapifys: [10, 40]
intervals[2]: 15 > 10? yes so pop the smallest and append this 20.
at the end return length of heap
'''