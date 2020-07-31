# -------------------------------------------------------
# Word Subsets - https://leetcode.com/problems/word-subsets/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-31
# Project: 100-days-of-leetcode
# -------------------------------------------------------
from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        dict = {}
        subsets = []

        for b in B:
            for bb in b:
                wordCount = b.count(bb)
                if bb not in dict or dict[bb] < wordCount:
                    dict[bb] = wordCount

        lettersRequired = len(dict)
        for a in A:
            matches = 0
            for letter in dict:
                count = a.count(letter)
                if count >= dict[letter]:
                    matches += 1
                if matches >= lettersRequired:
                    subsets.append(a)
                    break

        return subsets

A = ["acaac","cccbb","aacbb","caacc","bcbbb"]
B = ["c","cc","b"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["ec","oc","ceo"]

solution = Solution()
subsets = solution.wordSubsets(A, B)
print(subsets)