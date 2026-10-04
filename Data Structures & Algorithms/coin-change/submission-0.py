class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for curr_amount in range(1, len(dp)):
            for c in coins:
                if curr_amount >= c:
                    dp[curr_amount] = min(1 + dp[abs(c - curr_amount)],dp[curr_amount] )

        if dp[amount] != float('inf'):
            return dp[amount]
        return -1

'''
dp[i] = minimum number of coins needed to make amount i

so dp is based on amount and not coins

amount = 6
dp = [0,0, 0 ,0 ,0 ,0 , 0]
          
coins = [1,3,4]
           i

            curr amount = 5
            /     |    \
            dp[4] dp[2] dp[1]
            take min of these conditions


coin <= curr_amount
'''