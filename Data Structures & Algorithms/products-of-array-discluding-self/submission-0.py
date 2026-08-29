class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * (N)
        prefix = 1
        for i in range(N):
            res[i]= prefix
            # update prefix
            prefix = prefix * nums[i]
        suffix = 1 # will keep track of everything to the right of i
        for i in range(N - 1, -1, -1):
            res[i] *= suffix # 8 * 1
            suffix *= nums[i]
            

        return res

'''

well an optimal solution def uses prefix and suffix 
ex:
nums = [1,2,4,6]
prefix = [1,2,8,48]
suffix = [48,48,24,6]
res =  [48,24,12,8]

at res[i] we would want product of everything left of i and
product of everything right of i.
Which prefix index gives me everything before i?
Which suffix index gives me everything after i?


so res[i] = prefix[i - 1] * suffix[i + 1]

edge case for res[3] i + 1 is out of boounds so just default it to 1

however, we could get O(1) space using a variables for prefix and suffix

ex:
nums = [1,2,4,6]
prefix = 1
loop through
and update prefix as you go left to right
res = [1, 1, 2, 8]
now it holds everything to left of i
now loop through again and calculate answers

'''