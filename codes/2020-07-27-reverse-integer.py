# -------------------------------------------------------
# Reverse Integer - https://leetcode.com/problems/reverse-integer/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-27
# Project: 100-days-of-leetcode
# -------------------------------------------------------

class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        sign = 1
        if string.startswith('-'):
            sign = -1
        if sign == 1:
            strint = int(string[::-1])
        else:
            strint = int(string[:0:-1])

        return 0 if strint.bit_length() >= 32 else sign * strint

num = 16021

solution = Solution()
num = solution.reverse(num)
print(num)