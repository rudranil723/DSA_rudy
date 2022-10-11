def difference(arr, n):
    diff = abs(arr[0]-arr[1])
    for i in range(0, n-1):
        for j in range(1, n):
            if diff < abs(arr[i]-arr[j]):
                diff = abs(arr[i]-arr[j])
    return diff



arr = [7, 9, 5, 6, 3, 2]
n = len(arr)
print(difference(arr, n))