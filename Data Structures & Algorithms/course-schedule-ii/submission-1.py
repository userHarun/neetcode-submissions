from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))
        adj = defaultdict(list)
        for course, preq in prerequisites:
            adj[course].append(preq)
        # set for explored
        black = set()
        # for curr being explored
        grey = set()

        res = []

        def dfs(node):
            if node in grey:
                return False

            if node in black:
                return True
            grey.add(node)
            # check its edges
            for preq in adj[node]:
                
                # explore it
                if not dfs(preq):
                    return False
            black.add(node)
            grey.remove(node)
            res.append(node)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res

'''
Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

to take course 0, we must take 1
0->1
1->2
2->0

impossible because there is cycle

so we just have to return the valid ordering 
so store valid ordering in a res arr while doing cycle detec
post order dfs style for adding to res

grey = currently in recursion stack
black = recursion finished
white = unexplored nodes

ex: preq = [[0,1],[1,2]] num courses = 4
create adj list
{0: 1, 1: 2}
start at 0
then we go 1
then we go 2
2 has no preq
append it to our res
res = [2]
now when we are going back up to the path start appending
[2,1,0]
if we ever reacha  cycle just immediately return []



'''