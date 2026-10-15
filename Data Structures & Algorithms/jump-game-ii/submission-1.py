class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        res = 0
        while r < n - 1:
            furthest = 0
            # loop through window
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])

            l = r + 1
            r = furthest
            res += 1
        return res

'''
you have nums[i] choices
so if nums[i] = 2
we have jump 1 or 2 steps
and then we just want to reach the end

bottom up dp:
dp[i] = fastest way to reach the end ( total)
nums = [2,4,1,1,1,1]
          i
dp =   [2,1,4,3,2,1,0]

4 - len(nums) - 1 = 0 so take 1 + 0
we need the furthest index we can jump to by end = min(n, i + nums[i] + 1)
try positinos from i + 1 to end - 1
dp[i] = min(dp[i], 1 + dp[j])

O(n^2) time and space is o(n)

optimal approach is greedy using windows and finding the min jump to reach to end
from the windows

the furthest jump it can make would classify the right ptr of the window

'''