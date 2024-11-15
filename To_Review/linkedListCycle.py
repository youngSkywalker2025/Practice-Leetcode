'''
Same as linked list cycle problem but this time need to return the node where the cycle begins.
'''


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def detectCycle(head):
    if not head or not head.next:
        return None

    slow, fast = head, head

    # Detect if a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Cycle detected, find the start of the cycle
            pointer = head
            while pointer != slow:
                pointer = pointer.next
                slow = slow.next
            return pointer

    return None
