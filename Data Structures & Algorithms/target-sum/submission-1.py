class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def back(i, total):
            # Base case: reached the end of the array
            if i == len(nums):
                return 1 if total == target else 0

            # Return cached result if already computed
            if (i, total) in memo:
                return memo[(i, total)]

            add = back(i + 1, total + nums[i])
            subtract = back(i + 1, total - nums[i])

            # Cache and return the result
            memo[(i, total)] = add + subtract
            return memo[(i, total)]

        return back(0, 0)

'''
so at each index you have 2 choices.
either add it or substract it
it seems like a recursive soln is brute force

time complexity would be 2^n
constraints allow us to use backtracking

can also use dp because its similar to knapsack



'''