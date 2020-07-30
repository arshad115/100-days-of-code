# -------------------------------------------------------
# Minimum Add to Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-30
# Project: 100-days-of-leetcode
# -------------------------------------------------------

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not S:
            return 0

        while '()' in S :
            S = S.replace("()", "")

        if not S:
            return 0

        if S:
            #Can count or simply return the len
            # counter = Counter(S)
            # left = counter['(']
            # right = counter[')']
            # return left + right

            return len(S)
        else:
            return 0

paran = "())"

solution = Solution()
minpara = solution.minAddToMakeValid(paran)
print(minpara)