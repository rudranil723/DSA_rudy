# This method is used to find the bit at a particular 
# position(say i) of the given number N.
#  The idea is to find the Bitwise AND of the
#  given number and 2i that can be represented as (1 << i).
#  If the value return is 1 then the bit at the ith position is set.
#  Otherwise, it is unset.

# Below is the pseudo-code for the same:


# Function to get the bit at the
# ith position
def getBit(num, i):

    # Return true if the bit is
    # set. Otherwise return false
    return ((num & (1 << i)) != 0)


print(getBit(50, 1))


