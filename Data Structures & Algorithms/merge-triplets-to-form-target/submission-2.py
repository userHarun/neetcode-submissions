class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                # skip
                continue
            
            for j, num in enumerate(trip):
                if num == target[j]:
                    good.add(j)
            
        return len(good) == 3

'''
questions? can they be in any order when we update it to match the target

brute force:
go through each triplet and update it with another, if they equal target return true

if we every try to merge a triplet and it has one index that is larger than target values, we just completely ignore that triplet
'''