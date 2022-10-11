# # Write a program to print all the LEADERS in the array.

# # # An element is a leader if it is greater than all the elements to its right side.

# Follow the below steps to implement the idea:

# We run a loop from the first index to the 2nd last index:-

# 1. And for each index, we run another loop from the next index to the last index.
# 2. If all the values to the right of that index are smaller than the index,
# 3.we simply add the value in our answer data structure.


# def leader(arr, n):
#     for i in range(0, n):
#         for j in range(i+1, n):
#             if arr[i] <= arr[j]:
#                 break
#             if j == n-1:
#                 print(arr[i], end=' ')


# arr = [16, 17, 4, 3, 5, 2]
# print(leader(arr, len(arr)))


def printLeaders(arr,size):
	
	for i in range(0, size):
		for j in range(i+1, size):
			if arr[i]<=arr[j]:
				break
		if j == size-1: # If loop didn't break
			print (arr[i],end=' ')

# Driver function
arr=[16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))

