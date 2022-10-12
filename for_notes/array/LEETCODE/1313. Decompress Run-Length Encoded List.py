class Solution:
    # def decompressRLElist(self, nums: List[int]) -> List[int]:
    def decompressRLElist(nums):
        ans = []
        for i in range(0, len(nums), 2):
            ans += [nums[i+1]]*nums[i]
        return ans

    nums = [1, 2, 3, 4]
    print(decompressRLElist(nums))
