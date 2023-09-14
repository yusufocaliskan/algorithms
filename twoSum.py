class Solution:
    def twoSum(self, nums, target):
        indexs = {}
        for index, current in enumerate(nums):
            if target-current in indexs:
                return [indexs[target-current], index]
            indexs[current] = index

print("Solution#1: ",Solution().twoSum([2,4,5],7))

class Solution2:
    def twoSum(self, nums, target):
        indexs = {}
        for index, current in enumerate(nums):
            if target-current in indexs:
                return [indexs[target-current], index]
            indexs[current] = index

print("Solution#2: ",Solution2().twoSum([2,4,5],7))