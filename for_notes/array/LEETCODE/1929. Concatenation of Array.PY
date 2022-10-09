class Solution:
    # def getConcatenation(self, nums: List[int]) -> List[int]:
    def getConcatenation(nums):
        a = []
        b = []
        ans = []
        for i in nums:
            a.append(i)
            b.append(i)
        for i in a:
            ans.append(i)
        for i in b:
            ans.append(i)
        return ans

    print(getConcatenation(nums=[1, 2, 3]))
