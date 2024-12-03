# check base case if nodes are none
# check base case if one of the nodes is none
# check base case if the values do not match
# Recursive Case:



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # If both nodes are Null, they are empty trees (technically equal)
    if not p and not q:
        return True
    # If one of the nodes is Null
    if not p or not q:
        return False
    # Now check the values
    if p.val != q.val:
        return False
    # Recursively check the left subtree and right subtree
    # both must be true then will return true
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
