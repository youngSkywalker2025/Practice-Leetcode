"""
What is a cycle?
last element does not point to nullptr instead it points back to the front of list

How to determine if a cycle is present?
Tortoise and Hare (Floyds Cycle Detection)
Tortoise moves one node forward
Hare moves two nodes forward

Approach:
Floyds Cycle Detection
Hash Set

Solution:
Think of two runners running on a circular track and one is twice as fast, the faster runner will eventually overtake the slower runner.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    if not head or not head.next:
        return False  # if either of these conditions is true, it means the linked list cannot possibly have a cycle

    tortoise = head
    hare = head
    # loop continues as long as the tortoise and hare pointers are not pointing to the same node
    while tortoise != hare:
        # check if hare has reached end of list
        if not hare or not hare.next:  # if hare is None (end of list), then not hare evaluates to True... This means that there is no cycle since hare pointer reaches the end of the list
            return False
        tortoise = tortoise.next
        hare = hare.next.next
    # pointing to the same node 
    return True  #  Cycle has been detected
