class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''


'''
def deleteDuplicates(head):
    # Dummy node to handle edge cases... common convention
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy  # This will track the last node with unique value

    while head:

        # Check if it's a start of duplicates sublist
        if head.next and head.val == head.next.val:
            # start of duplicates sublist
            while head.next and head.val == head.next.val: # Skip all nodes with the same value
                head = head.next
            prev.next = head.next # Link prev node to the node after the duplicates
        # No Duplicates
        else:
            prev = prev.next # No duplicates, move prev pointer
            
        # Move forward
        head = head.next

    return dummy.next
