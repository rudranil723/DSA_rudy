# Write a python function to return minimum and maximum in an array. Your program should make the minimum number of comparisons.


#written below is my process: but here the number of search is high resulting is huge time complexity

list = []
size = int(input())
for i in range(0, size):
    list.append(int(input()))
max = list[0]
min = list[0]
for i in range(0, size):
    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]
print(max, min)


#best case solution :

# Python program of above implementation

# structure is used to return two values from minMax()

class pair:
	def __init__(self):
		self.min = 0
		self.max = 0

def getMinMax(arr: list, n: int) -> pair:
	minmax = pair()

#If there is only one element then return it as min and max both
	if n == 1:
		minmax.max = arr[0]
		minmax.min = arr[0]
		return minmax

#If there are more than one elements, then initialize min and max
	if arr[0] > arr[1]:
		minmax.max = arr[0]
		minmax.min = arr[1]
	else:
		minmax.max = arr[1]
		minmax.min = arr[0]

	for i in range(2, n):
		if arr[i] > minmax.max:
			minmax.max = arr[i]
		elif arr[i] < minmax.min:
			minmax.min = arr[i]

	return minmax

# Driver Code
if __name__ == "__main__":
	arr = [1000, 11, 445, 1, 330, 3000]
	arr_size = 6
	minmax = getMinMax(arr, arr_size)
	print("Minimum element is", minmax.min)
	print("Maximum element is", minmax.max)

# This code is contributed by

#time complexity: O(n)