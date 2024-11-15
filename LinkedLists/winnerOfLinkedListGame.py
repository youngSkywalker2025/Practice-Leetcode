'''
iterate in pairs from index 0
compare each pairs 1st and 2nd value
'''


def team_winner(head):
    odd_score = 0
    even_score = 0
    index = 0
    current = head

    while current and current.next: # since even length list, will exit loop when reach end of list
        # Compare the even-indexed node with the odd-indexed node (current and current.next)
        if index % 2 == 0:  # even index
            if current.data > current.next.data:
                even_score += 1
            else:
                odd_score += 1
        # Move to the next pair
        current = current.next.next
        index += 2

    # Determine the winner based on scores
    if odd_score > even_score:
        return "Odd"
    elif even_score > odd_score:
        return "Even"
    else:
        return "Tie"
