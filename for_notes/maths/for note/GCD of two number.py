n, m = map(int, input().split())
gcd = 1
if n > m:
    small = m
else:
    small = n

for i in range(1, small+1):
    if ((n % i == 0) and (m % i == 0)):
        gcd = i
print(gcd)
