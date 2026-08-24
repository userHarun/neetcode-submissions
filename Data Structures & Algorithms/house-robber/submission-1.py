class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        num1, num2 = 0, 0
        for n in nums:
            temp = max(n + num1, num2)
            num1 = num2
            num2 = temp
            
        return num2


'''
so we cant rob adjacent houses

well, at each position we can ask should I rob this or skip it

we can start with a recursive implementation first

[1, 2,3,4]

i = 0 rob or skip?
rob
that means we have to go to i + 2: take 1 + 3 = 4
if we skip we go to i + 1: 2 -> 2 + 4 = 6

bottom up:
dp = [6, 6, 4, 4, 0]
i = 3 nums[3] = 4 take it
always takw the number at the end
then do dp[i] = max(dp[i + 1], nums[i] + dp[i + 2] )
s

to optimize space we could use 2 var and keep track of them

num1 = 0, num2 =0
num1  will hold 2 before it , num2 will hold max


[1, 2,3,4]
    n
temp = max(n + num1, num2)  
at the end num2 will have ur max

'''