'''
Using the Merging technique
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    # Initialize a dummy node to simplify the merged list creation
    dummy = ListNode()
    current = dummy  # Pointer to construct the new list

    # Iterate while both lists are non-empty
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1  # Attach list1's node
            list1 = list1.next  # Move to the next node in list1
        else:
            current.next = list2  # Attach list2's node
            list2 = list2.next  # Move to the next node in list2
        current = current.next  # Move to the newly added node

    # If either list has remaining nodes, attach them
    current.next = list1 if list1 else list2

    # Return the merged list, which starts after the dummy node
    return dummy.next
