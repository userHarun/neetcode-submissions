class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+','-','*','/'}
        stk = []
        for token in tokens:
            res = 0
            if token in operators:
                # pop from stk and do operaton
                b = int(stk.pop())
                a = int(stk.pop())

                if token == '/':
                    res = (a / b)
                elif token == '*':
                    res = (a * b)
                
                elif token  == '+':
                    res = (a + b)
                else:
                    res = (a - b)
                stk.append(res)
        
            else:
                stk.append(token)
        return int(stk[0])


        
'''

[1,2]
+
pop stk
1 + 2 = 3
[3,3, *]
pop 3 * 3 = 9
[9,4,-]
9 - 4 = 5

stk approach

need to change to integer


'''