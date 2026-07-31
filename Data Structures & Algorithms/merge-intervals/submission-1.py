class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if merged[-1][1] >= start:
                merged[-1][1] = max(end, merged[-1][1])
            else:
                merged.append([start,end])

            
        return merged


'''
how do we know they overlap?:
if curr intervals end  you are tracking is > new intervals start then the intervals overlap

if they do overlap we can handle them by taking the max(curr_intervals[end], newIntervals[end])

'''