# -------------------------------------------------------
# Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-03
# Project: 100-days-of-leetcode
# -------------------------------------------------------
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

A = [1,3,2,6]

solution = Solution()
nums = solution.removeDuplicates(A)
print(nums)