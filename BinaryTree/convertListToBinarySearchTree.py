def sortedListToBST(head):
    # Helper function to find the middle node and split the list
    def findMiddle(left, right):
        slow = left # initial positions
        fast = left
        # Move fast pointer twice as fast as slow
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Main function that recursively builds the tree
    def convertListToBST(left, right):
        # Base case
        if left == right:
            return None

        # Find the middle node, which will be the root of this subtree
        mid = findMiddle(left, right)
        node = TreeNode(mid.val)

        # Recursively build the left subtree using all nodes from left up to (but not including) mid 
        # in arrays we would pass mid - 1 but in Linked list we dont have direct
        # access we only have pointers to nodes which define the BOUNDARIES of the list segments
        # What passing mid as the Right Bound means in a Linked List
        # convertListToBST(left, mid) call handles nodes in the list up to, but NOT INCLUDING mid
        # passing mid as the right boundary effectively makes mid the "exclusive end" for the left half

        node.left = convertListToBST(left, mid)

        # Recursively build the right subtree
        node.right = convertListToBST(mid.next, right)

        return node

    # Start the recursive process with the head of the list
    return convertListToBST(head, None)
