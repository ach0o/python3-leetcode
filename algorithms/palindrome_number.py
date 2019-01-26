# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
