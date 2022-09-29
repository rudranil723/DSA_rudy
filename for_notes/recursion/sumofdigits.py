def sumdigit(n, sum):
    if n == 0:
        return sum
    sum = sum+(n % 10)
    sumdigit(n//10, sum)


n = int(input())
sum = 0
print(sumdigit(n, sum))
