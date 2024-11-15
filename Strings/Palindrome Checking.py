'''
1. Direct Comparison with Two Pointers
Start at both ends of the string.
Compare the characters at the beginning and end
Move inwards, comparing characters until you reach the middle

2. Copy, Reverse, Compare
Create a reverse copy of the string
Compare the original string with the reversed

3. Recursive Approach with Two Pointers
Check if the first and last characters are equal
If they are, move inwards by
recursively call the function on the substring without the first and last characters
'''


def is_palindrome(s):
    s = s.lower()  # Converts string to lowercase
    if len(s) <= 1:  # if length is less than or equal to 1 it is palindrome
        return True
    if s[0] != s[-1]:  # Compares the first and last characters of the string
        return False
    # Creates a substring of s that excludes the first and last characters and makes a recursive call
    return is_palindrome(s[1:-1])
