class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
         
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i+=1
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i+=1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i+=1
        return res

'''
We are dealing with 3 different cases.
first case is append elements that dont need merging at the start,
then we append elements that are overlapping,
then append any left over elemetns
while newIntervals[start] > intervals[end]:
    res.append([start,end])
    append elements that dont need merging

while newIntervals[end] >= intervals[start]
        append merged intergvals

while newIntervals[end] <= intervals[start]:
    append remaining elements( )
'''