class Solution:
    # def smallestEvenMultiple(self, n: int) -> int:
    def smallestEvenMultiple(n):
        m = 2
        i = 3
        while (i <= n):
            if m % i == 0:
                print(m)
                break
            m = m*2
        i=+1
    n = int(input())
    print(smallestEvenMultiple(n))
