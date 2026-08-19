class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483648
        res = 0
        while x:
            # extract the digit
            digit = int(math.fmod(x, 10))

            x = int(x / 10)
            # check for overflow
            if (res > MAX // 10) or (res == MAX // 10 and digit > MAX % 10):
                return 0

            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0


            res = res * 10 + digit
        return res
            


'''
we want to extract last digit of x
remove it from x
before adding to res check for overflow
overflow:
If res * 10 + digit would overflow the 32-bit signed integer range:
Return 0.
if not update res = res*10 + digit


'''