n = int(input())
m = n
sum = 0
while n > 0:
    r = n % 10
    sum = sum*10+r
    n = n//10
if sum == m:
    print("yes")
else:
    print("no")
