def linked_list_to_array(head):
    # Initialize an empty array to store the result
    result = []

    # Start traversal from the head
    current = head

    # Traverse until the end of the list
    while current is not None: # same thing as while current:
        # Append the current node's value to the result array
        result.append(current.value)

        # Move to the next node
        current = current.next

    return result
'''
Traverse
Append


'''