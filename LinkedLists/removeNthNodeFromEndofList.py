"""
Since linked list should know that operations for linked list require pointer adjustments
removing a node will require a prev pointer
Kth node from the end*

Two-Pointer Approach:
Key Idea: is to maintain the distance of N between the fast and slow pointer
once fast pointer reaches last node
slow pointer will be at the node before our target node to remove
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)  # Create a dummy node to handle edge cases
    fast = dummy
    slow = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both fast and slow pointers until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next

    # when breakout from loop slow is at the node BEFORE target node want to remove
    # Skip the target node
    slow.next = slow.next.next

    return dummy.next
