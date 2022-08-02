import math



class Solution:
    # def constructRectangle(self, area: int) -> List[int]:
    def constructRectangle(area):
        x = int(math.sqrt(area))
        while True:
            y = area / x
            if y.is_integer():
                if x > y:
                    return [x, int(y)]
                else:
                    return [int(y), x]
            x -= 1
    print(constructRectangle(10))
