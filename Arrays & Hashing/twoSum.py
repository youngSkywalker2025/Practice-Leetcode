def twoSum(nums, target):
    num_dict = {}  # To store each number and its index
    for i, num in enumerate(nums):
        complement = target - num
        # if found complement return index of complement and index of current num
        if complement in num_dict:
            return [num_dict[complement], i]
        # if not found add
        num_dict[num] = i  # Hashmap[value] = index
