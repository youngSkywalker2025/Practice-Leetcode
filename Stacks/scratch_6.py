"""
DFS: Preorder, Inorder, PostOrder
PreOrder: Root, Left, Right
Inorder: Left, Root, Right
PostOrder: Left, Right, Root

Stack plays the role of a temporary memory in the iterative inorder traversal
* Simulating Recursion: pushing nodes onto stack to rmr for later
* Backtracking: reached leftmost node in subtree, need to backtrack and visit parent node
* Maintaining Order: stack ensures visit the nodes in correct sequence
"""


def inorder_traversal_iterative(root):
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
