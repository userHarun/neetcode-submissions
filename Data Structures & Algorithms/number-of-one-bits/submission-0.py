class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1 if n & 1 else 0
            n >>= 1
        return count

'''
n = 01111111111111111111111111111101
count = 0
we need to check the least signfic bit. we can do that by mod by 2
then keep on checking by shifitng the bin number to the right

1 mod 2 = 1 (increment count)
0 mod 2 = 0
.... 
we can use & instead of mod doesnt matter
this is O(32) because it checks the zeros too



'''
        