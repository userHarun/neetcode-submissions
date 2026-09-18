class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cache = {}
        def jump(i):
            
            if i >= n:
                return False
            if i == n - 1:
                return True
            if i in cache:
                return cache[i]
            for path in range(1, nums[i] + 1):
                if jump(i + path):
                    cache[i] = True
                    return True 
            cache[i] = False
            return False
            
        return jump(0)