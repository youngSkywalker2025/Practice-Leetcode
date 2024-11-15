"""
Performing Binary Search on a Matrix is O(m * logn)
More Efficient Approach is: 
Performing Binary Search Vertically and then Horizontally O(log m + log n)
"""


def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)  # Rows in our matrix
    n = len(matrix[0])  # Columns in our matrix

    # performing binary search vertically
    top = 0
    bottom = m - 1

    while top <= bottom:
        row = (top + bottom) // 2
        if matrix[row][0] <= target <= matrix[row][n - 1]:
            start = 0  # starting index
            end = n - 1  # end index
            while start <= end:
                mid = (start + end) // 2
                if matrix[row][mid] == target:
                    return True
                # search right half of array
                elif matrix[row][mid] < target:
                    start = mid + 1
                    # search left half of array
                else:
                    end = mid - 1
            return False  # Target not found in the selected array

        # Search top half of matrix (Smaller)
        # current arrays leading element is greater than our target value
        elif matrix[row][0] > target:
            bottom = row - 1
        # Search Bottom Half of the Matrix (larger)
        # current arrays leading element is smaller than our target value
        else:
            top = row + 1