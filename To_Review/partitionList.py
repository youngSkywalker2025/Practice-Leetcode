'''
Initialize Pointers
Traverse the Original List
Concatenate the Two Lists
Return the Modified List
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    # Create the Two Separate lists
    before_head = before = ListNode(0)  # Dummy nodes for 'before' list
    after_head = after = ListNode(0)  # Dummy nodes for 'after' list

    current = head
    while current:
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next

    after.next = None  # Important: Terminate the 'after' list
    before.next = after_head.next  # Connect the two lists

    return before_head.next  # Return the head of the partitioned list
