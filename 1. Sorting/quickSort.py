def quicksort(arr):
    if len(arr) <= 1:
        return arr

    def partition(low, high):
        pivot = arr[low]  # pivot selection
        left = low + 1
        right = high

        while True:
            # Move left pointer to the right until we find a value greater than the pivot
            while left <= right and arr[left] <= pivot:
                left += 1

            # Move right pointer to the left until we find a value less than or equal to the pivot
            while left <= right and arr[right] > pivot:
                right -= 1

            # If pointers have crossed, end the partitioning phase
            if left > right:
                break

            # Swap elements at the left and right pointers
            arr[left], arr[right] = arr[right], arr[left]

        # Place the pivot element in its final sorted position
        arr[low], arr[right] = arr[right], arr[low]
        return right

    def quicksort_helper(low, high):
        # Base case for recursion
        if low < high:
            partition_pos = partition(low, high)
            quicksort_helper(low, partition_pos - 1)  # Recursively sort left partition
            quicksort_helper(partition_pos + 1, high)  # Recursively sort right partition

    quicksort_helper(0, len(arr) - 1)
    return arr

'''
*Divide-and-Conquer: embodies this principle by breaking down a problem into smaller, self-similar subproblems, 
solving them independently, and combining the results
*Recursion: uses recursion to apply the same sorting logic to smaller and smaller subarrays 
*Efficiency: avg. O(n log n) but in worst-case degrades to O(n^2) choosing an optimal pivot can help mitigate this 

'''