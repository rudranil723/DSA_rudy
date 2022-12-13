def binarysearch(arr, f, l, n):
    # f=first index
    # l= last index
    while l-f > 1:
        mid = (f+l)//2
        if arr[mid] < n:
            f = mid+1
        else:
            l = mid
    if arr[f] == n:
        print(f)
    elif arr[l] == n:
        print(l)
    else:
        print('not found')


arr = [1, 2, 6, 7, 8, 9]
# n = number we are searching
n = 6
f = 0
l = len(arr)-1
binarysearch(arr, f, l, n)
