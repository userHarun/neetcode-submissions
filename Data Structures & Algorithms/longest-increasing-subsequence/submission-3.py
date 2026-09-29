class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tails = []
        
        for x in nums:
            l = 0
            r = len(tails)
            while l < r:
                mid = (l + r) // 2
                if tails[mid] >= x:
                    # 1st index whos val is greater > x
                    r  = mid
                else:
                    l = mid + 1
                
            # now explore if x belongs at the end or should replace mid
            
            if l == len(tails):
                tails.append(x)
            else:
                # Give a subsequence of this length
                # a smaller ending value # 1, 4 , 5 x = 2
                tails[l] = x


                

        return len(tails)
            


'''

brute force with memo -> o(n^2)

we could create a dp arr of size n + 1
each index just holds the LIS from that index

dp = [1, 1, 1,1,2,1]
start from bottom and build it
if nums[j] >nums[i]:
    dp[i]=  max(1 + dp[i + 1],dp[i])


optimal is to use binary search on the arr

for ex:

we encounter a number x. we do binary search and find out if we can add the number
x to tails (a seperate arr to find lis) where it gives us a possibility to extend the subsequence
[1,3,5, 8] x = 4
4 <= 5 so we can replace it

if no number is less than x we can simply just append it to end

If x > everything in tails:
    append x
    → LIS length potentially grows

Otherwise:
    find the first value >= x
    replace it with x
    → LIS length stays the same,
      but we get a better/smaller ending
'''