# dynamic programing explore card
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        dp_prev1 = 1
        dp_prev2 = 2

        for i in range(3, n+1):
            dp_curr = dp_prev1 + dp_prev2
            (dp_prev1, dp_prev2) = (dp_prev2, dp_curr)
        
        return dp_curr

sol = Solution()
n = 3
result = sol.climbStairs(n)
print(result)