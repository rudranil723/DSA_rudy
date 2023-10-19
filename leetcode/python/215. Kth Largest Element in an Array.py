# the accepted and a simpler approach is to sort the array and return the [-k] element


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         return nums[-k]

# but in order to perform this without sorting we can use the quickselect algorithm

class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    def findKthLargest(nums, k):
        def partition(low, high):
            pivot = nums[low]
            i = low + 1

            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

                nums[i+1], nums[high] = nums[high], nums[i+1]
                return i+1

        def quickselect(low, high, k):
            if low < high:
                pi = partition(low, high)

                if pi == k:
                    return nums[pi]
                elif pi < k:
                    return quickselect(pi+1, high, k)
                else:
                    return quickselect(low, pi-1, k)
            return nums[low]

        return quickselect(0, len(nums)-1, len(nums)-k)

    nums = [3, 1, 2, 2, 4]
    k = 2  # Find the 2nd largest element
    result = findKthLargest(nums, k)
    print(f"The {k}-th largest element is: {result}")
