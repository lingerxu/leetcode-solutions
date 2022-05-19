# graph problems
from collections import defaultdict


class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    # def cloneGraph1(self, node): #DFS iteratively
    #     if not node:
    #         return node
    #     clone_dict = {node: Node(node.val)}
    #     stack = [node]
    #     while stack:
    #         curr_node = stack.pop()
    #         for neigh in curr_node.neighbors:
    #             if neigh not in clone_dict:
    #                 stack.append(neigh)
    #                 clone_dict[neigh] = Node(neigh.val)
    #             clone_dict[curr_node].neighbors.append(clone_dict[neigh])
    #     return clone_dict[node]

class Solution(object):
    def __init__(self):
        self.rank = {}
        self.graph = defaultdict(list)
        self.conn_dict = {}
    
    def formGraph(self, n, connections):
        # Reinitialize for each test case
        self.rank = {}
        self.graph = defaultdict(list)
        
        # Default rank for unvisited nodes is None
        for i in range(n):
            self.rank[i] = None
        
        for edge in connections:
            # Bidirectional edges.
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u) 
            self.conn_dict[(min(u, v), max(u, v))] = 1

    def dfs(self, node, discovery_rank):
        # That means this node is already visited. We simply return the rank.
        if self.rank[node] is not None:
            return self.rank[node]
        
        # Update the rank of this node.
        self.rank[node] = discovery_rank
        print(f"current node is [{node}] with discovery_rank {discovery_rank}")
        
        # minimum rank till now from amongst all the neighbors
        # This is the max we have seen till now. So we start with this instead of INT_MAX or something.
        min_rank = discovery_rank + 1
        for neighbor in self.graph[node]:
            # Skip the parent.
            if self.rank[neighbor] is not None and self.rank[neighbor] == discovery_rank - 1:
                continue
                
            print(f"for current node [{node}] getting its neighbor [{neighbor}] with rank {self.rank[neighbor]}")
            # Recurse on the neighbor.
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)
            print(f"for current node [{node}] its neighbor [{neighbor}] recursive_rank is {recursive_rank}")
            
            # Step 1, check if this edge needs to be discarded.
            if recursive_rank <= discovery_rank:
                print(f"REMOVE edge between [{node}] and [{neighbor}]")
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]
            
            # Step 2, update the minRank if needed.
            min_rank = min(min_rank, recursive_rank)
        
        print(f"for node [{node}], min rank is {min_rank}")
        return min_rank

    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        self.formGraph(n, connections)
        self.dfs(0, 0)
        
        result = []
        for u, v in self.conn_dict:
            result.append([u, v])
        
        return result

# adjList = [[2,4],[1,3],[2,4],[1,3]]
# node_list = []
# for i in range(0, len(adjList)):
#     new_node = Node(val = i+1)
#     node_list.append(new_node)
# for i, val in enumerate(adjList):
#     neigh_list = val
#     for neigh_val in neigh_list:
#         node_list[i].neighbors.append(node_list[neigh_val-1])

# for node in node_list:
#     print(node.val)
#     print(f"neighs {node.neighbors[0].val} {node.neighbors[1].val}")
# so = Solution()
# result = so.cloneGraph1(node_list[0])
# print(result.val)

so = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
result = so.criticalConnections(n, connections)
print(result)