

class Solution:
    def totalMoney(n):
        sum,d=0,0
        for i in range(n):
            if i%7==0:
                d+=1
            sum=sum+d+(i%7)
        return sum
    print(totalMoney(10))



