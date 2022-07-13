from collections import deque
import math

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

"""
root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
bSTIterator = BSTIterator(root)
result = bSTIterator.next()
result = bSTIterator.next()
result = bSTIterator.hasNext()
result = bSTIterator.next()
result = bSTIterator.hasNext()
result = bSTIterator.next()
result = bSTIterator.hasNext()
result = bSTIterator.next()
result = bSTIterator.hasNext()
"""
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.curr = root 
        self.stack = []

    def next(self):
        """
        :rtype: int
        """
        if self.curr or self.stack:
            while self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left
            self.curr = self.stack.pop()
            nextval = self.curr.val
            self.curr = self.curr.right
            return nextval

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack or self.curr:
            return True
        else:
            return False

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
        treequeue = deque[root]

        while treequeue:
            levels.append([])
            # go through current level first
            level_length = len(treequeue)
            
            for _ in range(level_length):
                # pop the first node from tree queue
                curr = treequeue.popleft()
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
        stack = [root]
        parent_dict = {root: None}
        while p not in parent_dict or q not in parent_dict:
            curr = stack.pop()
            if curr.left:
                parent_dict[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                parent_dict[curr.right] = curr
                stack.append(curr.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent_dict[p]
        while q not in ancestors:
            q = parent_dict[q]
        return q

    def lowestCommonAncestorBTS(self, root, p, q):
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

    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        # go through all notes, check value boundary
        # because it is bts, it is sorted, so conditions will be
        # < low; > low & < high; > high
        # if < low, then, the node as well as its left side should be trimed
        # parent.left = curr.right
        # if within range, then search left and right sub-trees
        # if > high, parent.right = curr.left
        # edge case check: at least one node, all vals >= 0, sorted, unique bts
        dummyhead = TreeNode(-1, None, root)
        stack = [(root, dummyhead)]
        while stack:
            curr, parent = stack.pop()
            if curr.val < low: # need to trim curr and all its left nodes
                if parent.val > curr.val:
                    parent.left = curr.right
                else:
                    parent.right = curr.right
                if curr.right:
                    stack.append((curr.right, parent))
            elif curr.val > high: # need to trim curr and all its right nodes
                if parent.val < curr.val:
                    parent.right = curr.left
                else:
                    parent.left = curr.left
                if curr.left:
                    stack.append((curr.left, parent))
            else:
                if curr.right:
                    stack.append((curr.right, curr))
                if curr.left:
                    stack.append((curr.left, curr))
                
        return dummyhead.right

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummyhead = TreeNode(-1, None, root)
        curr = root
        prev = dummyhead
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            prev.right = curr
            curr.left = None
            prev = curr
            curr = curr.right
        
        return dummyhead.right

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        curr = root
        # result = []
        counter = k
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            counter -= 1
            if counter < 1:
                return curr.val
            curr = curr.right

        return None # should not happen

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 1. inorder traversal find the node that needs to swapped, 2. swap values
        stack = []
        prev = None
        curr = root
        one = two = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev and curr.val < prev.val:
                one = curr
                if not two:
                    two = prev
                else:
                    break
            prev = curr
            curr = curr.right
        
        one.val, two.val = two.val, one.val

        return root

    # inorder traversal successor
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    # inorder traversal predecessor
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # found key
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            
        return root

root = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, TreeNode(4, None, None), None)), TreeNode(3, TreeNode(6, None, None), None))
root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))

# p = TreeNode(1)
# q = TreeNode(2, p)
# root = TreeNode(3, TreeNode(0, None, q), TreeNode(4))
# root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
root.prettyprint()
sol = Solution()
result = sol.deleteNode(root, 8)
if isinstance(result, TreeNode):
    result.prettyprint()
else:
    print(result)