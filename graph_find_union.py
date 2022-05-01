from cmath import inf
from collections import defaultdict
from enum import unique
import heapq


class QuickFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # quick find - find parent
    def find(self, x):
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # quick union - find root
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    # quick union
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class UnionFindRank:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        #     return True
        # else:
        #     return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class UnionFindRankCompressed:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False # already in graph no union needed

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# thought, converting the matrix into disjoint sets, then return total number of roots with compressed
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        size = len(isConnected)
        mydissets = UnionFindRankCompressed(size)
        for i in range(size):
            for j in range(i+1, size):
                if isConnected[i][j] > 0:
                    mydissets.union(i, j)

        rootsets = set()
        for i in range(size):
            root = mydissets.find(i)
            if root not in rootsets:
                rootsets.add(root)
        
        print(mydissets.root)
        print(rootsets)
        return len(rootsets)


    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        mydissets = UnionFindRankCompressed(n)
        for val in edges:
            isunion_suc = mydissets.union(val[0], val[1])
            print(mydissets.root)
            if not isunion_suc:
                return False
        
        rootsets = set()
        for i in range(n):
            root = mydissets.find(i)
            if root not in rootsets:
                rootsets.add(root)

        return len(rootsets) == 1

    
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        mydissets = UnionFindRankCompressed(n)
        for val in edges:
            mydissets.union(val[0], val[1])
        
        rootsets = set()
        for i in range(n):
            root = mydissets.find(i)
            if root not in rootsets:
                rootsets.add(root)

        return len(rootsets)

    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        slist = list(s)
        n = len(s)

        # turn pairs into disjoint sets
        myuf = UnionFindRankCompressed(n)
        for e1, e2 in pairs:
            myuf.union(e1, e2)
        print(myuf.root)

        # get all the sets/sub-graphs
        root2component = defaultdict(list)
        for i in range(n):
            root = myuf.find(i)
            root2component[root].append(i)
        
        # within each sub-graph, form the  lexicographically smallest string
        for _, indices in root2component.items():
            chars = []
            for i in indices:
                chars.append(s[i])
            chars = sorted(chars)
        
            # then stitch them back into slist
            for c, i in zip(chars, indices):
                slist[i] = c
                
        return "".join(slist)

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        # using Dijkstra's algorithm
        nrow = len(heights)
        ncol = len(heights[0])

        diff_matrix = [[float(inf)]*ncol for _ in range(nrow)]
        diff_matrix[0][0] = 0
        visited = [[False]*ncol for _ in range(nrow)]
        queue = [(0, 0, 0)]  # difference, x, y

        while queue:
            difference, x, y = heapq.heappop(queue) # getting the cell with min diff
            visited[x][y] = True
            # iterate through four possible directions
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                if 0 <= adjacent_x < nrow and 0 <= adjacent_y < ncol and not visited[adjacent_x][adjacent_y]:
                    curr_diff = abs(heights[adjacent_x][adjacent_y]-heights[x][y])
                    max_diff = max(curr_diff, diff_matrix[x][y])
                    if diff_matrix[adjacent_x][adjacent_y] > max_diff:
                        diff_matrix[adjacent_x][adjacent_y] = diff_matrix
                        heapq.heappush(queue, (diff_matrix, adjacent_x, adjacent_y))
        return diff_matrix[-1][-1]


    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        gid_weight = {}

        def find(node_id):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]
            # The above statements are equivalent to the following one
            #group_id, node_weight = gid_weight.setdefault(node_id, (node_id, 1))

            if group_id != node_id:
                # found inconsistency, trigger chain update
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = (new_group_id, node_weight * group_weight)
            return gid_weight[node_id]

        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # merge the two groups together,
                # by attaching the dividend group to the one of divisor
                gid_weight[dividend_gid] = (divisor_gid, divisor_weight * value / dividend_weight)

        # Step 1). build the union groups
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        results = []
        # Step 2). run the evaluation, with "lazy" updates in find() function
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                # case 1). at least one variable did not appear before
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    # case 2). the variables do not belong to the same chain/group
                    results.append(-1.0)
                else:
                    # case 3). there is a chain/path between the variables
                    results.append(dividend_weight / divisor_weight)
        return results


n = 5
edges = [[0,1],[1,2],[0,2],[3,4]]
sol = Solution()
s = "cba"
pairs = [[0,1],[1,2]]
# heights = [[1,2,2],[3,8,2],[5,3,5]]
# result = sol.minimumEffortPath(heights)
# print(result)

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
result = sol.calcEquation(equations, values, queries)
print(result)