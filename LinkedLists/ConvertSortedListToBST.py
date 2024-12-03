'''
Note: a list that is sorted when converted to a BST resembles a List leading to O(n) search times negating the benefits of a tree 
Approach
1. use the Middle Element of the list as the root of the BST ---> becomes the root
    if even, either one can become the root
2. Recursively use the left half of the list for the left subtree
3. Recursively use the right half of the list for the right subtree
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedListToBST(head):
    # Base case: if head is None
    if not head:
        return None

    # Helper function to find the middle of the linked list
    def find_middle(left, right):
        slow = left
        fast = left
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Main recursive function
    def convert_to_bst(left, right):
        if left == right:
            return None

        mid = find_middle(left, right)
        root = TreeNode(mid.val)

        # Recursively construct left and right subtrees
        root.left = convert_to_bst(left, mid)
        root.right = convert_to_bst(mid.next, right)

        return root

    return convert_to_bst(head, None)

'''
Find middle of linked list:
Convert to BST:
    recursively construct left and right subtrees
    


'''