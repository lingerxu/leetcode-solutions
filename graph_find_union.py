from enum import unique


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

n = 5
edges = [[0,1],[1,2],[0,2],[3,4]]
sol = Solution()
result = sol.countComponents(n, edges)
print(result)