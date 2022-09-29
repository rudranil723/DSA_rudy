# what is tail Recursion

# Tail recursion is defined as a recursive function 
# in which the recursive call is the last statement 
# that is executed by the function. 
# So basically nothing is left to execute after the recursion call.


# An example of tail recursive function


def prints(n):

	if (n < 0):
		return 0
	print(str(n), end=' ')

	# The last executed statement is recursive call
	prints(n-1)

	# This code is contributed by Pratham76
	# improved by ashish2021
