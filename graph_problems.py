# graph problems
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph1(self, node): #DFS iteratively
        if not node:
            return node
        clone_dict = {node: Node(node.val)}
        stack = [node]
        while stack:
            curr_node = stack.pop()
            for neigh in curr_node.neighbors:
                if neigh not in clone_dict:
                    stack.append(neigh)
                    clone_dict[neigh] = Node(neigh.val)
                clone_dict[curr_node].neighbors.append(clone_dict[neigh])
        return clone_dict[node]

adjList = [[2,4],[1,3],[2,4],[1,3]]
node_list = []
for i in range(0, len(adjList)):
    new_node = Node(val = i+1)
    node_list.append(new_node)
for i, val in enumerate(adjList):
    neigh_list = val
    for neigh_val in neigh_list:
        node_list[i].neighbors.append(node_list[neigh_val-1])

for node in node_list:
    print(node.val)
    print(f"neighs {node.neighbors[0].val} {node.neighbors[1].val}")

so = Solution()
result = so.cloneGraph1(node_list[0])
print(result.val)