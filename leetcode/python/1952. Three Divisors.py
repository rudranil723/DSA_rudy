from itertools import count


class Solution:
    def isThree(n):
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        if count == 3:
            return True
        else:
            return False
    print(isThree(5))
