'''
Use merge sort
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortLinkedList(head):
    # Base case: if the list is empty or has only one element
    if not head or not head.next:
        return head

    # Function to split the linked list into two halves
    def splitList(head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid  # actual splitting occurs this function

    # Function to merge two sorted linked lists
    def mergeLists(l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next  # upwards comparisons

    # Split the list into halves
    left, right = splitList(head)

    # Recursively sort both halves
    left = sortLinkedList(left)  # keep recursing until single element left
    right = sortLinkedList(right)  # keep recursing until single element left

    # Merge the sorted halves
    return mergeLists(left, right)  # occurs on the way up
