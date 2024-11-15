class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
Two pointer technique 
Have a previous pointer that trails current
keep iterating as long as target not found
if target found then skip the node to be removed by assigning previous.next = current.next   
'''
def removeElements(head, val):
    dummy = ListNode(0)  # Create a dummy node to simplify head removal
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        # if target value to remove found
        if curr.val == val:
            prev.next = curr.next  # Skip the current node
        # value not found then keep moving previous and current pointers forward
        else:
            prev = curr  # Move the previous pointer forward
        curr = curr.next  # Move the current pointer forward

    return dummy.next  # Return the head of the modified list

