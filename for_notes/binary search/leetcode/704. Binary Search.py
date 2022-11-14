class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    def search(nums, target):
        hi = len(nums)-1
        lo = 0
        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target))
