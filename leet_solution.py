import numpy as np

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        for _ in range(n):
            result.append([0] * n)

        def fill_circle(val, start, n):
            i = start
            j = start
            for k in range(j, j+n):
                result[i][k] = val
                val += 1
            for k in range(i+1, i+n):
                result[k][j+n-1] = val
                val += 1
            for k in reversed(range(j, j+n - 1)):
                result[i+n-1][k] = val
                val += 1
            for k in reversed(range(i+1, i+n-1)):
                result[k][j] = val
                val += 1
            return val

        val = 1
        start = 0
        while n > 0:
            next_val = fill_circle(val, start, n)
            val = next_val
            n -= 2
            start += 1

        return result

sol = Solution()
result = sol.generateMatrix(4)
print(result)
