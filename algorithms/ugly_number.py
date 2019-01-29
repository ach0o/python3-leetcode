# https://leetcode.com/problems/ugly-number/


class Solution:
    def __init__(self):
        self.factors = (2, 3, 5)

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        if num == 1:
            return True

        for f in self.factors:
            if num % f == 0:
                if num / f == 1:
                    return True
                if self.isUgly(num / f):
                    return True
                else:
                    return False
        return False
