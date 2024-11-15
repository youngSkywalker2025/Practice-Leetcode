'''
Set Approach:
maintains a set to store the characters in our current window.
'''


def length_of_longest_substring(s: str) -> int:
    char_set = set() # Set to store characters in the current window
    left = 0
    max_length = 0

    # Expanding of our sliding window using right pointer
    for right in range(len(s)):
        # if value is in set slide left pointer until repeat value is no longer in set
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the current character to the set
        char_set.add(s[right])

        # Update the max length of substring
        max_length = max(max_length, right - left + 1)

    return max_length