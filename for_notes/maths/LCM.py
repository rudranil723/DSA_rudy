
n, m = map(int, input().split())

if n > m:
    big = n
else:
    big = m
while(True):
    if ((big % n == 0) and (big % m == 0)):
        lcm = big
        break
    big += 1

print(lcm)
