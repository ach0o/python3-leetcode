# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.index(needle) if needle in haystack else -1
