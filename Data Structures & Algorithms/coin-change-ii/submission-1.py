class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i: int, remaining: int) -> int:
            # Base cases
            if remaining == 0:
                return 1
            if remaining < 0 or i == len(coins):
                return 0
            if (i, remaining) in memo:
                return memo[(i,remaining)]
            # Choice 1: Include coins[i] (stay at index i so we can reuse it)
            # Choice 2: Exclude coins[i] (move permanently to index i + 1)
            memo[(i, remaining)] = dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)
            return memo[(i, remaining)]

        return dfs(0, amount)


'''
knapsack problem
number of combos to make that amount:
1. ways to make amont without using the coin
2. ways to make amount using at least one instance of coin

so brute force would be just adding up those 2 conditions


'''