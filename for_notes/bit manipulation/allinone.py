# Python program to implement all the
# above functionalities
# Function to get the bit at the
# ith position
def getBit(num, i):

    # Return true if the ith bit is
    # set. Otherwise return false
    return ((num & (1 << i)) != 0)

# Function to set the ith bit of the
# given number num


def setBit(num, i):

    # Sets the ith bit and return
    # the updated value
    return num | (1 << i)

# Function to clear the ith bit of
# the given number N


def clearBit(num, i):

    # Create the mask for the ith
    # bit unset
    mask = ~(1 << i)

    # Return the update value
    return num & mask


# Driver Code
# Given number N
N = 70
print("The bit at the 3rd position from LSB is: ", 1 if (getBit(N, 3)) else '0')

print("The value of the given number",
      "after setting the bit at", "LSB is: ", setBit(N, 0))

print("The value of the given number",
      "after clearing the bit at", "LSB is: ", clearBit(N, 0))

# This code is contributed by shivanisinghss2110
