class MinStack:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        ''' 
        2nd stk holds smallest value
        

        '''

    def push(self, val: int) -> None:
        self.stk1.append(val)
        if not self.stk2:
            self.stk2.append(val)
        else:
            # push smallest from top stk1 and stk 2
            smallest = min(self.stk2[-1],val)
            self.stk2.append(smallest)
        

    def pop(self) -> None:
        # pop from both
        self.stk1.pop()
        self.stk2.pop()
    
        

        

    def top(self) -> int:
        return self.stk1[-1]

        

    def getMin(self) -> int:
        return self.stk2[-1]
