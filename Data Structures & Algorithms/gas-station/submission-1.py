class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        N = len(gas)
        tank = 0
        starting = 0
        total = 0
        for i in range(N):
            tank += gas[i] - cost[i]
            total += gas[i]
            if tank < 0:
                starting = i + 1
                tank = 0
        if total > 0:
            return starting
        return -1
'''


my first idea is to try every index and see if you can circle back to it. but that would be O(gas * cost)
how can we optimize?
well if we start somewhere and fail on station j, that means every index up to gas station J wont work so skip to it

gas  = [4, 2, 1, 3, 5], cost = [2, 3, 2, 5, 1]
lets say we start at gas[0] = 4
eventually we get to station 3. however we get 3 - 5 = -2 < 0
now we know every station in between [0, 3] is invalid


regardless of where we begin we always accumulate the total cost and total gas

if sum(gas) >= sum(cost) then there is a possible index where it will work

therefore we need to track total and tank . total we let us know if its possible to find a solution


'''