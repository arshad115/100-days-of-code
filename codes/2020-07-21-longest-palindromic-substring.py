# -------------------------------------------------------
# Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-21
# Project: 100-days-of-leetcode
# Comments: Learned from https://www.callicoder.com/longest-palindromic-substring/
# -------------------------------------------------------
import sys
from math import inf
from statistics import median
from typing import List

class Solution:
    def recursionPalindrome(self, s: str) -> str:
        """
        Very slow O(N^3)
        """
        if s == s[::-1]:
            return s
        s1 = self.longestPalindrome(s[:-1])
        s2 = self.longestPalindrome(s[1:])
        if len(s1) > len(s2):
            return s1
        else:
            return s2

    def longestPalindrome(self, s: str) -> str:
        """
        Using dynamic programming, store the results of past tests
        """
        # no need to run if its a full palindrome
        if s == s[::-1]:
            return s

        n = len(s)
        table = [[0 for x in range(n)] for y in range(n)]

        longestSoFar = 0
        startIndex = 0
        endIndex = 0

        for j in range(0, n):
            table[j][j] = True
            for i in range(0, j):
                if s[i] == s[j] and (j-i <= 2 or table[i+1][j-1]):
                    table[i][j] = True
                    if j-i+1 > longestSoFar:
                        longestSoFar = j - i + 1
                        startIndex = i
                        endIndex = j

        return s[startIndex:endIndex + 1]

solution = Solution()
palindrome = solution.longestPalindrome("abab")
print(palindrome)