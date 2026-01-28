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
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and j != i:
                    return [i, j]

nums = [3, 2, 3]
target = 6
test = Solution()

print(test.twoSum(nums, target))

