class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def brute(i):
            if i in memo:
                return memo[i]
            longest = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    longest = max(longest, 1 + brute(j))
            memo[i] = longest

            

            return longest


        res = 0
        for i in range(n):
            res = max(brute(i), res)
        
        return res


'''

brute force with memo -> o(n^2)
dp is optimal



'''