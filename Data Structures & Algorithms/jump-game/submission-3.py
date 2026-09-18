class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, - 1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        if goal == 0:
            return True
        return False


'''
dp approach, start from end
reaching is always True
then loop backwards
check the values at the indices
if nums[i] + i  == n -1:
    set its dp[i] to True
then go on
nums = [1,2,1,0,1]
[F,F,F,F,T]
you can see that index 3 cant reach n -1
or index 2 it can go to i = 3 but i = 3 is F
i = 1 can go to index 2 or 3 but both are false
still requires an inner loop to check all those future indice

'''