from pickle import TRUE
from re import L


class Solution:
    # def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    def kidsWithCandies(candies, extraCandies):
        maxcandies = max(candies)
        ans = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxcandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans

    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(kidsWithCandies(candies, extraCandies))
