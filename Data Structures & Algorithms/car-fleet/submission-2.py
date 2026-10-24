class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        
        for p, s in pairs:
            time = (target - p) / s
            if stk and time <= stk[-1]:
                continue
            else:
                stk.append(time)
            
        return len(stk)




'''
so calculate the hours it takes to reach the final destination
if two cars have reach the destination at the same time bundle them
count how many unique cars reach the target in there own mph

target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]
output -> 3
car E can reach car D becasue its faster and then it can join its fleet
so total unique would be 3.
maybe sorting by car sby postion with earliest car at the start

if time of car ahead (held in stk) is greaeter or equal we can make a fleet

sorted->
[10,8,5,3,0]

stk = [1]

pos 8(4mph) time = 1 which is greater than or equal to top of stk
so the car must slow down to the same speed 
stk = [1,7,
7 >= 3 so it can catch it up and create fleet
and turn it into 7 becomes it must slow down
[1,7,12]
at the end check if stk is not empty

return size of stk


'''