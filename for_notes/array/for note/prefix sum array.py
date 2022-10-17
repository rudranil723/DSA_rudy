# # Prefix Sum Array – Implementation and Applications in Competitive Programming


# Given an array arr[] of size n, its prefix sum array is another array prefixSum[] of the same size, such that the value of prefixSum[i] is arr[0] + arr[1] + arr[2] … arr[i].

# Examples : 

# Input  : arr[] = {10, 20, 10, 5, 15}
# Output : prefixSum[] = {10, 30, 40, 45, 60}
# Explanation : While traversing the array, update the element by adding it with its previous element.
# prefixSum[0] = 10, 
# prefixSum[1] = prefixSum[0] + arr[1] = 30, 
# prefixSum[2] = prefixSum[1] + arr[2] = 40 and so on.

# Python Program for Implementing
# prefix sum array

# Fills prefix sum array
def fillPrefixSum(arr, n, prefixSum):

	prefixSum[0] = arr[0]

	# Adding present element
	# with previous element
	for i in range(1, n):
		prefixSum[i] = prefixSum[i - 1] + arr[i]

# Driver code
arr =[10, 4, 16, 20 ]
n = len(arr)

prefixSum = [0 for i in range(n + 1)]

fillPrefixSum(arr, n, prefixSum)

for i in range(n):
	print(prefixSum[i], " ", end ="")

# This code is contributed
# by Anant Agarwal.
