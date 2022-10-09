class Solution:
    # def shuffle(self, nums: List[int], n: int) -> List[int]:
    def shuffle(nums, n):
        ans = []
        a = nums[:n]
        b = nums[n:]
        for i in range(n):
            ans.append(a[i])
            ans.append[b[i]]
        return ans

    nums = [2, 5, 1, 3, 4, 7]
    print(shuffle(nums, 3))
