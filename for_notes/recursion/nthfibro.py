def firbo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return firbo(n-1) + firbo(n-2)


n = int(input())
print(firbo(n))
