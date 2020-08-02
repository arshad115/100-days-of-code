# -------------------------------------------------------
# Permutations - https://leetcode.com/problems/permutations/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-02
# Project: 100-days-of-leetcode
# -------------------------------------------------------
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools
        return list(itertools.permutations(nums))

A = [1,3,2,6]

solution = Solution()
subsets = solution.permute(A)
print(subsets)