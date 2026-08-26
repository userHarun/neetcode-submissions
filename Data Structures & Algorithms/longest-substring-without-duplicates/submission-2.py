class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        if len(s) == 1:
            return 1
        res = float('-inf')
        position = {s[0]: 0}
        i = 0
        for j in range(1, len(s)):
            if s[j] in position:
                if position[s[j]] >= i:
                    i = position[s[j]] + 1
            position[s[j]] = j
            res = max(res, (j - i + 1))
        
       
        return res
        



'''

simplest idea im thinking of is visited set to track duplicates
and sliding window
s = "zxyzxyz"
         i
           j    

oh ok store a hashmap instead with letter-> index
then if we find a letter in the hashmap, we can just to 
map[letter] +1
s = "harza"
       i
         j

{h:0, a:1, r:2, z:3, }

'''