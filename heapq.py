from collections import deque
import heapq

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        treequeue = deque()
        rowidx = 0
        colidx = 0
        treequeue.append((root, rowidx, colidx))
        vertical_tree = []

        # iterate through the tree, calculating coordinates
        while treequeue:
            node, rowidx, colidx = treequeue.pop()
            if node:
                heapq.heappush(vertical_tree, (colidx, rowidx, node.val))
                treequeue.append((node.left, rowidx+1, colidx-1))
                treequeue.append((node.right, rowidx+1, colidx+1))

        vertical_list = []
        mincol = vertical_tree[0][0]
        onelist = []
        while vertical_tree:
            if vertical_tree[0][0] == mincol:
                _, _, val = heapq.heappop(vertical_tree)
                onelist.append(val)
            else:
                mincol = vertical_tree[0][0]
                vertical_list.append(onelist)
                onelist = []
        if onelist:
            vertical_list.append(onelist) # append the last one

        return vertical_list

sol = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(6, None, None)), TreeNode(3, TreeNode(5, None, None), TreeNode(7, None, None)))
result = sol.verticalTraversal(root)
if isinstance(result, TreeNode):
    result.prettyprint()
else:
    print(result)