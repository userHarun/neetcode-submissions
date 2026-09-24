class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(subs):
            l = 0
            r = len(subs) - 1
            while l < r:
                if subs[l] != subs[r]:
                    return False
                l += 1
                r -= 1
            return True
        res = []
        n = len(s)
        path = []
        def dfs(i, path):
            if i == n:
                res.append(path.copy())
                return
            
            for end in range(i + 1, n + 1):
                substring = s[i:end]
                if isPalindrome(substring):
                    path.append(substring)
                    dfs(end,path)
                    path.pop()

        dfs(0, [])    
        return res



'''
s = 'aab'

['a','a','b']
we can start at i = 0
at i = 0 we can build
a
then 0-1
aa
0-2
aab
backtrack to i = 1
a
1-2
ab
back track to i = 2
b

im just conufsed on how to append to the res in this order
Output: [["a","a","b"],["aa","b"]]


'''