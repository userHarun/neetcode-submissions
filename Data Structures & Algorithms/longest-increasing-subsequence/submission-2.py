class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i+ 1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])
            
        
        return max(dp)


'''

brute force with memo -> o(n^2)
dp is may be better

we could create a dp arr of size n + 1
each index just holds the LIS from that index

dp = [1, 1, 1,1,2,1]
start from bottom and build it
if nums[j] >nums[i]:
    dp[i]=  max(1 + dp[i + 1],dp[i])


'''