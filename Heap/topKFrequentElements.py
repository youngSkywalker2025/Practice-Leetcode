import heapq
from collections import Counter


def topKFrequent(nums, k):
    # build the frequency map
    freq_map = Counter(nums)

    # Use a min-heap to keep track of the top k frequent elements
    min_heap = []

    # note must convert dictionary items {element:frequency} into a Tuple (element, frequency)  via .items()
    # because heapq module is designed to work with lists
    for num, freq in freq_map.items():
        # iterate through each item which is a tuple (element, frequency) in the map
        # and push the item (frequency, element) into the min-heap while also changing the order of the tuple
        heapq.heappush(min_heap, (freq, num))
        # once our heap exceeds k we will pop
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    # Extract results from the heap
    top_k_elements = [num for freq, num in min_heap]

    return top_k_elements
