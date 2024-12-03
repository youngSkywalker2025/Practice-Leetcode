'''
Using a Set: fast, but may not preserve order
Using a Dictionary Keys: efficient and preserves order

Using a loop and
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    current = head # initial setup
    while current and current.next: # compare current node with nodes next value
        if current.val == current.next.val:
            current.next = current.next.next  # Skip the duplicate
        else:
            current = current.next  # Move to the next node
    return head

