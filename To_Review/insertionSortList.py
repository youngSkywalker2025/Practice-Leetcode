'''
Have a singly linked list
Sort the list using insertion sort
return head

starts with first element compares with adjacent element



'''

'''Insertion Sort'''


# Iterate through the list
# extract nodes one by one
# insert them into their correct position in a new or existing sorted list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head):
    # Create a dummy node for the sorted part of the list
    dummy = ListNode(0)  # Acts as the new head for the sorted list
    current = head  # Pointer to iterate through the input list

    while current:
        # Extract the current node
        next_node = current.next  # Save the next node
        # Find the correct position in the sorted part
        prev = dummy
        while prev.next and prev.next.val < current.val:  # iterate
            prev = prev.next
        # Insert the current node into the sorted part
        current.next = prev.next
        prev.next = current
        # Move to the next node in the input list
        current = next_node

    return dummy.next  # Return the head of the sorted list
