'''
3 Pointers to reverse list
Previous Ptr: our previous node that our current node will point to
Current Ptr: our current node that we are reversing
Next_node Ptr: to keep track of our list

Recursive Solution: best way to understand is to trace and draw it out
'''


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Temp holds the next node so dont lose rest of list
        current.next = prev  # Reverses pointer of current making it point to previous node
        prev = current  # advances prev to the current node
        current = next_node  # advances current to next node that was stored earlier

    return prev  # Prev is the new head of the reversed list


def reverse_linked_list_recursive(head):
    # Base case: if the list is empty or has one node, it's already reversed
    if not head or not head.next:
        return head

    # Recursively reverse the rest of the list
    new_head = reverse_linked_list_recursive(head.next)

    # Reverse the current node's link
    head.next.next = head
    head.next = None
    # as each recursive call unwinds we need to keep passing this new_head up to ensure original caller of function retrieves it as the final result
    return new_head

