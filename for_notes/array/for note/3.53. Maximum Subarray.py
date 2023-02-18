
class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(nums):
        Max = nums[0]
        Sum = 0
        for num in nums:
            Sum += num
            Max = max(Max, Sum)
            if Sum < 0:
                Sum = 0
        return Max


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution.maxSubArray(nums))
