class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        ans = 0

        for n in snums:
            if n - 1 not in snums:
                length = 1
                while (n + length) in snums:
                    length += 1
                ans = max(ans, length)

        return ans


'''
make it a set
if n + 1 in set
recursively call your function from that num
hash map for quick lookup to return out if its already stored

if you get recursion exceeded in python you need
to use a multiple passes


'''