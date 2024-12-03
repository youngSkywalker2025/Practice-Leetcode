class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    # Base Case
    if root is None:
        return None

    # Swap the children of node
    root.left, root.right = root.right, root.left
    # recursion
    invert_tree(root.left)
    invert_tree(root.right)

    return root
