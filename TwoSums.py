# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target and j != i:
#                     return [i, j]

# nums = [3, 2, 3]
# target = 6
# test = Solution()

# print(test.twoSum(nums, target))
# Expected answer [0, 2]
# The above answer is correct and its O(n^2) in time complexity 


# Extended challenge: Optimise the above answer to below O(n^2)
# Target time complexity: O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            temp = nums[nums.index(nums[i], 0 , len(nums))]
            print(temp)
            # if nums[i] + temp == target and i != nums.index(temp):
            #     return [i, nums.index(temp)]
            

# nums = [3, 2, 3]
# target = 6
nums = [2,7,11,15]
target = 9

test = Solution()
print(test.twoSum(nums, target))

