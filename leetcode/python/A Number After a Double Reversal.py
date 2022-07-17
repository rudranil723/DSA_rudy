class Solution:
    # def isSameAfterReversals(self, num: int) -> bool :
    def isSameAfterReversals(num):
        if num == 0:
            return True
        else:
            r = num % 10
            if r == 0:
                return False
            else:
                return True
    print(isSameAfterReversals(526))
