class Solution:
    # def subtractProductAndSum(self, num: int) ->int :
    def subtractProductAndSum(num):
        a = 1
        b = 0
        while num > 0:
            r = num % 10
            a = a*r
            b = b+r
            num //= 10
        return int(a-b)
    print(subtractProductAndSum(234))
