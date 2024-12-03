'''
when hits base case 0 is returned
during return of recursive call count takes place
'''


def maxDepth(root):
    # Base Case
    if root is None:  # Base case: an empty tree has a depth of 0
        return 0

    # Recursion
    left_depth = maxDepth(root.left)  # Recursively find the depth of the left subtree
    right_depth = maxDepth(root.right)  # Recursively find the depth of the right subtree
    return max(left_depth, right_depth) + 1  # once gets to leaf nodes returns 0 for both... and when getting max
    # will be 0 so need to add 1 to account for that level.. each time go up stack adds 1 all the way till root node
