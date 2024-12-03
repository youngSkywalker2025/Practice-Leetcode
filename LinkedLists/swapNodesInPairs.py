class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    # Base Case
    if not head or not head.next:
        return head

    first = head
    second = head.next

    # Swap nodes
    first.next = swapPairs(second.next)
    second.next = first

    return second
