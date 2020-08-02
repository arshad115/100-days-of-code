# -------------------------------------------------------
# Merge Intervals - https://leetcode.com/problems/merge-intervals/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-01
# Project: 100-days-of-leetcode
# -------------------------------------------------------
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return []
        intervals.sort()
        merged = [intervals[0]]
        for i in intervals[1:]:
            if i[0]<= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1],i[1])
            else:
                merged.append(i)
        return merged

A = [[1,3],[2,6],[8,10],[15,18]]

solution = Solution()
subsets = solution.merge(A)
print(subsets)