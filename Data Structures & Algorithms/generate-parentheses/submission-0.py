class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def dfs(openN, closedN):
            if openN == closedN == n:
                res.append("".join(curr[:]))
            
            # append opens and backtrack
            if openN < n:
                curr.append('(')
                dfs(openN + 1, closedN)
                curr.pop()
            # match opens with closed if closedN < openN
            if closedN < openN:
                curr.append(')')
                dfs(openN, closedN + 1)
                curr.pop()
        dfs(0,0)
        return res

'''

we know we can append N opens

so just naively append N opens

match them with closed if # of closed < # of Opens

we backtrack in both conditions to find more

base case:
if n == OpenN == closedN:
    append to our res 
'''