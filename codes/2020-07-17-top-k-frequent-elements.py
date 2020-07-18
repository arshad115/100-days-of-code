# -------------------------------------------------------
# Add Two Numbers - https://leetcode.com/problems/top-k-frequent-elements/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-17
# Project: 100-days-of-leetcode
# -------------------------------------------------------

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums):
            return nums

        mostFrequent = {}

        for x in nums:
            if x in mostFrequent:
                mostFrequent[x] += 1
            else:
                mostFrequent[x] = 1

        # Sort list in descending order to get most frequent on top
        mostFrequent = {k:v for k, v in sorted(mostFrequent.items(), key= lambda x: x[1], reverse=True)}

        return list(mostFrequent.keys())[:k] # slicing top k


nums = [4,1,-1,2,-1,2,3]
k = 2

solution = Solution()
print(solution.topKFrequent(nums,k))