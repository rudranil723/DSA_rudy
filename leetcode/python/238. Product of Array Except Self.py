def productExceptSelf(nums):
    p = 1
    num_zeros = nums.count(0)  # Count the number of zeros in the array

    # If there's more than one zero, the result will be all zeros.
    if num_zeros > 1:
        return [0] * len(nums)

    # Calculate the product of all non-zero elements
    for i in nums:
        if i != 0:
            p = p * i

    answer = []
    for i in nums:
        # Check if i is zero
        if i == 0:
            answer.append(p)
        elif num_zeros == 1:
            answer.append(0)
        else:
            answer.append(int(p // i))
    return answer


my_list = [-1, 1, 0, -3, 3]
result = productExceptSelf(my_list)
print(result)
