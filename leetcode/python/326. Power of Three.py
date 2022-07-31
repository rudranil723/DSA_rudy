from operator import truediv


class Solution:
    # def isPowerOfThree(self, n: int) -> bool:
    def isPowerOfThree(n):
        x, p = 1, 1
        if n == 0:
            return True
        while n > p:
            p=p*pow(3,x)
            x+=1
        return True
    print(isPowerOfThree(27))