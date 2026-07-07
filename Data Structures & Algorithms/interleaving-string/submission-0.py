class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}

        def inter(i, j):
            k = i + j
            if (i, j) in memo:
                return memo[(i, j)]
            # base case
            if i == len(s1) and j == len(s2):
                return True

            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = inter(i + 1, j)
            # if we havent found valid path from s1 and more chars left in s2
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = inter(i, j + 1)

            memo[(i, j)] = res
            return res

        return inter(0, 0)


"""
naive solution would be generate splits/substrs for s1 /s2 and check if s3 is a combination of them.

if we get to the end of s1 or s2 and didnt move the ptr on both sstrings then its invalid

"aabcc"
   i
"dbbca"  
  j
"aadbbcbcac"
    ^
greedy wont work

we can ask we can finish the string from (i, j) which eventually has overlapping subproblems
so we use DP

how to keep track of chars from s3? we simply do i + j
curr position in s3 is k = i + j

dp = 


"""
