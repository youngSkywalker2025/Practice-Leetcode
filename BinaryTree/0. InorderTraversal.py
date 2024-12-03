class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    result = []

    def helper(node):
        if not node:
            return
        helper(node.left)  # Visit left subtree
        result.append(node.val)  # Visit root
        helper(node.right)  # Visit right subtree

    helper(root)
    return result


'''
Keep recursing on the left side once reach null node the base case is met --> return 
so now it returns to the previous state which is the node before the null
now it continues code execution which in our code is result.append(node.val) 
and then it will call the right hand side '''

