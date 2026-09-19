class Solution:
    def isHappy(self, n: int) -> bool:
        def digitSquareSum(n):
            curr_sum = 0
            while n:
                digit = n % 10
                curr_sum += digit * digit
                n = n // 10

            return curr_sum
        
        fast = digitSquareSum(n)
        slow = n
        while slow != fast:
            slow = digitSquareSum(slow)
            fast = digitSquareSum(fast)
            fast = digitSquareSum(fast)
            print(slow, fast)
        print(slow,fast)
        if slow == 1:
            return True

        return False

'''
naive approach use a hash set
repeatly find sum of squares of digits
if its in our hashset return False
if it eveyr equals 1 return true

use slow/fast ptr approach. if fast reaches slow, we have a cycle.


'''