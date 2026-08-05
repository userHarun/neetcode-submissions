class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        
        return res



'''
we Can use exclusive or operation
XOR operation returns true if and only if one of the inputs is true
SO in this case, if we get 2 same numbers it will return 0. if we xor 0 and the single number we get the single number 

nums = [7, 6, 6, 7, 8]

bin(7)  = 111
bin(6) = 110
111 ^ 110 = 001
001 ^ 110 = 111
111 ^ 111 = 000
000 ^ bin(8) = 000 ^ 1000 = 1000 which we return 8
'''