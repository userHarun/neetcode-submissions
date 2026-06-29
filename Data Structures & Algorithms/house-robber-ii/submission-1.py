class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robber(nums):
            rob_prev1, rob_prev2 = 0, 0
            for n in nums:
                curr_rob = max(rob_prev2 + n, rob_prev1)
                # shift forward
                rob_prev2 = rob_prev1

                rob_prev1 = curr_rob
            return rob_prev1
        with_first = robber(nums[:-1])
        with_last = robber(nums[1:])
        return max(with_first,with_last)



'''
House robber 1:
dp[i] = max(dp[i - 1] , dp[i - 2 ] + nums[i]) or we use other solution
which was o(1) space solution with 2 vars tracked

so we just perform house robber 1 multiple times
one time where we include the first number and without last 
and once where we include last and not first
return max of those




'''