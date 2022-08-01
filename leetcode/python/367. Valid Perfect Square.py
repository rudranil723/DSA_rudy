class Solution:
    # def isPerfectSquare(self, num: int) -> bool:
    def isPerfectSquare(num):
        if num <= 0:
            return False
        i = 1
        while(i * i <= num):
            if ((num % i == 0) and (num / i == i)):
                return True
            i = i + 1
        return False
    print(isPerfectSquare(1))
