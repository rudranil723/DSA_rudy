# Python3 code to demonstrate
# to check if list is sorted
# using naive method

# initializing list
test_list = [1, 4, 5, 8, 10]
flag = 0
i = 1
while i < len(test_list):
	if(test_list[i] < test_list[i - 1]):
		flag = 1
	i += 1

if (not flag) :
	print ("Yes, List is sorted.")
else :
	print ("No, List is not sorted.")
