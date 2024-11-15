'''
Not given access to the first node of the list**
Guaranteed not to be last node
unique elements
randomly selected node to delete
'''
'''want to remove current node'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteNode(node):
    """
    Deletes a node (except the tail) in a singly linked list.

    :param node: The node to delete.
    """
    if node is None or node.next is None:
        raise ValueError("Cannot delete the last node with this method.")

    # Copy the value from the next node to this node
    node.val = node.next.val
    # Update the next pointer to skip the next node
    node.next = node.next.next
