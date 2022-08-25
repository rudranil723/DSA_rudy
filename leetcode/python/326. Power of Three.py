from operator import truediv


class Solution:
    # def isPowerOfThree(self, n: int) -> bool:
    def isPowerOfThree(n):
        if n == 0:
            return False
        while n % 3 == 0:
            n //= 3
        return True if n == 1 else False
    print(isPowerOfThree(9))
