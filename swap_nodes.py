from linked_list import convert_list, prettyprint

def swapPairs(head):
    current_node = head
    previous_node = None # since the current_node is the head for this case, it is init as None
    while current_node is not None:
        # check if current_node is the single last node
        # if yes, then return the list_head
        if current_node.next is None:
            return head
        else:
            # if not empty, then we have a pair of nodes for swapping
            swap_node = current_node.next
            if previous_node is None:
                # first swap, meaning that we need to ressign head in this case
                head = swap_node
            else:
                previous_node.next = swap_node
            current_node.next = swap_node.next
            swap_node.next = current_node
            previous_node = current_node
            current_node = current_node.next

    return head


input_list = [1]
head = convert_list(input_list)
swapped = swapPairs(head)
prettyprint(swapped)