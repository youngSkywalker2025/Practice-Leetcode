import heapq


def lastStoneWeight(stones):
    # Convert to a max-heap by negating values List Comprehension: concise way to create a new list by applying an
    # operation to each item in an existing iterable (like a list, tuple, or string)
    # -stone is the operation applied to each stone
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    # Keep smashing the two heaviest stones until one or none are left
    while len(stones) > 1:
        #  Pop the two heaviest stones
        y = -heapq.heappop(stones) # Largest
        x = -heapq.heappop(stones) # Second Largest

        # If they are not the same, push the difference back into the heap
        if y != x:
            heapq.heappush(stones, -(y - x))

    # return the last stone or 0 if no stones are left
    return -stones[0] if stones else 0
