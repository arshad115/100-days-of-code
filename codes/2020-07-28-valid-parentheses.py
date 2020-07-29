# -------------------------------------------------------
# Valid Parentheses - https://leetcode.com/problems/valid-parentheses/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-28
# Project: 100-days-of-leetcode
# -------------------------------------------------------
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        #52 ms
        if not s:
            return True

        if s.startswith((']', ')', '}')):
            return False

        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace("[]", "").replace("()", "").replace("{}", "")

        if s:
            return False
        else:
            return True

    def isValidStack(self, s: str) -> bool:
        # 40 ms
        if not s:
            return True

        if s.startswith((']', ')', '}')):
            return False

        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif len(stack) <= 0:
                return False
            elif char == ")" and stack.pop() != "(":
                return False
            elif char == "]" and stack.pop() != "[":
                return False
            elif char == "}" and stack.pop() != "{":
                return False
        return not len(stack)

paran = "){[]}"

solution = Solution()
janein = solution.isValid(paran)
print(janein)