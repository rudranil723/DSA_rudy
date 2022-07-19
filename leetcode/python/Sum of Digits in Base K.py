class Solution:
    # def sumBase(self, n: int, k: int) -> int:
    def sumBase(n, k):
        sum = 0
        while n > 0:
            r = n % k
            sum = sum+r
            n = n//k
        return sum
    print(sumBase(10, 10))

# first problem i solvced totally by myself, started to understand leetcode
