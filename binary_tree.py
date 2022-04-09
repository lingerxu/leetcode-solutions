from platform import node


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
        treequeue.append((root, 1))
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

    def dfs(self):
        curr_node = self
        if not curr_node.left and not curr_node.right:
            return 0

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

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            
        
        

# root = TreeNode(0, TreeNode(3, None), TreeNode(2, None, TreeNode(5, None, None)))
root = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, TreeNode(4, None, None), None)), TreeNode(3, TreeNode(6, None, None), None))
root.prettyprint()
sol = Solution()
result = sol.inorderTraversal(root)
print(result)
