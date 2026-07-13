class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def back(i, pathSum, path):
            if pathSum == target:
                res.append(list(path))
                return
            if pathSum > target or i == len(nums):
                return
            back(i+ 1, pathSum, path)
            path.append(nums[i])
            back(i, pathSum + nums[i], path)
            path.pop()
        back(0,0, [])
        return res