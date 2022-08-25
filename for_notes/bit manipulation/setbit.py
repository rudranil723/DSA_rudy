# Set Bit:
# This method is used to set the bit at a particular position(say i)
#  of the given number N. The idea is to update the value of the
# given number N to the Bitwise OR of the given number N and 2i
# that can be represented as (1 << i).
#  If the value return is 1 then the bit at the ith position is set.
#  Otherwise, it is unset.

# Below is the pseudo-code for the same:

# Function to set the ith bit of the
# given number num
def setBit(num, i):

    # Sets the ith bit and return
    # the updated value
    return num | (1 << i)

