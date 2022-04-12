import numpy as np

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid) # how many rows
        n = len(grid[0]) # how many cols and n >= 1
        k = k % (m * n)
        grid_size = m * n

        onelist = []
        for row in grid:
            onelist = onelist + row

        onelist = onelist[grid_size-k:] + onelist[:grid_size-k]

        result = []
        for rowidx in range(m):
            result.append(onelist[rowidx*n:rowidx*n+n])

        return result

sol = Solution()
grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4

result = sol.shiftGrid(grid, k)
