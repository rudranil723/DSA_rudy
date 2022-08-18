
# class Solution:
#     # def search(self, nums: List[int], target: int) -> int:
#     def search(target, nums):
#         n = len(nums)
#         temp = []
#         i = 0
#         d = target
#         while i < d:
#             temp.append(nums[i])
#             i += 1
#         i = 0
#         while d < n:
#             nums[i] = nums[d]
#             i = i+1
#             d = d+1
#         nums[:] = nums[:i]+temp
#         print(nums)

#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#                 break
#         return -1

#     nums = [4, 5, 6, 7, 0, 1, 2]
# #     print(search(2, nums))

# the code written above is correct but,
#  idk the leetcode compiler is saying there is a runtime error 

class Solution:
    def search(self, A: List[int], target: int) -> int:
        n = len(A)
        left, right = 0, n - 1
        if n == 0: return -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == target: return mid
            
            # inflection point to the right. Left is strictly increasing
            if A[mid] >= A[left]:
                if A[left] <= target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # inflection point to the left of me. Right is strictly increasing
            else:
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1