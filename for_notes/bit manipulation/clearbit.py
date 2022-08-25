# Clear Bit:
# This method is used to clear the bit at a particular position(say i)
#  of the given number N. The idea is to update the value of the 
# given number N to the Bitwise AND of the given number N and the
#  compliment of 2i that can be represented as ~(1 << i). 
# If the value return is 1 then the bit at the ith position is set.
#  Otherwise, it is unset.

# Below is the pseudo-code for the same:


# Function to clear the ith bit of
# the given number N

def clearBit(num, i):

	# Create the mask for the ith
	# bit unset
	mask = ~(1 << i)

	# Return the update value
	return num & mask

# This code is contributed by subhammahato348
