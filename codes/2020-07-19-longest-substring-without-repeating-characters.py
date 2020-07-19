# -------------------------------------------------------
# Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-19
# Project: 100-days-of-leetcode
# -------------------------------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        visited = {} # Store last index of the char instead of just occurence
        start = max_len = 0

        for i in range(len(s)):
            if s[i] in visited:
                start = max(start, visited[s[i]] + 1)

            max_len = max(max_len, i - start + 1)

            visited[s[i]] = i

        return max_len

string = "pwwkew"
solution = Solution()
num = solution.lengthOfLongestSubstring(string)
print(num)