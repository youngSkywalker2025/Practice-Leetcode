
    """
    Finds the number of times a sorted array was rotated to the right.

    Key insight: sorted rotated array, the minimum element is our pivot point [3,4,5,1,2], meaning amount of indices to left is equal to k.
    # of rotations is equal to the index of the minimum element

    Algorithm:
    1. Find the minimum element: use algorithm to find min element in a rotated sorted array.
    Well in a rotated sorted array to algorithm of choice is binary search (most efficient choice)
    2. Return the Index: the index of the minimum element is the number of rotations
    """
