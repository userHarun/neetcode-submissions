class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # nlogn
        n = len(nums)
        res = []
        # n* 2^n
        def dfs(i, path):
            if i == n:
                res.append(path[::])
                return
           
            # include 
            path.append(nums[i])
            dfs(i + 1, path)
            # exclude
            path.pop()

            # if theres a duplicate we skip it
            # make sure you're inbounds
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, path)
        
        dfs(0,[])
        return res


'''


'''