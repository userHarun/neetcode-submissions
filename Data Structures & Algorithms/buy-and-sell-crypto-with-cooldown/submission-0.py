class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {} #(i, buy/sell) : maxprofit

        def dfs(i, buying):
            if i >=n:
                return 0
            if (i, buying) in cache:
                return cache[(i,buying)]

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                cache[(i,buying)] = max(buy,cooldown)

            else:
                sold = prices[i] + dfs(i + 2, not buying)
                cooldown = dfs(i + 1, buying)
                cache[(i,buying)] = max(sold, cooldown)
            return cache[(i,buying)]

        return dfs(0, True)



'''
cooldown period of one day

total profit we can achieve

brute force recursion:
at each i, you can decide to buy or sell,
if you buy you have a choice of selling or hold ,

if you sold on prev day you cant buy on curr day

so, at the end of each day your status is , holding, sold, and resting

we just need to know at each index if you bought or sold on the prev day


'''