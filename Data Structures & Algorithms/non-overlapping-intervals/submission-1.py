class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return 0
        count = 0
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        for interval in intervals[1:]:
            start, end = interval[0], interval[1]
            if curr_end > start:
                count += 1
            else:
                curr_start = start
                curr_end = end

        return count 


'''
min

we need to sort first  by end times

[1,2] [1,4], [2,4]

how to check if they overlap?
if the next interval starts before the curr one finishes

compare start of next interval
with end of curr interval
if curr end is > next interval start

intervals=[[1,100],[11,22],[1,11],[2,12]]
we want to remove [1,100], and [2,12]
so i think we just store the inetervals instead of count that we need
to remove
after sorting;
[[1, 11], [2, 12], [11, 22], [1, 100]]

remove the larger interval because it will extend th elongest

so [2,12] is remove
now compare [1,11] [11,22] is valid dont overlap
not compare[1,100] to [11,22] 
overlaps so remove larger which is that [1,100]
'''