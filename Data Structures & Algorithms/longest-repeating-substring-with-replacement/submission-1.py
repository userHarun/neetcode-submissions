from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        freq = defaultdict(int)
        max_freq = 0
        res = 0
        while r < len(s):
            #expand
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
            if (r- l + 1) - max_freq <= k:
                # update rs
                res = max(res, (r- l + 1))
                
            else:
                # shrink
                while (r - l + 1) - max_freq > k:
                    freq[s[l]] -= 1
                    l += 1
                

            r += 1
        return res

'''
Input: s = "AAABABBBBBB", k = 1
                l
                      r
s[r] replace with curr ch:
s[r] = A
AAAAA
longest = 4-> 5
keep track of most freq char and to find out if you can fit other chars
is to check window_length - max_frequency <= k

how to efficiently keep track of the freq inside window we can use hash table

freq_map = {3:a, 1: B}

WHEN WIndow becomes invalid we want to move left ptr up and decrease freq of s[l]


'''