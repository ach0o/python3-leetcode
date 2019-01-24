# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = str(x)
        num = int(num[::-1]) if x >= 0 else -int(num[:0:-1])

        if num > (2 ** 31) - 1:
            return 0
        elif num < (-2 ** 31):
            return 0
        else:
            return num
