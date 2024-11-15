'''
Traverse and Retain the First M nodes
After keeping M nodes, delete the next N nodes
Repeat until end of list
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Ask Self: if we are retain M nodes then why only loop execute M - 1 times? --> mentally visualize it
def deleteNodes(head: ListNode, M: int, N: int) -> ListNode:
    current = head

    while current:
        # Step 1: Keep M nodes
        for i in range(1, M):  # loop executes M - 1 times
            if current is None:
                return head
            current = current.next

        # `current` is now at the M-th node
        if current is None:
            return head

        # Step 2: Delete next N nodes
        temp = current.next
        for j in range(N): # loop repeats N times
            if temp is None:
                break
            temp = temp.next

        # Step 3: Link the M-th node to the node after the N deleted nodes
        current.next = temp
        current = temp
        # Repeat Process 

    return head
