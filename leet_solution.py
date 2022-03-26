class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)

        total_tank = 0
        curr_tank = 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1

sol = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

result = sol.canCompleteCircuit(gas, cost)
print(result)