
def rev(n, temp):

    # base case
    if (n == 0):
        return temp

    # stores the reverse of a number
    temp = (temp * 10) + (n % 10)

    return rev(n // 10, temp)


# Driver Code
n = int(input())
temp = rev(n, 0)

if (temp == n):
    print("yes")
else:
    print("no")
