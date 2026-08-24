class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        using = set() # to keep track of what num ur using
        res = []
        def back(path):
            if len(path) == N:
                res.append(list(path))
                return
            
            for n in nums:
                if n in using:
                    continue
                path.append(n)
                using.add(n)     
                back(path)
                using.remove(n)
                path.pop()
            
        
        back([])
        return res
        






'''
backtracking:
1
/\
2 3
/ /
3 2
now remove 1 from using and move on to 2
2
/\
1 3
for each number you're on you have n - 1 choices


'''