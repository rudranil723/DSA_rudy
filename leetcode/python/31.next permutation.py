def next_permutation(nums):
    # Find the first element from the right that is smaller than the element to its right.
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # If no such element is found, the entire array is in descending order, and it's the last permutation.
    if i == -1:
        nums.reverse()  # Reverse the array to get the first permutation.
        return

    # Find the smallest element to the right of i that is greater than nums[i].
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1

    # Swap nums[i] and nums[j].
    nums[i], nums[j] = nums[j], nums[i]

    # Reverse the elements to the right of i to get the next permutation.
    nums[i + 1:] = nums[i + 1:][::-1]

# Example usage:
nums = [1, 2, 3]
next_permutation(nums)
print(nums)  # This will print the next permutation.
