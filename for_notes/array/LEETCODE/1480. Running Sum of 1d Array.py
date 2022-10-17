class Solution:
    # def runningSum(self, nums: List[int]) -> List[int]:
    def runningSum(nums):
        ans = []
        sum = 0
        for i in range(0, len(nums)):
            sum = sum+nums[i]
            ans.append(sum)
        return ans
    nums = [3, 1, 2, 10, 1]
    print(runningSum(nums))
