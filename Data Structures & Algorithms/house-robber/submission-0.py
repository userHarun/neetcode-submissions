class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * (n + 1)
        dp[n - 1] = nums[-1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        return dp[0]
'''
so we cant rob adjacent houses

well, at each position we can ask should I rob this or skip it

we can start with a recursive implementation first

[1, 2,3,4]

i = 0 rob or skip?
rob
that means we have to go to i + 2: take 1 + 3 = 4
if we skip we go to i + 1: 2 -> 2 + 4 = 6

bottom up:
dp = [6, 6, 4, 4, 0]
i = 3 nums[3] = 4 take it
always takw the number at the end
then do dp[i] = max(dp[i + 1], nums[i] + dp[i + 2] )
s

'''