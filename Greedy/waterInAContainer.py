"""
Maximize the water contained in container must consider two factors:
1. Width of the Container: distance between the two lines
2. Height of the Container: height of the shorter line

The water that can be contained between two lines is limited by the SHORTER OF THE TWO LINES.
If we take two lines at indices i and j, the amount of water they can contain is
Water = distance x min(height[i], height[j]); where distance is |j - i|

GREEDY
"""


def maxArea(height):
    left, right = 0, len(height) - 1  # Initialize two pointers
    max_water = 0  # Variable to store the maximum water

    while left < right:
        # Calculate the area with the current left and right pointers
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height

        # Update max_water if the current area is larger
        max_water = max(max_water, current_area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water
