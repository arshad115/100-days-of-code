# -------------------------------------------------------
# String to Integer (atoi) - https://leetcode.com/problems/string-to-integer-atoi/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-25
# Project: 100-days-of-leetcode
# -------------------------------------------------------
import re
import sys
from math import inf
from statistics import median
from typing import List

class Solution:
    def myAtoi(self, str: str) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        reg = re.compile("^[+-]?\d*")
        nstr = reg.findall(str.strip())

        if len(nstr)> 0:
            nstr = nstr[0]
        else:
            return 0

        if not nstr or nstr == "-" or nstr == "+":
            return 0

        num = int(nstr)

        if num > MAX_INT:
            return MAX_INT
        elif num < MIN_INT:
            return MIN_INT
        else:
            return num

solution = Solution()
num  = solution.myAtoi("+1")
print(num)