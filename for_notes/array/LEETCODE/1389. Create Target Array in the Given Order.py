class Solution:
    # def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    def createTargetArray(nums, index):
        arr = []
        for i in range(len(nums)):
            arr.insert(index[i], nums[i])
        return arr

    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    print(createTargetArray(nums, index))


# funtion


# list.insert()

# # create a list of vowels
# vowel = ['a', 'e', 'i', 'u']

# # 'o' is inserted at index 3 (4th position)
# vowel.insert(3, 'o')


# print('List:', vowel)

# # Output: List: ['a', 'e', 'i', 'o', 'u']
