class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N

        stk =[]
        stk.append(N - 1)

        # loop backwards
        for i in range(N - 1, -1, -1):
            curr = temperatures[i]
            # if is less than curr pop it
            while stk and temperatures[stk[-1]] <= curr:
                stk.pop()
            # if its not empty now we got the warmer temp
            if stk:
                res[i] = stk[-1] - i
            # always append idx to stk
            
            stk.append(i)
            


        return res


'''
monotonic stk:
start from end of temp because it allows us to find immediate larger val
to the right
append stk with indices
Input: temperatures = [30,38,30,36,35,40,28]
                                    i
stk = [6]
res = [,0,0]
40 > 28: pop, 6, add index 5

stk = [5]
35 < 40 , append 1 
append 35 idx to stk too
stk[4,5]

36 > temp[4] pop it
36 < temp[5] store res and add idx to stk too
stk[3,5]

30 < 36 : store res and add idx to stk
( we are always adding idx to stk, we only pop when its actually greater than the one at the top of the stk)

stk = [2,3,5]
38 > temo[2],temp[3] pop them
its less than temp[5] so add different to res. 
add idx 1
stk[1,5]
30 < 38 append diff again and we are done

'''