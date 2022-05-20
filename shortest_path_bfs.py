from collections import deque
import heapq

class Solution:
    def shortestPathLength(self, graph):
        if not graph:
            return 0

    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # Helper function for the A* heuristic.
        def best_case_estimate(row, col):
            return max(n - row - 1, n - col - 1)

        # Check that the first and last cells are open. 
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        visited = set()
        # best estimate distance is max_row - current_row
        # (total distance estimate, distance so far, (cell row, cell col))
        priority_queue = [(1 + best_case_estimate(0, 0), 1, 0, 0)]
        
        while priority_queue:
            # always pop the min
            estimate, distance, row, col = heapq.heappop(priority_queue)
            if (row, col) in visited:
                continue
            if (row, col) == (n-1, n-1):
                return distance
            visited.add((row, col))
            for diff_row, diff_col in directions:
                new_row = row + diff_row
                new_col = col + diff_col
                if not(0 <= new_row < n and 0 <= new_col < n):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                if (new_row, new_col) in visited:
                    continue
                estimate = best_case_estimate(new_row, new_col) + distance + 1
                entry = (estimate, distance + 1, new_row, new_col)
                heapq.heappush(priority_queue, entry)
        
        # There was no path.
        return -1
    
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # the cache for already computed max_increasing_path_length for index (i, j)
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0
            
            # already computed
            if dp[i][j] != -1:
                return dp[i][j]
            
            left = dfs(i, j - 1, matrix[i][j])
            right = dfs(i, j + 1, matrix[i][j])
            top = dfs(i - 1, j, matrix[i][j])
            bottom = dfs(i + 1, j, matrix[i][j])
            
            dp[i][j] = max(left, right, top, bottom) + 1
            return dp[i][j]
        
        result = -1
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j, -1))
        return result

# graph = [[1,2,3],[0],[0],[0]]
sol = Solution()
# grid = [[0,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,1,0,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,0,1,0],[0,0,0,0,0,1,1,0],[1,1,1,1,1,1,1,0]]
# result = sol.shortestPathBinaryMatrix(grid)
matrix = [[9,9,4],[6,6,8],[2,1,1]]
result = sol.longestIncreasingPath(matrix)
print(result)