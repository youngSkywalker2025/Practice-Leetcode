def find_min_rotated_sorted_array(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        # compare midpoint with our high value
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    # low = high we have found our minimum value
    return arr[low]
