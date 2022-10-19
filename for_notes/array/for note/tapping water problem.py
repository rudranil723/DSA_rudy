# # Trapping Rain Water

# # Given an array of N non-negative integers arr[] representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# # nput: arr[] = {2, 0, 2}
# # Output: 2
# # Explanation: The structure is like below.
# # We can trap 2 units of water in the middle gap.

# Approach 1 (Brute Approach): This approach is the brute approach. The idea is to:

# ollow the steps mentioned below to implement the idea:

# Traverse the array from start to end:
# For every element: 
# Traverse the array from start to that index and find the maximum height (a) and 
# Traverse the array from the current index to the end, and find the maximum height (b).
# The amount of water that will be stored in this column is min(a,b) – array[i], add this value to the total amount of water stored
# Print the total amount of water stored.
# Below is the implementation of the above approach.


# Python3 implementation of the approach

# Function to return the maximum
# water that can be stored
def maxWater(arr, n):

	# To store the maximum water
	# that can be stored
	res = 0

	# For every element of the array
	for i in range(1, n - 1):

		# Find the maximum element on its left
		left = arr[i]
		for j in range(i):
			left = max(left, arr[j])

		# Find the maximum element on its right
		right = arr[i]

		for j in range(i + 1, n):
			right = max(right, arr[j])

		# Update the maximum water
		res = res + (min(left, right) - arr[i])

	return res


# Driver code
if __name__ == "__main__":

	arr = [0, 1, 0, 2, 1, 0,
		1, 3, 2, 1, 2, 1]
	n = len(arr)

	print(maxWater(arr, n))



# Complexity Analysis: 

# Time Complexity: O(N2). There are two nested loops traversing the array.
# Space Complexity: O(1). No extra space is required.