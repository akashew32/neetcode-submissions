class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        idx = 0
        n = len(gas)
        curr = 0
        flag = False

        while True:
            total += gas[curr] - cost[curr]
            if total < 0:
                idx = (curr + 1) % n
                total = 0
                flag = True
            curr = (curr + 1) % n
            if flag:
                flag = False
                continue
            if curr == idx:
                return idx
            

            