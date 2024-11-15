'''
Involves creating a deep copy of a special type of singly linked list where each node has two pointers

Deep Copy: new list is entirely independent of the original list.
basically No node in the new list points to any node in the original list.


Approach:
1. Copy nodes and insert into Original list
2. Assign Random pointers for new nodes
3. Restore the original list and extract the deep copy
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
        new_node = Node(current.val)  # Create a new node
        new_node.next = current.next
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
