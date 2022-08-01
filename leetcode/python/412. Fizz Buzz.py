
class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
    def fizzBuzz(n):
        list = []
        for i in range(1, n+1):
            if i % 15 == 0:
                list.append(str('FizzBuzz'))
            elif i % 3 == 0:
                list.append(str('Fizz'))
            elif i % 5 == 0:
                list.append(str('Buzz'))
            else:
                list.append(str(i))
        return list
    print(fizzBuzz(15))
