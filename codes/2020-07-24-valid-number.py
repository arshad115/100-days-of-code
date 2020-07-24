# -------------------------------------------------------
# Valid Number - https://leetcode.com/problems/valid-number/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-24
# Project: 100-days-of-leetcode
# -------------------------------------------------------
import re
import sys
from math import inf
from statistics import median
from typing import List

class Solution:
    def isNumberUsingExceptionHandling(self, s: str) -> bool:
        try:
            f = float(s)
            return True
        except:
            return False
    def isNumber(self, s: str) -> bool:
        reg = re.compile("^[+-]?((\d+\.?\d*)|(\d*\.\d+))((e[+-]?\d+$)|$)")
        return reg.match(s.strip())

solution = Solution()
num  = solution.isNumber("10e5")
print(num)