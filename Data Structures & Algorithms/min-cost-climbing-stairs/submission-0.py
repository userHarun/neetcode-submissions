class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}
        def recurse(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(recurse(i+1), recurse(i+2))
            return cache[i]
        
        return min(recurse(0), recurse(1))


'''

'''