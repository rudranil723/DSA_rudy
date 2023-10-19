

def productExceptSelf(nums):
    p = 1
    nzero = nums.count(0)
    if nzero > 1:
        return [0 for i in nums]
    for i in nums:
        if i != 0:
            p = p*i

    answer = []
    for i in nums:
        if i == 0:
            answer.append(p)
        elif nzero == 1:
            answer.append(0)
        else:
            answer.append(int(p//i))
    return answer


list = [-1, 1, 0, -3, 3]
print(productExceptSelf(list))
