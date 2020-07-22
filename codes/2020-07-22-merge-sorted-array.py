# -------------------------------------------------------
# Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-22
# Project: 100-days-of-leetcode
# -------------------------------------------------------
import sys
from math import inf
from statistics import median
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j, k, total = 0,0,0
        temp = []

        while j<=m or k <= n:
            if j<m:
                if k < n and nums1[j] <= nums2[k]:
                    temp.append(nums1[j])
                    j+=1
                    total +=1
                elif k < n and nums1[j] > nums2[k]:
                    temp.append(nums2[k])
                    k += 1
                    total += 1
                elif total<m+n:
                    temp.append(nums1[j])
                    j += 1
                    total += 1
            elif k < n:
                if j < m and nums1[j] > nums2[k]:
                    temp.append(nums2[k])
                    k += 1
                    total +=1
                elif j < m  and nums1[j] < nums2[k]:
                    temp.append(nums1[j])
                    j += 1
                    total +=1
                elif total<m+n:
                    temp.append(nums2[k])
                    k += 1
                    total += 1
            else:
                break

        nums1[:] = temp

solution = Solution()
nums1 = [1, 2, 3, 5, 7, 15]
m = 6
nums2 = [2, 3 ,4 ,5]
n = 4

solution.merge(nums1, m, nums2, n)
print(nums1)