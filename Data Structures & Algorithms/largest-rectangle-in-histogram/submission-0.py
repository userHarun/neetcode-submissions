class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        area = 0
        for i in range(n):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx, height = stack.pop()
                width = i - idx
                area = max(area, height * width)
                # idx can extend to this one so track it
                start = idx
            # push left most idx it can extend
            stack.append((start, heights[i]))
        # there were no values smaller in the stack
        # so we know they can make a rectangle all the way up until N
        print(stack)
        while stack:
            idx,height = stack.pop()
            width = n - idx
            area = max(area, height * width)
        return area


'''
montonic stack that holds (idx, height)
if you finda smaller heeight while iterating,
pop frm the stack and calc max Area
area would be width * height
width can be calcd by curr idex minues idx for height in stack


'''