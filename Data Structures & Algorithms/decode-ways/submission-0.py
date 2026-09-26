class Solution:
    def numDecodings(self, s: str) -> int:

        res = 0
        memo = {} 
        def dfs(i):
            ways = 0
            if i in memo:
                return memo[i] # memo: {index: number of decoding from index}
            if i == len(s):
                return 1
            
            # single digit
            if 1 <= int(s[i]) < 10:
                ways += dfs(i + 1)
            # double digit
            if 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)
            
            # store in memo
            memo[i] = ways
            return memo[i]

            
        
        return dfs(0)
        
        

'''

s = '303' impossibl
brute force with recursion
start at i = 0
try to decode
2 choices, decode curr number or take next number plus current

'''