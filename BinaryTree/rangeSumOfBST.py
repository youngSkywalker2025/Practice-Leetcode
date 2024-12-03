def rangeSumBST(root, Left, Right):
    # Base Case
    if not root:
        return 0

    # Sum of nodes within the range
    total_sum = 0

    # if current value falls within range
    if Left <= root.val <= Right:
        total_sum += root.val
    # if current node is greater than Left Boundary
    if root.val > Left:
        total_sum = total_sum + rangeSumBST(root.left, Left, Right)
    # if current node value is less than right boundary
    if root.val < Right:
        total_sum += rangeSumBST(root.right, Left, Right)

    return total_sum
