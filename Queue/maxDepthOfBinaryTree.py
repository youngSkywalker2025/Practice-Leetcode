# Binary Tree level Order Traversal
# Going from Left to Right
'''Better for Larger or Deep Trees ....Level-Order Traversal BFS'''

from collections import deque


def maxDepth(root):
    if root is None:
        return 0

    queue = deque([root])  # Start with the root node in the queue
    depth = 0

    while queue:
        depth += 1  # Increment depth for each level
        for _ in range(len(queue)):  # Process all nodes at the current level (loop iterates a specific number times as defined by range)
            node = queue.popleft()  # Remove the node from the queue (Dequeue - front)
            if node.left:
                queue.append(node.left)  # Add left child to the queue (Enqueued - back)
            if node.right:
                queue.append(node.right)  # Add right child to the queue (Enqueued - back)

    return depth

