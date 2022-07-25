# time complexity O(log(n))
# space complexity O(1)

class Solution:
    def reverse(x):
        flag = False
        prv, rev = 0, 0
        if x < 0:
            flag = True
            x = -x
        while x > 0:
            r = x % 10
            rev = (rev*10)+r
            if (rev >= pow(2, 31) or rev <= -pow(2, 31)+1):
                rev = 0
            if ((rev-r)//10 != prv):
                return 0
            prv = rev
            x = x//10
        return -rev if (flag == True) else rev
    print(reverse(-325))