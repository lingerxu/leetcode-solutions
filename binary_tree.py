from collections import deque


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
                    curr_level.append(-1)

            if curr_level != curr_level[::-1]:
                return False

        return is_symmetric

root = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, TreeNode(4, None, None), None)), TreeNode(3, TreeNode(6, None, None), None))
root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))

root.prettyprint()
sol = Solution()
result = sol.isSymmetric(root)
print(result)
