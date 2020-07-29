# -------------------------------------------------------
# 3sum - https://leetcode.com/problems/3sum/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-29
# Project: 100-days-of-leetcode
# -------------------------------------------------------
from typing import List

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        resultslist = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            twosumlist = self.twoSum(nums[i + 1:], -nums[i])
            if not twosumlist:
                continue
            else:
                for x in twosumlist:
                    x.insert(0, nums[i])
                    resultslist.append(x)

        unique_data = [list(x) for x in set(tuple(x) for x in resultslist)]
        return unique_data

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        results = []
        for i, num in enumerate(nums):
            if num in dict:
                results.append([nums[dict[num]], num]) #can have multiple two sums for the three sum
            else:
                # storing index of the target - num in the dict
                dict[target - num] = i
        return results

nums = [-1,0,1,2,-1,-4]

solution = Solution()
num = solution.threeSum(nums)
print(num)