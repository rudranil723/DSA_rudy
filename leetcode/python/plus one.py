
class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(digits: list[int]):
        if (digits[len(digits)-1] == 9):
            sum = 0
            for i in digits:
                sum = sum*10+i
            newnum = sum+1
            return (list(str(newnum)))
        else:
            digits[len(digits)-1] += 1
            return digits
    print(plusOne(digits=[1,2,3]))
