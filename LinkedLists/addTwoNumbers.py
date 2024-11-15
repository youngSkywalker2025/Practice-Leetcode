class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# BEST WAY TO UNDERSTAND IS TO DRAW IT OUT
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Initialize dummy node
    dummy = ListNode() # Common Technique
    curr = dummy
    # Initialize pointers and carry
    p1 = l1
    p2 = l2
    carry = 0

    # Add digits until both lists are exhausted
    while p1 or p2:
        # Calculate the sum of the digits and the carry
        total = (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
        # Create a new node with the remainder of the sum ... the second digit if there is one aka tens place
        curr.next = ListNode(total % 10)
        # Update the carry to the quotient of the sum... only want the first digit aka ones place
        carry = total // 10
        # Move pointers to the next nodes if they exist
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None

    # Edge case
    # Add the final carry if necessary...
    if carry != 0:
        curr.next = ListNode(carry)

    # Return the head node of the result linked list, skipping the dummy
    return dummy.next
