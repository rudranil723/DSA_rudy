def show(n):
    if n <= 0:
        return 0
    else:
        print(n, end=" ")
        show(n-1)


n = int(input())
print(show(n))
