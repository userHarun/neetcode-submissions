class Solution:
    def numDecodings(self, s: str) -> int:

        res = 0
        dp = {len(s): 1}
        # memo = {} 
        # def dfs(i):
        #     ways = 0
        #     if i in memo:
        #         return memo[i] # memo: {index: number of decoding from index}
        #     if i == len(s):
        #         return 1
            
        #     # single digit
        #     if 1 <= int(s[i]) < 10:
        #         ways += dfs(i + 1)
        #     # double digit
        #     if 10 <= int(s[i:i+2]) <= 26:
        #         ways += dfs(i + 2)
            
        #     # store in memo
        #     memo[i] = ways
        #     return memo[i]
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            # two digit avail
            if i + 1 < n and (s[i] == "1" or (s[i] == '2' and s[i + 1] in '0123456')):
                dp[i] += dp[i+2]
        
        return dp[0]
'''

s = '303' impossibl
brute force with recursion
start at i = 0
try to decode
2 choices, decode curr number or take next number plus current

dp

s = '121'


'''