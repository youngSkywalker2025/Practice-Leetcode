'''
1. Linked list is formed using the tree's right pointers
2. left pointers of all nodes must be set to None --> because its resembling a Linked list
3. the order of nodes in the flattened list must match the preorder traversal of the original tree
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''Iterative Solution'''


def flatten(root):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        # Connect the current node's right to the top of the stack
        if stack:
            node.right = stack[-1] # sets the right child of the current node to the node at the top of the stack
        node.left = None


''' Optimized Morris Traversal O(1) '''
