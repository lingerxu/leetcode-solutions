from collections import deque
import math
from platform import node

from numpy import insert


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def prettyprint(self):
        root = self
        if not root:
            return None
        
        treequeue = []
        treequeue.append((root, 1)) # col index
        while treequeue:
            # go through current level first
            level_length = len(treequeue)
            head_node, level_head_index = treequeue[0]
            # if all elements in queue are null, then do not print, meaning
            # that this level is empty
            num_nones = sum(x is None for x, _ in treequeue)
            if num_nones == level_length:
                print("end of tree")
                break
            for _ in range(level_length):
                node, col_index = treequeue.pop(0)

                #prepare for the next level
                if node:
                    val = node.val
                    print(f"-{val}-", end="")

                    if node.left:
                        treequeue.append((node.left, 2*col_index))
                    else:
                        treequeue.append((None, 2*col_index))
                    if node.right:
                        treequeue.append((node.right, 2*col_index+1))
                    else:
                        treequeue.append((None, 2*col_index+1))
                else:
                    print(f"-[]-", end="")
            print("")

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        treequeue = []
        treequeue.append((root, 1))
        max_width = 0
        
        while treequeue:
            length_level = len(treequeue)
            _, level_head_index = treequeue[0]
            for _ in range(length_level):
                node, col_idx = treequeue.pop(0)

                #prepare for the next level if not end
                if node.left:
                    treequeue.append((node.left, 2*col_idx))
                if node.right:
                    treequeue.append((node.right, 2*col_idx+1))

            max_width = max(max_width, col_idx-level_head_index+1)
        
        return max_width

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return 0

        level = 0
        treequeue = deque([root])

        while treequeue:
            # go through current level first
            level_length = len(treequeue)
            
            for _ in range(level_length):
                # pop the first node from tree queue
                curr = treequeue.popleft()

                #prepare for the next level
                if curr.left:
                    treequeue.append(curr.left)
                if curr.right:
                    treequeue.append(curr.right)

            # go to next level
            level += 1
            
        return level

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = [] # a queue to store the roots of current level
        stack.append(root)
        while stack:
            curr = stack.pop()
            if curr:
                result.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
                
        return result

    def preorderTraversalMorris(self, root):
        result = []
        curr = root
        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    result.append(curr.val)
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        return result

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = [] # a queue to store the roots of current level
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
                
        return result

    def inorderTraversalMorris(self, root):
        result = []
        curr = root
        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    result.append(curr.val)
                    curr = curr.right
        return result

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ##### use visited flag ####
        # result = []
        # stack = [(root, False)]
        # while stack:
        #     curr, visited = stack.pop()
        #     if curr:
        #         if visited:
        #             result.append(curr.val)
        #         else:
        #             # postorder append to stack
        #             stack.append((curr, True))
        #             if curr.right:
        #                 stack.append((curr.right, False))
        #             if curr.left:
        #                 stack.append((curr.left, False))

        # return result
        #### the reverse preorder method ####
        result = []
        stack = [root] # a queue to store the roots of current level
        while stack:
            curr = stack.pop()
            if curr:
                result.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                
        return result[::-1]

    def postorderTraversalMorris(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        dummyhead = TreeNode(-1, None, None)
        curr = dummyhead
        curr.left = root
        while curr:
            if not curr.left:
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev = curr.left
                    counter = 1
                    while prev.right and prev.right != curr:
                        result.append(prev.val)
                        prev = prev.right
                        counter += 1
        return result
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        level = 0
        treequeue = [root]

        while treequeue:
            levels.append([])
            # go through current level first
            level_length = len(treequeue)
            
            for _ in range(level_length):
                # pop the first node from tree queue
                curr = treequeue.pop(0)
                levels[level].append(curr.val)
                #prepare for the next level
                if curr.left:
                    treequeue.append(curr.left)
                if curr.right:
                    treequeue.append(curr.right)

            # go to next level
            level += 1

        return levels

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        treequeue = deque([root])
        is_symmetric = True
        while treequeue:
            len_level = len(treequeue)
            curr_level = []
            for _ in range(len_level):
                curr = treequeue.popleft()
                if curr:
                    curr_level.append(curr.val)
                    treequeue.append(curr.left)
                    treequeue.append(curr.right)
                else: # could be None o!
                    curr_level.append(-101)

            if curr_level != curr_level[::-1]:
                return False

        return is_symmetric

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                curr.left, curr.right = curr.right, curr.left
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        return root

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, targetSum - root.val)]
        while stack:
            curr, curr_sum = stack.pop()
            if not curr.left and not curr.right and curr_sum == 0:
                return True
            if curr.right:
                stack.append((curr.right, curr_sum - curr.right.val))
            if curr.left:
                stack.append((curr.left, curr_sum - curr.left.val))
        
        return False

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # if it is sorted, then just two lines of code:
        # while root and root.val != val:
        #     root = root.left if root.val < val else root.right
        # return root 
        if not root:
            return None
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == val:
                return curr
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return None

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        curr = root
        while curr:
            prev = curr
            if val > curr.val:
                curr = curr.right
            else: # smaller
                curr = curr.left

        if val < prev.val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)

        return root

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        prev = -2**31-1
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            
            if root.val <= prev:
                return False

            prev = root.val
            root = root.right
        
        return True

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nodeset = set()
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if (k - curr.val) in nodeset:
                return True
            nodeset.add(curr.val)
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)

        return False

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
                
        # # establish a set of nodes travelled to reach p
        # stackp = []
        # curr = root
        # while curr and curr.val != p.val:
        #     stackp.append(curr)
        #     if p.val < curr.val:
        #         curr = curr.left
        #     else:
        #         curr = curr.right
        
        # # go through each node is see if there is q with bts range guide
        # # go from low to high with stack FILO
        # while stackp:
        #     subroot = stackp.pop()
        #     curr = subroot
        #     while curr and curr.val != q.val:
        #         curr = curr.left if q.val < curr.val else curr.right
        #     if curr: # meaning search success
        #         return subroot
        #     # else it means that this subtree is exhausted but q is not there
        
        # return None # this should not happen!

# root = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, TreeNode(4, None, None), None)), TreeNode(3, TreeNode(6, None, None), None))
root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
# root = TreeNode(2, TreeNode(1), TreeNode(3))

root.prettyprint()
sol = Solution()
p = TreeNode(4)
q = TreeNode(2)
result = sol.lowestCommonAncestor(root, p, q)
if isinstance(result, TreeNode):
    result.prettyprint()
else:
    print(result)