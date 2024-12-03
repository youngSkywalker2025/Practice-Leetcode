'''
Goal is to create an entirely new list that replicates the structure and relationships of the original list.
Deep copy: ensures the new list is independent of the original 
'''


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return None

    # Step 1: Create new nodes interleaved with original nodes
    current = head
    while current:
        new_node = Node(current.val)  # Create a new node with the current nodes value
        new_node.next = current.next  # have it point to what current point to
        current.next = new_node
        current = new_node.next

    # Step 2: Assign random pointers for new nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the copied list from the original list
    current = head
    new_head = head.next
    while current:
        copy = current.next
        current.next = copy.next
        current = current.next
        if copy.next:
            copy.next = copy.next.next

    return new_head
