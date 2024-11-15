def binary_search(arr, target, start, end):
    # base case
    if start > end:
        return -1  # not found searched all the way to last element.... do a visual drawing
    # calculate mid as usual when splitting
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid # returns index of target
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)