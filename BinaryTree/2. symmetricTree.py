'''Similar as the same tree problem but here we want to check one tree from the root node '''
# if x is None: explicitly check if the var x holds the exact value

def isMirror(leftSub, rightSub):
    # Both are null, so they are mirror images
    if leftSub is None and rightSub is None:
        return True

    # One of them is null, so they aren't mirror images
    if leftSub is None or rightSub is None:
        return False

    # Check if the current nodes are equal
    # and their subtrees are mirrors
    return (leftSub.data == rightSub.data) and \
        isMirror(leftSub.left, rightSub.right) and \
        isMirror(leftSub.right, rightSub.left)


def isSymmetric(root):
    # If tree is empty, it's symmetric
    if root is None:
        return True

    # Check if the left and right subtrees are
    # mirrors of each other
    return isMirror(root.left, root.right)
