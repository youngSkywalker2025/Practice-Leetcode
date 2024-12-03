'''convert to height balanced BST'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):  # constructor of the class,... initialized the variables
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums):
    def build_bst(start, end):
        # Base Case
        if start > end:
            return None
        # Midpoint index
        mid = (start + end) // 2
        node = TreeNode(nums[mid])  # creates a new node with the value at the middle index of nums
        # Recursion
        node.left = build_bst(start, mid - 1)
        node.right = build_bst(mid + 1, end)
        return node
    return build_bst(0, len(nums) - 1)
