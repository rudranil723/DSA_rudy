class Solution:
    def plusOne(digit=[]):
        num=0
        for i in digit:
            num=num*10+i
        plusnum=num+1
        plusdigit=[]
        while plusnum>0:
            r=plusnum%10
            plusdigit.append(r)
        return plusdigit
    print(plusOne(digit=[1,2,3]))