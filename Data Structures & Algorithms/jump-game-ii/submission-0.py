class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n)
        dp[-1] = 0
        for i in range(n - 2, -1,-1):
            end = min(n, i  + nums[i] + 1)
            for j in range(i + 1, end):
                dp[i] = min(dp[i], 1 + dp[j])
        

        return dp[0]

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
'''