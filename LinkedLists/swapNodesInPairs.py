'''Swapping every two adjacent nodes

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):

    if not head or not head.next:
        return head

    dummy = ListNode(0)  # Create a dummy node
    dummy.next = head
    prev = dummy

    while head and head.next:
        # Nodes to be swapped
        first_node = head
        second_node = head.next # so dont lose our list

        # Swapping
        prev.next = second_node # putting first
        first_node.next = second_node.next
        second_node.next = first_node

        # Move pointers ahead
        prev = first_node
        head = first_node.next

    return dummy.next  # Return the head of the modified list