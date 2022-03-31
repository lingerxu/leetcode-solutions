# Definition for singly-linked list and some related functions
def prettyprint(input_data):
    # more of a general function to pretty print things
    if isinstance(input_data, ListNode):
        input_data.prettyprint()
    else:
        print(input_data)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def prettyprint(self):
        head = self
        if head:
            print(f"head [{head.val}] --> ", end="", flush=True)
            curr = head.next
            counter = 100 # to avoid cycles
            while curr and counter > 0:
                print(f"[{curr.val}] --> ", end="", flush=True)
                curr = curr.next
                counter -= 1
        print("None")

def convert_list(input_list):
    if len(input_list) < 1:
        return None
    
    head_node = ListNode(val = input_list[0], next = None)
    current_node = head_node
    for i in range(1, len(input_list)):
        new_node = ListNode(val = input_list[i], next = None)
        current_node.next = new_node
        current_node = new_node
    tail = current_node
    
    return head_node, tail

class Solution(object):
    def split_middle(self, head):
        prev_mid = ListNode(-1)
        middle = fast = head
        while fast and fast.next:
            prev_mid = middle
            middle = middle.next
            fast = fast.next.next
        prev_mid.next = None
        return middle

    def merge(self, left, right):
        prev_head = ListNode(-1)
        prev_node = prev_head

        while left and right:
            if left.val <= right.val:
                prev_node.next = left
                left = left.next
            else:
                prev_node.next = right
                right = right.next
            prev_node = prev_node.next

        prev_node.next = left if left else right
        return prev_head.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        middle = self.split_middle(head)
        left = self.sortList(head)
        right = self.sortList(middle)
        result = self.merge(left, right)
        return result
    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        slow = head
        fast = head
        is_cycle = False
        
        # find the intersect
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                is_cycle = True
                break
                
        if not is_cycle:
            return None
        
        # now slow and fast are both at the intersect
        # next we find the starting point of cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
    

        
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
head, tail = convert_list(input_list)
head.prettyprint()
tail.next = head.next

# head = convert_list([7, 1, 9, 11])
# head.prettyprint()

sol = Solution()
result = sol.detectCycle(head)
if result:
    print(result.val)
    # result.prettyprint()
else:
    print(result)