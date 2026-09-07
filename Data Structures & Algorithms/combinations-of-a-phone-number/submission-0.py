class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        res = []

        phone = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        def dfs(i, curr):
            if len(curr) == n:
                res.append("".join(curr))
                return
            if i > n:
                return
            
            for ch in phone[digits[i]]:
                curr.append(ch)
                dfs(i + 1, curr)
                curr.pop()
        dfs(0, [])

        return res
                

        

'''
[2,9]
2: a,b,c
3: d,e,f
def back tracking brute force approach

digits = '22'


grab first char in map
'a', then since its dfs go down again
res = 'a' + 'a' = "aa"
len(res) == len(digits):
append to final
return out

then backtrack
'a' += 'b' -> "ab"
append and return out
and so on

we need to represent path as list
'''