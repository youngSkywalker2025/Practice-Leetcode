def rotate(nums: list[int], k: int) -> None:
    """
    Rotates the array nums to the right by k steps using an extra array.
    """
    n = len(nums) # getting the size of nums
    k %= n  # Normalize k... say array size is 4 but k is 5... well according to modular arithmetic 1 shift is equivalent to 5 shifts
    temp = [0] * n # creates a new list called temp filled with zeros and its length is equal to the value of n

    for i in range(n): # looping
        new_index = (i + k) % n # (i+k) gives us the shifted position then we % n in-case rotations exceed size of array
        temp[new_index] = nums[i]

    nums[:] = temp  # Copy temp back to nums


