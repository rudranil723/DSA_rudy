class Solution:
    # def smallestRangeI(self, nums: List[int], k: int) -> int:
    def smallestRangeI(nums, k):
        if max(nums)-min(nums) <= 2*k:
            return 0
        else:
            return max(nums)-min(nums)-2*k
    print(smallestRangeI([0, 10], 2))

# gg good question

# solution:

# https://leetcode.com/problems/smallest-range-i/discuss/535164/Python-O(n)-by-min-and-Max.-85%2B-w-Visualization
