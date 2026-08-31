class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            carry = ((a & b) << 1) & MASK
            a =  (a ^ b) & MASK
            b = carry
        if a >= MAX_INT:
            a -= 0x100000000 # subtract 2^32

        return a




'''
EDge case in python for negative numbers:
in python integers grow arbitrarily so we our carry will go on forever.
we must use a MASK to represent 32 bits. MASK = 0xFFFFFFFF
Then after each operation, you keep only the lowest 32 bits


we can use XOR operation and then AND for the carried and then left shifted by 1
Then add them together
Instead of adding them we just repeat the process until carry is 0

b = 13 -> 1101
a = 8->   1000
find carry and left shift it
carry = 1000 << = 10000
a = a^b = 0101
b = carry = 10000
REPEAT until b == 0


'''