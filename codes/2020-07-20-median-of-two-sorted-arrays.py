# -------------------------------------------------------
# Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-20
# Project: 100-days-of-leetcode
# Comments: Binary search algorithm learned from https://www.youtube.com/watch?v=LPFhl65R7ww https://github.com/mission-peace/interview/blob/master/src/com/interview/binarysearch/MedianOfTwoSortedArrayOfDifferentLength.java
# -------------------------------------------------------
import sys
from math import inf
from statistics import median
from typing import List


class Solution:
    def medianUsingStatistics(self, nums1: List[int], nums2: List[int]) -> float:
        numbs = nums1 + nums2
        numbs = sorted(numbs)  # n log n

        m = median(numbs)
        return m
    def medianUsingPython(self, nums1: List[int], nums2: List[int]) -> float:
        numbs = nums1 + nums2
        numbs = sorted(numbs)  # n log n

        n = len(numbs)
        if n %2 == 0:
            return float(numbs[n//2 - 1] + numbs[n//2 + 1])/2 # // is floor
        else:
            return numbs[n//2]
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Solution
        Take minimum size of two array. Possible number of partitions are from 0 to m in m size array.
        Try every cut in binary search way. When you cut first array at i then you cut second array at (m + n + 1)/2 - i
        Now try to find the i where a[i-1] <= b[j] and b[j-1] <= a[i]. So this i is partition around which lies the median.

        Time complexity is O(log(min(x,y))
        Space complexity is O(1)
        """
        # if input1 length is greater than switch them so that input1 is smaller than input2.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 #swap

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = int((low + high) / 2)
            partitionY = int((x + y + 1) / 2 - partitionX) # +1 to deal with odd cases

            # if partitionX is 0 it means nothing is there on left side.Use -INF for maxLeftX
            #  if partitionX is length of input then there is nothing on right side.Use +INF for minRightX
            maxLeftX = nums1[partitionX - 1] if partitionX != 0 else -inf
            minRightX = nums1[partitionX] if partitionX != x else inf

            maxLeftY = nums2[partitionY - 1] if partitionY != 0 else -inf
            minRightY = nums2[partitionY] if partitionY != y else inf

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # We have partitioned array at correct place
                # Now get max of left elements and min of right elements to get the median in case of even length combined array size
                # or get max of left for odd length combined array size.
                if ((x + y) % 2 == 0):
                    return float(max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2;
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif (maxLeftX > minRightY): # we are too far on right side for partitionX.Go on left side.
                high = partitionX - 1
            else: # we are too far on left side for partitionX.Go on right side.
                low = partitionX + 1
        return 0


solution = Solution()
num = solution.findMedianSortedArrays([1,3],[2])
print(num)