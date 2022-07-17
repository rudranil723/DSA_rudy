

class Solution:
    # def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    def selfDividingNumbers(left, right):
        ago = []
        for i in range(left, right+1):
            if i < 10:
                ago.append(i)
            else:
                temp = i
                while temp != 0:
                    r = temp % 10
                    if r != 0 and i % r == 0:
                        temp //= 10
                    else:
                        break
                if temp == 0:
                    ago.append(i)
        return ago
    print(selfDividingNumbers(1, 22))
