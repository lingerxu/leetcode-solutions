class Solution:
    def shortestPathLength(self, graph):
        if not graph:
            return 0

graph = [[1,2,3],[0],[0],[0]]
sol = Solution()
result = sol.shortestPathLength(graph)
print(result)