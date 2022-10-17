class Solution:
    # def buildArray(self, nums: List[int]) -> List[int]:
    def buildArray(nums):
        ans = []
        for i in range(0, len(nums)):
            ans.append(nums[nums[i]])
        return ans
    nums = [0, 2, 1, 5, 3, 4]
    print(buildArray(nums))
