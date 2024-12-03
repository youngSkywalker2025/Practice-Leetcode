'''
Find the length of the list
Normalize K by setting k = k mod n (incase k > n)
Find the New Head
Update Pointers

Since we are creating a circular linked list and having the new end point to head we dont need the previous pointer to trail.
if we want to rotate list by k that means move k element to the front of the list
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    # Checks if the head is empty or next node after head or k is 0
    if not head or not head.next or k == 0:
        return head

    # Step 1: Find the length of the list
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    # Step 2: Normalize k
    k %= length
    if k == 0:
        return head

    # Step 3: Find the new tail length starts at 1
    new_tail_position = length - k - 1
    new_tail = head
    for _ in range(new_tail_position):
        new_tail = new_tail.next

    # Step 4: Update pointers
    new_head = new_tail.next
    new_tail.next = None
    current.next = head  # Connect tail to head to make it circular

    return new_head


'''
Rotating a List imagine a circular linked list 
get the length 
Normalize K incase k > n 
locate 
'''