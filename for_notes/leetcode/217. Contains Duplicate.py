class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    def containsDuplicate(nums=[int]):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    print(containsDuplicate(nums=[1, 3, 2, 4, 2]))
