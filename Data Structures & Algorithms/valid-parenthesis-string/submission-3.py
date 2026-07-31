class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                # two choicess
                leftMin -= 1
                leftMax += 1


            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

'''
instead of using stks we can just track range of possible open parentheses count
leftMin: The minimum number of unmatched ( we could have (assuming stars act as ) whenever possible to close brackets).

leftMax: The maximum number of unmatched ( we could have (assuming stars act as ( to open more brackets).

'''