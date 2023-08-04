# Write a program to reverse an array or string

# example
# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

# STEPS
# 1) Initialize start and end indexes as start = 0, end = n-1
# 2) In a loop, swap arr[start] with arr[end] and change start and end as follows :
# start = start +1, end = end – 1

def reverse(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


A = [1, 2, 3, 4, 5, 6, 7]
print(A)
n = len(A)
reverse(A, 0, n-1)
print('the reversed array is : ')
print(A)


# Time Complexity: O(n)
# Auxiliary Space: O(1)