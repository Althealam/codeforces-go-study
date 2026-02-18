class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        pure_gas = [0]*len(gas) # the left gas at the station i
        for i in range(len(gas)):
            pure_gas[i] = gas[i]-cost[i]
        # sum(pure_gas)=sum(gas)-sum(cost)<0 ==> it can not run all the stations

        start = 0
        current_gas = 0 
        for i in range(len(pure_gas)):
            current_gas+=pure_gas[i]
            if current_gas<0:
                current_gas = 0
                start = i+1
        return start
