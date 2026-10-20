import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        low = 1
        high = max(piles)
        while low <= high:
            m = low + (high - low) // 2
            total_hours = 0
            for pile in piles:
                hours = (pile + m - 1) // m
                total_hours += hours
            
            if total_hours > h:
                low = m + 1
            else:
                high = m - 1
        return low


'''
binary search on the range

let high = max(piles)
let low = 1
ex:
[1                           25]
Input: piles = [25,10,23,4], h = 4

try mid  = 25 + 1 // 2 = 13

eating rate of 13: [2,1,2,1] -> 6 hours > 4 hours so move low ptr up
[13...25]
13 + 25
mid = 19 -> [2,1,2,1]
[20....25]
m = 22
still same
l = 23 h = 25
m = 24- > [2,1,1,1] ->5
l = m + 1
[25,25]
m = 25 -> [1,1,1,1]-> 4 yes works so 25 is min
and low is our answer because it 


'''