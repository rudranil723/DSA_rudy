def reverse(num):
    newnum = 0
    while num != 0:
        r = num % 10
        newnum = newnum*10+r
        num = num//10
    return newnum


print(reverse(123))
