class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def back(start, pathSum, path):
            if pathSum == target:
                res.append(list(path))
                return
            
            if pathSum > target or start == len(candidates):
                return

            for j in range(start,len(candidates)):
                if j > start and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                back(j + 1, candidates[j] + pathSum, path)
                path.pop()
        
        back(0, 0, [])
        return res
            

'''
we can try sorting first
[1,1,2,5,6,7,10]
 ^
target = 3
[1,2] = 3
index 1 :[1,2] = 3
we have to deal with the duplicates while exploring
since we sorted we can just check if the prev is the same as curr element when branching
The duplicate check only prevents starting two identical branches from the same level
also we dont make binary choices here, we are asking from the remanining candidates which
candidiate can i take

'''