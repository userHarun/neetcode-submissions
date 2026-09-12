class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r= 0, n - 1
        maxL = height[l]
        maxR = height[r]
        res = 0
        while l < r:
            #shift smaller ptr a
            if maxL <= maxR:
                l += 1
                maxL = max(height[l], maxL)
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                res += maxR - height[r]
        return res


            

'''
keep track largest height to the left
and largest height to right
then the amount of rain that can be trapped is min(leftmax,rightmax) - height[i]
O(1):
use two ptrs
shift minimum ptr val
also track max values
we really dont need the max value directly to the right because the bottleneck of the min is what helps us
find the trapped rain


'''