class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #
        n = len(coins)
        dp = [[0] * (n + 1) for _ in range(amount + 1)]
        # base case
        dp[0] = [1] * (n + 1)
       
        # skip first row
        for i in range(1, amount + 1):
            # go backwards from cols 
            for j in range(n - 1, -1, -1):
                # can you make this amount using this coin
                # choice 1 exclude coin
                dp[i][j] = dp[i][j + 1]
                # choice 2
                if i - coins[j] >= 0:
                    dp[i][j] += dp[i - coins[j]][j]
        
        return dp[amount][0]
        


'''
knapsack problem
number of combos to make that amount:
1. ways to make amont without using the coin
2. ways to make amount using at least one instance of coin

so brute force would be just adding up those 2 conditions

dp solution with 2 dimesnions of memory
use same approach but store a 2d dp



'''