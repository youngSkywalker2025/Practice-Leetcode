'''
Multiply all the elements in the array EXCEPT current element itself and do this for all indexes
Prefix Product: product of all elements to the left of a given index.. so it does not include the element itself
Suffix Loop: calculates product of all elements to the right of each index and multiplies it with the existing values
'''


def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n # creates list that contains n copies of 1

    # Step 1: Calculate prefix products and store in answer
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Step 2: Calculate suffix products and update answer
    suffix = 1
    for i in range(n - 1, -1, -1): # (starting value, ending value, step size)
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
