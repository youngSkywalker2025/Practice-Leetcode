'''
Two-Pointer Technique
Initialize pointers for both arrays
Compare the current elements of Array A and Array B
Append the smaller element to a new array and move the pointer in which the element was taken from
Once one of the arrays is exhausted append all remaining elements from the other array
'''


def merge_sorted_arrays(A, B):
    # store sorted array
    result = []
    # pointers to iterate each array respectively
    i = 0
    j = 0

    # Process elements until one collection is exhausted
    while i < len(A) and j < len(B):
        # Comparison and Decision-Making
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1

    # Append remaining elements
    while i < len(A):
        result.append(A[i])
        i += 1

    while j < len(B):
        result.append(B[j])
        j += 1

    return result


'''
Two-Pointer Technique:
Have two or more collections (arrays or lists) that need to compare, merge, analyze based on relative positions 
Collections are often sorted or require sequential processing
'''
