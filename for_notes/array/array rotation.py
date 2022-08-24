# Program for array rotation


# Approach 1 (Using temp array): This problem can be solved using the below idea:

# After rotating d positions to the left, the first d elements become the last d elements of the array

# First store the elements from index d to N-1 into the temp array.
# Then store the first d elements of the original array into the temp array.
# Copy back the elements of the temp array into the original array


def rotate(L, d, n):
    k = L.index(d)
    new_lis = []
    new_lis = L[k+1:]+L[0:k+1]
    return new_lis


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    N = len(arr)

    # Function call
    arr = rotate(arr, d, N)
    for i in arr:
        print(i, end=" ")

# Approach 2 (Rotate one by one): This problem can be solved using the below idea:

# At each iteration, shift the elements by one position to the left circularly (i.e., first element becomes the last).
# Perform this operation d times to rotate the elements to the left by d position.


# Follow the steps below to solve the given problem.

# Rotate the array to left by one position. For that do the following:
# Store the first element of the array in a temporary variable.
# Shift the rest of the elements in the original array by one place.
# Update the last index of the array with the temporary variable.
# Repeat the above steps for the number of left rotations required.

# Python program to rotate an array by d elements

# Function to left rotate arr[] of size n by d

def Rotate(arr, d, n):


p = 1
while(p <= d):
    last = arr[0]
    for i in range(n - 1):
    arr[i] = arr[i + 1]
    arr[n - 1] = last
    p = p + 1

# Function to print an array


def printArray(arr, size):


for i in range(size):
    print(arr[i], end=" ")

# Driver code
arr = [1, 2, 3, 4, 5, 6, 7]
N = len(arr)
d = 2

# Function calling
Rotate(arr, d, N)
printArray(arr, N)


# Time Complexity: O(N * d)
# Auxiliary Space: O(1)


# Approach 3 (A Juggling Algorithm): This is an extension of method 2.

# Instead of moving one by one, divide the array into different sets where the number of sets is equal to the GCD of N and d (say X. So the elements which are X distance apart are part of a set) and rotate the elements within sets by 1 position to the left.

# Calculate the GCD between the length and the distance to be moved.
# The elements are only shifted within the sets.
# We start with temp = arr[0] and keep moving arr[I+d] to arr[I] and finally store temp at the right place


# Python3 program to rotate an array by
# d elements
# Function to left rotate arr[] of size n by d


def leftRotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):

        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

# UTILITY FUNCTIONS
# function to print an array


def printArray(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")

# Function to get gcd of a and b


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
leftRotate(arr, d, n)
printArray(arr, n)

# This code is contributed by Shreyanshi Arun

# Time complexity : O(N) 
# Auxiliary Space : O(1)