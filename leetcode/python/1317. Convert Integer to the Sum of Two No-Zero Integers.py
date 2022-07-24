
class Solution:
    # def getNoZeroIntegers(self, n: int) -> List[int]:
    def getNoZeroIntegers(n):
        num1 = 1
        num2 = n-1
        while True:
            if ('0' in str(num1)) or ('0' in str(num2)):
                num1 += 1
                num2 -= 1
            else:
                return [num1, num2]
