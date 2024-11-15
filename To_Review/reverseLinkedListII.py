'''
Reverse Sublist of a Linked List II 
Traverse to the starting Position
Reverse the Sublist
Reattach the Reversed Sublist
1 <= m <= n
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, m, n):
    if not head or m == n:
        return head

    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Step 1: Traverse to the (m-1)th node
    for _ in range(m - 1): # since we are reversing the mth node
        prev = prev.next

    # Step 2: Reverse the sublist from m to n
    current = prev.next
    next_node = None
    tail = current
    for _ in range(n - m + 1): # reversing each node individually
        next_node = current.next
        current.next = prev.next
        prev.next = current
        current = next_node

    # Step 3: Reattach the reversed sublist
    tail.next = current

    return dummy.next
