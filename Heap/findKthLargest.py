import heapq

''' NOTE: using heap as a fixed container '''


def findKthLargest(nums, k):
    # initialize min-heap with the first k elements
    min_heap = nums[:k]  # inclusive of k (creates a sublist or a slice of the original list)
    heapq.heapify(min_heap)  # creates a min-heap in place via the heapify function with our sliced nums array

    # Process the remaining elements in the array
    for num in nums[k:]:
        if num > min_heap[0]:  # compare with the root of min heap
            heapq.heappop(min_heap)  # remove current root
            heapq.heappush(min_heap, num)  # insert new element into heap

    # Root of min-heap is the k-th largest element
    return min_heap[0]


'''
Another way would be to 
1. Build a max heap with n elements 
2. pop from heap k times -> each pop operation takes O(log N) and since need to pop k times -> O(n + k*log n) 
The drawback is if we have a really large array, and K is lets say somewhere in the middle, we would have to do K pops 
'''


